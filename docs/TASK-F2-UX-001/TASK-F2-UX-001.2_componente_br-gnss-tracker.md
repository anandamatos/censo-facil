# 🛰️ Especificação Técnica: Componente `br-gnss-tracker`

## Para o Sistema "Censo Fácil" — 12º Censo Agropecuário IBGE 2026

---

## 1. Contexto e Fundamentação

O `br-gnss-tracker` é um **Web Component** nativo projetado para encapsular a lógica de captura de sinais GNSS no sistema "Censo Fácil", fornecendo feedback visual imediato e aplicando as regras de consistência lógica exigidas pelo IBGE para o georreferenciamento de estabelecimentos agropecuários.

A captura precisa de coordenadas geográficas é fundamental para a qualidade dos dados censitários. O Manual do Recenseador estabelece que a localização correta dos estabelecimentos é essencial para evitar omissões e sobreposições durante a cobertura do setor censitário. Em áreas rurais, onde as unidades são mais dispersas e as referências de endereço são menos estruturadas, o georreferenciamento confiável torna-se ainda mais crítico.

O componente atua como uma **trava de qualidade geodésica**, bloqueando o encerramento do questionário quando a precisão do sinal é insuficiente, garantindo a integridade da base cartográfica do Censo Agropecuário.

---

## 2. Propriedades e Atributos (Reatividade)

O componente utiliza atributos observados para garantir que a interface reflita instantaneamente as mudanças na qualidade do sinal captado pelo Dispositivo Móvel de Coleta (DMC).

| Atributo | Tipo | Valor Padrão | Descrição |
|----------|------|--------------|-----------|
| `hdop` | Number | `null` | Valor da diluição de precisão horizontal do sensor. O HDOP é um indicador da qualidade da constelação de satélites — quanto menor o valor, melhor a precisão. |
| `lat` | Number | `0.0` | Coordenada de latitude capturada em tempo real. |
| `long` | Number | `0.0` | Coordenada de longitude capturada em tempo real. |
| `status` | String | `'loading'` | Estado operacional: `optimal`, `acceptable`, `insufficient` ou `error`. |
| `precision` | Number | `10.0` | Incerteza calculada (σₕ = HDOP × σ₀) em metros, conforme o Manual do Recenseador. |

**Conformidade com Padrões de Web Components:**

Segundo a especificação do WHATWG, o construtor do elemento customizado deve ser utilizado para configurar o estado inicial e valores padrão, bem como para configurar ouvintes de eventos e, possivelmente, uma shadow root. O trabalho que envolve busca de recursos ou renderização deve ser adiado para o `connectedCallback` tanto quanto possível, pois o `connectedCallback` pode ser chamado mais de uma vez .

---

## 3. Estados Operacionais e Regras de Campo

Conforme o rigor metodológico do Censo Agropecuário, o registro automatizado é condicionado aos seguintes limiares de precisão:

| Estado | Condição | Indicador | Mensagem | Ação do Sistema |
|--------|----------|-----------|----------|-----------------|
| **🟢 Ótimo** | HDOP ≤ 2.5m | Verde | "Precisão ótima para registro" | Permite a continuidade da coleta |
| **🟡 Aceitável** | 2.5m < HDOP ≤ 5.0m | Amarelo | "Precisão aceitável" | Orienta o agente a buscar um local mais aberto |
| **🔴 Insuficiente** | HDOP > 5.0m | Vermelho | "Sinal bloqueado" | **Bloqueia o encerramento do questionário** |

A exigência de HDOP inferior a 5.0 metros está alinhada com as práticas estabelecidas para o georreferenciamento em operações censitárias. Conforme o Manual do Recenseador, a precisão do sinal é essencial para garantir a integridade da base cartográfica e evitar inconsistências nos dados de localização .

---

## 4. API de Eventos (Interação com a Aplicação)

Permite que o "Censo Fácil" reaja às atualizações do sensor de forma assíncrona:

| Evento | Descrição | Payload |
|--------|-----------|---------|
| `br-position-update` | Disparado a cada mudança de coordenadas | `{ lat, long, precision }` |
| `br-status-change` | Emitido quando a precisão cruza os limiares de estado | `{ previousStatus, currentStatus, hdop }` |
| `br-gnss-error` | Disparado em caso de falha de hardware ou permissão negada | `{ code, message }` |

**Documentação de Eventos com JSDoc:**

A especificação do Custom Elements Manifest recomenda o uso de JSDoc para documentar eventos, utilizando as tags `@fires` ou `@event` . Isso permite que ferramentas de documentação e IDEs reconheçam e forneçam autocompletar para os eventos do componente.

```javascript
/**
 * @fires br-position-update - Emitido a cada mudança de posição. Payload: { lat, long, precision }
 * @fires br-status-change - Emitido quando a precisão cruza os limiares de estado.
 * @fires br-gnss-error - Disparado em caso de falha de hardware ou permissão negada.
 */
class BrGnssTracker extends HTMLElement {
  // ...
}
```

---

## 5. Especificação de Slots

Permite a personalização de elementos internos mantendo o encapsulamento do **Shadow DOM**:

| Slot | Descrição |
|------|-----------|
| `icon` | Substitui o ícone padrão de satélite |
| `status-message` | Permite injetar orientações contextuais ou traduções em Linguagem Simples, conforme o Manual do Recenseador |
| `actions` | Espaço para botões de suporte, como o atalho para o Manual do Recenseador |

A documentação de slots é suportada pelo Custom Elements Manifest através da tag JSDoc `@slot` . Para slots sem nome, utiliza-se `@slot -` .

---

## 6. Acessibilidade e Comportamento (e-MAG 3.1 e WCAG 2.2 AA)

Para garantir que agentes e produtores operem o sistema sem barreiras, aplicam-se as seguintes regras:

### 6.1 Regiões Vivas (aria-live)

O container de status utiliza `aria-live="polite"` para anunciar mudanças de precisão sem interromper o preenchimento. Este padrão está em conformidade com a Área de Comportamento do e-MAG 3.1.

### 6.2 Independência de Cor

Todos os estados coloridos são acompanhados por ícones distintos e rótulos textuais explícitos (ex: "Sinal Bloqueado"), atendendo ao critério do e-MAG e ao WCAG 2.2 (Critério 1.4.1 — Uso de Cor).

### 6.3 Target Size (WCAG 2.2 — 2.5.8)

A WCAG 2.2, oficialmente uma recomendação do W3C desde outubro de 2023, estabelece que alvos interativos devem ter um tamanho mínimo de **24x24 pixels CSS** para conformidade com o Nível AA. Alvos com tamanho inferior a 24x24px devem ter pelo menos 24px de espaçamento entre si.

**Especificação do Componente:**

| Tipo de Alvo | Tamanho | Justificativa |
|--------------|---------|---------------|
| Alvos padrão | 24×24px CSS | Mínimo exigido pela WCAG 2.2 (2.5.8) |
| **Botões críticos no DMC** | **48×48px CSS** | Recomendado para uso em campo, superando o mínimo |

> **Nota:** A Apple iOS recomenda 44×44 pontos como mínimo para alvos de toque, e a Google Android recomenda 48×48 dp. A especificação do componente adota 48x48px para botões críticos, alinhando-se com as melhores práticas de plataformas móveis .

### 6.4 Foco Não Obscurecido (WCAG 2.2 — 2.4.11)

O indicador de foco deve ter contraste mínimo de 3:1 contra as cores adjacentes e não pode ser obscurecido por componentes fixos, como a Barra Gov.Br. Este critério é essencial para usuários de teclado e pessoas com baixa visão.

### 6.5 Aparência do Foco (WCAG 2.2 — 2.4.11)

O indicador de foco deve ter uma área mínima equivalente ao perímetro de 2px do componente não focado e contraste de 3:1. Recomenda-se o uso de `outline` com `outline-offset` para garantir visibilidade em diferentes fundos.

```css
:host(:focus-visible) {
  outline: 3px solid var(--color-primary-pure);
  outline-offset: 2px;
  border-radius: 2px;
}
```

---

## 7. Custom Elements Manifest (CEM) — Fragmento JSON

O **Custom Elements Manifest** é um formato padronizado para documentação de Web Components, permitindo que ferramentas de desenvolvimento, linters e geradores de documentação reconheçam e forneçam informações sobre os componentes .

O manifesto deve ser incluído no `package.json` do componente através da propriedade `"customElements": "./custom-elements.json"`, permitindo que ferramentas o encontrem facilmente.

```json
{
  "schemaVersion": "1.0.0",
  "readme": "",
  "modules": [
    {
      "kind": "javascript-module",
      "path": "src/br-gnss-tracker.js",
      "declarations": [
        {
          "kind": "class",
          "name": "BrGnssTracker",
          "tagName": "br-gnss-tracker",
          "description": "Componente para captura de coordenadas com validação de precisão HDOP.",
          "attributes": [
            { "name": "hdop", "type": { "text": "number" }, "description": "Valor da diluição de precisão horizontal" },
            { "name": "status", "type": { "text": "string" }, "description": "Estado operacional: optimal, acceptable, insufficient, error" }
          ],
          "events": [
            { "name": "br-position-update", "description": "Emitido na mudança de posição. Payload: { lat, long, precision }" }
          ],
          "slots": [
            { "name": "status-message", "description": "Área para orientações ao usuário (Linguagem Simples)" }
          ]
        }
      ]
    }
  ]
}
```

A ferramenta `@custom-elements-manifest/analyzer` pode gerar este manifesto automaticamente a partir do código-fonte, utilizando JSDoc para extrair informações adicionais .

---

## 8. Segurança e Privacidade (LGPD)

Todas as coordenadas capturadas são serializadas e encriptadas via **AES-256** no IndexedDB local antes da sincronização, garantindo conformidade com a **LGPD**.

A LGPD estabelece que dados pessoais sensíveis devem ser protegidos por medidas técnicas e administrativas. A criptografia AES-256 em repouso e em trânsito é uma prática recomendada para proteção de dados pessoais.

**Requisitos de Implementação:**

| Camada | Tecnologia | Justificativa |
|--------|------------|---------------|
| **Dados em repouso** | AES-256 via Web Crypto API | Proteção de dados locais no IndexedDB |
| **Derivação de chaves** | PBKDF2 com salt | Prevenção contra ataques de força bruta |
| **Dados em trânsito** | TLS 1.3 | Criptografia em canais de comunicação |
| **Descarte seguro** | Remoção imediata após sincronização | Direito ao esquecimento (Art. 18 da LGPD) |

---

## 9. Referências

### Manuais e Documentos Oficiais do IBGE
1. IBGE. **Manual do Recenseador do Censo Demográfico 2022 (CD-1.09)** . Disponível em: https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5723.pdf.

2. IBGE. **Manual do Recenseador em Áreas Indígenas e Quilombolas (CD-1.18)** . Disponível em: https://censo2022.ibge.gov.br/component/rsfiles/download-file/files.html?path=censo2021%252Fmanuais%252FCD_1_18_Manual_Recenseador_PCT_ebook.pdf&Itemid=7959.

3. IBGE. **Instruções Operacionais para Supervisores (CA 2.10 – Manual do ACS/ACM)** . Disponível em: https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc0934.pdf.

### Padrões Web e Acessibilidade
4. WHATWG. **HTML Standard — Custom Elements**. Disponível em: https://html.spec.whatwg.org/multipage/custom-elements.html.

5. W3C. **Web Content Accessibility Guidelines (WCAG) 2.2**. Disponível em: https://www.w3.org/TR/WCAG22/.

6. W3C. **Custom Elements Manifest Specification**. Disponível em: https://github.com/webcomponents/custom-elements-manifest.

7. Open Web Components. **Getting Started: Custom Elements Manifest Analyzer**. Disponível em: https://custom-elements-manifest.open-wc.org/analyzer/getting-started/.

### Legislação
8. BRASIL. **Lei nº 13.709, de 14 de agosto de 2018 (LGPD)** . Lei Geral de Proteção de Dados Pessoais. Disponível em: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm.

---

**Versão:** 1.0
**Data:** Agosto 2026
**Status:** ✅ Especificação validada com DSGov 4.0, e-MAG 3.1 e WCAG 2.2 AA