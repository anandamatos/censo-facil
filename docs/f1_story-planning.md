# 📋 Exemplo de Cards de Stories - Projeto "Censo Fácil"

## Baseado no modelo do card STORY-M1-CORE-001

---

## 🎯 STORY-F1-UX-001.1: Criação da Persona "Seu José"

```markdown
## 📖 User Story
Como UX Researcher, quero criar uma persona detalhada do produtor rural para orientar as decisões de design do "Censo Fácil", garantindo que a solução atenda às necessidades reais do público-alvo do Censo Agropecuário.

## ✅ Critérios de Aceite
- [ ] Persona com nome, idade, ocupação e escolaridade definidos
- [ ] Nível de alfabetização digital mapeado (smartphone básico, uso limitado de apps)
- [ ] Dores e necessidades no contexto do Censo identificadas
- [ ] Mapeamento nos 5 planos de Garrett (Estratégia, Escopo, Estrutura, Esqueleto, Superfície)
- [ ] Card da persona criado com foto, citação, bio, objetivos e frustrações
- [ ] Persona validada com stakeholders do IBGE/SGD

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-001.1.1: Levantamento de dados demográficos do produtor rural (IBGE, Censo Agropecuário anterior)
- [ ] TASK-F1-UX-001.1.2: Definição do perfil tecnológico (smartphone básico, conectividade limitada)
- [ ] TASK-F1-UX-001.1.3: Mapeamento de dores e necessidades no contexto do Censo
- [ ] TASK-F1-UX-001.1.4: Aplicação dos 5 planos de Garrett (Estratégia → Superfície)
- [ ] TASK-F1-UX-001.1.5: Criação do card da persona (nome, foto, citação, bio, objetivos, frustrações)
- [ ] TASK-F1-UX-001.1.6: Validação com stakeholders do IBGE

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-001.1
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 3 Story Points
**Prioridade:** P0
**Épico:** EPIC-F1-UX-001
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-research` `doc`

## 📚 Referências e Links de Estudo

### Documentos Oficiais
- **Manual do Recenseador do Censo Agropecuário (CD-1.09)** – Perfil do produtor rural e procedimentos de campo
  - 🔗 https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5723.pdf
- **Censo Agropecuário 2017 – Resultados Preliminares** – Dados demográficos do produtor rural
  - 🔗 https://censoagro2017.ibge.gov.br/
- **Política Nacional de Desenvolvimento Sustentável dos Povos e Comunidades Tradicionais (Decreto 6.040/2007)** – Comunidades tradicionais no contexto do Censo
  - 🔗 https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/decreto/d6040.htm

### UX Research
- **5 Planos de Garrett (The Elements of User Experience)** – Modelo conceitual para estruturação de personas
  - 🔗 https://www.jjg.net/elements/
- **Design Thinking: O Triplo Diamante** – Metodologia de pesquisa centrada no usuário
  - 🔗 https://www.zendesk.com.br/blog/design-thinking/

### Geografia Agrária
- **Estrutura Fundiária Brasileira** – Contexto do produtor rural
  - 🔗 https://www.ibge.gov.br/geociencias/
```

---

## 🖌️ STORY-F2-UX-001.3: Especificação do Componente br-gnss-tracker

```markdown
## 📖 User Story
Como UX/UI Designer, quero especificar o componente customizado `br-gnss-tracker` para captura de coordenadas GNSS, para que os recenseadores possam georreferenciar estabelecimentos agropecuários com precisão em áreas remotas.

## ✅ Critérios de Aceite
- [ ] Nome e propósito do componente definidos
- [ ] Propriedades (slots, atributos) especificadas
- [ ] Estados operacionais definidos (HDOP ótimo/aceitável/rejeitado)
- [ ] Regras de acessibilidade (e-MAG) documentadas
- [ ] Variáveis CSS customizáveis definidas
- [ ] Documentação do componente validada com time de engenharia

## 📋 Tarefas (Checklist)
- [ ] TASK-F2-UX-001.3.1: Definição do nome e propósito do componente
- [ ] TASK-F2-UX-001.3.2: Especificação de propriedades (slots, atributos)
- [ ] TASK-F2-UX-001.3.3: Definição de estados operacionais (HDOP)
- [ ] TASK-F2-UX-001.3.4: Especificação de regras de acessibilidade (e-MAG)
- [ ] TASK-F2-UX-001.3.5: Definição de variáveis CSS customizáveis
- [ ] TASK-F2-UX-001.3.6: Validação com time de engenharia

---
## 🏷️ Metadados
**ID:** STORY-F2-UX-001.3
**Squad:** UX & Experience + Foundation
**Fase:** Fase 2
**Tipo:** Story
**Estimativa:** 5 Story Points
**Prioridade:** P0
**Épico:** EPIC-F2-UX-001
**Responsável:** @executor-unico
**Labels:** `story` `fase-2` `ux-design` `frontend` `ds`

## 📚 Referências e Links de Estudo

### Documentos Oficiais
- **Manual do Recenseador – Captura de Coordenadas GNSS** – Procedimentos e validação de HDOP < 5.0m
  - 🔗 https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5723.pdf (Capítulo 4)
- **e-MAG 3.1 – Área de Comportamento** – Operabilidade por teclado e interação
  - 🔗 https://emag.governoeletronico.gov.br/
- **DSGov 4.0 – Web Components (@govbr-ds/webcomponents)** – Padrão de componentes do Governo Federal
  - 🔗 https://www.gov.br/ds/padroes/visao-geral

### Tecnologias Web
- **Custom Elements Manifest (CEM)** – Documentação de Web Components
  - 🔗 https://github.com/webcomponents/custom-elements-manifest
- **Web Components (MDN)** – Documentação oficial
  - 🔗 https://developer.mozilla.org/en-US/docs/Web/API/Web_components
- **Shadow DOM (MDN)** – Encapsulamento de componentes
  - 🔗 https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM

### Acessibilidade
- **WCAG 2.2 AA – Critério 2.5.8 (Target Size)** – Área de toque mínima de 24x24px
  - 🔗 https://www.w3.org/TR/WCAG22/#target-size-minimum
- **WAI-ARIA Authoring Practices** – Práticas para componentes interativos
  - 🔗 https://www.w3.org/WAI/ARIA/apg/
```

---

## 💻 STORY-F3-FND-001.1: Implementação do Componente br-gnss-tracker

```markdown
## 📖 User Story
Como desenvolvedor frontend, quero implementar o Web Component `br-gnss-tracker` em XHTML com Shadow DOM, para que os recenseadores possam capturar coordenadas GNSS diretamente no Dispositivo Móvel de Coleta (DMC) em áreas sem conectividade.

## ✅ Critérios de Aceite
- [ ] Web Component implementado com Shadow DOM (@govbr-ds/webcomponents)
- [ ] Validação de HDOP com níveis ótimo/aceitável/rejeitado
- [ ] XHTML Estrito (tags minúsculas, fechamento obrigatório, atributos entre aspas)
- [ ] Manipulação DOM com `createElementNS` para garantir namespace XHTML
- [ ] CDATA encapsulando scripts inline
- [ ] Mensagens de erro acessíveis (e-MAG)
- [ ] Testes de integração com a API de geolocalização

## 📋 Tarefas (Checklist)
- [ ] TASK-F3-FND-001.1.1: Criar estrutura do Web Component com Shadow DOM
- [ ] TASK-F3-FND-001.1.2: Implementar validação de HDOP (3 níveis)
- [ ] TASK-F3-FND-001.1.3: Garantir conformidade XHTML (tags, atributos)
- [ ] TASK-F3-FND-001.1.4: Implementar `createElementNS` para DOM
- [ ] TASK-F3-FND-001.1.5: Encapsular scripts com CDATA
- [ ] TASK-F3-FND-001.1.6: Adicionar mensagens de erro acessíveis
- [ ] TASK-F3-FND-001.1.7: Escrever testes de integração

---
## 🏷️ Metadados
**ID:** STORY-F3-FND-001.1
**Squad:** Foundation + Core Business
**Fase:** Fase 3
**Tipo:** Story
**Estimativa:** 8 Story Points
**Prioridade:** P0
**Épico:** EPIC-F3-FND-001
**Responsável:** @executor-unico
**Labels:** `story` `fase-3` `frontend` `backend` `code` `test`

## 📚 Referências e Links de Estudo

### Tecnologias Web (XHTML, ES6, DOM)
- **XHTML 1.0 Strict – Especificação W3C** – Regras de sintaxe (tags minúsculas, fechamento obrigatório)
  - 🔗 https://www.w3.org/TR/xhtml1/
- **JavaScript ES6 Modules (import/export)** – Documentação MDN
  - 🔗 https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules
- **DOM Level 2 – createElementNS** – Manipulação com namespaces XML
  - 🔗 https://developer.mozilla.org/en-US/docs/Web/API/Document/createElementNS
- **CDATA Sections (MDN)** – Encapsulamento de scripts para parsers XML
  - 🔗 https://developer.mozilla.org/en-US/docs/Web/API/CDATASection

### Offline-first e LGPD
- **Service Workers (MDN)** – Cache e sincronização offline
  - 🔗 https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API
- **Web Crypto API (MDN)** – Criptografia AES-256 para dados locais
  - 🔗 https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API
- **LGPD – Lei nº 13.709/2018** – Proteção de dados pessoais
  - 🔗 https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm

### Integração Gov.br
- **Barra Gov.Br – Documentação Oficial** – Padrão de Governo Digital
  - 🔗 https://www.gov.br/ds/padroes/visao-geral
- **OpenID Connect (OIDC) – Documentação** – Autenticação federada
  - 🔗 https://openid.net/developers/specs/

### Design System e Acessibilidade
- **DSGov 4.0 – Web Components (@govbr-ds/webcomponents)**
  - 🔗 https://www.gov.br/ds/padroes/visao-geral
- **e-MAG 3.1 – Área de Marcação** – Conformidade com padrões de acessibilidade
  - 🔗 https://emag.governoeletronico.gov.br/
- **WCAG 2.2 AA – Critério 2.4.11 (Focus Not Obscured)**
  - 🔗 https://www.w3.org/TR/WCAG22/#focus-not-obscured-minimum
```

---

## 📚 Referências Gerais por Disciplina

### 🎯 UX/UI e Design

| Disciplina | Recurso | Link |
|:---|:---|:---|
| **5 Planos de Garrett** | The Elements of User Experience | https://www.jjg.net/elements/ |
| **10 Heurísticas de Nielsen** | NN/g – 10 Heuristics for User Interface Design | https://www.nngroup.com/articles/ten-usability-heuristics/ |
| **LATCH (Arquitetura da Informação)** | Evernote – LATCH Method | https://evernote.com/learn/what-is-the-latch-method-method-a-practical-guide |
| **Leis da Gestalt** | Smashing Magazine – Gestalt Principles | https://www.smashingmagazine.com/2014/03/design-principles-visual-perception-and-the-principles-of-gestalt/ |
| **UX Writing** | Google – UX Writing Hub | https://uxwritinghub.com/ |

### 🏛️ Acessibilidade e Governo Digital

| Disciplina | Recurso | Link |
|:---|:---|:---|
| **e-MAG 3.1** | Modelo de Acessibilidade em Governo Eletrônico | https://emag.governoeletronico.gov.br/ |
| **WCAG 2.2 AA** | Web Content Accessibility Guidelines | https://www.w3.org/TR/WCAG22/ |
| **DSGov 4.0** | Padrão Digital de Governo | https://www.gov.br/ds/padroes/visao-geral |
| **Ferramenta de Avaliação Gov.br** | Avaliação de Serviços Digitais | https://www.gov.br/governodigital/pt-br/plataformas-e-servicos-digitais/ferramenta-de-avaliacao |
| **Barra Gov.Br** | Componente oficial do Governo Federal | https://www.gov.br/ds/padroes/visao-geral |

### 🔤 Tipografia e Identidade Visual

| Disciplina | Recurso | Link |
|:---|:---|:---|
| **Manual de Identidade Visual IBGE** | Política de Comunicação do IBGE | https://www.ibge.gov.br/np_download/novoportal/documentos_institucionais/politica_de_comunicacao_2ed_2016.pdf |
| **Neuropolitical / Univers** | Manual do Censo Agropecuário | https://censoagro2017.ibge.gov.br/media/com_mediaibge/arquivos/eef5f0ccde06ff68919a3e9fc940f06a.pdf |
| **Azul IBGE (Pantone 286 C)** | Especificações CMYK/RGB/HEX | https://www.ibge.gov.br/ |

### 💻 Tecnologias Web

| Disciplina | Recurso | Link |
|:---|:---|:---|
| **XHTML 1.0 Strict** | W3C Specification | https://www.w3.org/TR/xhtml1/ |
| **JavaScript ES6 Modules** | MDN – Modules | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules |
| **DOM Level 2 – createElementNS** | MDN – Document.createElementNS() | https://developer.mozilla.org/en-US/docs/Web/API/Document/createElementNS |
| **CDATA Sections** | MDN – CDATASection | https://developer.mozilla.org/en-US/docs/Web/API/CDATASection |
| **Web Components** | MDN – Web Components | https://developer.mozilla.org/en-US/docs/Web/API/Web_components |
| **Service Workers** | MDN – Service Worker API | https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API |
| **Web Crypto API** | MDN – Web Crypto API | https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API |

### ⚖️ Legislação e Regulamentação

| Disciplina | Recurso | Link |
|:---|:---|:---|
| **Lei 8.112/90** | Regime Jurídico dos Servidores Públicos | https://www2.camara.leg.br/legin/fed/lei/1990/lei-8112-11-dezembro-1990-322161-publicacaooriginal-1-pl.html |
| **Lei 8.745/93** | Contratação Temporária de Excepcional Interesse Público | https://www2.camara.leg.br/legin/fed/lei/1993/lei-8745-9-dezembro-1993-363171-publicacaooriginal-1-pl.html |
| **LGPD – Lei 13.709/2018** | Lei Geral de Proteção de Dados | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm |

---

## 🎯 Resumo dos Cards Criados

| Story | ID | Fase | Estimativa | Prioridade |
|:---|:---|:---|:---|:---|
| Criação da Persona "Seu José" | STORY-F1-UX-001.1 | Fase 1 | 3 | P0 |
| Especificação do Componente br-gnss-tracker | STORY-F2-UX-001.3 | Fase 2 | 5 | P0 |
| Implementação do Componente br-gnss-tracker | STORY-F3-FND-001.1 | Fase 3 | 8 | P0 |