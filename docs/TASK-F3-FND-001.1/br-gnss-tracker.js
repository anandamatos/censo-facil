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
 *
 * @attr {number} hdop - Índice de diluição de precisão horizontal (dilution of precision) medido pelo receptor integrado.
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
   * Desvio padrão de base do receptor integrado do DMC (DMC baseline uncertainty).
   * Conforme especificação geodésica do Censo Agropecuário 2026.
   * @type {number}
   * @private
   */
  static _SIGMA_0 = 1.2;

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

    // Anexação da raiz do Shadow DOM no modo aberto (open)
    this.attachShadow({ mode: 'open' });

    // Namespace XHTML para criação de elementos
    const ns = 'http://www.w3.org/1999/xhtml';
    const shadow = this.shadowRoot;

    // --- 1. ESTILOS via createElementNS ---
    const style = document.createElementNS(ns, 'style');
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

      /* Configuração de Cores Funcionais baseadas no Status */
      .gnss-tracker[data-status="loading"] {
        border-left-color: var(--color-neutral-medium, #C5D4EB);
      }

      .gnss-tracker[data-status="optimal"] {
        border-left-color: var(--color-success, #4CAF50);
      }

      .gnss-tracker[data-status="acceptable"] {
        border-left-color: var(--color-warning, #F5A623);
      }

      .gnss-tracker[data-status="insufficient"] {
        border-left-color: var(--color-error, #E53935);
      }

      .gnss-tracker[data-status="error"] {
        border-left-color: var(--color-error, #E53935);
      }

      .gnss-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 16px;
      }

      .gnss-icon-container {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 32px;
        height: 32px;
      }

      .icon-svg {
        width: 24px;
        height: 24px;
        fill: currentColor;
      }

      .gnss-status {
        font-weight: 700;
        font-size: 1.125rem; /* 18px */
        color: var(--color-neutral-dark, #071D41);
      }

      .gnss-data {
        background-color: var(--color-neutral-white, #FFFFFF);
        border: 1px solid var(--color-neutral-medium, #C5D4EB);
        border-radius: 4px;
        padding: 12px;
        margin-bottom: 16px;
      }

      .data-row {
        display: flex;
        justify-content: space-between;
        padding: 8px 0;
        border-bottom: 1px dashed var(--color-neutral-medium, #C5D4EB);
        font-size: 1rem; /* 16px para acessibilidade de acordo com o e-MAG */
      }

      .data-row:last-child {
        border-bottom: none;
      }

      .data-label {
        font-weight: 700;
        color: var(--color-text-secondary, #555770);
      }

      .data-value {
        font-family: monospace;
        font-weight: bold;
        color: var(--color-text-primary, #1C1C1E);
      }

      .gnss-actions {
        display: flex;
        justify-content: flex-end;
        gap: 12px;
      }

      .btn-recalibrate {
        font-family: var(--font-family-ui, "Univers LT Std", "Univers", Arial, sans-serif);
        font-weight: 700;
        font-size: 1rem; /* 16px */
        background-color: var(--color-primary-pure, #0033A0);
        color: var(--color-neutral-white, #FFFFFF);
        border: none;
        border-radius: 4px;
        padding: 12px 24px;
        min-height: 48px; /* Target size de 48px conforme diretriz mobile WCAG 2.5.8 */
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        transition: background-color 0.2s ease;
      }

      .btn-recalibrate:hover {
        background-color: var(--color-primary-dark, #002680);
      }

      .btn-recalibrate:active {
        background-color: var(--color-primary-light, #3366CC);
      }

      /* Outline customizado para foco não obscurecido (WCAG 2.4.11/2.4.13) */
      .btn-recalibrate:focus-visible {
        outline: 3px solid var(--color-primary-pure, #0033A0);
        outline-offset: 2px;
      }

      /* Estilo dinâmico para ícone rotativo no estado de carregamento */
      .rotating {
        animation: spin 2s linear infinite;
      }

      @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
      }
    `;
    shadow.appendChild(style);

    // --- 2. CONTAINER PRINCIPAL ---
    const trackerDiv = document.createElementNS(ns, 'div');
    trackerDiv.className = 'gnss-tracker';
    trackerDiv.setAttributeNS(null, 'id', 'tracker-card');
    trackerDiv.setAttributeNS(null, 'data-status', 'loading');
    trackerDiv.setAttributeNS(null, 'lang', 'pt');
    trackerDiv.setAttributeNS(null, 'xml:lang', 'pt');

    // --- 3. HEADER ---
    const header = document.createElementNS(ns, 'div');
    header.className = 'gnss-header';

    // 3.1 Container do Ícone
    const iconContainer = document.createElementNS(ns, 'div');
    iconContainer.className = 'gnss-icon-container';
    iconContainer.setAttributeNS(null, 'id', 'icon-box');

    const iconSlot = document.createElementNS(ns, 'slot');
    iconSlot.setAttributeNS(null, 'name', 'icon');
    // Ícone SVG padrão (inserido como fallback via texto)
    const svgFallback = document.createElementNS(ns, 'span');
    svgFallback.setAttributeNS(null, 'id', 'status-icon-fallback');
    svgFallback.textContent = '🛰️';
    iconSlot.appendChild(svgFallback);

    iconContainer.appendChild(iconSlot);
    header.appendChild(iconContainer);

    // 3.2 Status
    const statusDiv = document.createElementNS(ns, 'div');
    statusDiv.className = 'gnss-status';
    statusDiv.setAttributeNS(null, 'id', 'status-title');
    statusDiv.setAttributeNS(null, 'role', 'status');
    statusDiv.setAttributeNS(null, 'aria-live', 'polite');

    const msgSlot = document.createElementNS(ns, 'slot');
    msgSlot.setAttributeNS(null, 'name', 'status-message');
    const fallbackText = document.createElementNS(ns, 'span');
    fallbackText.setAttributeNS(null, 'id', 'status-text-fallback');
    fallbackText.textContent = 'Aguardando sinal dos satélites...';
    msgSlot.appendChild(fallbackText);

    statusDiv.appendChild(msgSlot);
    header.appendChild(statusDiv);

    trackerDiv.appendChild(header);

    // --- 4. DATA DISPLAY ---
    const dataDiv = document.createElementNS(ns, 'div');
    dataDiv.className = 'gnss-data';
    dataDiv.setAttributeNS(null, 'role', 'region');
    dataDiv.setAttributeNS(null, 'aria-label', 'Dados Geodésicos de Campo');

    const dataRows = [
      { id: 'lat', label: 'Latitude:', valueId: 'lat-val' },
      { id: 'long', label: 'Longitude:', valueId: 'long-val' },
      { id: 'hdop', label: 'HDOP:', valueId: 'hdop-val' },
      { id: 'precision', label: 'Precisão Horizontal (σₕ):', valueId: 'precision-val' }
    ];

    dataRows.forEach((row) => {
      const rowDiv = document.createElementNS(ns, 'div');
      rowDiv.className = 'data-row';

      const label = document.createElementNS(ns, 'span');
      label.className = 'data-label';
      label.setAttributeNS(null, 'id', 'lbl-' + row.id);
      label.textContent = row.label;

      const value = document.createElementNS(ns, 'span');
      value.className = 'data-value';
      value.setAttributeNS(null, 'id', row.valueId);
      value.setAttributeNS(null, 'aria-labelledby', 'lbl-' + row.id);
      value.textContent = '-';

      rowDiv.appendChild(label);
      rowDiv.appendChild(value);
      dataDiv.appendChild(rowDiv);
    });

    trackerDiv.appendChild(dataDiv);

    // --- 5. AÇÕES ---
    const actionsDiv = document.createElementNS(ns, 'div');
    actionsDiv.className = 'gnss-actions';

    const actionsSlot = document.createElementNS(ns, 'slot');
    actionsSlot.setAttributeNS(null, 'name', 'actions');

    // Botão padrão (fallback)
    const defaultBtn = document.createElementNS(ns, 'button');
    defaultBtn.setAttributeNS(null, 'type', 'button');
    defaultBtn.className = 'btn-recalibrate';
    defaultBtn.setAttributeNS(null, 'id', 'recalibrate-btn');
    defaultBtn.setAttributeNS(null, 'aria-label', 'Recalibrar sinal dos satélites');
    defaultBtn.textContent = '🔄 Recalibrar';
    actionsSlot.appendChild(defaultBtn);

    actionsDiv.appendChild(actionsSlot);
    trackerDiv.appendChild(actionsDiv);

    shadow.appendChild(trackerDiv);
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
    const btn = this.shadowRoot.getElementById('recalibrate-btn');
    if (btn && this._recalibrateHandler) {
      btn.removeEventListener('click', this._recalibrateHandler);
      this._recalibrateHandler = null;
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

    // Simulação do comportamento assíncrono do sensor físico do DMC
    if (this._recalibrateTimeout) {
      clearTimeout(this._recalibrateTimeout);
    }
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
    const iconFallback = shadow.getElementById('status-icon-fallback');

    // Sincroniza o atributo do dataset do card de container para reatividade CSS
    if (card) {
      card.setAttribute('data-status', this._status);
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

    // Atualiza classes CSS e estado de rotação do ícone fallback
    if (iconFallback) {
      if (this._status === 'loading') {
        iconFallback.style.display = 'inline-block';
        iconFallback.style.animation = 'spin 2s linear infinite';
      } else {
        iconFallback.style.display = 'inline-block';
        iconFallback.style.animation = 'none';
      }
    }
  }
}

// Registro global seguro e semântico do Custom Element na CustomElementRegistry do W3C
if (!customElements.get('br-gnss-tracker')) {
  customElements.define('br-gnss-tracker', BrGnssTracker);
}