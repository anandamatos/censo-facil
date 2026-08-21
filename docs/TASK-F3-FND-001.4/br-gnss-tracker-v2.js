/**
 * @license
 * Copyright (c) 2026 Instituto Brasileiro de Geografia e Estatística (IBGE)
 * All rights reserved.
 * This source code is licensed under the MIT-style license found in the
 * LICENSE file in the root directory of this source tree.
 */

/**
 * @customElement br-gnss-tracker
 * @description Componente PWA nativo para captura de coordenadas GNSS e validação de precisão horizontal (HDOP) no Censo Agropecuário 2026.
 * Implementado utilizando estritamente a API DOM Level 2 Core com createElementNS para integridade em ambientes XHTML.
 *
 * @attr {number} hdop - Índice de diluição de precisão horizontal medido pelo receptor integrado.
 * @attr {string} status - Estado operacional da precisão: 'loading', 'optimal', 'acceptable', 'insufficient', 'error'.
 *
 * @property {number} lat - Latitude atual capturada pelo sensor em graus decimais.
 * @property {number} long - Longitude atual capturada pelo sensor em graus decimais.
 * @property {number} precision - Incerteza horizontal estimada calculada em metros (σ_h = HDOP * σ_0).
 *
 * @fires br-position-update - Disparado a cada atualização das coordenadas geográficas e precisão horizontal.
 * @fires br-status-change - Disparado quando o status operacional transiciona entre os limites geodésicos.
 * @fires br-gnss-error - Disparado em caso de erro de hardware ou permissão negada de localização.
 *
 * @slot icon - Substitui o ícone padrão de conexão de satélite na barra de cabeçalho.
 * @slot status-message - Área para orientações dinâmicas ao recenseador escritas em Linguagem Simples.
 * @slot actions - Espaço para botões de ação e suporte (como links de ajuda e manuais).
 */
export class BrGnssTracker extends HTMLElement {
  /**
   * Desvio padrão de base do receptor integrado do DMC.
   * Conforme especificação geodésica do Censo Agropecuário 2026.
   * @type {number}
   * @private
   */
  static _SIGMA_0 = 1.2;

  /**
   * Namespaces oficiais do W3C para manipulação rigorosa em XHTML.
   * Conforme DOM Level 2 Core Specification e XML Namespaces 1.1.
   * @private
   */
  static _NAMESPACES = {
    xhtml: 'http://www.w3.org/1999/xhtml',
    svg: 'http://www.w3.org/2000/svg',
    xlink: 'http://www.w3.org/1999/xlink'
  };

  /**
   * Atributos observados pelo ciclo de vida do Custom Element.
   * @type {string[]}
   */
  static get observedAttributes() {
    return ['hdop', 'status'];
  }

  constructor() {
    super();

    // Inicialização do estado interno privado
    this._lat = 0.0;
    this._long = 0.0;
    this._hdop = null;
    this._status = 'loading';
    this._precision = null;
    this._recalibrateTimeout = null;

    // Anexação da raiz do Shadow DOM no modo aberto (open)
    this.attachShadow({ mode: 'open' });

    // Construção programática da árvore DOM utilizando exclusivamente createElementNS
    this._buildShadowDOM();
  }

  /**
   * Cria de forma rigorosa toda a árvore de elementos do Shadow DOM,
   * associando cada nó ao seu namespace correto (XHTML ou SVG).
   * @private
   */
  _buildShadowDOM() {
    const ns = BrGnssTracker._NAMESPACES;

    // 1. Elemento de estilo (<style>)
    const style = document.createElementNS(ns.xhtml, 'style');
    style.setAttributeNS(null, 'type', 'text/css');
    style.textContent = `
      :host {
        display: block;
        font-family: var(--font-family-ui, "Univers LT Std", "Univers", Arial, sans-serif);
        box-sizing: border-box;
        width: 100%;
      }
      .gnss-tracker {
        background-color: var(--color-neutral-light, #F5F5F5);
        border: 1px solid var(--color-neutral-medium, #C5D4EB);
        border-radius: 8px;
        padding: 16px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
        color: var(--color-text-primary, #1C1C1E);
        transition: border-left-color 0.3s ease;
        border-left: 6px solid var(--color-neutral-medium, #C5D4EB);
      }
      .gnss-tracker[data-status="loading"] { border-left-color: var(--color-neutral-medium, #C5D4EB); }
      .gnss-tracker[data-status="optimal"] { border-left-color: var(--color-success, #4CAF50); }
      .gnss-tracker[data-status="acceptable"] { border-left-color: var(--color-warning, #F5A623); }
      .gnss-tracker[data-status="insufficient"] { border-left-color: var(--color-error, #E53935); }
      .gnss-tracker[data-status="error"] { border-left-color: var(--color-error, #E53935); }

      .gnss-header { display: flex; align-items: center; gap: 12px; margin-bottom: 16px; }
      .gnss-icon-container { display: flex; align-items: center; justify-content: center; width: 32px; height: 32px; }
      .icon-svg { width: 24px; height: 24px; fill: currentColor; }
      .gnss-status { font-weight: 700; font-size: 1.125rem; color: var(--color-neutral-dark, #071D41); }
      .gnss-data { background-color: var(--color-neutral-white, #FFFFFF); border: 1px solid var(--color-neutral-medium, #C5D4EB); border-radius: 4px; padding: 12px; margin-bottom: 16px; }
      .data-row { display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px dashed var(--color-neutral-medium, #C5D4EB); font-size: 1rem; }
      .data-row:last-child { border-bottom: none; }
      .data-label { font-weight: 700; color: var(--color-text-secondary, #555770); }
      .data-value { font-family: monospace; font-weight: bold; color: var(--color-text-primary, #1C1C1E); }
      .gnss-actions { display: flex; justify-content: flex-end; gap: 12px; }
      .btn-recalibrate {
        font-family: var(--font-family-ui, "Univers LT Std", "Univers", Arial, sans-serif);
        font-weight: 700;
        font-size: 1rem;
        background-color: var(--color-primary-pure, #0033A0);
        color: var(--color-neutral-white, #FFFFFF);
        border: none;
        border-radius: 4px;
        padding: 12px 24px;
        min-height: 48px;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        transition: background-color 0.2s ease;
      }
      .btn-recalibrate:hover { background-color: var(--color-primary-dark, #002680); }
      .btn-recalibrate:active { background-color: var(--color-primary-light, #3366CC); }
      .btn-recalibrate:focus-visible { outline: 3px solid var(--color-primary-pure, #0033A0); outline-offset: 2px; }
      .rotating { animation: spin 2s linear infinite; }
      @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
      }
    `;
    this.shadowRoot.appendChild(style);

    // 2. Container principal (.gnss-tracker)
    const container = document.createElementNS(ns.xhtml, 'div');
    container.setAttributeNS(null, 'class', 'gnss-tracker');
    container.setAttributeNS(null, 'id', 'tracker-card');
    container.setAttributeNS(null, 'data-status', 'loading');
    container.setAttributeNS(null, 'lang', 'pt');
    container.setAttributeNS(null, 'xml:lang', 'pt');

    // 3. Cabeçalho (.gnss-header)
    const header = document.createElementNS(ns.xhtml, 'div');
    header.setAttributeNS(null, 'class', 'gnss-header');
    header.setAttributeNS(null, 'lang', 'pt');
    header.setAttributeNS(null, 'xml:lang', 'pt');

    // Container do ícone (.gnss-icon-container)
    const iconContainer = document.createElementNS(ns.xhtml, 'div');
    iconContainer.setAttributeNS(null, 'class', 'gnss-icon-container');
    iconContainer.setAttributeNS(null, 'id', 'icon-box');

    const iconSlot = document.createElementNS(ns.xhtml, 'slot');
    iconSlot.setAttributeNS(null, 'name', 'icon');

    // Ícone padrão SVG (Satélite) com namespace SVG estrito
    const svg = document.createElementNS(ns.svg, 'svg');
    svg.setAttributeNS(null, 'class', 'icon-svg');
    svg.setAttributeNS(null, 'id', 'status-icon');
    svg.setAttributeNS(null, 'viewBox', '0 0 24 24');
    svg.setAttributeNS(null, 'aria-hidden', 'true');

    const path = document.createElementNS(ns.svg, 'path');
    path.setAttributeNS(null, 'd', 'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z');
    svg.appendChild(path);
    iconSlot.appendChild(svg);
    iconContainer.appendChild(iconSlot);

    // Título de Status (.gnss-status)
    const statusTitle = document.createElementNS(ns.xhtml, 'div');
    statusTitle.setAttributeNS(null, 'class', 'gnss-status');
    statusTitle.setAttributeNS(null, 'id', 'status-title');
    statusTitle.setAttributeNS(null, 'role', 'status');
    statusTitle.setAttributeNS(null, 'aria-live', 'polite');
    statusTitle.setAttributeNS(null, 'lang', 'pt');
    statusTitle.setAttributeNS(null, 'xml:lang', 'pt');

    const statusSlot = document.createElementNS(ns.xhtml, 'slot');
    statusSlot.setAttributeNS(null, 'name', 'status-message');

    const fallbackSpan = document.createElementNS(ns.xhtml, 'span');
    fallbackSpan.setAttributeNS(null, 'id', 'status-text-fallback');
    fallbackSpan.setAttributeNS(null, 'lang', 'pt');
    fallbackSpan.setAttributeNS(null, 'xml:lang', 'pt');
    fallbackSpan.textContent = 'Aguardando sinal dos satélites...';
    statusSlot.appendChild(fallbackSpan);
    statusTitle.appendChild(statusSlot);

    header.appendChild(iconContainer);
    header.appendChild(statusTitle);
    container.appendChild(header);

    // 4. Painel de Dados (.gnss-data)
    const dataPanel = document.createElementNS(ns.xhtml, 'div');
    dataPanel.setAttributeNS(null, 'class', 'gnss-data');
    dataPanel.setAttributeNS(null, 'role', 'region');
    dataPanel.setAttributeNS(null, 'aria-label', 'Dados Geodésicos de Campo');
    dataPanel.setAttributeNS(null, 'lang', 'pt');
    dataPanel.setAttributeNS(null, 'xml:lang', 'pt');

    // Linha de Latitude
    const rowLat = this._createDataRow('lbl-lat', 'Latitude:', 'lat-val');
    // Linha de Longitude
    const rowLong = this._createDataRow('lbl-long', 'Longitude:', 'long-val');
    // Linha de HDOP
    const rowHdop = this._createDataRow('lbl-hdop', 'HDOP:', 'hdop-val');
    // Linha de Precisão Horizontal
    const rowPrec = this._createDataRow('lbl-precision', 'Precisão Horizontal (σ_h):', 'precision-val');

    dataPanel.appendChild(rowLat);
    dataPanel.appendChild(rowLong);
    dataPanel.appendChild(rowHdop);
    dataPanel.appendChild(rowPrec);
    container.appendChild(dataPanel);

    // 5. Seção de Ações (.gnss-actions)
    const actionsPanel = document.createElementNS(ns.xhtml, 'div');
    actionsPanel.setAttributeNS(null, 'class', 'gnss-actions');

    const actionsSlot = document.createElementNS(ns.xhtml, 'slot');
    actionsSlot.setAttributeNS(null, 'name', 'actions');

    const recalibrateBtn = document.createElementNS(ns.xhtml, 'button');
    recalibrateBtn.setAttributeNS(null, 'type', 'button');
    recalibrateBtn.setAttributeNS(null, 'class', 'btn-recalibrate');
    recalibrateBtn.setAttributeNS(null, 'id', 'recalibrate-btn');
    recalibrateBtn.setAttributeNS(null, 'aria-label', 'Recalibrar sinal dos satélites');
    recalibrateBtn.setAttributeNS(null, 'lang', 'pt');
    recalibrateBtn.setAttributeNS(null, 'xml:lang', 'pt');
    recalibrateBtn.textContent = '🔄 Recalibrar';

    actionsSlot.appendChild(recalibrateBtn);
    actionsPanel.appendChild(actionsSlot);
    container.appendChild(actionsPanel);

    // Acopla o container ao Shadow Root
    this.shadowRoot.appendChild(container);
  }

  /**
   * Helper para criar linhas de dados estruturados em XHTML Estrito.
   * @param {string} labelId - ID do rótulo para associação ARIA.
   * @param {string} labelText - Texto descritivo.
   * @param {string} valueId - ID do nó de valor.
   * @returns {HTMLElement} Linha de dados XML.
   * @private
   */
  _createDataRow(labelId, labelText, valueId) {
    const ns = BrGnssTracker._NAMESPACES;
    const row = document.createElementNS(ns.xhtml, 'div');
    row.setAttributeNS(null, 'class', 'data-row');
    row.setAttributeNS(null, 'lang', 'pt');
    row.setAttributeNS(null, 'xml:lang', 'pt');

    const label = document.createElementNS(ns.xhtml, 'span');
    label.setAttributeNS(null, 'class', 'data-label');
    label.setAttributeNS(null, 'id', labelId);
    label.setAttributeNS(null, 'lang', 'pt');
    label.setAttributeNS(null, 'xml:lang', 'pt');
    label.textContent = labelText;

    const val = document.createElementNS(ns.xhtml, 'span');
    val.setAttributeNS(null, 'class', 'data-value');
    val.setAttributeNS(null, 'id', valueId);
    val.setAttributeNS(null, 'aria-labelledby', labelId);
    val.setAttributeNS(null, 'lang', 'pt');
    val.setAttributeNS(null, 'xml:lang', 'pt');
    val.textContent = '-';

    row.appendChild(label);
    row.appendChild(val);
    return row;
  }

  /**
   * Método de ciclo de vida invocado ao acoplar o elemento ao DOM.
   * Executa a vinculação de eventos e inicializa os displays de dados.
   */
  connectedCallback() {
    // Configura o evento do botão de recalibragem padrão do template
    const btn = this.shadowRoot.getElementById('recalibrate-btn');
    if (btn) {
      // Remove listeners antigos para evitar duplicação
      btn.removeEventListener('click', this._recalibrateHandler);
      this._recalibrateHandler = () => this.recalibrate();
      btn.addEventListener('click', this._recalibrateHandler);
    }

    // Inicializa a renderização com base nas propriedades atuais
    this._updateUI();
  }

  /**
   * Método de ciclo de vida invocado ao desvincular o elemento do DOM.
   */
  disconnectedCallback() {
    // Remove o listener do botão para evitar memory leaks
    const btn = this.shadowRoot.getElementById('recalibrate-btn');
    if (btn && this._recalibrateHandler) {
      btn.removeEventListener('click', this._recalibrateHandler);
      this._recalibrateHandler = null;
    }

    // Limpa o timeout pendente para evitar memory leaks
    if (this._recalibrateTimeout) {
      clearTimeout(this._recalibrateTimeout);
      this._recalibrateTimeout = null;
    }
  }

  /**
   * Método de ciclo de vida que detecta alterações em atributos observados.
   *
   * @param {string} name - Nome do atributo modificado.
   * @param {string} oldValue - Valor anterior.
   * @param {string} newValue - Novo valor atribuído.
   */
  attributeChangedCallback(name, oldValue, newValue) {
    if (oldValue === newValue) return;

    if (name === 'hdop') {
      const parsedHdop = newValue !== null ? parseFloat(newValue) : null;
      this._hdop = parsedHdop;
      if (parsedHdop !== null && !isNaN(parsedHdop)) {
        // Cálculo da incerteza geodésica σ_h baseada na diluição horizontal
        this._precision = parseFloat((parsedHdop * BrGnssTracker._SIGMA_0).toFixed(1));
        // Recalcula o status automaticamente de acordo com as travas lógicas
        this._autoUpdateStatus(parsedHdop);
      } else {
        this._precision = null;
        this.status = 'loading';
      }
    } else if (name === 'status') {
      this._status = newValue || 'loading';
    }

    this._updateUI();
  }

  // --- Getters e Setters com Reflexão de Atributos (Property Reflection) ---

  /** @type {number|null} */
  get hdop() {
    return this._hdop;
  }

  set hdop(value) {
    if (value === null || value === undefined) {
      this.removeAttribute('hdop');
    } else {
      this.setAttribute('hdop', String(value));
    }
  }

  /** @type {string} */
  get status() {
    return this._status;
  }

  set status(value) {
    if (!value) {
      this.removeAttribute('status');
    } else {
      this.setAttribute('status', value);
    }
  }

  /** @type {number} */
  get lat() {
    return this._lat;
  }

  set lat(value) {
    const num = parseFloat(value);
    this._lat = isNaN(num) ? 0.0 : num;
    this._updateUI();
    this._dispatchPositionUpdate();
  }

  /** @type {number} */
  get long() {
    return this._long;
  }

  set long(value) {
    const num = parseFloat(value);
    this._long = isNaN(num) ? 0.0 : num;
    this._updateUI();
    this._dispatchPositionUpdate();
  }

  /** @type {number|null} */
  get precision() {
    return this._precision;
  }

  // --- Métodos de Controle Interno e Regras de Campo ---

  /**
   * Calcula e atualiza dinamicamente o status com base na diluição de precisão (HDOP).
   *
   * @param {number} hdopVal - Valor numérico medido de HDOP.
   * @private
   */
  _autoUpdateStatus(hdopVal) {
    let newStatus = 'loading';

    if (hdopVal <= 2.5) {
      newStatus = 'optimal';
    } else if (hdopVal <= 5.0) {
      newStatus = 'acceptable';
    } else {
      newStatus = 'insufficient';
    }

    if (this.status !== newStatus) {
      const oldStatus = this.status;
      this.status = newStatus;

      // Dispara o evento de alteração de estado para a aplicação pai
      this.dispatchEvent(new CustomEvent('br-status-change', {
        bubbles: true,
        composed: true,
        detail: {
          previousStatus: oldStatus,
          currentStatus: newStatus,
          hdop: hdopVal
        }
      }));
    }
  }

  /**
   * Força uma simulação de recalibragem ou reinicia busca por satélite.
   * Método público acessível imperativamente via JS pela aplicação pai.
   */
  recalibrate() {
    const prevStatus = this.status;
    this.status = 'loading';
    this._updateUI();

    // Limpa timeout anterior se existir
    if (this._recalibrateTimeout) {
      clearTimeout(this._recalibrateTimeout);
      this._recalibrateTimeout = null;
    }

    // Simulação do comportamento assíncrono do sensor físico do DMC
    this._recalibrateTimeout = setTimeout(() => {
      // Gera HDOP randômico entre 1.0 e 7.0 para simular a varredura real em campo
      const simulatedHdop = parseFloat((Math.random() * 6.0 + 1.0).toFixed(1));
      this.hdop = simulatedHdop;
      this._recalibrateTimeout = null;
    }, 1200);
  }

  /**
   * Dispara o evento CustomEvent com os metadados georreferenciados atualizados.
   * @private
   */
  _dispatchPositionUpdate() {
    if (this._lat !== 0.0 && this._long !== 0.0) {
      this.dispatchEvent(new CustomEvent('br-position-update', {
        bubbles: true,
        composed: true,
        detail: {
          lat: this._lat,
          long: this._long,
          precision: this._precision || 0.0
        }
      }));
    }
  }

  /**
   * Atualiza a árvore do Shadow DOM com base nas mudanças de propriedades e dados.
   * @private
   */
  _updateUI() {
    const shadow = this.shadowRoot;
    if (!shadow) return;

    const card = shadow.getElementById('tracker-card');
    const latDisplay = shadow.getElementById('lat-val');
    const longDisplay = shadow.getElementById('long-val');
    const hdopDisplay = shadow.getElementById('hdop-val');
    const precisionDisplay = shadow.getElementById('precision-val');
    const fallbackText = shadow.getElementById('status-text-fallback');
    const iconSvg = shadow.getElementById('status-icon');

    // Sincroniza o atributo do dataset do card de container para reatividade CSS
    if (card) {
      card.setAttributeNS(null, 'data-status', this._status);
    }

    // Renderiza dados numéricos na interface do DMC
    if (latDisplay) latDisplay.textContent = this._lat !== 0.0 ? `${this._lat.toFixed(6)}°` : '-';
    if (longDisplay) longDisplay.textContent = this._long !== 0.0 ? `${this._long.toFixed(6)}°` : '-';
    if (hdopDisplay) hdopDisplay.textContent = this._hdop !== null ? String(this._hdop) : '-';
    if (precisionDisplay) {
      precisionDisplay.textContent = this._precision !== null ? `${this._precision} metros` : '-';
    }

    // Configura textos informativos em Linguagem Simples no Slot de status
    if (fallbackText) {
      switch (this._status) {
        case 'optimal':
          fallbackText.innerHTML = '🟢 <strong>Precisão ótima para registro.</strong>';
          break;
        case 'acceptable':
          fallbackText.innerHTML = '🟡 <strong>Precisão aceitável. Se possível, busque um local mais aberto.</strong>';
          break;
        case 'insufficient':
          fallbackText.innerHTML = '🔴 <strong>Sinal bloqueado. Precisão insuficiente para o Censo (&gt; 5,0m).</strong>';
          break;
        case 'error':
          fallbackText.innerHTML = '❌ <strong>Erro no receptor GNSS. Verifique as configurações do DMC.</strong>';
          break;
        case 'loading':
        default:
          fallbackText.innerHTML = '🔄 <strong>Buscando conexão estável com satélites...</strong>';
          break;
      }
    }

    // Atualiza classes CSS e estado de rotação do ícone SVG
    if (iconSvg) {
      if (this._status === 'loading') {
        iconSvg.classList.add('rotating');
      } else {
        iconSvg.classList.remove('rotating');
      }
    }
  }
}

// Registro global seguro e semântico do Custom Element na CustomElementRegistry do W3C
if (!customElements.get('br-gnss-tracker')) {
  customElements.define('br-gnss-tracker', BrGnssTracker);
}