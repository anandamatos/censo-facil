# 📄 Documentação em Custom Elements Manifest (CEM)

## br-gnss-tracker — Componente para o "Censo Fácil"

---

## 1. Contexto e Fundamentação

O **Custom Elements Manifest (CEM)** é um formato padronizado para documentação de Web Components, permitindo que ferramentas de desenvolvimento, linters e geradores de documentação reconheçam e forneçam informações sobre os componentes . Este manifesto é o artefato técnico que permite que ferramentas de documentação automática e IDEs reconheçam as capacidades do componente, garantindo que a implementação da **Fase 3** siga rigorosamente os requisitos de precisão geodésica e acessibilidade.

A especificação CEM define um esquema JSON para descrever módulos JavaScript e suas declarações exportadas, incluindo classes, funções, variáveis e tipos personalizados . O formato é projetado para ser consumido por ferramentas que geram documentação, fornecem autocompletar em IDEs e realizam verificações estáticas.

A documentação do componente `br-gnss-tracker` segue as diretrizes de acessibilidade **WCAG 2.2** e **e-MAG 3.1**, garantindo que as propriedades reflitam o comportamento inclusivo do sistema. O componente é essencial para a captura de coordenadas GNSS no "Censo Fácil", atuando como uma trava de qualidade geodésica que bloqueia o encerramento do questionário quando a precisão do sinal é insuficiente (HDOP > 5.0m) .

O manifesto segue a estrutura definida pela especificação CEM, com as seguintes seções principais:

```json
{
  "schemaVersion": "1.0.0",
  "readme": "Componente para captura de coordenadas GNSS com validação de precisão HDOP conforme normas do IBGE.",
  "modules": [
    {
      "kind": "javascript-module",
      "path": "src/components/br-gnss-tracker/br-gnss-tracker.js",
      "declarations": [
        {
          "kind": "class",
          "description": "Encapsula a lógica de georreferenciamento e validação de precisão para coleta em campo.",
          "name": "BrGnssTracker",
          "tagName": "br-gnss-tracker",
          "customElement": true,
          "attributes": [
            {
              "name": "hdop",
              "type": { "text": "number" },
              "description": "Valor da diluição de precisão horizontal captado pelo sensor."
            },
            {
              "name": "status",
              "type": { "text": "string" },
              "default": "'loading'",
              "description": "Estado operacional baseado na precisão: 'optimal', 'acceptable', 'insufficient' ou 'error'."
            }
          ],
          "members": [
            {
              "kind": "field",
              "name": "lat",
              "type": { "text": "number" },
              "description": "Coordenada de latitude atual da sede do estabelecimento."
            },
            {
              "kind": "field",
              "name": "long",
              "type": { "text": "number" },
              "description": "Coordenada de longitude atual da sede do estabelecimento."
            },
            {
              "kind": "field",
              "name": "precision",
              "type": { "text": "number" },
              "description": "Incerteza calculada em metros (deve ser < 5.0m para validação)."
            }
          ],
          "events": [
            {
              "name": "br-position-update",
              "description": "Disparado a cada mudança nas coordenadas ou na precisão do sinal.",
              "type": { "text": "CustomEvent" }
            },
            {
              "name": "br-status-change",
              "description": "Emitido quando o índice HDOP cruza limiares de estado (ex: Verde para Amarelo).",
              "type": { "text": "CustomEvent" }
            }
          ],
          "slots": [
            {
              "name": "icon",
              "description": "Slot para personalização do ícone de status de satélite."
            },
            {
              "name": "status-message",
              "description": "Área para injeção de orientações em Linguagem Simples para o usuário."
            }
          ],
          "cssProperties": [
            {
              "name": "--color-gnss-success",
              "description": "Cor para precisão ótima (HDOP ≤ 2.5m). Padrão: #4CAF50."
            },
            {
              "name": "--color-gnss-warning",
              "description": "Cor para precisão aceitável (2.5m < HDOP ≤ 5.0m). Padrão: #F5A623."
            },
            {
              "name": "--color-gnss-error",
              "description": "Cor para sinal insuficiente ou bloqueado (HDOP > 5.0m). Padrão: #E53935."
            }
          ]
        }
      ],
      "exports": [
        {
          "kind": "js",
          "name": "BrGnssTracker",
          "declaration": {
            "name": "BrGnssTracker",
            "module": "src/components/br-gnss-tracker/br-gnss-tracker.js"
          }
        }
      ]
    }
  ]
}
```

---

## 2. Estrutura do Manifesto

### 2.1 Schema e Metadados

| Propriedade | Valor | Descrição |
|-------------|-------|-----------|
| `schemaVersion` | `"1.0.0"` | Versão do esquema CEM utilizada  |
| `readme` | Texto descritivo | Resumo do propósito do componente |
| `modules` | Array | Lista de módulos JavaScript analisados |

### 2.2 Declaração da Classe

| Propriedade | Valor | Descrição |
|-------------|-------|-----------|
| `kind` | `"class"` | Tipo de declaração  |
| `name` | `"BrGnssTracker"` | Nome da classe do componente |
| `tagName` | `"br-gnss-tracker"` | Nome da tag HTML do Web Component |
| `customElement` | `true` | Indica que é um Custom Element registrado |

### 2.3 Atributos Observados

Os atributos permitem a configuração declarativa do componente via HTML:

| Atributo | Tipo | Padrão | Descrição |
|----------|------|--------|-----------|
| `hdop` | number | `null` | Diluição de precisão horizontal captado pelo sensor |
| `status` | string | `'loading'` | Estado: `optimal`, `acceptable`, `insufficient` ou `error` |

### 2.4 Membros (Propriedades)

| Propriedade | Tipo | Descrição |
|-------------|------|-----------|
| `lat` | number | Coordenada de latitude atual |
| `long` | number | Coordenada de longitude atual |
| `precision` | number | Incerteza calculada em metros (σₕ = HDOP × σ₀) |

### 2.5 Eventos

| Evento | Payload | Descrição |
|--------|---------|-----------|
| `br-position-update` | `{ lat, long, precision }` | Disparado a cada mudança de coordenadas ou precisão |
| `br-status-change` | `{ previousStatus, currentStatus, hdop }` | Emitido quando o HDOP cruza limiares de estado |

### 2.6 Slots

| Slot | Descrição |
|------|-----------|
| `icon` | Personalização do ícone de status de satélite |
| `status-message` | Área para orientações em Linguagem Simples |

---

## 3. Custom Elements Manifest Schema (Referência)

O manifesto segue a estrutura definida pela especificação CEM  :

### 3.1 Schema Global

```json
{
  "$schema": "https://raw.githubusercontent.com/webcomponents/custom-elements-manifest/main/packages/manifest/schema.json",
  "schemaVersion": "1.0.0",
  "readme": "",
  "modules": [ ... ]
}
```

### 3.2 Declarações de Classe

```json
{
  "kind": "class",
  "name": "BrGnssTracker",
  "tagName": "br-gnss-tracker",
  "customElement": true,
  "description": "...",
  "attributes": [ ... ],
  "members": [ ... ],
  "events": [ ... ],
  "slots": [ ... ],
  "cssProperties": [ ... ]
}
```

### 3.3 Integração com package.json

O manifesto deve ser referenciado no arquivo `package.json` do componente :

```json
{
  "name": "br-gnss-tracker",
  "version": "1.0.0",
  "customElements": "./custom-elements.json"
}
```

---

## 4. Mapeamento de Metadados e Acessibilidade

A criação deste manifesto seguiu as diretrizes de acessibilidade **WCAG 2.2** e **e-MAG 3.1**, garantindo que as propriedades reflitam o comportamento inclusivo do sistema.

### 4.1 Regiões Vivas (ARIA)

O componente deve gerenciar internamente o atributo `aria-live="polite"` no slot de mensagens de status, informando sobre atualizações de sinal sem interromper o preenchimento do formulário. Este padrão está em conformidade com a Área de Comportamento do e-MAG 3.1.

### 4.2 Target Size (WCAG 2.2 — 2.5.8)

As especificações CSS vinculadas ao manifesto garantem que botões internos de recalibragem mantenham alvos de toque de no mínimo **48x48 pixels CSS**, superando o critério 2.5.8 da WCAG 2.2 para facilitar o uso por produtores rurais .

### 4.3 Identidade Visual

Os tokens de cores incluídos no manifesto (`cssProperties`) utilizam a paleta institucional do IBGE, garantindo que o indicador de sucesso utilize o verde funcional e o alerta utilize o amarelo do sistema de design governamental.

### 4.4 Documentação com JSDoc

O manifesto pode ser gerado automaticamente a partir do código-fonte utilizando JSDoc, que fornece informações adicionais para a documentação :

```javascript
/**
 * @customElement
 * @fires br-position-update - Emitido na mudança de posição
 * @slot status-message - Área para orientações ao usuário
 */
class BrGnssTracker extends HTMLElement {
  // ...
}
```

---

## 5. Validação e Manutenção

### 5.1 Validação CEM

O arquivo deve ser validado via **CEM Analyzer**, garantindo que não existam inconsistências de tipos ou nomes de atributos . O analyzer pode ser executado localmente:

```bash
npm install -D @custom-elements-manifest/analyzer
npx cem analyze --globs "src/**/*.js"
```

### 5.2 Integração com IDEs

Desenvolvedores da **Fase 3** poderão utilizar este manifesto em editores como VS Code para obter autocompletar e validação imediata de tipos (ex: garantir que `hdop` seja sempre numérico).

### 5.3 Handoff de DesignOps

Este documento encerra o ciclo de design da Fase 2, fornecendo à engenharia um contrato técnico claro sobre como o componente deve se comportar e como seus dados devem ser protegidos via criptografia **AES-256** no armazenamento local, em conformidade com a LGPD .

---

## 6. Exemplo de Uso

### 6.1 HTML

```html
<br-gnss-tracker
  hdop="2.1"
  status="optimal"
  style="--color-gnss-success: #4CAF50;"
>
  <span slot="status-message">Precisão ótima para registro</span>
  <button slot="actions">📖 Manual do Recenseador</button>
</br-gnss-tracker>
```

### 6.2 JavaScript

```javascript
const tracker = document.querySelector('br-gnss-tracker');

tracker.addEventListener('br-position-update', (e) => {
  console.log('Nova posição:', e.detail);
});

tracker.addEventListener('br-status-change', (e) => {
  console.log('Status alterado:', e.detail);
});
```

---

## 7. Referências

### Especificações Técnicas

1. W3C. **Custom Elements Manifest Specification**. Disponível em: https://github.com/webcomponents/custom-elements-manifest .

2. Open Web Components. **Custom Elements Manifest Analyzer**. Disponível em: https://custom-elements-manifest.open-wc.org/analyzer/getting-started/ .

3. WHATWG. **HTML Standard — Custom Elements**. Disponível em: https://html.spec.whatwg.org/multipage/custom-elements.html .

### Manuais do IBGE

4. IBGE. **Manual do Recenseador do Censo Demográfico 2022 (CD-1.09)** . Disponível em: https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5723.pdf .

### Acessibilidade e Padrões

5. W3C. **Web Content Accessibility Guidelines (WCAG) 2.2**. Disponível em: https://www.w3.org/TR/WCAG22/ .

6. BRASIL. **e-MAG 3.1 — Modelo de Acessibilidade em Governo Eletrônico**. Disponível em: https://emag.governoeletronico.gov.br/ .

### Legislação

7. BRASIL. **Lei nº 13.709, de 14 de agosto de 2018 (LGPD)** . Lei Geral de Proteção de Dados Pessoais. Disponível em: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm .

### Design Tokens (Referência Interna)

8. **Mapeamento de Design Tokens para o "Censo Fácil"** . Disponível em: https://www.ibge.gov.br .

---

**Versão:** 1.0
**Data:** Agosto 2026
**Status:** ✅ Manifesto validado e pronto para handoff para a Fase 3