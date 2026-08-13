# Épicos do Projeto "Censo Fácil"

## Conteúdo Programático do Edital IBGE 2026

---

## 🎯 Estrutura do Documento

Este documento organiza todos os Épicos do projeto "Censo Fácil", vinculando cada um ao conteúdo programático do edital do IBGE 2026 e fornecendo referências de estudo consolidadas por disciplina.

---

## FASE 1: Pesquisa, Estratégia, Arquitetura da Informação e Acessibilidade

### 📌 EPIC-F1-UX-001: Pesquisa, Personas e Jornadas do Usuário

```
┌─────────────────────────────────────────────────────────────────┐
│  📌 EPIC-F1-UX-001: Pesquisa, Personas e Jornadas do Usuário  │
├─────────────────────────────────────────────────────────────────┤
│  🎯 Objetivo: Mapear as necessidades, comportamentos e dores  │
│     dos stakeholders do Censo Agropecuário para orientar o    │
│     design do "Censo Fácil".                                   │
│  📅 Estimativa: 2 dias                                         │
│  👤 Responsável: UX/UI Lead (FE) + Product Owner (BE)         │
│  ✅ Critério de Aceite: Personas validadas com stakeholders   │
└─────────────────────────────────────────────────────────────────┘
```

**Stories que compõem este Épico:**

| Story | Descrição | Estimativa |
|-------|-----------|------------|
| **STORY-F1-UX-001.1** | Criação da Persona "Seu José" (Produtor Rural) | 0.5 dia |
| **STORY-F1-UX-001.2** | Criação da Persona "Mariana" (Recenseadora) | 0.5 dia |
| **STORY-F1-UX-001.3** | Criação da Persona "Carlos" (Agente Censitário de Qualidade - ACQ) | 0.5 dia |
| **STORY-F1-UX-001.4** | Validação das Personas com stakeholders do IBGE | 0.5 dia |

**Conteúdo Programático do Edital:**

| Disciplina | Conteúdo | Aplicação no Épico |
|:---|:---|:---|
| **Geografia Agrária** | Caracterização do produtor rural, estrutura fundiária e comunidades tradicionais | Persona "Seu José" – dados demográficos, perfil socioeconômico, atividades agropecuárias |
| **Legislação (Lei 8.745/93)** | Contratação temporária de recenseadores | Persona "Mariana" – regime de contratação por processo seletivo simplificado, prazo de 12 meses |
| **Legislação (Lei 8.112/90)** | Regime jurídico de servidores efetivos | Persona "Carlos" – servidor público efetivo com estabilidade, papel na auditoria de dados |
| **UX/UI** | 5 planos de Garrett (Estratégia → Superfície) | Aplicação dos 5 planos na construção da Jornada do Produtor, Recenseador e ACQ |

**Referências e Links de Estudo:**

#### Documentos Oficiais do IBGE
- **Manual do Recenseador do Censo Agropecuário (CD-1.09)** – Perfil do produtor rural e procedimentos de campo
  - 🔗 https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5723.pdf
- **Censo Agropecuário 2017 – Resultados Preliminares** – Dados demográficos do produtor rural
  - 🔗 https://censoagro2017.ibge.gov.br/
- **Política Nacional de Desenvolvimento Sustentável dos Povos e Comunidades Tradicionais (Decreto 6.040/2007)**
  - 🔗 https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/decreto/d6040.htm

#### UX Research
- **5 Planos de Garrett (The Elements of User Experience)**
  - 🔗 https://www.jjg.net/elements/
- **Design Thinking: O Triplo Diamante**
  - 🔗 https://www.zendesk.com.br/blog/design-thinking/

#### Legislação
- **Lei nº 8.112/90** – Regime Jurídico dos Servidores Públicos
  - 🔗 https://www2.camara.leg.br/legin/fed/lei/1990/lei-8112-11-dezembro-1990-322161-publicacaooriginal-1-pl.html
- **Lei nº 8.745/93** – Contratação Temporária de Excepcional Interesse Público
  - 🔗 https://www2.camara.leg.br/legin/fed/lei/1993/lei-8745-9-dezembro-1993-363171-publicacaooriginal-1-pl.html

---

### 📌 EPIC-F1-UX-002: Jornadas do Usuário e Heurísticas de Nielsen

```
┌─────────────────────────────────────────────────────────────────┐
│  📌 EPIC-F1-UX-002: Jornadas do Usuário e Heurísticas         │
├─────────────────────────────────────────────────────────────────┤
│  🎯 Objetivo: Mapear as jornadas completas dos usuários e     │
│     avaliar o fluxo do "Censo Fácil" sob as 10 heurísticas   │
│     de Nielsen para identificar pontos de fricção.            │
│  📅 Estimativa: 2 dias                                         │
│  👤 Responsável: UX/UI Lead (FE)                              │
│  ✅ Critério de Aceite: Jornadas validadas e heurísticas     │
│     aplicadas ao protótipo                                    │
└─────────────────────────────────────────────────────────────────┘
```

**Stories que compõem este Épico:**

| Story | Descrição | Estimativa |
|-------|-----------|------------|
| **STORY-F1-UX-002.1** | Mapeamento da Jornada do Produtor Rural | 0.5 dia |
| **STORY-F1-UX-002.2** | Mapeamento da Jornada do Recenseador | 0.5 dia |
| **STORY-F1-UX-002.3** | Mapeamento da Jornada do ACQ | 0.5 dia |
| **STORY-F1-UX-002.4** | Análise das 10 Heurísticas de Nielsen | 0.5 dia |

**Conteúdo Programático do Edital:**

| Disciplina | Conteúdo | Aplicação no Épico |
|:---|:---|:---|
| **UX/UI** | 10 Heurísticas de Nielsen | Avaliação do fluxo do "Censo Fácil" sob as 10 heurísticas, identificando pontos de fricção |
| **Redação Oficial** | Comunicação clara e impessoal | Jornadas com linguagem acessível para diferentes perfis de usuários |
| **UX/UI** | Jornadas do Usuário (online/offline) | Diferenciação de estados online/offline para cenários de campo |

**Referências e Links de Estudo:**

#### UX/UI
- **10 Heurísticas de Nielsen – NN/g**
  - 🔗 https://www.nngroup.com/articles/ten-usability-heuristics/
- **UX Research em Governo Eletrônico (ESDI/UERJ)**
  - 🔗 https://www.esdi.uerj.br/assets/60131c71d30a78161ca77a0b959818e4/da35ec6b6c8982bcfd253b2c78eb9def.pdf
- **Dual Track Agile (Marty Cagan)**
  - 🔗 https://www.svpg.com/dual-track-agile/

#### Redação Oficial
- **Manual de Redação da Presidência da República**
  - 🔗 https://www.gov.br/planalto/pt-br/conheca-a-presidencia/acervo/manual-de-redacao

---

### 📌 EPIC-F1-UX-003: Arquitetura da Informação (LATCH e Gestalt)

```
┌─────────────────────────────────────────────────────────────────┐
│  📌 EPIC-F1-UX-003: Arquitetura da Informação                  │
├─────────────────────────────────────────────────────────────────┤
│  🎯 Objetivo: Estruturar a organização da informação do      │
│     questionário do Censo Agropecuário usando o método LATCH │
│     e os princípios da Gestalt para otimizar a navegação e   │
│     a compreensão do usuário.                                 │
│  📅 Estimativa: 2 dias                                         │
│  👤 Responsável: UX/UI Lead (FE) + Product Owner (BE)         │
│  ✅ Critério de Aceite: Matriz LATCH validada e princípios   │
│     Gestalt aplicados ao layout                               │
└─────────────────────────────────────────────────────────────────┘
```

**Stories que compõem este Épico:**

| Story | Descrição | Estimativa |
|-------|-----------|------------|
| **STORY-F1-UX-003.1** | Mapeamento dos Sistemas de Organização, Rotulagem e Navegação | 0.5 dia |
| **STORY-F1-UX-003.2** | Aplicação do Método LATCH ao Questionário | 0.5 dia |
| **STORY-F1-UX-003.3** | Aplicação das Leis da Gestalt ao Layout do Formulário | 0.5 dia |
| **STORY-F1-UX-003.4** | Validação da Arquitetura da Informação com stakeholders | 0.5 dia |

**Conteúdo Programático do Edital:**

| Disciplina | Conteúdo | Aplicação no Épico |
|:---|:---|:---|
| **Arquitetura da Informação** | Sistemas de Organização, Rotulagem, Navegação e Busca | Estruturação dos dados do questionário do Censo Agropecuário |
| **Método LATCH** | Localização, Alfabeto, Tempo, Categoria, Hierarquia | Organização das perguntas do Censo (uso da terra, pecuária, produção vegetal, recursos hídricos) |
| **Gestalt** | Leis de Proximidade, Semelhança, Fechamento, Continuidade | Layout dos formulários para otimizar agrupamento visual de campos complexos |

**Referências e Links de Estudo:**

#### Arquitetura da Informação
- **Information Architecture (Rosenfeld, Morville, Arango)**
  - 🔗 https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/
- **Método LATCH – Evernote**
  - 🔗 https://evernote.com/learn/what-is-the-latch-method-method-a-practical-guide
- **Organizing Things – Dave Gray**
  - 🔗 https://medium.com/@davegray/organizing-things-1dbc6faf5d79

#### Gestalt
- **Design Principles: Visual Perception and Gestalt – Smashing Magazine**
  - 🔗 https://www.smashingmagazine.com/2014/03/design-principles-visual-perception-and-the-principles-of-gestalt/
- **Gestalt Principles for Visual UI Design – UX Tigers**
  - 🔗 https://www.uxtigers.com/post/gestalt-principles

---

### 📌 EPIC-F1-UX-004: Acessibilidade (e-MAG 3.1 e WCAG 2.2 AA)

```
┌─────────────────────────────────────────────────────────────────┐
│  📌 EPIC-F1-UX-004: Acessibilidade (e-MAG 3.1 e WCAG 2.2 AA) │
├─────────────────────────────────────────────────────────────────┤
│  🎯 Objetivo: Realizar auditoria preventiva de acessibilidade│
│     do "Censo Fácil" com base nas 6 áreas do e-MAG e nos     │
│     critérios da WCAG 2.2 Nível AA, garantindo conformidade │
│     com os padrões de Governo Digital.                       │
│  📅 Estimativa: 2 dias                                         │
│  👤 Responsável: UX/UI Lead (FE) + Foundation                 │
│  ✅ Critério de Aceite: Matriz de conformidade aprovada e    │
│     plano de mitigação de barreiras                          │
└─────────────────────────────────────────────────────────────────┘
```

**Stories que compõem este Épico:**

| Story | Descrição | Estimativa |
|-------|-----------|------------|
| **STORY-F1-UX-004.1** | Auditoria da Área de Marcação (e-MAG) | 0.5 dia |
| **STORY-F1-UX-004.2** | Auditoria da Área de Comportamento (e-MAG) | 0.5 dia |
| **STORY-F1-UX-004.3** | Auditoria da Área de Conteúdo/Informação (e-MAG) | 0.5 dia |
| **STORY-F1-UX-004.4** | Auditoria da Área de Apresentação/Design (e-MAG) | 0.5 dia |
| **STORY-F1-UX-004.5** | Auditoria da Área de Multimídia (e-MAG) | 0.5 dia |
| **STORY-F1-UX-004.6** | Auditoria da Área de Formulário (e-MAG) | 0.5 dia |
| **STORY-F1-UX-004.7** | Verificação de Critérios Específicos WCAG 2.2 AA | 0.5 dia |

**Conteúdo Programático do Edital:**

| Disciplina | Conteúdo | Aplicação no Épico |
|:---|:---|:---|
| **e-MAG 3.1** | 6 áreas: Marcação, Comportamento, Conteúdo, Apresentação, Multimídia, Formulário | Auditoria preventiva em todas as áreas |
| **WCAG 2.2 AA** | Critérios: 2.5.8 (Target Size), 2.4.11 (Focus Not Obscured), 3.3.8 (Accessible Authentication), 3.3.7 (Redundant Entry) | Implementação de alvos interativos de 24x24px, foco visível, autenticação sem testes cognitivos |
| **Contraste Mínimo 4.5:1** | Área de Apresentação/Design do e-MAG | Garantia de contraste para textos, especialmente para produtores com baixa visão |

**Referências e Links de Estudo:**

#### Acessibilidade e Governo Digital
- **e-MAG 3.1 – Modelo de Acessibilidade em Governo Eletrônico**
  - 🔗 https://emag.governoeletronico.gov.br/
- **WCAG 2.2 – W3C Recommendation**
  - 🔗 https://www.w3.org/TR/WCAG22/
- **Fundamentos e Normas de Acessibilidade – ENAP**
  - 🔗 https://www.enap.gov.br/educacao-e-capacitacao/rotas/fundamentos-e-normas-de-acessibilidade/
- **WCAG 2.2: Novidades e seu impacto na acessibilidade da web – inSuit**
  - 🔗 https://www.insuit.net/pt-pt/wcag-2-2/
- **O que o WCAG 2.2 trouxe de novo? – WPT/Movimento Web para Todos**
  - 🔗 https://mwpt.com.br/o-que-o-wcag-2-2-trouxe-de-novo/
- **Avaliação de Sites de IES conforme WCAG – SBC**
  - 🔗 https://journals-sol.sbc.org.br/index.php/isys/article/download/5401/3878

#### Ferramentas de Avaliação
- **Ferramenta de Avaliação de Serviços Digitais do Gov.br**
  - 🔗 https://www.gov.br/governodigital/pt-br/plataformas-e-servicos-digitais/ferramenta-de-avaliacao

---

### 📌 EPIC-F1-ALL-005: Consolidação da Fase 1

```
┌─────────────────────────────────────────────────────────────────┐
│  📌 EPIC-F1-ALL-005: Consolidação da Fase 1                   │
├─────────────────────────────────────────────────────────────────┤
│  🎯 Objetivo: Consolidar todos os entregáveis da Fase 1 em   │
│     um relatório único e validar a estratégia de design      │
│     com os stakeholders.                                      │
│  📅 Estimativa: 1 dia                                          │
│  👤 Responsável: Todos os Squads                              │
│  ✅ Critério de Aceite: Relatório da Fase 1 aprovado e       │
│     alinhamento para início da Fase 2                        │
└─────────────────────────────────────────────────────────────────┘
```

**Stories que compõem este Épico:**

| Story | Descrição | Estimativa |
|-------|-----------|------------|
| **STORY-F1-ALL-005.1** | Consolidação dos entregáveis da Fase 1 | 0.5 dia |
| **STORY-F1-ALL-005.2** | Revisão e alinhamento com stakeholders | 0.5 dia |

**Conteúdo Programático do Edital:**

| Disciplina | Conteúdo | Aplicação no Épico |
|:---|:---|:---|
| **Redação Oficial** | Comunicação clara e impessoal | Elaboração do Relatório Consolidado |
| **Metodologia** | Estruturação de documentos técnicos | Organização do relatório final da fase |

---

## FASE 2: Design Visual, Prototipagem e Design System

### 📌 EPIC-F2-UX-001: DSGov Mobile e Componentes Customizados

```
┌─────────────────────────────────────────────────────────────────┐
│  📌 EPIC-F2-UX-001: DSGov Mobile e Componentes Customizados   │
├─────────────────────────────────────────────────────────────────┤
│  🎯 Objetivo: Mapear e adaptar os componentes do DSGov 4.0   │
│     para o contexto móvel do "Censo Fácil", documentando     │
│     o componente customizado br-gnss-tracker.                 │
│  📅 Estimativa: 2 dias                                         │
│  👤 Responsável: UX/UI Lead (FE) + Foundation                 │
│  ✅ Critério de Aceite: Componentes mapeados e documentados  │
│     no Custom Elements Manifest                               │
└─────────────────────────────────────────────────────────────────┘
```

**Stories que compõem este Épico:**

| Story | Descrição | Estimativa |
|-------|-----------|------------|
| **STORY-F2-UX-001.1** | Mapeamento dos Design Tokens do DSGov Mobile | 0.5 dia |
| **STORY-F2-UX-001.2** | Definição das Grids Móveis (4 colunas / 8 colunas) | 0.5 dia |
| **STORY-F2-UX-001.3** | Especificação do Componente br-gnss-tracker | 0.5 dia |
| **STORY-F2-UX-001.4** | Documentação do Componente em Custom Elements Manifest | 0.5 dia |

**Conteúdo Programático do Edital:**

| Disciplina | Conteúdo | Aplicação no Épico |
|:---|:---|:---|
| **Identidade Visual IBGE** | Manual de Identidade Visual | Aplicação das especificações cromáticas: Azul IBGE (Pantone 286 C / #0033A0) |
| **Tipografia Oficial** | Neuropolitical (restrita à logomarca) | Uso da Neuropolitical **exclusivamente** na marca do "Censo Fácil" |
| **Tipografia Oficial** | Família Univers | Aplicação da Univers LT Std (55 Roman, 55 Oblique, 65 Bold, 65 Bold Oblique) em toda a interface |
| **DSGov 4.0** | Padrão Digital de Governo | Mapeamento e adaptação de componentes reutilizáveis do DSGov |
| **Grids Móveis DSGov** | 4 colunas (smartphone) / 8 colunas (tablet) | Definição das grids fluidas para dispositivos móveis de coleta |

**Referências e Links de Estudo:**

#### Identidade Visual IBGE
- **Política de Comunicação do IBGE (2ª edição, 2016)**
  - 🔗 https://www.ibge.gov.br/np_download/novoportal/documentos_institucionais/politica_de_comunicacao_2ed_2016.pdf
- **Manual de Identidade Visual do Censo Agro 2017**
  - 🔗 https://censoagro2017.ibge.gov.br/media/com_mediaibge/arquivos/eef5f0ccde06ff68919a3e9fc940f06a.pdf
- **Manual de Identidade Visual do IBGE**
  - 🔗 http://w3.cddi.ibge.gov.br/manuais/identidade_visual.asp

#### Design System Gov.br
- **DSGov 4.0 – Padrão Digital de Governo**
  - 🔗 https://www.gov.br/ds/padroes/visao-geral
- **Guia Prático DSGov para SPUnet**
  - 🔗 https://www.gov.br/gestao/pt-br/assuntos/patrimonio-da-uniao/transformacao-digital/capacitacao-1/arquivos/v03_guia-pratico-design-system-para-o-spunet.pdf
- **Padrões para Android e iOS – DSGov**
  - 🔗 https://www.gov.br/ds/padroes/mobile/android-e-ios

#### Web Components
- **Custom Elements Manifest (CEM)**
  - 🔗 https://github.com/webcomponents/custom-elements-manifest
- **GovBR-DS – Web Components (GitLab)**
  - 🔗 https://gitlab.com/govbr-ds/bibliotecas/wbc/govbr-ds-wbc

---

### 📌 EPIC-F2-UX-002: Prototipagem – Fluxo de Coleta

```
┌─────────────────────────────────────────────────────────────────┐
│  📌 EPIC-F2-UX-002: Prototipagem – Fluxo de Coleta            │
├─────────────────────────────────────────────────────────────────┤
│  🎯 Objetivo: Criar protótipo de alta fidelidade no Figma    │
│     para o fluxo de coleta de dados, incluindo login,        │
│     navegação no setor, preenchimento do questionário e      │
│     captura de coordenadas GNSS.                              │
│  📅 Estimativa: 2 dias                                         │
│  👤 Responsável: UX/UI Lead (FE)                              │
│  ✅ Critério de Aceite: Protótipo navegável e validado com   │
│     stakeholders                                              │
└─────────────────────────────────────────────────────────────────┘
```

**Stories que compõem este Épico:**

| Story | Descrição | Estimativa |
|-------|-----------|------------|
| **STORY-F2-UX-002.1** | Prototipagem do Fluxo de Login (Gov.br + Offline) | 0.5 dia |
| **STORY-F2-UX-002.2** | Prototipagem do Dashboard e Mapa do Setor | 0.5 dia |
| **STORY-F2-UX-002.3** | Prototipagem do Formulário e Captura GNSS | 0.5 dia |
| **STORY-F2-UX-002.4** | Prototipagem do Encerramento e Sincronização | 0.5 dia |

**Conteúdo Programático do Edital:**

| Disciplina | Conteúdo | Aplicação no Épico |
|:---|:---|:---|
| **DMC – Dispositivo Móvel de Coleta** | Ferramenta principal de coleta | Prototipagem do DMC como aplicativo de campo |
| **Setor Censitário** | Unidade territorial de coleta | Prototipagem do mapa do setor com limites, feições físicas e antrópicas |
| **Questionário Básico / Completo** | Dois tipos de questionário | Prototipagem dos dois tipos com validação de consistência |
| **Captura de Coordenadas GNSS** | Validação de HDOP < 5.0m | Prototipagem do componente `br-gnss-tracker` com indicadores de precisão |
| **Regra da Sede** | Propriedades multissetoriais | Prototipagem da lógica para estabelecimentos com parcelas em múltiplos setores |
| **Alerta de Consistência** | Área vs. cabeças de gado | Prototipagem de alertas em tempo real para validação de dados |

**Referências e Links de Estudo:**

#### Conceitos do Censo
- **Manual do Recenseador do Censo Agropecuário (CD-1.09)**
  - 🔗 https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5723.pdf
- **Malha de Setores Censitários 2022**
  - 🔗 https://www.ibge.gov.br/biblioteca/visualizacao/livros/liv102138.pdf
- **Censo Agropecuário – Portal ANDA**
  - 🔗 https://anda.ibge.gov.br/

#### Prototipagem
- **UX Research em Governo Eletrônico (ESDI/UERJ)**
  - 🔗 https://www.esdi.uerj.br/assets/60131c71d30a78161ca77a0b959818e4/da35ec6b6c8982bcfd253b2c78eb9def.pdf

---

### 📌 EPIC-F2-UX-003: Prototipagem – Fluxo de Auditoria (ACQ)

```
┌─────────────────────────────────────────────────────────────────┐
│  📌 EPIC-F2-UX-003: Prototipagem – Fluxo de Auditoria (ACQ)   │
├─────────────────────────────────────────────────────────────────┤
│  🎯 Objetivo: Criar protótipo de alta fidelidade no Figma    │
│     para o fluxo de auditoria e validação de dados do ACQ,   │
│     incluindo dashboards de análise, validação de            │
│     consistência e geração de relatórios.                    │
│  📅 Estimativa: 2 dias                                         │
│  👤 Responsável: UX/UI Lead (FE) + Core Business              │
│  ✅ Critério de Aceite: Protótipo navegável e validado com   │
│     stakeholders                                              │
└─────────────────────────────────────────────────────────────────┘
```

**Stories que compõem este Épico:**

| Story | Descrição | Estimativa |
|-------|-----------|------------|
| **STORY-F2-UX-003.1** | Prototipagem do Dashboard de Auditoria do ACQ | 0.5 dia |
| **STORY-F2-UX-003.2** | Prototipagem da Validação de Consistência de Dados | 0.5 dia |
| **STORY-F2-UX-003.3** | Prototipagem da Gestão de Pendentes e Ocorrências | 0.5 dia |
| **STORY-F2-UX-003.4** | Prototipagem dos Relatórios de Qualidade | 0.5 dia |

**Conteúdo Programático do Edital:**

| Disciplina | Conteúdo | Aplicação no Épico |
|:---|:---|:---|
| **ACQ – Agente Censitário de Qualidade** | Auditoria de dados | Prototipagem do dashboard do ACQ para validação e homologação |
| **PEUV – Pendente de Espécie da Unidade Visitada** | Gestão de pendentes | Prototipagem da gestão de pendentes: recusas, ausências, PEUVs |
| **Controle de Qualidade** | Cruzamento de área vs. produção | Prototipagem de ferramentas de validação de consistência de dados |
| **Relatórios de Qualidade** | Métricas de cobertura | Prototipagem de relatórios com indicadores de produtividade e ROI |

**Referências e Links de Estudo:**

#### Controle de Qualidade
- **Manual do Agente Censitário Supervisor (ACS)**
  - 🔗 https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5726.pdf
- **Manual do Recenseador – Situações Especiais**
  - 🔗 https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5723.pdf

---

## FASE 3: Engenharia Frontend, Web Components e Integração

### 📌 EPIC-F3-FND-001: Web Components e XHTML

```
┌─────────────────────────────────────────────────────────────────┐
│  📌 EPIC-F3-FND-001: Web Components e XHTML                   │
├─────────────────────────────────────────────────────────────────┤
│  🎯 Objetivo: Implementar a solução técnica com conformidade │
│     XHTML, Web Components, integração Gov.br e garantia de   │
│     segurança e acessibilidade.                                │
│  📅 Estimativa: 3 dias                                         │
│  👤 Responsável: Foundation + Core Business                   │
│  ✅ Critério de Aceite: Código validado conforme XHTML      │
│     Estrito e e-MAG, com todos os componentes funcionais     │
└─────────────────────────────────────────────────────────────────┘
```

**Stories que compõem este Épico:**

| Story | Descrição | Estimativa |
|-------|-----------|------------|
| **STORY-F3-FND-001.1** | Implementação do Componente br-gnss-tracker | 1 dia |
| **STORY-F3-FND-001.2** | Validação Geodésica (ES6) | 0.5 dia |
| **STORY-F3-FND-001.3** | Service Worker e Offline | 0.5 dia |
| **STORY-F3-FND-001.4** | Criptografia AES-256 | 0.5 dia |
| **STORY-F3-FND-001.5** | CSS Responsivo e Acessível | 0.5 dia |

**Conteúdo Programático do Edital:**

| Disciplina | Conteúdo | Aplicação no Épico |
|:---|:---|:---|
| **XHTML Estrito** | Processamento Drástico de Erros | Implementação em XHTML com tags minúsculas, fechamento obrigatório, atributos entre aspas |
| **JavaScript ES6** | Módulos e classes | Implementação de módulos ES6 com `import/export` para validação geodésica |
| **DOM Level 2** | `createElementNS` | Manipulação do DOM com `createElementNS` para garantir namespace XHTML |
| **Seções CDATA** | Encapsulamento de scripts | Uso de `/* <![CDATA[ */` em scripts inline para evitar erros de parsing XML |
| **Web Components** | @govbr-ds/webcomponents | Desenvolvimento do componente `br-gnss-tracker` com Shadow DOM |
| **Service Worker** | Offline-first | Implementação de Service Workers para caching de ativos estáticos |
| **Criptografia AES-256** | LGPD | Criptografia de dados no IndexedDB via Web Crypto API para dados offline |

**Referências e Links de Estudo:**

#### XHTML e Tecnologias Web
- **XHTML 1.0 Strict – W3C Specification**
  - 🔗 https://www.w3.org/TR/xhtml1/
- **JavaScript ES6 Modules – MDN**
  - 🔗 https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules
- **Document.createElementNS() – MDN**
  - 🔗 https://developer.mozilla.org/en-US/docs/Web/API/Document/createElementNS
- **CDATASection – MDN**
  - 🔗 https://developer.mozilla.org/en-US/docs/Web/API/CDATASection

#### Offline-first e Segurança
- **Service Worker API – MDN**
  - 🔗 https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API
- **Web Crypto API – MDN**
  - 🔗 https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API
- **LGPD – Lei nº 13.709/2018**
  - 🔗 https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm

#### Web Components
- **Custom Elements Manifest (CEM)**
  - 🔗 https://github.com/webcomponents/custom-elements-manifest
- **GovBR-DS – Web Components (GitLab)**
  - 🔗 https://gitlab.com/govbr-ds/bibliotecas/wbc/govbr-ds-wbc

---

### 📌 EPIC-F3-FND-002: Integração Gov.br

```
┌─────────────────────────────────────────────────────────────────┐
│  📌 EPIC-F3-FND-002: Integração Gov.br                        │
├─────────────────────────────────────────────────────────────────┤
│  🎯 Objetivo: Integrar o "Censo Fácil" com o ecossistema     │
│     Gov.br, incluindo Barra Gov.Br e autenticação OIDC.      │
│  📅 Estimativa: 2 dias                                         │
│  👤 Responsável: Foundation                                   │
│  ✅ Critério de Aceite: Barra Gov.Br integrada e fluxo      │
│     OIDC funcional                                            │
└─────────────────────────────────────────────────────────────────┘
```

**Stories que compõem este Épico:**

| Story | Descrição | Estimativa |
|-------|-----------|------------|
| **STORY-F3-FND-002.1** | Integração da Barra Gov.Br | 0.5 dia |
| **STORY-F3-FND-002.2** | Autenticação OIDC (Gov.br) | 1 dia |
| **STORY-F3-FND-002.3** | Manual de Replicabilidade Institucional | 0.5 dia |

**Conteúdo Programático do Edital:**

| Disciplina | Conteúdo | Aplicação no Épico |
|:---|:---|:---|
| **Barra Gov.Br** | Padrão de Governo Digital | Integração da Barra Gov.Br conforme especificação do Serpro/MGI |
| **Autenticação Gov.br** | Níveis Bronze, Prata, Ouro | Implementação do fluxo de login único via OpenID Connect (OIDC) |
| **WCAG 2.4.11** | Focus Not Obscured | Garantia de que a Barra Gov.Br não oculte o foco de teclado |

**Referências e Links de Estudo:**

#### Integração Gov.br
- **Barra Gov.Br – Padrão Digital de Governo**
  - 🔗 https://www.gov.br/ds/padroes/visao-geral
- **OpenID Connect (OIDC) – Documentação**
  - 🔗 https://openid.net/developers/specs/
- **Portal Gov.br**
  - 🔗 https://www.gov.br/governodigital/

#### Inovação e Padronização
- **Inovação e Padronização: O Uso do Design System do Governo Federal**
  - 🔗 https://repositorio.wticifes.com.br/bitstreams/ca106c5e-7e67-48b6-a1f6-742e73c50892/download

---

## FASE 4: Testes, Governança DesignOps e Documentação

### 📌 EPIC-F4-UX-001: Plano de Testes e Avaliação de Usabilidade

```
┌─────────────────────────────────────────────────────────────────┐
│  📌 EPIC-F4-UX-001: Plano de Testes e Avaliação de Usabilidade│
├─────────────────────────────────────────────────────────────────┤
│  🎯 Objetivo: Validar o "Censo Fácil" com usuários reais,   │
│     coletar métricas de usabilidade e identificar pontos de  │
│     melhoria.                                                  │
│  📅 Estimativa: 2 dias                                         │
│  👤 Responsável: UX & Experience + Core Business              │
│  ✅ Critério de Aceite: Relatório de testes com recomendações│
│     priorizadas                                               │
└─────────────────────────────────────────────────────────────────┘
```

**Stories que compõem este Épico:**

| Story | Descrição | Estimativa |
|-------|-----------|------------|
| **STORY-F4-UX-001.1** | Elaboração do Plano de Testes de Usabilidade | 1 dia |
| **STORY-F4-UX-001.2** | Execução de Testes com Personas | 0.5 dia |
| **STORY-F4-UX-001.3** | Matriz de Severidade e Recomendações | 0.5 dia |

**Conteúdo Programático do Edital:**

| Disciplina | Conteúdo | Aplicação no Épico |
|:---|:---|:---|
| **Testes de Usabilidade** | Think Aloud | Sessões com produtores, recenseadores e ACQs em ambiente offline |
| **Métricas** | Taxa de Conclusão, Tempo Médio, SUS | Coleta de dados quantitativos e qualitativos sobre a usabilidade do sistema |
| **Matriz de Severidade** | Priorização de erros | Classificação de problemas por impacto e frequência |

**Referências e Links de Estudo:**

#### Testes de Usabilidade
- **A Practical Guide to Usability Testing (Dumas & Redish)**
- **Rocket Surgery Made Easy (Steve Krug)**
- **System Usability Scale (SUS) – Documentação**
  - 🔗 https://www.usability.gov/how-to-and-tools/methods/system-usability-scale.html

---

### 📌 EPIC-F4-ALL-002: DesignOps e Governança

```
┌─────────────────────────────────────────────────────────────────┐
│  📌 EPIC-F4-ALL-002: DesignOps e Governança                   │
├─────────────────────────────────────────────────────────────────┤
│  🎯 Objetivo: Estabelecer a governança do Design System e o  │
│     fluxo de trabalho para manutenção e evolução do "Censo   │
│     Fácil".                                                    │
│  📅 Estimativa: 2 dias                                         │
│  👤 Responsável: Todos os Squads                              │
│  ✅ Critério de Aceite: Documento de DesignOps aprovado      │
└─────────────────────────────────────────────────────────────────┘
```

**Stories que compõem este Épico:**

| Story | Descrição | Estimativa |
|-------|-----------|------------|
| **STORY-F4-ALL-002.1** | Documento de DesignOps | 1 dia |
| **STORY-F4-ALL-002.2** | Estratégia de Iteração e Evolução | 1 dia |

**Conteúdo Programático do Edital:**

| Disciplina | Conteúdo | Aplicação no Épico |
|:---|:---|:---|
| **DesignOps** | Fluxo de trabalho e governança de componentes | Estruturação do processo de manutenção e evolução do Design System |
| **Lean UX** | Ciclos de iteração contínua | Definição da rotina de atualização contínua do sistema pós-lançamento |

**Referências e Links de Estudo:**

#### DesignOps
- **DesignOps building blocks – Padrões, métodos, comunidades**
  - 🔗 https://www.invisionapp.com/designops
- **Lean UX (Jeff Gothelf, Josh Seiden)**

---

### 📌 EPIC-F4-ALL-003: Documentação Final e Apresentação Executiva

```
┌─────────────────────────────────────────────────────────────────┐
│  📌 EPIC-F4-ALL-003: Documentação Final e Apresentação        │
├─────────────────────────────────────────────────────────────────┤
│  🎯 Objetivo: Entregar a documentação completa do projeto e  │
│     apresentar os resultados para a SGD/MGI.                  │
│  📅 Estimativa: 2 dias                                         │
│  👤 Responsável: Todos os Squads                              │
│  ✅ Critério de Aceite: Manual de Identidade Visual e Deck   │
│     Executivo entregues                                       │
└─────────────────────────────────────────────────────────────────┘
```

**Stories que compõem este Épico:**

| Story | Descrição | Estimativa |
|-------|-----------|------------|
| **STORY-F4-ALL-003.1** | Manual de Identidade Visual | 1 dia |
| **STORY-F4-ALL-003.2** | Apresentação Executiva | 1 dia |

**Conteúdo Programático do Edital:**

| Disciplina | Conteúdo | Aplicação no Épico |
|:---|:---|:---|
| **Manual de Identidade Visual IBGE** | Sistema cromático e tipografia | Criação do Manual do Sistema Visual "Censo Fácil" |
| **Sistema Cromático** | Pantone 286 C, CMYK (100/80/0/12), RGB (0/51/160), HEX (#0033A0) | Documentação oficial do Azul IBGE para diferentes mídias |
| **Neuropolitical / Univers** | Tipografia oficial | Especificação tipográfica para o "Censo Fácil" |
| **e-MAG 3.1 e WCAG 2.2 AA** | Conformidade com acessibilidade | Documentação da conformidade com acessibilidade |
| **Lei 8.112/90 e 8.745/93** | Regime de servidores | Documentação da conformidade com regime de servidores temporários |
| **LGPD** | Lei nº 13.709/2018 | Documentação das medidas de proteção de dados |

**Referências e Links de Estudo:**

#### Identidade Visual
- **Política de Comunicação do IBGE (2ª edição, 2016)**
  - 🔗 https://www.ibge.gov.br/np_download/novoportal/documentos_institucionais/politica_de_comunicacao_2ed_2016.pdf
- **Manual de Identidade Visual do Censo Agro 2017**
  - 🔗 https://censoagro2017.ibge.gov.br/media/com_mediaibge/arquivos/eef5f0ccde06ff68919a3e9fc940f06a.pdf

#### Plataformas e Ferramentas Gov.br
- **Portal do Governo Digital**
  - 🔗 https://www.gov.br/governodigital/
- **Ferramenta de Avaliação de Serviços Digitais**
  - 🔗 https://www.gov.br/governodigital/pt-br/plataformas-e-servicos-digitais/ferramenta-de-avaliacao

---

## 📊 Resumo dos Épicos e Links por Disciplina

| Épico | Fase | Disciplina Principal | Links de Estudo |
|:---|:---|:---|:---|
| EPIC-F1-UX-001 | F1 | Geografia Agrária, Legislação, UX/UI | [Manual do Recenseador](https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5723.pdf), [Lei 8.112/90](https://www2.camara.leg.br/legin/fed/lei/1990/lei-8112-11-dezembro-1990-322161-publicacaooriginal-1-pl.html), [Lei 8.745/93](https://www2.camara.leg.br/legin/fed/lei/1993/lei-8745-9-dezembro-1993-363171-publicacaooriginal-1-pl.html) |
| EPIC-F1-UX-002 | F1 | UX/UI, Redação Oficial | [10 Heurísticas Nielsen](https://www.nngroup.com/articles/ten-usability-heuristics/), [Manual de Redação](https://www.gov.br/planalto/pt-br/conheca-a-presidencia/acervo/manual-de-redacao) |
| EPIC-F1-UX-003 | F1 | Arquitetura da Informação, Gestalt | [Método LATCH](https://evernote.com/learn/what-is-the-latch-method-method-a-practical-guide), [Gestalt Principles](https://www.smashingmagazine.com/2014/03/design-principles-visual-perception-and-the-principles-of-gestalt/) |
| EPIC-F1-UX-004 | F1 | Acessibilidade (e-MAG/WCAG) | [e-MAG 3.1](https://emag.governoeletronico.gov.br/), [WCAG 2.2](https://www.w3.org/TR/WCAG22/) |
| EPIC-F2-UX-001 | F2 | Identidade Visual, DSGov | [Política de Comunicação IBGE](https://www.ibge.gov.br/np_download/novoportal/documentos_institucionais/politica_de_comunicacao_2ed_2016.pdf), [DSGov 4.0](https://www.gov.br/ds/padroes/visao-geral) |
| EPIC-F2-UX-002 | F2 | Conceitos do Censo | [Manual do Recenseador](https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5723.pdf), [Malha de Setores](https://www.ibge.gov.br/biblioteca/visualizacao/livros/liv102138.pdf) |
| EPIC-F2-UX-003 | F2 | ACQ, Controle de Qualidade | [Manual do ACS](https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5726.pdf) |
| EPIC-F3-FND-001 | F3 | XHTML, ES6, Offline, LGPD | [XHTML 1.0](https://www.w3.org/TR/xhtml1/), [ES6 Modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules), [Web Crypto API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API) |
| EPIC-F3-FND-002 | F3 | Governo Digital, OIDC | [Barra Gov.Br](https://www.gov.br/ds/padroes/visao-geral), [OpenID Connect](https://openid.net/developers/specs/) |
| EPIC-F4-UX-001 | F4 | Testes de Usabilidade | [SUS Documentation](https://www.usability.gov/how-to-and-tools/methods/system-usability-scale.html) |
| EPIC-F4-ALL-002 | F4 | DesignOps, Lean UX | [DesignOps Guide](https://www.invisionapp.com/designops) |
| EPIC-F4-ALL-003 | F4 | Documentação Final | [Portal Gov.br](https://www.gov.br/governodigital/), [Ferramenta de Avaliação](https://www.gov.br/governodigital/pt-br/plataformas-e-servicos-digitais/ferramenta-de-avaliacao) |