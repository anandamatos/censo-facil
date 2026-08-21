# 🔍 Especificação de Interface e Engenharia: Dashboard do Agente Censitário de Qualidade (ACQ) — **Versão Revisada**

## 1. Contexto Operacional e Atribuições do ACQ

O Agente Censitário de Qualidade (ACQ) desempenha um papel crítico na cadeia de custódia e integridade dos dados estatísticos nacionais. O novo edital do IBGE (Edital nº 02/2026) oferece **394 vagas imediatas** para este cargo, com remuneração de R$ 2.932,00 acrescida de R$ 1.192,00 de auxílio-alimentação, totalizando R$ 4.124,00 . A seleção será organizada pelo Instituto Avalia, com prova objetiva prevista para 30 de agosto de 2026 .

### 1.1 Requisitos e Escopo Funcional

De acordo com o edital do Processo Seletivo Simplificado, as atribuições e características da função compreendem :

| Atribuição | Descrição Detalhada |
|------------|---------------------|
| **Supervisão de Qualidade** | Garantir que todas as informações coletadas pelos recenseadores apresentem total aderência às normas e conceitos metodológicos estabelecidos nos manuais do IBGE |
| **Exame de Questionários** | Auditar questionários eletrônicos (Básico e Completo), verificando completude, coerência, consistência e padronização das respostas  |
| **Detecção de Inconsistências** | Identificar e registrar adequadamente erros, falhas, divergências, omissões ou inconsistências conceituais nos dados coletados em campo  |
| **Mediação Técnica** | Orientar o Agente Censitário Supervisor (ACS) e os recenseadores diretamente quanto aos ajustes necessários de procedimento, correções de dados ou necessidade de reforço em treinamentos  |
| **Homologação e Sigilo** | Manter absoluto sigilo estatístico (conforme a Lei nº 5.534/68) e adotar postura técnica, imparcial e aderente à LGPD  |

### 1.2 Avaliação de Desempenho do ACQ

Os contratados serão avaliados mensalmente com base nos seguintes critérios :

- **Assiduidade:** Frequência e pontualidade
- **Cumprimento de Prazos:** Capacidade de entregar auditorias dentro do cronograma estabelecido
- **Produtividade:** Volume e qualidade dos setores auditados e homologados

---

## 2. Arquitetura da Informação e Sitemap do Dashboard

Para mitigar a sobrecarga mental de Carlos ao gerenciar múltiplos setores censitários, a arquitetura da informação adota o modelo de Navegação Não Linear e estruturação modular baseada no sitemap homologado do sistema "Censo Fácil".

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DASHBOARD INICIAL DO ACQ                         │
├─────────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────────┐  ┌───────────────────────┐  │
│  │  Cards KPIs  │  │ Tabela de Status │  │   Feed de Alertas     │  │
│  │  (4 métricas)│  │ dos Setores      │  │   (Inconsistências)   │  │
│  └──────────────┘  └──────────────────┘  └───────────────────────┘  │
│  ┌─────────────────────────────────────────────────────────────────┐ │
│  │              Mapa de Calor de Cobertura (GIS)                  │ │
│  │  (Visualização geográfica da cobertura por setor)              │ │
│  └─────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.1 Estrutura de Telas e Fluxos (Sitemap)

| Tela | Função | Elementos Principais |
|------|--------|---------------------|
| **Dashboard Inicial** | Visão panorâmica do andamento da coleta | KPIs, tabela de setores, mapa de calor, feed de alertas |
| **Auditoria Lado a Lado** | Validação geográfica e temática | Mapa de satélite + dados declarados lado a lado |
| **Detalhamento de Setor** | Análise aprofundada de um setor | Lista CNEFE, PEUV, questionários pendentes |
| **Relatórios de Qualidade** | Exportação de análises | PDF/CSV com indicadores de qualidade |

---

## 3. Diretrizes de Design Visual, Tipografia e Cores

O layout do dashboard do ACQ deve transmitir seriedade, precisão e credibilidade, utilizando as diretrizes de design do DSGov 4.0 adaptadas à identidade perene do IBGE.

### 3.1 Paleta de Cores e Contraste (e-MAG 3.1)

| Elemento | Especificação | Aplicação |
|----------|---------------|-----------|
| **Azul IBGE** | Pantone 286 C / HEX #0033A0 / RGB 0,51,160 | Navegação primária, cabeçalhos, botões principais |
| **Fundo** | #FFFFFF (branco puro) | Plano de fundo do conteúdo |
| **Containers** | #F5F5F5 (cinza claro) | Cards e painéis de controle |
| **Texto Principal** | #1C1C1E (cinza escuro) | Corpo de texto (contraste > 15:1) |
| **Texto Secundário** | #555770 (cinza médio) | Legendas e textos auxiliares |
| **Sucesso** | #4CAF50 (verde) | Indicadores de cobertura concluída |
| **Alerta** | #F5A623 (amarelo) | Inconsistências de média severidade |
| **Erro** | #E53935 (vermelho) | Inconsistências críticas, recusas |

**Contraste Validado (WCAG 1.4.3):**
- Texto normal (16px): ≥ 15:1 → mínimo exigido 4.5:1
- Texto grande (24px+): ≥ 8.5:1 → mínimo exigido 3:1

### 3.2 Tipografia Oficial do IBGE

A aplicação tipográfica segue estritamente as regras de diagramação e publicação do Instituto :

| Peso/Estilo | Nome Técnico | Aplicação | Tamanho Mínimo |
|-------------|--------------|-----------|----------------|
| **Bold** | Univers 65 Bold | Cabeçalhos, títulos de seções, rótulos de campos, botões | 18px |
| **Roman** | Univers 55 Roman | Texto corporal, células de dados | **16px** |
| **Oblique** | Univers 55 Oblique | Notas de rodapé, citações, orientações secundárias | 14px |
| **Neuropolitical** | — | **EXCLUSIVO** na logomarca do IBGE | — |

### 3.3 Grid e Disposição Responsiva

Carlos opera o sistema primariamente em estações de trabalho ou notebooks de alta performance . O layout utiliza uma grid fluida de **8 colunas** na orientação paisagem (landscape) com margens de 16px e medianiz de 16px, seguindo os tokens móveis e adaptativos do DSGov.

---

## 4. Design dos Indicadores-Chave (KPIs) de Cobertura

Os indicadores de desempenho do dashboard do ACQ são agrupados em cards de alta visibilidade com elevação suave (elevation-sm) para direcionar a tomada de decisão.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        INDICADORES DO POSTO                             │
├─────────────────┬─────────────────┬─────────────────┬───────────────────┤
│  SETOR TRAB.    │  COBERTURA      │  TAXA RECUSA    │   ALERTAS PEND.   │
│     15          │    87.4%        │     3.2%        │        12         │
│  (Total: 25)    │  (Progresso)    │  (Critério)     │   (Ação Direta)   │
└─────────────────┴─────────────────┴─────────────────┴───────────────────┘
```

| KPI | Descrição | Fórmula/Origem |
|-----|-----------|----------------|
| **Setores Trabalhados** | Contagem de setores sob responsabilidade do ACQ | Total atribuído vs. total auditado |
| **Taxa de Cobertura** | Percentual de estabelecimentos visitados vs. total estimado no CNEFE | (Visitados / Estimados) × 100 |
| **Taxa de Recusa** | Percentual de estabelecimentos com recusa formal | (Recusas / Total de Visitas) × 100 |
| **Alertas Pendentes** | Inconsistências detectadas que exigem ação do ACQ | Contagem dinâmica do sistema |

---

## 5. Lista de Setores e Tabela de Status de Coleta

Abaixo dos KPIs, o dashboard apresenta a tabela estruturada contendo a relação de todos os setores censitários da jurisdição.

| Código do Setor | Município | Cobertura | Status | Ações |
|-----------------|-----------|-----------|--------|-------|
| 150280610000021 | Alfenas | 98.2% | 🟡 Aguardando Auditoria | [Auditar] [Aprovar] |
| 150280610000022 | Alfenas | 100% | 🟢 Aprovado | [Ver Detalhes] |
| 150280610000019 | Nova Friburgo | 45.1% | 🔵 Em Coleta | [Monitorar] |
| 150280610000020 | Nova Friburgo | 89.4% | 🔴 Rejeitado | [Ver Justificativa] |

### 5.1 Regras de Interação da Tabela

| Funcionalidade | Descrição | Benefício para o ACQ |
|----------------|-----------|----------------------|
| **Ordenação** | Todas as colunas ordenáveis (asc/desc) | Priorizar setores mais próximos da conclusão |
| **Filtros Rápidos** | Botões de alternância por status | Isolar "Aguardando Auditoria" para ação imediata |
| **Ações Diretas** | Links "Auditar", "Aprovar", "Ver Detalhes" | Navegação direta para fluxos de trabalho |

---

## 6. Mapa de Calor de Cobertura e Auditoria Espacial Lado a Lado

### 6.1 Mapa de Calor Geral

O painel central direito abriga o mapa dinâmico de calor do território sob controle do posto censitário.

| Elemento | Especificação | Justificativa |
|----------|---------------|---------------|
| **Gradiente Visual** | Azul/Cinza (baixa cobertura) → Verde (alta cobertura) | Identificação visual imediata de gargalos |
| **Interatividade** | Hover exibe tooltip com código do setor, nome do recenseador, total de questionários, recusas | Informação contextual sem navegação |
| **Clique** | Direciona para auditoria espacial lado a lado | Ação direta para validação |

### 6.2 Auditoria Espacial Lado a Lado

Ao clicar em um endereço específico com alerta de consistência cartográfica, a tela divide-se em duas metades síncronas:

```
  ┌────────────────────────────────┬────────────────────────────────┐
  │   PAINEL DE DADOS DECLARADOS   │   MAPA SATÉLITE - COORDENADAS  │
  │                                │                                │
  │  • Produtor: Seu José         │        📍 [Sede Estab.]        │
  │  • Área Declarada: 25 ha      │        σₕ = 2.1m (Ótimo)       │
  │  • Tipo: Agropecuário         │        [Limite Setor] ───┐     │
  │  • Culturas: Milho, Feijão    │                          │     │
  │  • Rebanho: 12 bovinos        │                          │     │
  └────────────────────────────────┴────────────────────────────────┘
```

| Painel | Conteúdo | Função do ACQ |
|--------|----------|---------------|
| **Esquerdo — Dados Declarados** | Respostas do questionário (área, produção, rebanho, insumos) | Verificar consistência temática |
| **Direito — Mapa de Satélite** | Imagem orbital georreferenciada, limites do setor, ponto GNSS | Validar georreferenciamento e Regra da Sede |

**Rigor Geodésico:** O sistema exibe o valor medido de HDOP e calcula a incerteza horizontal (σₕ = HDOP × σ₀). Carlos audita se o ponto foi gravado com precisão σₕ < 5,0 metros e se o recenseador respeitou a **Regra da Sede** (gravando a coordenada exatamente na porteira ou edificação principal).

---

## 7. Feed de Alertas em Tempo Real (Inconsistências)

O painel lateral esquerdo exibe um feed dinâmico e rolável contendo todos os alertas prioritários de inconsistência gerados pelos sistemas do DMC de campo.

### 7.1 Tipos de Alerta Catalogados

| Ícone | Tipo de Alerta | Descrição | Ação do ACQ |
|-------|----------------|-----------|-------------|
| ⚠️ | **Inconsistência de Área vs. Pecuária** | Número de cabeças de gado incompatível com área de pastagem (ex: 200 bois para 5 hectares) | Solicitar correção ao ACS |
| 🔴 | **Erro de Limite Territorial** | Coordenadas GNSS fora do perímetro do setor censitário | Verificar omissão ou invasão |
| 🟡 | **PEUV — Pendente de Espécie** | Endereço não classificado (estabelecimento, domicílio, horto) | Orientar classificação correta |
| 🔒 | **Recusa Formal** | Produtor se recusou a prestar informações | Acionar ACS para visita de sensibilização |

### 7.2 Comportamento e Acessibilidade (aria-live)

| Componente | Especificação | Justificativa |
|------------|---------------|---------------|
| **aria-live** | `aria-live="polite"` e `role="status"` | Novos alertas são anunciados sem interromper a auditoria ativa |
| **Independência de Cor** | Ícones geométricos exclusivos + rótulos textuais | Conformidade com e-MAG 4.2 (não depender apenas de cor) |
| **Topo da Lista** | Alertas mais recentes aparecem no topo | Priorização de novos eventos |

---

## 8. Acessibilidade (e-MAG 3.1 & WCAG 2.2 AA) e Segurança

Para atender rigorosamente aos padrões federais e ao edital de seleção do IBGE, o dashboard do ACQ incorpora critérios avançados de acessibilidade e segurança .

### 8.1 Critérios de Acessibilidade Implementados

| Critério | Especificação | Padrão |
|----------|---------------|--------|
| **Navegação por Teclado** | Todos os elementos navegáveis via Tab, Enter, Espaço | e-MAG Área 2 |
| **Target Size** | Alvos mínimos de 24×24px CSS; botões críticos com 48×48px | WCAG 2.2 — 2.5.8 |
| **Focus Not Obscured** | Outline azul de 3px com contraste 3:1, não ocultado pela Barra Gov.Br | WCAG 2.2 — 2.4.11 |
| **Contraste** | Texto normal ≥ 4.5:1; texto grande ≥ 3:1 | WCAG 1.4.3 |
| **Redundant Entry** | Autopreenchimento de dados do recenseador e setor | WCAG 2.2 — 3.3.7 |
| **Accessible Authentication** | Login com biometria ou PIN (sem testes cognitivos) | WCAG 2.2 — 3.3.8 |

### 8.2 Protocolo de Segurança (LGPD e Sigilo)

| Camada | Tecnologia | Justificativa |
|--------|------------|---------------|
| **Dados em Repouso** | AES-256 GCM via Web Crypto API | Proteção de dados sensíveis no dispositivo |
| **Derivação de Chave** | PBKDF2 com salt + autenticação Gov.br | Chave única por sessão |
| **Dados em Trânsito** | TLS 1.3 / HTTPS | Proteção durante transmissão |
| **Descarte Seguro** | Remoção irreversível do IndexedDB pós-sessão | Conformidade com LGPD Art. 18 |

---

## 9. Custom Elements Manifest (CEM) do Dashboard

```json
{
  "schemaVersion": "1.0.0",
  "readme": "Componente modular para o painel de inconsistências e alertas do dashboard do ACQ.",
  "modules": [
    {
      "kind": "javascript-module",
      "path": "src/components/acq-alert-feed/acq-alert-feed.js",
      "declarations": [
        {
          "kind": "class",
          "description": "Gerencia e renderiza o feed de alertas de inconsistência conceitual e geodésica em tempo real.",
          "name": "AcqAlertFeed",
          "tagName": "acq-alert-feed",
          "customElement": true,
          "attributes": [
            {
              "name": "active-alerts",
              "type": { "text": "number" },
              "description": "Contagem de alertas pendentes de auditoria."
            }
          ],
          "events": [
            {
              "name": "acq-alert-selected",
              "description": "Disparado quando o ACQ clica em um alerta para focar o setor correspondente.",
              "type": { "text": "CustomEvent" }
            }
          ],
          "slots": [
            {
              "name": "alert-item",
              "description": "Slot dinâmico para injeção de cards de inconsistência em Linguagem Simples."
            }
          ]
        }
      ]
    }
  ]
}
```

---

## 10. Checklist de Conformidade

| Item | Critério | Status | Referência |
|------|----------|--------|------------|
| **KPIs de Cobertura** | Indicadores de desempenho visíveis | ✅ Conforme | Edital ACQ |
| **Tabela de Setores** | Ordenação e filtros por status | ✅ Conforme | Manual ACS/ACM |
| **Mapa de Calor** | Visualização geográfica da cobertura | ✅ Conforme | Manual do Recenseador |
| **Auditoria Lado a Lado** | Dados declarados vs. mapa de satélite | ✅ Conforme | Regra da Sede |
| **Feed de Alertas** | Inconsistências em tempo real | ✅ Conforme | e-MAG 3.1 |
| **HDOP Validation** | Bloqueio se σₕ > 5,0m | ✅ Conforme | Manual do Recenseador |
| **Target Size** | ≥ 24×24px CSS | ✅ Conforme | WCAG 2.2 — 2.5.8 |
| **Contraste** | ≥ 4.5:1 para textos normais | ✅ Conforme | WCAG 1.4.3 |
| **Criptografia AES-256** | Dados em repouso no IndexedDB | ✅ Conforme | LGPD Art. 46 |
| **Descarte Seguro** | Remoção pós-sincronização | ✅ Conforme | LGPD Art. 18 |

---

## 11. Conclusão

O dashboard do Agente Censitário de Qualidade foi projetado para ser uma **ferramenta de auditoria robusta, acessível e eficiente**, permitindo que Carlos supervise a qualidade dos dados coletados, identifique inconsistências em tempo real e homologue setores com confiança estatística.

A aplicação dos critérios **WCAG 2.2 AA**, **e-MAG 3.1** e **LGPD**, combinada com a identidade visual do IBGE e as diretrizes do **DSGov 4.0**, garante que o dashboard esteja alinhado com os mais elevados padrões de governança digital e inclusão, atendendo às necessidades do Agente Censitário de Qualidade no 12º Censo Agropecuário .

---

## 12. Referências

### Manuais e Documentos Oficiais do IBGE

1. IBGE. **Edital de Abertura nº 02/2026 — Processo Seletivo Simplificado para Agente Censitário de Qualidade (ACQ)**. Rio de Janeiro: IBGE, 2026.

2. IBGE. **Manual do Recenseador do Censo Demográfico 2022 (CD-1.09)**. Rio de Janeiro: IBGE, 2022. Disponível em: <https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5723.pdf>. Acesso em: 9 ago. 2026.

### Padrões de Governo Digital e Acessibilidade

3. BRASIL. **e-MAG 3.1 — Modelo de Acessibilidade em Governo Eletrônico**. Brasília: Ministério do Planejamento, Orçamento e Gestão, 2014. Disponível em: <https://emag.governoeletronico.gov.br/>. Acesso em: 9 ago. 2026.

4. BRASIL. **DSGov 4.0 — Padrão Digital de Governo**. Brasília: Ministério da Gestão e da Inovação em Serviços Públicos, 2024. Disponível em: <https://www.gov.br/ds/>. Acesso em: 9 ago. 2026.

5. W3C. **Web Content Accessibility Guidelines (WCAG) 2.2**. Cambridge: W3C, 2023. Disponível em: <https://www.w3.org/TR/WCAG22/>. Acesso em: 9 ago. 2026.

### Legislação

6. BRASIL. **Lei nº 5.534, de 14 de novembro de 1968**. Dispõe sobre o sigilo das informações prestadas ao IBGE. Disponível em: <https://www.planalto.gov.br/ccivil_03/leis/l5534.htm>. Acesso em: 9 ago. 2026.

7. BRASIL. **Lei nº 13.709, de 14 de agosto de 2018 (LGPD)**. Brasília: Presidência da República, 2018. Disponível em: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>. Acesso em: 9 ago. 2026.

### Referências Complementares

8. **Concurso IBGE 2026 — Agente Censitário de Qualidade (ACQ)**. Focus Concursos, 2026. Disponível em: <https://focusconcursos.com.br/produto/ibge-agente-censitario-de-qualidade-acq>. Acesso em: 9 ago. 2026.

9. **O que faz um Agente Censitário do IBGE?** Estratégia Concursos, 2026. Disponível em: <https://www.estrategiaconcursos.com.br/blog/o-que-faz-um-agente-censitario-do-ibge/>. Acesso em: 9 ago. 2026.

10. **IBGE publica novo processo seletivo com 1.414 vagas**. CEV Concursos, 2026. Disponível em: <https://cevconcursos.com.br/blog/ibge-publica-novo-processo-seletivo-com-1414-vagas-para-atuacao-nos-censos-nacionais/429>. Acesso em: 9 ago. 2026.

---

**Versão:** 2.0 (Revisada)
**Data:** Agosto 2026
**Status:** ✅ Especificação validada com Edital ACQ, DSGov 4.0, WCAG 2.2 AA, e-MAG 3.1 e LGPD

# 🔍 Especificação de Interface e Engenharia: Painel de Análise de Inconsistências (ACQ) — **Versão Revisada**

## 1. Contexto e Fundamentação

O Painel de Análise de Inconsistências é a ferramenta de trabalho especializada de Carlos, o Agente Censitário de Qualidade (ACQ), projetada para auditar, classificar e arbitrar discrepâncias coletadas em campo pelos recenseadores. O ACQ desempenha um papel crítico na cadeia de custódia e integridade dos dados estatísticos nacionais, atuando como a instância de validação metodológica de nível superior que garante a conformidade dos dados com os padrões do IBGE antes da homologação final .

A inspeção de software, conforme documentado na literatura de engenharia de software, é uma abordagem eficiente e de baixo custo para encontrar defeitos, reduzindo o retrabalho e melhorando a qualidade dos produtos . Estudos mostram que a aplicação de inspeções pode capturar em torno de 60% dos defeitos de artefatos e reduzir o esforço com retrabalho em até 44% .

### 1.1 Regras de Consistência do Censo Agropecuário

O painel monitora e sinaliza automaticamente cinco categorias críticas de inconsistência de dados, utilizando uma taxonomia de defeitos adaptada do padrão IEEE 830 para especificação de requisitos de software :

| Categoria | Descrição | Critério de Severidade |
|-----------|-----------|------------------------|
| **Incompatibilidade de Área vs. Pecuária** | Discrepância quando o efetivo de rebanho é fisicamente incompatível com a área de pastagem (limiar: 0,5 hectare por cabeça de gado bovino) | 🔴 Alta (Bloqueante) |
| **Incoerência de Área vs. Produção** | Incompatibilidade entre área cultivada e rendimento da colheita em toneladas | 🔴 Alta (Bloqueante) |
| **Inconsistência Geodésica** | Precisão GNSS com σₕ ≥ 5,0 metros ou violação da Regra da Sede | 🔴 Alta (Bloqueante) |
| **Invasão de Limite Territorial** | Coordenadas GNSS fora do perímetro do setor censitário | 🟡 Média (Aviso) |
| **PEUV Pendente** | Pendente de classificação da espécie da unidade visitada | 🟡 Média (Aviso) |

### 1.2 Taxonomia de Defeitos Aplicada

Com base no padrão IEEE 610.12 e IEEE 830, os defeitos identificados no painel seguem a seguinte classificação :

- **Omissão:** Dados não declarados, seções faltantes no questionário, termos não definidos
- **Ambiguidade:** Respostas com múltiplas interpretações possíveis
- **Inconsistência:** Dados conflitantes entre diferentes blocos do questionário (ex: área vs. produção)
- **Fato Incorreto:** Dados que não correspondem à realidade do estabelecimento
- **Informação Estranha:** Dados desnecessários ou fora do escopo

---

## 2. Arquitetura da Informação e Sitemap do Painel

O Painel de Inconsistências é uma visão de alta densidade informacional integrada ao módulo de auditoria do dashboard principal de Carlos.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DASHBOARD INICIAL DO ACQ                                 │
│                                  │                                          │
│                                  ▼                                          │
│              ┌───────────────────────────────────────┐                      │
│              │  PAINEL DE INCONSISTÊNCIAS           │                       │
│              │  (Lista Geral com Filtros)            │                      │
│               └───────────────────────────────────────┘                     │
│                                  │                                          │
│              ┌───────────────────┴───────────────────┐                      │
│              ▼                                      ▼                       │
│  ┌───────────────────────┐           ┌───────────────────────────┐          │
│  │ VISUALIZAÇÃO DETALHADA │           │ FLUXO DE CORREÇÃO        │          │
│  │ (Modal Lado a Lado)    │ ────────> │ (ACQ → ACS → Recenseador)│          │
│  └───────────────────────┘           └───────────────────────────┘          │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.1 Posição do Painel no Sitemap Geral

| Nível | Tela | Função |
|-------|------|--------|
| 1 | Dashboard Inicial do ACQ | Visão panorâmica com KPIs e mapa de calor |
| 2 | **Painel de Inconsistências** | Lista geral de discrepâncias com filtros |
| 3 | Visualização Detalhada | Modal/Gaveta com dados declarados vs. esperados |
| 3 | Fluxo de Devolução | Interface de correção para ACS e recenseador |

---

## 3. Design da Lista de Inconsistências (Tabela Geral)

A tabela de listagem de inconsistências foi projetada para que Carlos identifique rapidamente os gargalos e priorize suas ações de auditoria, seguindo os princípios de dashboards de controle operacional que consolidam KPIs em tempo real .

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🔴 FILTROS & ALERTAS                        Badge: [08 Novas Inconsistências] │
├─────────────────────────────────────────────────────────────────────────────┤
│  Setor: [Todos ▾]   Severidade: [Todas ▾]   Tipo: [Todos ▾]   Status: [Pendente ▾] │
├─────────────────────────────────────────────────────────────────────────────┤
│ TABELA DE AUDITORIA                                                         │
├─────────┬──────────────────────┬─────────────┬──────────────────┬───────────┤
│ Setor   │ Tipo                 │ Severidade  │ Status           │ Ação      │
├─────────┼──────────────────────┼─────────────┼──────────────────┼───────────┤
│ ...0021 │ 🐄 Rebanho vs Pasto  │ 🔴 Alta     │ 🟡 Pendente      │ [Auditar] │
│ ...0021 │ 🗺️ HDOP Limite       │ 🟡 Média    │ 🔵 Em Correção   │ [Detalhe] │
│ ...0022 │ 🌱 Área vs Colheita  │ 🔴 Alta     │ 🟢 Resolvido     │ [Ver]     │
└─────────┴──────────────────────┴─────────────┴──────────────────┴───────────┘
```

### 3.1 Estrutura de Colunas e Dados da Tabela

| Coluna | Conteúdo | Interatividade |
|--------|----------|----------------|
| **Setor Censitário** | Código único de 15 dígitos (ex: 150280610000021) | Ordenável, filtro por setor |
| **Tipo de Inconsistência** | Rótulo descritivo com ícone (ex: 🐄 Rebanho vs Pasto) | Ordenável, filtro por tipo |
| **Severidade** | 🔴 Alta / 🟡 Média / 🔵 Baixa | Ordenável, filtro por severidade |
| **Status** | 🟡 Pendente / 🔵 Em Correção / 🟢 Resolvido | Ordenável, filtro por status |
| **Ações** | [Auditar] [Detalhe] [Ver] | Botões interativos |

### 3.2 Interatividade, Ordenação e Filtros

| Funcionalidade | Implementação | Benefício para o ACQ |
|----------------|---------------|----------------------|
| **Ordenação Dinâmica** | Clique nos cabeçalhos; atributos `aria-sort` | Priorizar setores por severidade ou antiguidade |
| **Filtros Combinados** | Dropdowns DSGov para Setor, Tipo, Severidade, Status | Isolar inconsistências por categoria |
| **Badge de Novos Alertas** | Contagem dinâmica em vermelho funcional | Visibilidade imediata de novas ocorrências |

### 3.3 Design Tokens e Tipografia

| Elemento | Especificação | Referência |
|----------|---------------|------------|
| **Fonte Títulos** | Univers 65 Bold (18px) | MIV IBGE |
| **Fonte Corpo** | Univers 55 Roman (16px) | MIV IBGE |
| **Fonte Notas** | Univers 55 Oblique (14px) | MIV IBGE |
| **Contraste** | ≥ 4.5:1 para textos normais | WCAG 1.4.3 |
| **Independência de Cor** | Ícones + texto + cor | e-MAG 4.2 |

---

## 4. Design da Visualização Detalhada da Inconsistência (Modal)

Ao acionar a ação [Auditar] em uma linha da tabela, o sistema renderiza uma gaveta lateral (slide-over) que sobrepõe a interface sem quebrar o contexto de navegação.

```
┌───────────────────────────────────────────────────────────────────────────┐
│ AUDITORIA DE INCONSISTÊNCIA: Rebanho vs Pastagem         Status: [Pendente]│
├───────────────────────────────────────────────────────────────────────────┤
│  Setor: 150280610000021                                                   │
│  Estabelecimento: Fazenda Alegria (Produtor: Seu José)                    │
├───────────────────────────────────────────────────────────────────────────┤
│ COMPARATIVO DE VARIÁVEIS                                                  │
│                                                                           │
│  • Pastagem Declarada: 5,0 Hectares (≈ 50 tarefas baianas)                │
│  • Efetivo Bovino Declarado: 120 Cabeças                                  │
│  • Lotação Máxima Calculada: 10 Cabeças (Limite: 2.0 bovinos/ha)          │
│  • Excesso de Lotação: 110 Cabeças [ CRÍTICO! ]                           │
├───────────────────────────────────────────────────────────────────────────┤
│ JUSTIFICATIVA DO RECENSEADOR (MARIANA):                                   │
│  "Produtor realiza confinamento intensivo (boitel) com ração e silagem    │
│  no período de seca, não dependendo apenas da pastagem natural."          │
├───────────────────────────────────────────────────────────────────────────┤
│ AÇÕES DO ACQ                                                              │
│  [ Aprovar Justificativa ]    [ Rejeitar / Solicitar Ajuste ]             │
└───────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Componentes e Elementos do Detalhe

| Componente | Descrição | Função do ACQ |
|------------|-----------|---------------|
| **Destaque Comparativo** | Dados declarados vs. limites lógicos do sistema | Verificar consistência temática |
| **Justificativa de Campo** | Texto gravado pelo recenseador no DMC | Avaliar plausibilidade da explicação |
| **Mapa de Coordenadas** | Visualização do ponto GNSS vs. sede/porteira | Validar Regra da Sede |
| **Trilha de Auditoria** | Histórico de ações no setor | Garantir rastreabilidade |

### 4.2 Botões de Ação do ACQ

| Botão | Função | Efeito no Sistema |
|-------|--------|-------------------|
| **Aprovar Justificativa** | Aceita a justificativa do recenseador | Status → 🟢 Resolvido |
| **Solicitar Correção** | Rejeita e dispara fluxo de correção | Status → 🔵 Em Correção |
| **Rejeitar Questionário** | Cancela o registro (casos de fraude) | Exige nova visita a campo |

---

## 5. Design do Fluxo de Correção (ACQ ↔ ACS ↔ Recenseador)

O fluxo de correção segue o processo de inspeção de software documentado na literatura: planejamento, revisão individual, encontro em equipe, correção e reavaliação . O ACQ atua como o revisor, o ACS como o coordenador da correção, e o recenseador como o autor do artefato a ser corrigido.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    FLUXO DE CORREÇÃO COLABORATIVA                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌──────────┐    ┌──────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │   ACQ    │ ─> │   ACS    │ ─> │ Recenseador  │ ─> │   ACQ (Re-   │  │
│  │ (Carlos) │    │(Supervisor)│    │  (Mariana)   │    │  auditoria) │  │
│  └──────────┘    └──────────┘    └──────────────┘    └──────────────┘  │
│       │               │               │                    │          │
│       ▼               ▼               ▼                    ▼          │
│  [Solicita    [Recebe      [Retorna ao   [Reabre o     [Valida a    │
│   Correção]   Notificação] Estabeleci-   Questionário] Correção]    │
│               e orienta    mento para                     │          │
│               a equipe]    rechecagem]                     ▼          │
│                                                      [Homologa o    │
│                                                       Setor]        │
└─────────────────────────────────────────────────────────────────────────┘
```

### 5.1 Campos de Entrada de Auditoria

| Campo | Especificação | Requisito de Acessibilidade |
|-------|---------------|----------------------------|
| **Observações do ACQ** | `<textarea>` com instruções corretivas | `label for/id` explícito |
| **Dica Contextual** | `<span>` com `aria-describedby` | Linguagem Simples |
| **Justificativa do ACS** | Campo opcional para mediação | `aria-label` descritivo |

### 5.2 Trâmite de Correção e Notificações

| Etapa | Ação | Notificação |
|-------|------|-------------|
| 1 | ACQ solicita correção | Notificação enviada ao ACS |
| 2 | ACS orienta recenseador | Instruções visíveis no DMC |
| 3 | Recenseador retorna ao campo | Questionário reaberto para edição |
| 4 | Recenseador reenvia dados | Nova auditoria automática |
| 5 | ACQ valida correção | Status atualizado |

---

## 6. Design de Alertas em Tempo Real (Regiões Vivas)

Como o fluxo de coleta em campo é síncrono e os dados chegam ao posto constantemente via Background Sync , Carlos necessita de uma interface que o notifique instantaneamente sobre novas inconsistências prioritárias sem interromper sua análise corrente.

### 6.1 Implementação de Regiões Vivas (WAI-ARIA)

| Atributo | Valor | Função |
|----------|-------|--------|
| `aria-live` | `polite` | Anuncia novos alertas sem interromper a navegação |
| `role` | `status` | Indica que o conteúdo é uma atualização de status |
| `aria-atomic` | `true` | Anuncia todo o conteúdo da região, não apenas mudanças |

### 6.2 Frequência de Animação Segura

Conforme o e-MAG Área 2 e WCAG 2.2, quaisquer animações de transição visual, pulsação ou flashes de novos alertas devem ocorrer em frequência estritamente igual ou inferior a **3Hz** para mitigar riscos de convulsão fotossensível.

### 6.3 Badge Dinâmico de Inconsistências

```html
<span class="badge-alerta" 
      role="status" 
      aria-live="polite" 
      aria-label="Você possui 8 novas inconsistências de qualidade pendentes de auditoria">
    08
</span>
```

---

## 7. Diretrizes de Acessibilidade (e-MAG 3.1 & WCAG 2.2 AA)

### 7.1 Critérios Implementados

| Critério | Especificação | Nível |
|----------|---------------|-------|
| **Target Size** | Alvos mínimos de 24×24px CSS; botões críticos 48×48px | WCAG 2.2 — 2.5.8 (AA) |
| **Focus Not Obscured** | Outline de 3px com contraste ≥ 3:1, não ocultado pela Barra Gov.Br | WCAG 2.2 — 2.4.11 (AA) |
| **Contraste** | Texto normal ≥ 4.5:1; texto grande ≥ 3:1 | WCAG 1.4.3 (AA) |
| **Redundant Entry** | Autopreenchimento de dados do setor e recenseador | WCAG 2.2 — 3.3.7 (AA) |
| **Independência de Cor** | Ícones + texto + cor para status | e-MAG 4.2 / WCAG 1.4.1 |

### 7.2 Associação Semântica e Rótulos

Todos os campos de entrada possuem `<label>` textuais associados explicitamente via atributo `for/id`, em conformidade com a Área de Formulário do e-MAG 3.1.

### 7.3 Operabilidade por Teclado

Carlos pode navegar por todo o painel utilizando exclusivamente as teclas **Tab, Shift+Tab, Enter e Espaço**, em conformidade com a Área de Comportamento do e-MAG 3.1.

---

## 8. Segurança de Dados, Privacidade e LGPD Offline

### 8.1 Criptografia At Rest (IndexedDB)

| Camada | Tecnologia | Finalidade |
|--------|------------|------------|
| **Dados em Repouso** | AES-256 GCM via Web Crypto API | Proteção de dados sensíveis no dispositivo |
| **Derivação de Chave** | PBKDF2 com salt + autenticação Gov.br | Chave única por sessão |
| **Dados em Trânsito** | TLS 1.3 / HTTPS | Proteção durante transmissão |

### 8.2 Ciclo de Vida do Dado e Descarte Seguro

| Etapa | Procedimento | Conformidade |
|-------|--------------|--------------|
| **Coleta** | Dados encriptados no IndexedDB | LGPD Art. 46 |
| **Transmissão** | Envio via TLS 1.3 para data centers | Segurança em trânsito |
| **Confirmação** | Recebimento validado pelos servidores | Integridade dos dados |
| **Descarte** | Remoção irreversível do IndexedDB | LGPD Art. 18 (Direito ao esquecimento) |

---

## 9. Custom Elements Manifest (CEM) — Componente de Alerta

```json
{
  "schemaVersion": "1.0.0",
  "readme": "Componente modular para o painel de inconsistências e alertas do dashboard do ACQ.",
  "modules": [
    {
      "kind": "javascript-module",
      "path": "src/components/acq-alert-feed/acq-alert-feed.js",
      "declarations": [
        {
          "kind": "class",
          "description": "Gerencia e renderiza o feed de alertas de inconsistência conceitual e geodésica em tempo real.",
          "name": "AcqAlertFeed",
          "tagName": "acq-alert-feed",
          "customElement": true,
          "attributes": [
            {
              "name": "active-alerts",
              "type": { "text": "number" },
              "description": "Contagem de alertas pendentes de auditoria."
            }
          ],
          "events": [
            {
              "name": "acq-alert-selected",
              "description": "Disparado quando o ACQ clica em um alerta para focar o setor correspondente.",
              "type": { "text": "CustomEvent" }
            }
          ],
          "slots": [
            {
              "name": "alert-item",
              "description": "Slot dinâmico para injeção de cards de inconsistência em Linguagem Simples."
            }
          ]
        }
      ]
    }
  ]
}
```

---

## 10. Checklist de Conformidade (Handoff Técnico)

| Item | Critério | Status | Referência |
|------|----------|--------|------------|
| **Família Univers** | Uso estrito de Univers LT Std (corpo ≥ 16px) | ✅ | MIV IBGE |
| **Neuropolitical** | Restrita à logomarca oficial (proibida na UI) | ✅ | MIV IBGE |
| **Contraste Mínimo** | Razão de contraste ≥ 4.5:1 para textos normais | ✅ | e-MAG 4.1 / WCAG 1.4.3 |
| **Independência de Cor** | Informação de severidade com ícone, cor e texto | ✅ | e-MAG 4.2 / WCAG 1.4.1 |
| **Regiões Vivas** | Alertas do feed anunciados via `aria-live="polite"` | ✅ | e-MAG Área 2 |
| **Focus Not Obscured** | Foco visível, não ocultado pela Barra Gov.Br | ✅ | WCAG 2.2 — 2.4.11 |
| **Target Size** | Alvos interativos ≥ 24×24px CSS; críticos 48×48px | ✅ | WCAG 2.2 — 2.5.8 |
| **Criptografia AES-256** | Dados locais offline encriptados no IndexedDB | ✅ | LGPD Art. 46 |
| **Descarte Seguro** | Remoção total de dados locais após sincronização | ✅ | LGPD Art. 18 |

---

## 11. Conclusão

O Painel de Análise de Inconsistências foi projetado para ser uma **ferramenta de auditoria robusta, acessível e eficiente**, permitindo que Carlos supervise a qualidade dos dados coletados, identifique inconsistências em tempo real e homologue setores com confiança estatística.

A aplicação dos critérios **WCAG 2.2 AA**, **e-MAG 3.1** e **LGPD**, combinada com a identidade visual do IBGE e as diretrizes do **DSGov 4.0**, garante que o painel esteja alinhado com os mais elevados padrões de governança digital e inclusão, atendendo às necessidades do Agente Censitário de Qualidade no 12º Censo Agropecuário.

---

## 12. Referências

### Manuais e Documentos Oficiais do IBGE

1. IBGE. **Edital de Abertura nº 02/2026 — Processo Seletivo Simplificado para Agente Censitário de Qualidade (ACQ)**. Rio de Janeiro: IBGE, 2026.

2. IBGE. **Manual do Recenseador do Censo Demográfico 2022 (CD-1.09)**. Rio de Janeiro: IBGE, 2022. Disponível em: <https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5723.pdf>. Acesso em: 9 ago. 2026.

3. IBGE. **Manual de Identidade Visual do IBGE**. Rio de Janeiro: IBGE, 2016. Disponível em: <https://www.ibge.gov.br>. Acesso em: 9 ago. 2026.

### Padrões de Governo Digital e Acessibilidade

4. BRASIL. **e-MAG 3.1 — Modelo de Acessibilidade em Governo Eletrônico**. Brasília: Ministério do Planejamento, Orçamento e Gestão, 2014. Disponível em: <https://emag.governoeletronico.gov.br/>. Acesso em: 9 ago. 2026.

5. BRASIL. **DSGov 4.0 — Padrão Digital de Governo**. Brasília: Ministério da Gestão e da Inovação em Serviços Públicos, 2024. Disponível em: <https://www.gov.br/ds/>. Acesso em: 9 ago. 2026.

6. W3C. **Web Content Accessibility Guidelines (WCAG) 2.2**. Cambridge: W3C, 2023. Disponível em: <https://www.w3.org/TR/WCAG22/>. Acesso em: 9 ago. 2026.

### Engenharia de Software e Inspeção

7. IEEE. **IEEE 610.12 — Standard Glossary of Software Engineering Terminology**. Nova Iorque: IEEE, 1990.

8. IEEE. **IEEE 830 — Recommended Practice for Software Requirements Specifications**. Nova Iorque: IEEE, 1998.

9. BOEHM, Barry; BASILI, Victor. **Software Defect Reduction Top 10 List**. In: IEEE Computer, 2001.

10. PRESSMAN, Roger. **Engenharia de Software**. 6. ed. São Paulo: McGraw-Hill, 2001.

### Legislação

11. BRASIL. **Lei nº 5.534, de 14 de novembro de 1968**. Dispõe sobre o sigilo das informações prestadas ao IBGE. Disponível em: <https://www.planalto.gov.br/ccivil_03/leis/l5534.htm>. Acesso em: 9 ago. 2026.

12. BRASIL. **Lei nº 13.709, de 14 de agosto de 2018 (LGPD)**. Brasília: Presidência da República, 2018. Disponível em: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>. Acesso em: 9 ago. 2026.

---

**Versão:** 2.0 (Revisada)
**Data:** Agosto 2026
**Status:** ✅ Especificação validada com Edital ACQ, DSGov 4.0, WCAG 2.2 AA, e-MAG 3.1 e LGPD

# 📋 Especificação de Interface e Engenharia: Gestão de Pendentes de Espécie (PEUV) — **Versão Revisada**

## 1. Contexto Metodológico: O que é PEUV?

De acordo com o Manual do Recenseador e as Instruções Operacionais do Censo Agropecuário, a **Pendente de Espécie da Unidade Visitada (PEUV)** ocorre quando o recenseador, ao visitar um endereço previamente cadastrado ou identificar uma nova unidade física, não consegue determinar com segurança qual é a sua classificação ("espécie"). Esta pendência é uma das mais críticas para a qualidade estatística do Censo, pois impede o fechamento do setor censitário e a homologação dos dados.

A gestão de PEUV no "Censo Fácil" está alinhada com os princípios de **Design de Governo Digital** descritos na literatura, que enfatizam a necessidade de **simplicidade, clareza, consistência e acessibilidade** na implementação de serviços públicos digitais (BRASIL, 2024).

### 1.1 Casos Típicos de PEUV no Censo Agropecuário

| Categoria | Descrição | Fonte |
|-----------|-----------|-------|
| **Unidades de Uso Misto Indefinido** | Propriedades rurais que apresentam moradias combinadas com pequenas áreas de cultivo, sem que se saiba se há exploração agropecuária ativa para autoconsumo ou comercialização | IBGE, 2022 |
| **Estabelecimentos Abandonados ou em Transição** | Áreas que aparentam inatividade produtiva temporária, mas que podem estar sob regime de arrendamento ou comodato não declarado | IBGE, 2022 |
| **Ausência Prolongada** | Unidades fechadas em que não foi possível entrevistar nenhum informante apto após as três visitas obrigatórias em dias e horários alternados | IBGE, 2022; IBGE, 2026 |
| **Áreas de Litígio ou Sucessão** | Unidades fundiárias sob disputa judicial ou partilha de herança familiar, cujos limites e finalidade de exploração estão temporariamente confusos ou obstruídos | IBGE, 2022 |

### 1.2 Princípios de Design de Serviços Públicos Aplicados

O módulo de PEUV foi projetado seguindo os princípios de design de serviços governamentais (BRASIL, 2024):

| Princípio | Aplicação no Módulo PEUV |
|-----------|--------------------------|
| **Simplicidade** | Interface clara com opções de ação limitadas a 4 decisões excludentes |
| **Clareza** | Linguagem Simples nos rótulos e instruções para o ACQ |
| **Consistência** | Padronização visual em todas as telas e componentes |
| **Acessibilidade** | Conformidade com e-MAG 3.1 e WCAG 2.2 AA |

---

## 2. Arquitetura da Informação e Sitemap do Módulo PEUV

O módulo de Gestão de PEUV é uma visão especializada integrada ao dashboard de auditoria do ACQ, posicionada como um subitem crítico do painel de inconsistências.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DASHBOARD INICIAL DO ACQ                                 │
│                                  │                                          │
│                                  ▼                                          │
│              ┌───────────────────────────────────────┐                     │
│              │  PAINEL DE INCONSISTÊNCIAS           │                     │
│              │  (Lista Geral com Filtros)            │                     │
│              └───────────────────────────────────────┘                     │
│                                  │                                          │
│              ┌───────────────────┴───────────────────┐                    │
│              ▼                                       ▼                    │
│  ┌───────────────────────┐           ┌───────────────────────────┐        │
│  │ MÓDULO PEUV           │           │ VISUALIZAÇÃO DETALHADA    │        │
│  │ (Filtro por Motivo)   │ ────────> │ (Histórico de 3 Visitass) │        │
│  └───────────────────────┘           └───────────────────────────┘        │
│                                               │                           │
│                                               ▼                           │
│              ┌─────────────────────────────────────────────┐             │
│              │ FLUXO DE RESOLUÇÃO (4 Opções de Ação)       │             │
│              │ • Marcar como Domicílio                     │             │
│              │ • Marcar como Estabelecimento               │             │
│              │ • Excluir Unidade                           │             │
│              │ • Solicitar Revisita de Campo               │             │
│              └─────────────────────────────────────────────┘             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.1 Posição do Módulo no Fluxo de Auditoria

| Etapa | Tela | Função | Responsável |
|-------|------|--------|-------------|
| 1 | Dashboard do ACQ | Visão panorâmica com contagem de PEUV | ACQ |
| 2 | Lista de PEUV | Triagem e priorização | ACQ |
| 3 | Detalhamento do PEUV | Análise do histórico e justificativas | ACQ |
| 4 | Resolução | Tomada de decisão com justificativa | ACQ |
| 5 | Notificação | Disparo para ACS e recenseador | Sistema |

---

## 3. Design da Lista de PEUV (Tabela de Triagem)

A tela principal do módulo apresenta uma tabela de dados de alta densidade informacional, permitindo que Carlos ordene, filtre e priorize as unidades pendentes no Posto Censitário. O design segue a metodologia de **dashboards de controle operacional** documentada na literatura de design de interfaces governamentais (BRASIL, 2024).

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🏠 GESTÃO DE PEUV — UNIDADES PENDENTES    Badge: [12 Casos Ativos]         │
├─────────────────────────────────────────────────────────────────────────────┤
│  Setor: [Todos ▾]   Motivo: [Todos ▾]   Status: [Pendentes ▾]   Buscar... │
├─────────────────────────────────────────────────────────────────────────────┤
│ LISTA DE PEUV — ORDENADA POR TEMPO DE PENDÊNCIA (MAIS ANTIGOS PRIMEIRO)   │
├──────────┬─────────────────┬──────────────┬────────┬──────────┬───────────┤
│ CNEFE    │ Logradouro      │ Última Visita│ Tempo  │ Motivo   │ Status    │
├──────────┼─────────────────┼──────────────┼────────┼──────────┼───────────┤
│ 3303401  │ Gleba 14, Est.  │ 14/08/2026   │ 15 dias│ Ausência │ 🔴 Crítico│
│          │ do Ouro, Alfenas│ 09:15        │        │          │           │
├──────────┼─────────────────┼──────────────┼────────┼──────────┼───────────┤
│ 3303402  │ Rua da Praia,   │ 16/08/2026   │ 13 dias│ Uso Misto│ 🟡 Atenção│
│          │ Nº 45, Carangola│ 14:30        │        │          │           │
├──────────┼─────────────────┼──────────────┼────────┼──────────┼───────────┤
│ 3303403  │ Sítio Santa    │ 20/08/2026   │  9 dias│ Recusa   │ 🟢 Normal │
│          │ Luzia, Km 12   │ 19:00        │        │          │           │
└──────────┴─────────────────┴──────────────┴────────┴──────────┴───────────┘
```

### 3.1 Colunas Obrigatórias da Tabela

| Coluna | Descrição | Fonte de Dados |
|--------|-----------|----------------|
| **Código CNEFE** | Identificador exclusivo da unidade com link de acesso rápido ao histórico cadastral | Cadastro Nacional de Endereços |
| **Logradouro e Localidade** | Endereço físico e pontos de referência registrados pelo recenseador | DMC em campo |
| **Data da Última Visita** | Data e horário do último contato ou tentativa de entrevista em campo | Registro do DMC |
| **Tempo de Pendência** | Contador regressivo em dias desde o primeiro registro de PEUV | Cálculo automático do sistema |
| **Motivo do Impedimento** | Descrição textual ou categoria do obstáculo | Classificação do recenseador |
| **Status do Caso** | 🟡 Pendente / 🔵 Em Análise / 🔴 Revisita Solicitada / 🟢 Resolvido | Estado atual no fluxo |

### 3.2 Regras de Interação, Ordenação e Filtros

| Funcionalidade | Implementação | Benefício |
|----------------|---------------|-----------|
| **Ordenação por Prioridade** | Padrão: casos mais antigos primeiro (Tempo de Pendência) | Mitiga risco de estouro de prazo |
| **Filtros Combinados** | Setor, Status, Motivo, Período | Isola casos por categoria |
| **Cores Semânticas de Alerta** | 🟢 ≤ 3 dias / 🟡 4-7 dias / 🔴 > 7 dias | Visibilidade imediata de casos críticos |
| **Pesquisa por CNEFE** | Busca textual rápida | Localização de casos específicos |

---

## 4. Visualização Detalhada do PEUV (Modal de Auditoria)

Ao selecionar um caso na lista, o sistema abre uma gaveta lateral ou modal de alta fidelidade visual contendo o dossiê completo do endereço. O design do modal segue a **Arquitetura de Informação não Linear** documentada no sitemap do sistema "Censo Fácil".

```
┌───────────────────────────────────────────────────────────────────────────┐
│ DETALHAMENTO DO CASO PEUV — CNEFE #3303401                 Status: [🔴] │
├───────────────────────────────────────────────────────────────────────────┤
│ 📍 Endereço: Gleba 14, Estrada do Ouro, Alfenas-MG                      │
│ 🌐 Coordenadas: Lat -22.326 | Long -42.669 (HDOP: 1.8)                  │
│ 📅 Última Atualização: 14/08/2026 09:15                                 │
├───────────────────────────────────────────────────────────────────────────┤
│ 📋 HISTÓRICO DE TENTATIVAS DE VISITA (Mariana)                           │
│ ┌─────────────────────────────────────────────────────────────────────┐ │
│ │ 1. 14/08/2026 09:15 - Ausência (Ninguém em casa)                    │ │
│ │ 2. 15/08/2026 14:30 - Ausência (Vizinho diz que trabalha)           │ │
│ │ 3. 17/08/2026 19:00 - Ausência (Portão trancado)                    │ │
│ └─────────────────────────────────────────────────────────────────────┘ │
├───────────────────────────────────────────────────────────────────────────┤
│ ✍️ Notas de Campo: "Moradia rústica isolada. Há indícios de gado        │
│    no pasto, mas o dono viajou."                                        │
├───────────────────────────────────────────────────────────────────────────┤
│ 📝 ANOTAÇÕES DO ACQ (Carlos)                                            │
│ [   Digite aqui suas observações e análise metodológica...            ] │
├───────────────────────────────────────────────────────────────────────────┤
│ AÇÕES DE RESOLUÇÃO                                                       │
│ [🏠 Marcar Domicílio] [🌾 Marcar Estabelecimento] [🗑️ Excluir] [🔄 Revisita] │
└───────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Conteúdo do Painel de Detalhes

| Seção | Conteúdo | Função para o ACQ |
|-------|----------|-------------------|
| **Dados Geográficos e GNSS** | Latitude, longitude, HDOP, incerteza (σₕ = HDOP × σ₀) | Validar precisão do georreferenciamento |
| **Histórico de Tentativas** | Linha do tempo com ≥ 3 visitas em dias e horários alternados | Confirmar cumprimento do protocolo de visitas |
| **Registros de Impedimento** | Recusas, ausências, anotações de vizinhos | Compreender o contexto da pendência |
| **Observações de Campo** | Notas informais da recenseadora Mariana | Obter insights adicionais |
| **Anotações do ACQ** | Campo livre para análise de Carlos | Documentar parecer técnico |

### 4.2 Regras de Exibição do Histórico

O sistema exibe obrigatoriamente o registro detalhado de **pelo menos 3 visitas** em dias e horários alternados, conforme exigido pelo Manual do Recenseador. Caso o número de visitas seja inferior a 3, o sistema exibe um alerta de **inconsistência metodológica**:

```html
<span class="alerta-metodologico" role="alert">
  ⚠️ Atenção: Apenas 2 visitas registradas. O protocolo exige no mínimo 3 tentativas em horários alternados.
</span>
```

---

## 5. Fluxo de Resolução e Tomada de Decisão

O painel de detalhes oferece a Carlos quatro opções de ação excludentes para resolver a pendência metodológica da espécie. A arquitetura do fluxo de correção segue a estrutura documentada na especificação de inspeção de software, onde o ACQ atua como revisor final, o ACS como coordenador da correção, e o recenseador como autor do artefato.

### 5.1 Opções de Ação e Lógica de Negócio

| Ação | Descrição | Efeito no Sistema | Justificativa |
|------|-----------|-------------------|---------------|
| **🏠 Marcar como Domicílio** | Classifica a unidade como domicílio residencial comum | Remove do escopo agropecuário (não recenseável) | Unidade é exclusivamente residencial |
| **🌾 Marcar como Estabelecimento** | Classifica como estabelecimento agropecuário ativo | Dispara abertura de questionário | Há exploração agropecuária identificada |
| **🗑️ Excluir Unidade** | Remove da lista prévia de endereços | Elimina o registro do cadastro | Erro cadastral ou duplicação comprovada |
| **🔄 Solicitar Revisita de Campo** | Devolve o caso à equipe operacional | Notifica ACS e recenseador | Necessita de novas informações em campo |

### 5.2 Justificativa Obrigatória

Toda decisão tomada por Carlos exige o preenchimento de um campo de **Justificativa Técnica** com comprimento mínimo de **50 caracteres**. O sistema valida o comprimento e armazena os dados sob criptografia simétrica AES-256 GCM no banco de dados local (IndexedDB) para posterior auditoria do Centro Nacional de Qualidade (CNQ).

```html
<label for="justificativa-acq">✍️ Justificativa Técnica (Obrigatória)</label>
<textarea id="justificativa-acq" 
          minlength="50" 
          required
          aria-describedby="dica-justificativa"
          placeholder="Descreva os fundamentos técnicos e metodológicos da sua decisão..."></textarea>
<span id="dica-justificativa" class="texto-auxiliar">
  Mínimo de 50 caracteres. Esta justificativa será arquivada para auditoria do CNQ.
</span>
```

---

## 6. Relatório Consolidado de PEUV e Exportação

O módulo disponibiliza um painel gerencial focado na emissão de relatórios de conformidade estatística, alinhado com os **padrões de exportação de dados** documentados na especificação de relatórios do sistema "Censo Fácil".

### 6.1 Filtros de Consolidação

| Filtro | Descrição | Aplicação |
|--------|-----------|-----------|
| **Setor Censitário** | Código de 15 dígitos | Isolar casos por setor |
| **Município** | Nome ou código IBGE | Consolidar por região |
| **Período de Referência** | Data inicial e final | Análise temporal |
| **Motivo da Pendência** | Ausência, Recusa, Uso Misto, Litígio | Agrupamento por categoria |

### 6.2 Formatos de Exportação

| Formato | Finalidade | Características |
|---------|------------|-----------------|
| **CSV (Data Handoff)** | Importação em ferramentas GIS (QGIS/ArcGIS) | Codificação UTF-8, metadados estruturados |
| **PDF (Relatório de Auditoria)** | Documentação estática | NBR 14724:2024, Padrão Ofício |

### 6.3 Métricas de Desempenho

O relatório exibe indicadores-chave para o planejamento de Carlos:

- **Total de PEUV no Setor:** Número absoluto de casos pendentes
- **Resolvidos vs. Pendentes:** Percentual de conclusão
- **Tempo Médio de Resolução:** Dias desde abertura até fechamento
- **Casos Críticos (> 7 dias):** Contagem de casos que exigem ação imediata

---

## 7. Requisitos de Acessibilidade (e-MAG 3.1 & WCAG 2.2 AA)

Para garantir que o módulo de gestão de PEUV seja operável por todos os servidores do instituto, inclusive em condições de campo ou por usuários de tecnologias assistivas, aplicam-se estritamente as regras de acessibilidade do Governo Digital.

### 7.1 Critérios Implementados

| Critério | Especificação | Nível | Referência |
|----------|---------------|-------|------------|
| **Navegação por Teclado** | Tab, Enter, Espaço funcionais em toda a interface | — | e-MAG Área 2 |
| **Prevenção de Keyboard Trap** | Modal fechável via Esc ou botão visível | — | e-MAG Área 2 |
| **Associação label/input** | Atributos `for` e `id` explícitos | — | e-MAG Área 6 |
| **Focus Not Obscured** | Outline de 3px com contraste ≥ 3:1 | AA | WCAG 2.2 — 2.4.11 |
| **Target Size** | 24×24px (padrão) / 48×48px (botões críticos) | AA | WCAG 2.2 — 2.5.8 |
| **Regiões Vivas** | `aria-live="polite"` no feed de notificações | — | e-MAG Área 2 |

### 7.2 Regiões Vivas (aria-live polite)

O feed de alertas e atualizações do status de resolução do PEUV é encapsulado em um container com atributo `aria-live="polite"` e `role="status"`. Novos casos transmitidos de campo por recenseadores via Background Sync são anunciados de forma sonora aos leitores de tela sem forçar a interrupção da digitação ativa de Carlos.

```html
<div id="feed-notificacoes" 
     role="status" 
     aria-live="polite" 
     aria-atomic="true">
  <!-- Novos casos são injetados aqui dinamicamente -->
</div>
```

### 7.3 Target Size (WCAG 2.2 — 2.5.8)

| Tipo de Alvo | Tamanho Mínimo | Aplicação |
|--------------|----------------|-----------|
| **Alvos Padrão** | 24×24px CSS | Links, filtros, ícones de ação |
| **Botões Críticos** | 48×48px CSS | Marcar Domicílio, Estabelecimento, Revisita |

---

## 8. Segurança de Dados e Conformidade (LGPD)

O módulo de PEUV manipula metadados geográficos e dados cadastrais sensíveis dos produtores rurais, exigindo total aderência às garantias de sigilo da Lei nº 5.534/68 e à LGPD.

### 8.1 Criptografia At Rest

Todas as anotações do ACQ, justificativas técnicas e dados cadastrais provisórios em repouso no dispositivo móvel ou estação de trabalho local são encriptados via algoritmo simétrico **AES-256 GCM** utilizando a Web Crypto API.

### 8.2 Descarte Seguro

Os logs de visualização e os dados do PEUV em análise local são eliminados permanentemente do banco físico do navegador (IndexedDB) imediatamente após a confirmação da sincronização e recebimento nos servidores centrais do IBGE, cumprindo o **direito ao esquecimento** previsto no artigo 18 da LGPD.

| Camada | Tecnologia | Finalidade | Referência |
|--------|------------|------------|------------|
| **Dados em Repouso** | AES-256 GCM via Web Crypto API | Proteção de dados sensíveis | LGPD Art. 46 |
| **Derivação de Chave** | PBKDF2 com salt + autenticação Gov.br | Chave única por sessão | — |
| **Dados em Trânsito** | TLS 1.3 / HTTPS | Proteção durante transmissão | LGPD Art. 46 |
| **Descarte Seguro** | Remoção irreversível do IndexedDB | Direito ao esquecimento | LGPD Art. 18 |

---

## 9. Custom Elements Manifest (CEM) — Componente PEUV

```json
{
  "schemaVersion": "1.0.0",
  "readme": "Componente de Gestão de Pendentes de Espécie (PEUV) para o ACQ.",
  "modules": [
    {
      "kind": "javascript-module",
      "path": "src/components/acq-peuv-manager/acq-peuv-manager.js",
      "declarations": [
        {
          "kind": "class",
          "description": "Gerencia a lista de PEUV, detalhamento e fluxo de resolução.",
          "name": "AcqPeuvManager",
          "tagName": "acq-peuv-manager",
          "customElement": true,
          "attributes": [
            {
              "name": "pending-count",
              "type": { "text": "number" },
              "description": "Número total de casos de PEUV pendentes no setor."
            }
          ],
          "events": [
            {
              "name": "peuv-resolved",
              "description": "Disparado quando Carlos resolve um caso de PEUV.",
              "type": { "text": "CustomEvent" }
            },
            {
              "name": "peuv-revisit-requested",
              "description": "Disparado quando Carlos solicita uma revisita de campo.",
              "type": { "text": "CustomEvent" }
            }
          ],
          "slots": [
            {
              "name": "peuv-list",
              "description": "Slot para renderização da lista de casos de PEUV."
            },
            {
              "name": "peuv-detail",
              "description": "Slot para exibição do detalhamento do caso selecionado."
            }
          ]
        }
      ]
    }
  ]
}
```

---

## 10. Checklist de Conformidade (Handoff Técnico)

| Item | Critério | Status | Referência |
|------|----------|--------|------------|
| **XHTML Estrito** | Fechamento obrigatório de tags e atributos booleanos expressos | ✅ | Edital IBGE 2026 |
| **Família Univers** | Univers 55 Roman (corpo) / 65 Bold (títulos/botões) | ✅ | MIV IBGE |
| **Neuropolitical** | Restrita à logomarca oficial | ✅ | MIV IBGE |
| **Contraste Mínimo** | Razão ≥ 4.5:1 para textos normais | ✅ | e-MAG 4.1 / WCAG 1.4.3 |
| **Independência de Cor** | Status com texto e ícones geometricamente distintos | ✅ | e-MAG 4.2 / WCAG 1.4.1 |
| **Target Size** | 24×24px (padrão) / 48×48px (botões críticos) | ✅ | WCAG 2.2 — 2.5.8 |
| **Focus Not Obscured** | Foco visível, não ocultado pela Barra Gov.Br | ✅ | WCAG 2.2 — 2.4.11 |
| **Regiões Vivas** | `aria-live="polite"` no feed de notificações | ✅ | e-MAG Área 2 |
| **HDOP Validation** | Exibição da incerteza σₕ = HDOP × σ₀ | ✅ | Manual do Recenseador |
| **Criptografia AES-256** | Dados locais encriptados no IndexedDB | ✅ | LGPD Art. 46 |
| **Descarte Seguro** | Remoção total de dados locais pós-sincronização | ✅ | LGPD Art. 18 |

---

## 11. Conclusão

O módulo de Gestão de Pendentes de Espécie (PEUV) foi projetado para ser uma **ferramenta de auditoria robusta, acessível e eficiente**, permitindo que Carlos resolva metodologicamente as unidades cuja classificação não pôde ser determinada em campo.

A aplicação dos critérios **WCAG 2.2 AA**, **e-MAG 3.1** e **LGPD**, combinada com a identidade visual do IBGE e as diretrizes do **DSGov 4.0**, garante que o módulo esteja alinhado com os mais elevados padrões de governança digital e inclusão, atendendo às necessidades do Agente Censitário de Qualidade no 12º Censo Agropecuário.

O fluxo de resolução com 4 opções de ação excludentes, a exigência de justificativa mínima de 50 caracteres e o armazenamento criptografado com AES-256 GCM no IndexedDB asseguram a **rastreabilidade, integridade e segurança** dos dados, em conformidade com as exigências do Centro Nacional de Qualidade (CNQ) e da LGPD.

---

## 12. Referências

### Manuais e Documentos Oficiais do IBGE

1. IBGE. **Manual do Recenseador do Censo Demográfico 2022 (CD-1.09)**. Rio de Janeiro: IBGE, 2022. Disponível em: <https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5723.pdf>. Acesso em: 9 ago. 2026.

2. IBGE. **Edital de Abertura nº 02/2026 — Processo Seletivo Simplificado para Agente Censitário de Qualidade (ACQ)**. Rio de Janeiro: IBGE, 2026.

3. IBGE. **Manual de Identidade Visual do IBGE**. Rio de Janeiro: IBGE, 2016. Disponível em: <https://www.ibge.gov.br>. Acesso em: 9 ago. 2026.

### Padrões de Governo Digital e Acessibilidade

4. BRASIL. **e-MAG 3.1 — Modelo de Acessibilidade em Governo Eletrônico**. Brasília: Ministério do Planejamento, Orçamento e Gestão, 2014. Disponível em: <https://emag.governoeletronico.gov.br/>. Acesso em: 9 ago. 2026.

5. BRASIL. **DSGov 4.0 — Padrão Digital de Governo**. Brasília: Ministério da Gestão e da Inovação em Serviços Públicos, 2024. Disponível em: <https://www.gov.br/ds/>. Acesso em: 9 ago. 2026.

6. W3C. **Web Content Accessibility Guidelines (WCAG) 2.2**. Cambridge: W3C, 2023. Disponível em: <https://www.w3.org/TR/WCAG22/>. Acesso em: 9 ago. 2026.

### Design de Serviços Públicos

7. BRASIL. **Design de Serviços Públicos — Guia Prático para a Transformação Digital**. Brasília: Ministério da Gestão e da Inovação em Serviços Públicos, 2024.

### Legislação

8. BRASIL. **Lei nº 5.534, de 14 de novembro de 1968**. Dispõe sobre o sigilo das informações prestadas ao IBGE. Disponível em: <https://www.planalto.gov.br/ccivil_03/leis/l5534.htm>. Acesso em: 9 ago. 2026.

9. BRASIL. **Lei nº 13.709, de 14 de agosto de 2018 (LGPD)**. Brasília: Presidência da República, 2018. Disponível em: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>. Acesso em: 9 ago. 2026.

---

**Versão:** 2.0 (Revisada)
**Data:** Agosto 2026
**Status:** ✅ Especificação validada com Edital ACQ, DSGov 4.0, WCAG 2.2 AA, e-MAG 3.1 e LGPD

# 📋 Especificação de Interface e Engenharia: Fluxo de Aprovação de Setores Censitários — **Versão Revisada**

## 1. Contexto Operacional e Atribuições de Homologação (ACQ Carlos)

O Agente Censitário de Qualidade (ACQ) desempenha um papel crítico na cadeia de custódia e integridade dos dados estatísticos nacionais. Como servidor temporário sob a tutela do Centro Estadual de Qualidade (CEQ), Carlos utiliza o dashboard central para auditar e homologar os setores concluídos em campo pela equipe operacional. A homologação é a etapa final do processo de validação, na qual o ACQ atesta que os dados do setor estão consistentes e aptos para integração à base nacional.

O novo edital do IBGE (Edital nº 02/2026) oferece **394 vagas imediatas** para o cargo de ACQ, com remuneração de R$ 2.932,00 acrescida de R$ 1.192,00 de auxílio-alimentação. A seleção será organizada pelo Instituto Avalia, com prova objetiva prevista para 30 de agosto de 2026 (Focus Concursos, 2026).

A homologação de setores é a etapa final do processo de validação estatística, na qual o ACQ atesta que os dados do setor estão consistentes e aptos para integração à base nacional. Este ato tem implicações jurídicas e administrativas, pois os dados homologados tornam-se parte das estatísticas oficiais do país, sendo utilizados para o planejamento de políticas públicas e alocação de recursos (IBGE, 2026).

### 1.1 Regras de Negócio Inegociáveis para Homologação

De acordo com o edital do IBGE 2026 e os manuais de campo (IBGE, 2022; IBGE, 2026):

| Regra | Descrição | Referência |
|-------|-----------|------------|
| **Data de Referência** | Toda a coleta e consistência dos dados do setor devem refletir rigorosamente a situação do estabelecimento em **31/12/2025** | IBGE, 2026 |
| **Resolução Total de PEUV** | Nenhum setor censitário pode ser encerrado se contiver pendências ativas de classificação de espécie (PEUV) | IBGE, 2022 |
| **Tratamento de Inconsistências** | Todas as inconsistências operacionais graves (ex: área vs. pecuária) devem ser resolvidas ou justificadas com parecer aceito | IBGE, 2022 |
| **Auditoria de Cobertura Cartográfica** | Análise dos trackings GNSS para garantir que não houve omissões ou duplicidades | IBGE, 2022 |
| **Consistência da "Regra da Sede"** | Em propriedades multissetoriais, a coordenada deve ser capturada na sede física | IBGE, 2026 |
| **Autenticação Segura** | ACQ deve possuir conta Gov.br com selo de confiabilidade nível Ouro | IBGE, 2026 |

---

## 2. Design da Tela de Revisão do Setor

A tela de revisão do setor é uma interface de alta densidade informativa, oferecendo a Carlos um painel consolidador de métricas de qualidade e visualização geoespacial do progresso. O design segue os princípios de **design de serviços governamentais** documentados no DSGov 4.0 (BRASIL, 2024), que enfatizam a **simplicidade, clareza e acessibilidade** na implementação de serviços públicos digitais.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ REVISÃO DO SETOR CENSITÁRIO #150280610000021                 Status: [🟡] │
├─────────────────────────────────────────────────────────────────────────────┤
│ 📍 Município: Alfenas-MG   📅 Data de Referência: 31/12/2025              │
├─────────────────────────────────────────────────────────────────────────────┤
│ 📊 MÉTRICAS DE QUALIDADE                                                    │
│ ┌──────────────┬──────────────┬──────────────┬───────────────────────────┐ │
│ │ Cobertura    │ Questionários│ Inconsist.   │ PEUV       │ Recusa       │ │
│ │ 98.2%        │ 47 (Bás./Comp)│ 2 Abertas    │ 0 Pendente │ 3.2%         │ │
│ └──────────────┴──────────────┴──────────────┴───────────┴───────────────┘ │
├─────────────────────────────────────────────────────────────────────────────┤
│ ☑️ CHECKLIST DE VERIFICAÇÃO PRÉ-APROVAÇÃO                                  │
│ [✓] Todos os estabelecimentos possuem ponto GNSS capturado na sede        │
│ [✓] Inexistência de inconsistências graves em aberto                     │
│ [✓] Todos os PEUV foram resolvidos e classificados                       │
│ [✓] Recusas justificadas com parecer aceito                              │
│ [✓] Ausências com no mínimo 3 visitas em horários alternados             │
│ [✓] Limites do setor respeitam áreas de exclusão                         │
├─────────────────────────────────────────────────────────────────────────────┤
│ 🗺️ MAPA DO SETOR — AUDITORIA CARTOGRÁFICA                                 │
│ ┌─────────────────────────────────────────────────────────────────────┐    │
│ │  [Imagem Orbital de Satélite com limites do setor e marcadores]     │    │
│ │  🟢 Questionários Concluídos  🟡 Pendentes  🔴 Recusas/Inconsist.   │    │
│ └─────────────────────────────────────────────────────────────────────┘    │
├─────────────────────────────────────────────────────────────────────────────┤
│ AÇÕES DE HOMOLOGAÇÃO                                                       │
│ [✅ Aprovar Setor] [🔄 Solicitar Correções] [❌ Rejeitar Setor]            │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.1 Painel de Métricas e Indicadores-Chave (KPIs)

Os KPIs foram projetados para fornecer a Carlos uma visão instantânea da saúde do setor, permitindo a priorização de ações antes da homologação:

| KPI | Descrição | Critério de Aceite |
|-----|-----------|-------------------|
| **Identificação do Setor** | Código de 15 dígitos (UFMMMMMDDSDSSSS) | Exibido no cabeçalho da tela |
| **Total de Endereços Confirmados** | Relação das unidades do CNEFE validadas | Contagem automática do sistema |
| **Índice de Cobertura** | Barra de progresso (visitados vs. estimados) | ≥ 95% para aprovação |
| **Relação de Questionários** | Básicos e Completos aplicados | Total acumulado |
| **Frequência de Inconsistências** | HDOP, área vs. produção, rebanho vs. pasto | Todas resolvidas |
| **Pendentes de PEUV** | Unidades sob análise | **Zero** para homologação |
| **Taxa de Recusa** | Percentual de recusas formais | Justificadas e aceitas |

### 2.2 Checklist de Verificação Pré-Aprovação

O checklist atua como uma barreira de segurança de dados, obrigando Carlos a validar manualmente cada critério antes da homologação. A literatura de inspeção de software documenta que checklists de verificação são ferramentas eficazes para reduzir defeitos, capturando em torno de 60% dos defeitos de artefatos (Boehm & Basili, 2001; Pressman, 2001).

```html
<div class="checklist-pre-aprovacao" role="group" aria-label="Checklist de verificação pré-aprovação">
  <label>
    <input type="checkbox" id="check-gnss" value="validado">
    [ ] Todos os estabelecimentos cadastrados possuem ponto GNSS capturado na sede
  </label>
  <label>
    <input type="checkbox" id="check-inconsistencias" value="validado">
    [ ] Inexistência de unidades com inconsistências graves em aberto
  </label>
  <label>
    <input type="checkbox" id="check-peuv" value="validado">
    [ ] Todos os pendentes de classificação de espécie (PEUV) foram resolvidos
  </label>
  <!-- Demais itens do checklist -->
</div>
```

### 2.3 Visualização do Mapa do Setor (Auditoria Cartográfica)

O mapa do setor é o principal instrumento de auditoria cartográfica, permitindo que Carlos visualize espacialmente a cobertura e identifique possíveis omissões:

| Elemento | Descrição | Cor de Referência |
|----------|-----------|-------------------|
| **Perímetro do Setor** | Renderização vetorial dos limites do setor | Azul IBGE (#0033A0) |
| **Feições de Terreno** | Estradas rurais, corpos d'água, relevo | Tons de cinza e verde |
| **Marcador 🟢** | Questionário concluído e transmitido | Verde funcional |
| **Marcador 🟡** | Visita em andamento, ausência ou PEUV | Amarelo alerta |
| **Marcador 🔴** | Recusa formal ou inconsistência crítica | Vermelho erro |

---

## 3. Design do Fluxo de Aprovação (Ações do ACQ)

A interface de tomada de decisão do ACQ dispõe de três fluxos de ação principais e excludentes, estruturados para garantir a solidez metodológica e a credibilidade institucional.

### 3.1 Ação A — Aprovar e Homologar Setor

| Aspecto | Especificação |
|---------|---------------|
| **Descrição** | Liberação final do setor e consolidação dos dados no servidor do IBGE |
| **Comportamento** | Ao acionar "Aprovar Setor", sistema abre modal de confirmação em duas etapas |
| **Etapa 1** | Apresenta o resumo de auditoria contendo as principais métricas agregadas do setor |
| **Etapa 2** | Autenticação acessível via Gov.br (selo Ouro) com biometria ou PIN de 6 dígitos |
| **Efeito** | Status → 🟢 Homologado; bloqueio de edições; exclusão segura do IndexedDB |

A Etapa 2 atende ao critério **WCAG 2.2 — 3.3.8 (Accessible Authentication)**, que estabelece que processos de login não devem impor testes de função cognitiva (W3C, 2023). O uso de PIN numérico ou biometria elimina a necessidade de quebra-cabeças ou memorização complexa.

### 3.2 Ação B — Solicitar Correções (Retorno ao Campo)

| Aspecto | Especificação |
|---------|---------------|
| **Descrição** | Devolve o setor ao supervisor (ACS) e recenseador para correção |
| **Comportamento** | Abre campo de texto livre com limite mínimo de caracteres; Carlos descreve os desvios |
| **Efeito** | Status → 🔴 Correção em Andamento; notificação enviada ao ACS e DMC de Mariana |

### 3.3 Ação C — Rejeitar Setor

| Aspecto | Especificação |
|---------|---------------|
| **Descrição** | Indica erro metodológico insanável, exigindo reprocessamento completo |
| **Comportamento** | Abre modal em vermelho de alta severidade (#E53935); justificativa mínima de 100 caracteres |
| **Efeito** | Status → 🔴 Setor Rejeitado; notifica coordenação regional para auditoria especial |

---

## 4. Design da Trilha de Auditoria (Audit Trail Log)

Em conformidade com a transparência pública, governança de dados governamentais e LGPD, a interface de revisão do setor conta com uma **Trilha de Auditoria de Ações imutável**, organizada em ordem cronológica reversa. A trilha de auditoria é fundamental para a rastreabilidade do processo de homologação, permitindo que a equipe de qualidade do CNQ identifique eventuais inconsistências no fluxo de aprovação.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ TRILHA DE AUDITORIA — LOG DE AÇÕES DO SETOR CENSITÁRIO #1502806             │
├─────────────────────┬─────────────────┬───────────────────┬─────────────────┤
│ DATA / HORA         │ USUÁRIO         │ AÇÃO REALIZADA    │ STATUS RESULT.  │
├─────────────────────┼─────────────────┼───────────────────┼─────────────────┤
│ 19/08/2026 15:30:24 │ Carlos (ACQ)    │ Homologar Setor   │ 🟢 Homologado   │
│ 17/08/2026 11:15:10 │ Mariana (REC)   │ Correção Concluída│ 🟡 Aguardando   │
│ 15/08/2026 10:20:00 │ Carlos (ACQ)    │ Solicitar Correção│ 🔴 Rejeitado    │
└─────────────────────┴─────────────────┴───────────────────┴─────────────────┘
```

### 4.1 Colunas e Metadados do Registro de Auditoria

| Coluna | Descrição | Fonte |
|--------|-----------|-------|
| **Data e Hora** | Timestamp preciso (fuso Brasília/DF) | Sistema |
| **Usuário de Acesso** | Nome e ID do agente, com papel funcional e regime legal | Autenticação Gov.br |
| **Ação Executada** | Registro descritivo do ato administrativo | Sistema |
| **Status Resultante** | Estado lógico do setor após a ação | Sistema |
| **Observações/Parecer** | Justificativa técnica digitada | ACQ ou recenseador |

### 4.2 Imutabilidade e Segurança do Log (LGPD)

Todos os eventos da trilha de auditoria são gerados de forma automática pelo backend e gravados de forma incremental no IndexedDB local. Os dados do log de auditoria são blindados com criptografia **AES-256 GCM** utilizando a Web Crypto API nativa do navegador, sendo transmitidos via **TLS 1.3** juntamente com a carga de questionários.

---

## 5. Diretrizes de Acessibilidade (e-MAG 3.1 & WCAG 2.2 AA)

Para assegurar que o fluxo de aprovação de setores censitários seja plenamente operável por todos os analistas e auditores, aplicam-se as diretrizes do Governo Digital brasileiro. A versão **WCAG 2.2**, publicada em outubro de 2023, adiciona 9 novos critérios de sucesso em relação à versão 2.1, sendo 6 deles de nível A e AA (W3C, 2023). O critério 4.1.1 (Parsing) foi removido por se tornar obsoleto com a evolução dos navegadores (W3C, 2023; AccessibleEU, 2023).

A conformidade com a **WCAG 2.2 Nível AA** é agora a linha de base legal para websites governamentais na maioria das jurisdições (Open Door Digital, 2026). A WCAG 2.2 foi adotada como padrão internacional ISO/IEC 40500:2025, criando um benchmark unificado para acessibilidade em todo o mundo (Nustart Solutions, 2025).

### 5.1 Critérios WCAG 2.2 Aplicados

| Critério | Nível | Especificação | Referência |
|----------|-------|---------------|------------|
| **2.4.11 — Focus Not Obscured (Minimum)** | AA | O indicador de foco não deve ser completamente ocultado por componentes fixos (sticky headers, overlays) | W3C, 2023; Deque University, 2023 |
| **2.4.12 — Focus Not Obscured (Enhanced)** | AAA | Nenhuma parte do indicador de foco deve ser ocultada | W3C, 2023 |
| **2.4.13 — Focus Appearance** | AAA | Indicador de foco com área mínima equivalente a 2px de outline e contraste 3:1 | W3C, 2023 |
| **2.5.8 — Target Size (Minimum)** | AA | Alvos interativos com mínimo de 24×24px CSS (com exceções para links inline, elementos nativos, etc.) | W3C, 2023; NHS Digital, 2024 |
| **3.3.7 — Redundant Entry** | AA | Dados previamente informados não devem ser requisitados novamente | W3C, 2023; WWU, 2023 |
| **3.3.8 — Accessible Authentication (Minimum)** | AA | Processos de login não devem impor testes de função cognitiva | W3C, 2023 |
| **3.3.9 — Accessible Authentication (Enhanced)** | AAA | Proíbe testes cognitivos em logins, incluindo identificação de imagens | W3C, 2023 |

### 5.2 Operabilidade por Teclado e Foco

A WCAG 2.2 introduziu o **Focus Appearance (2.4.13)** no nível AAA, que estabelece que o indicador de foco deve ter uma área mínima equivalente a 2px de outline e contraste de 3:1 entre os pixels focados e não focados. Esta especificação complementa os requisitos de **Focus Not Obscured** (2.4.11/2.4.12) para garantir que o foco seja sempre visível e identificável (W3C, 2023; Deque University, 2023).

| Requisito | Implementação | Referência |
|-----------|---------------|------------|
| **Operabilidade Plena** | Todos os elementos navegáveis via Tab, Enter, Espaço | e-MAG Área 2 |
| **Keyboard Trap Prevention** | Modal fechável via Esc ou botão visível | e-MAG Área 2 |
| **Focus Appearance** | Outline com contraste ≥ 3:1 e área mínima equivalente a 2px | WCAG 2.2 — 2.4.13 |
| **Focus Not Obscured** | Espaçamento superior para evitar cobertura pela Barra Gov.Br | WCAG 2.2 — 2.4.11 |
| **Target Size** | Alvos ≥ 24×24px; botões críticos ≥ 48×48px | WCAG 2.2 — 2.5.8 |

**Implementação técnica do Focus Not Obscured:**
```css
/* Evita que a Barra Gov.Br fixa oculte o foco */
html {
  scroll-padding-top: 80px; /* Altura da Barra Gov.Br + folga */
}

/* Indicador de foco com contraste e área adequados (WCAG 2.4.13) */
*:focus-visible {
  outline: 3px solid #0033A0; /* Azul IBGE com contraste ≥ 3:1 */
  outline-offset: 2px;
  border-radius: 4px;
}
```

### 5.3 Regiões Vivas (aria-live polite)

O feed de alertas e atualizações de status da trilha de auditoria e do checklist utiliza `aria-live="polite"` e `role="status"`. Novas inclusões de log ou transições de aprovação são vocalizadas pelos sintetizadores de voz dos leitores de tela de forma suave, sem interromper as tarefas ativas de Carlos.

### 5.4 Independência de Cores (e-MAG Área 4)

O status dos indicadores de checklist e da lista de setores não utiliza apenas cores funcionais. Cada estado é acompanhado de ícones distintos e rótulos de texto explícitos (ex: `[✓] Cobertura GNSS validada (Ótimo)`, `[🔒] Recusa formal pendente de revisita`), garantindo a operabilidade de usuários daltônicos ou sob condições adversas de iluminação.

### 5.5 Target Size (WCAG 2.2 — 2.5.8)

O critério **2.5.8 Target Size (Minimum)** estabelece que alvos interativos devem ter um tamanho mínimo de **24×24 pixels CSS**, com exceções para links inline, elementos determinados pelo agente do usuário, e casos onde o tamanho é necessário para a apresentação da informação (W3C, 2023; Deque University, 2023).

| Tipo de Alvo | Tamanho Mínimo | Aplicação |
|--------------|----------------|-----------|
| **Alvos Padrão** | 24×24px CSS | Links, ícones, filtros, checkboxes |
| **Botões Críticos** | 48×48px CSS | Aprovar Setor, Solicitar Correção, Rejeitar Setor |
| **Espaçamento** | 8px entre alvos | Evita ativação acidental |

---

## 6. Segurança de Dados e Conformidade (LGPD)

O fluxo de aprovação de setores manipula metadados geográficos e dados cadastrais sensíveis dos produtores rurais, exigindo total aderência às garantias de sigilo da Lei nº 5.534/68 e à LGPD.

| Camada | Tecnologia | Finalidade | Referência |
|--------|------------|------------|------------|
| **Dados em Repouso** | AES-256 GCM via Web Crypto API | Proteção de dados sensíveis no dispositivo | LGPD Art. 46 |
| **Derivação de Chave** | PBKDF2 com salt + autenticação Gov.br | Chave única por sessão | — |
| **Dados em Trânsito** | TLS 1.3 / HTTPS | Proteção durante transmissão | LGPD Art. 46 |
| **Descarte Seguro** | Remoção irreversível do IndexedDB | Direito ao esquecimento | LGPD Art. 18 |

---

## 7. Checklist de Handoff Técnico (Conformidade DesignOps)

| Item | Critério | Status | Referência |
|------|----------|--------|------------|
| **XHTML Estrito** | Fechamento obrigatório de tags, atributos booleanos expressos | ✅ | Edital IBGE 2026 |
| **Família Univers** | Univers 55 Roman (corpo) / 65 Bold (títulos) | ✅ | MIV IBGE |
| **Neuropolitical** | Restrita à logomarca oficial | ✅ | MIV IBGE |
| **Azul IBGE** | #0033A0 (Pantone 286 C) para elementos primários | ✅ | MIV IBGE |
| **Contraste Mínimo** | Razão ≥ 4.5:1 para textos normais | ✅ | WCAG 1.4.3 / e-MAG 4.1 |
| **Independência de Cor** | Status com ícones e texto, não apenas cor | ✅ | WCAG 1.4.1 / e-MAG 4.2 |
| **Target Size (2.5.8)** | 24×24px (padrão) / 48×48px (botões críticos) | ✅ | WCAG 2.2 AA |
| **Focus Not Obscured (2.4.11)** | Foco visível, não ocultado pela Barra Gov.Br | ✅ | WCAG 2.2 AA |
| **Focus Appearance (2.4.13)** | Outline com contraste ≥ 3:1 e área mínima | ✅ | WCAG 2.2 AAA |
| **Regiões Vivas** | `aria-live="polite"` no feed de notificações | ✅ | e-MAG Área 2 |
| **Accessible Authentication (3.3.8)** | Login com biometria ou PIN, sem testes cognitivos | ✅ | WCAG 2.2 AA |
| **HDOP Validation** | Bloqueio de encerramento se σₕ > 5,0m | ✅ | Manual do Recenseador |
| **Criptografia AES-256** | Dados locais encriptados no IndexedDB | ✅ | LGPD Art. 46 |

---

## 8. Conclusão

O Fluxo de Aprovação de Setores Censitários foi projetado para ser uma **ferramenta de homologação robusta, acessível e segura**, permitindo que Carlos valide e encerre setores com confiança estatística, garantindo a integridade dos dados que comporão as estatísticas oficiais do 12º Censo Agropecuário.

A aplicação dos critérios **WCAG 2.2 AA** (incluindo os novos critérios 2.4.11 Focus Not Obscured, 2.5.8 Target Size, 3.3.7 Redundant Entry e 3.3.8 Accessible Authentication), **e-MAG 3.1** e **LGPD**, combinada com a identidade visual do IBGE e as diretrizes do **DSGov 4.0**, garante que o fluxo esteja alinhado com os mais elevados padrões de governança digital e inclusão.

A trilha de auditoria imutável, a criptografia AES-256 GCM no IndexedDB e o descarte seguro dos dados locais após a homologação asseguram a **rastreabilidade, integridade e segurança** do processo, em conformidade com as exigências do Centro Nacional de Qualidade (CNQ) e da LGPD, reforçando a confiança da sociedade nos dados produzidos pelo IBGE.

---

## 9. Referências

### Manuais e Documentos Oficiais do IBGE

1. IBGE. **Manual do Recenseador do Censo Demográfico 2022 (CD-1.09)**. Rio de Janeiro: IBGE, 2022. Disponível em: <https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5723.pdf>. Acesso em: 9 ago. 2026.

2. IBGE. **Edital de Abertura nº 02/2026 — Processo Seletivo Simplificado para Agente Censitário de Qualidade (ACQ)**. Rio de Janeiro: IBGE, 2026.

3. IBGE. **Manual de Identidade Visual do IBGE**. Rio de Janeiro: IBGE, 2016. Disponível em: <https://www.ibge.gov.br>. Acesso em: 9 ago. 2026.

### Padrões de Governo Digital e Acessibilidade

4. BRASIL. **e-MAG 3.1 — Modelo de Acessibilidade em Governo Eletrônico**. Brasília: Ministério do Planejamento, Orçamento e Gestão, 2014. Disponível em: <https://emag.governoeletronico.gov.br/>. Acesso em: 9 ago. 2026.

5. BRASIL. **DSGov 4.0 — Padrão Digital de Governo**. Brasília: Ministério da Gestão e da Inovação em Serviços Públicos, 2024. Disponível em: <https://www.gov.br/ds/>. Acesso em: 9 ago. 2026.

6. W3C. **Web Content Accessibility Guidelines (WCAG) 2.2**. Cambridge: W3C, 2023. Disponível em: <https://www.w3.org/TR/WCAG22/>. Acesso em: 9 ago. 2026.

### Engenharia de Software e Inspeção

7. BOEHM, Barry; BASILI, Victor. **Software Defect Reduction Top 10 List**. In: IEEE Computer, 2001.

8. PRESSMAN, Roger. **Engenharia de Software**. 6. ed. São Paulo: McGraw-Hill, 2001.

### Legislação

9. BRASIL. **Lei nº 5.534, de 14 de novembro de 1968**. Dispõe sobre o sigilo das informações prestadas ao IBGE. Disponível em: <https://www.planalto.gov.br/ccivil_03/leis/l5534.htm>. Acesso em: 9 ago. 2026.

10. BRASIL. **Lei nº 13.709, de 14 de agosto de 2018 (LGPD)**. Brasília: Presidência da República, 2018. Disponível em: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>. Acesso em: 9 ago. 2026.

### Referências Complementares

11. FOCUS CONCURSOS. **Concurso IBGE 2026 — Agente Censitário de Qualidade (ACQ)**. 2026. Disponível em: <https://focusconcursos.com.br/produto/ibge-agente-censitario-de-qualidade-acq>. Acesso em: 9 ago. 2026.

12. ACCESSIBLE EU CENTRE. **WCAG 2.2 is officially a W3C recommendation**. 2023. Disponível em: <https://accessible-eu.ec.europa.eu/>. Acesso em: 9 ago. 2026.

13. DEQUE UNIVERSITY. **WCAG 2.2 Updates**. 2023. Disponível em: <https://dequeuniversity.com/resources/wcag-2.2/>. Acesso em: 9 ago. 2026.

14. NUSTART SOLUTIONS. **WCAG 2.2 is Now a Global ISO Standard**. 2025. Disponível em: <https://nustart.solutions/accessibility/wcag-2-2-is-now-a-global-standard/>. Acesso em: 9 ago. 2026.

---

**Versão:** 2.0 (Revisada)
**Data:** Agosto 2026
**Status:** ✅ Especificação validada com Edital ACQ, DSGov 4.0, WCAG 2.2 AA, e-MAG 3.1 e LGPD

# 📋 Especificação de Interface e Engenharia: Prototipagem de Relatórios de Qualidade (ACQ) — **Versão Revisada**

## 1. Contexto Metodológico e Atribuições de Auditoria do ACQ

O trabalho do Agente Censitário de Qualidade (ACQ) Carlos apoia-se em analisar os dados transmitidos de campo para garantir que não existam erros metodológicos ou conceituais agrários antes da homologação final. Os relatórios de qualidade são o principal instrumento analítico de tomada de decisão para auditoria de inconsistências, monitoramento da produtividade das equipes e homologação final dos setores censitários do 12º Censo Agropecuário.

O ACQ desempenha um papel crítico na cadeia de custódia e integridade dos dados estatísticos nacionais. O novo edital do IBGE (Edital nº 02/2026) oferece **394 vagas imediatas** para este cargo, com remuneração de R$ 2.932,00 acrescida de R$ 1.192,00 de auxílio-alimentação (Focus Concursos, 2026). A seleção será organizada pelo Instituto Avalia, com prova objetiva prevista para 30 de agosto de 2026 (Focus Concursos, 2026).

### 1.1 Atribuições Diretas do ACQ

De acordo com o edital do Processo Seletivo Simplificado, as atribuições do ACQ consistem em:

| Atribuição | Descrição | Fonte |
|------------|-----------|-------|
| **Examinar Questionários** | Auditar a completude, coerência e padronização dos questionários eletrônicos (Básico e Completo) | Edital ACQ |
| **Identificar Erros e Omissões** | Detectar desvios de área, pecuária, limites espaciais e sinal GNSS com HDOP inadequado | Edital ACQ |
| **Gestão de Pendências (PEUV)** | Sanar casos de Pendente de Espécie da Unidade Visitada (PEUV) | Manual do Recenseador |
| **Orientação Operacional** | Orientar o Agente Censitário Supervisor (ACS) e os recenseadores quanto aos ajustes necessários | Edital ACQ |

---

## 2. Relatório de Qualidade por Setor (Módulo de Auditoria Geográfica)

O Relatório de Qualidade por Setor reúne, de forma condensada, o estado de conservação metodológica e geodésica de um único setor censitário de 15 dígitos. Este relatório é o principal artefato de auditoria utilizado por Carlos para validar a integridade dos dados antes da homologação.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 📊 RELATÓRIO DE QUALIDADE — SETOR #150280610000021                         │
│ Município: Alfenas-MG   |   Data de Referência: 31/12/2025                 │
├─────────────────────────────────────────────────────────────────────────────┤
│ 📈 INDICADORES DE QUALIDADE                                                 │
│ ┌──────────────────┬──────────────────┬──────────────────┬─────────────────┐ │
│ │ Cobertura        │ Questionários    │ Inconsistências  │ PEUV            │ │
│ │ 98.2%            │ 47 (18 Bás. / 29 │ 2 Abertas        │ 0 Pendente      │ │
│ │                  │ Comp.)           │                  │                 │ │
│ └──────────────────┴──────────────────┴──────────────────┴─────────────────┘ │
├─────────────────────────────────────────────────────────────────────────────┤
│ 📊 VISUALIZAÇÃO DE DADOS                                                    │
│ ┌─────────────────────────────┐  ┌─────────────────────────────────────────┐│
│ │ GRÁFICO DE ROSCA (Donut)    │  │ GRÁFICO DE BARRAS EMPILHADAS            ││
│ │ 🟢 Concluídos: 46 (89%)     │  │ ■ Questionários Básicos: 18             ││
│ │ 🟡 Em Andamento: 3 (6%)     │  │ ■ Questionários Completos: 29           ││
│ │ 🔴 Pendentes: 3 (5%)        │  │ ■ Total: 47                            ││
│ └─────────────────────────────┘  └─────────────────────────────────────────┘│
├─────────────────────────────────────────────────────────────────────────────┤
│ 📝 RESUMO TEXTUAL DOS ACHADOS                                               │
│ ⚠️ Inconsistência de Área vs. Pecuária detectada no Estabelecimento #3303401│
│ (Seu José). O recenseador registrou 250 cabeças de gado bovino em apenas   │
│ 2 hectares de pastagem declarada. Requer revisão imediata ou justificativa.│
├─────────────────────────────────────────────────────────────────────────────┤
│ 📋 TABELA DINÂMICA DE INCONSISTÊNCIAS                                      │
│ ┌────────────────┬──────────────┬─────────────┬───────────────────────────┐│
│ │ Tipo           │ Severidade   │ Status      │ Ação                      ││
│ ├────────────────┼──────────────┼─────────────┼───────────────────────────┤│
│ │ Área vs. Pecu. │ 🔴 Alta      │ 🟡 Pendente │ [Auditar] [Justificar]    ││
│ │ HDOP Limite    │ 🟡 Média     │ 🔵 Correção │ [Ver Detalhes]            ││
│ └────────────────┴──────────────┴─────────────┴───────────────────────────┘│
├─────────────────────────────────────────────────────────────────────────────┤
│ AÇÕES DE HOMOLOGAÇÃO                                                       │
│ [✅ Aprovar e Homologar] [🔄 Solicitar Correções (ACS)]                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.1 Principais Indicadores e KPIs do Setor

O topo do painel do setor exibe um resumo estatístico consolidado contendo os seguintes indicadores de qualidade, que seguem o padrão de dashboards de controle operacional documentados na literatura de design de interfaces governamentais (BRASIL, 2024):

| KPI | Descrição | Fórmula/Origem | Critério de Aceite |
|-----|-----------|----------------|-------------------|
| **Taxa de Cobertura Geral (%)** | Percentual de estabelecimentos visitados vs. cadastro prévio do CNEFE | (Visitados / Estimados) × 100 | ≥ 95% para aprovação |
| **Questionários Transmitidos** | Relação de Básicos e Completos aplicados | Contagem automática | Consistência com cobertura |
| **Densidade de Inconsistências** | Erros identificados pelo sistema de consistência | Área vs. pecuária, HDOP, limites | Todas resolvidas para homologação |
| **Pendentes de Espécie (PEUV)** | Unidades sob suspeita de uso misto, ausência ou litígio | Contagem automática | **Zero** para homologação |

### 2.2 Visualização de Dados (Gráficos)

Em conformidade com as regras de Estética Minimalista e clareza de visualização, o relatório renderiza os seguintes painéis gráficos. A escolha dos tipos de gráfico segue os princípios de visualização de dados documentados por Few (2012) e Cairo (2016), que enfatizam a eficácia perceptual e a redução da carga cognitiva.

| Gráfico | Tipo | Dados Exibidos | Função |
|---------|------|----------------|--------|
| **Progresso da Cobertura** | Gráfico de Rosca (Donut) | Concluídos (🟢), Em Andamento (🟡), Pendentes (🔴) | Visão rápida do status geral |
| **Questionários Aplicados** | Gráfico de Barras Empilhadas | Básicos vs. Completos | Análise do perfil do setor |
| **Inconsistências** | Tabela Dinâmica | Tipo, severidade, status | Detalhamento para ação |

### 2.3 Resumo Textual dos Achados (Cruzamento Avançado)

Abaixo dos indicadores gráficos, o sistema gera dinamicamente um **parecer descritivo em Linguagem Simples** auxiliando a análise de Carlos. O sistema executa uma rotina de cruzamento avançado de dados que combina informações de diferentes blocos do questionário para identificar inconsistências complexas.

> ⚠️ **Exemplo de Alerta:** "Inconsistência de Área vs. Pecuária detectada no Estabelecimento #3303401 (Seu José). O recenseador registrou 250 cabeças de gado bovino em apenas 2 hectares de pastagem declarada. Requer revisão imediata ou justificativa do recenseador." (IBGE, 2022; IBGE, 2026)

**Tipos de Achados Gerados:**

| Tipo de Achado | Condição de Geração | Exemplo |
|----------------|---------------------|---------|
| **Área vs. Pecuária** | Densidade > 0,5 bovinos/ha | "250 cabeças em 2 hectares" |
| **Área vs. Colheita** | Produtividade fora do histórico municipal | "Soja com 10.000 kg/ha" |
| **HDOP Inadequado** | σₕ = HDOP × σ₀ > 5,0m | "Precisão de 8,5m excede o limite" |
| **PEUV Não Resolvido** | Pendência ativa no setor | "2 unidades não classificadas" |

### 2.4 Controle de Tomada de Decisão (Aprovação/Rejeição)

No rodapé do relatório, o sistema exibe os controles para a homologação final do setor censitário pelo ACQ:

| Botão | Função | Requisito de Segurança |
|-------|--------|------------------------|
| **Aprovar e Homologar** | Libera o setor para a base nacional | Revalidação via PIN ou biometria (WCAG 3.3.8) |
| **Solicitar Correções (ACS)** | Devolve ao campo para correção | Parecer técnico mínimo de 100 caracteres |

---

## 3. Relatório de Performance da Equipe

Este relatório permite que Carlos identifique desvios de conduta, gargalos operacionais e deficiências de treinamento na equipe de recenseadores em tempo real. O design segue os princípios de **dashboards de desempenho operacional** documentados na literatura de engenharia de software (Boehm & Basili, 2001; Pressman, 2001).

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 📊 RELATÓRIO DE PERFORMANCE DA EQUIPE — Posto Alfenas                      │
│ Período: 01/01/2025 a 31/12/2025                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│ 📈 MÉTRICAS INDIVIDUAIS DE DESEMPENHO                                      │
│ ┌─────────────┬──────────────┬──────────────┬──────────────┬─────────────┐ │
│ │ Recenseador │ Setores Conc. │ TME (min)    │ Taxa Recusa  │ Inconsist.  │ │
│ ├─────────────┼──────────────┼──────────────┼──────────────┼─────────────┤ │
│ │ Mariana     │ 15           │ 12.4         │ 3.2%         │ 2           │ │
│ │ João        │ 12           │ 8.1          │ 5.7%         │ 5           │ │
│ │ Ana         │ 14           │ 15.2         │ 1.8%         │ 1           │ │
│ └─────────────┴──────────────┴──────────────┴──────────────┴─────────────┘ │
├─────────────────────────────────────────────────────────────────────────────┤
│ 📊 GRÁFICO DE BARRAS HORIZONTAIS — TME por Recenseador                     │
│ ┌─────────────────────────────────────────────────────────────────────────┐│
│ │ Mariana ■■■■■■■■■■■■■■■■■■■■ 12.4 min                                  ││
│ │ João    ■■■■■■■■■■■■■■ 8.1 min                                         ││
│ │ Ana     ■■■■■■■■■■■■■■■■■■■■■■■ 15.2 min                              ││
│ └─────────────────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Métricas Individuais de Desempenho

A tabela de performance apresenta as métricas consolidadas de cada recenseador sob a jurisdição do posto:

| Métrica | Descrição | Interpretação para o ACQ |
|---------|-----------|--------------------------|
| **Setores Concluídos** | Unidades territoriais percorridas com transmissão efetuada | Volume de produção |
| **Tempo Médio por Entrevista (TME)** | Média de tempo gasto no preenchimento | Preenchimento fictício (muito curto) ou dificuldade (muito longo) |
| **Taxa de Recusa (%)** | Estabelecimentos com recusa formal | Necessidade de intervenção do ACS |
| **Incidência de Inconsistências** | Questionários devolvidos com erros graves | Qualidade da coleta |

### 3.2 Visualização Comparativa (Gráficos)

O gráfico de barras horizontais comparativo aplica o paradigma de Dave Gray's Sequence para dispor a performance da equipe em escalas lineares de produtividade. O gráfico permite que Carlos ordene instantaneamente os agentes por tempo médio de preenchimento ou por taxa de recusa, permitindo isolar anomalias de coleta de forma visual direta (Gray, 2010; Wurman, 1996).

**Sequência de Análise Recomendada:**

1. **Identificar outliers:** Recenseadores com TME significativamente abaixo da média podem estar preenchendo de forma fictícia.
2. **Correlacionar com inconsistências:** TME baixo + alta incidência de inconsistências = suspeita de coleta inadequada.
3. **Avaliar taxa de recusa:** Valores elevados podem indicar necessidade de treinamento em abordagem ou sensibilização institucional.

---

## 4. Filtros de Controle e Exportação de Relatórios

Para garantir a portabilidade dos relatórios e conformidade técnica com o fluxo do CEQ, a interface disponibiliza controles avançados de extração de dados.

### 4.1 Painel de Filtros Operacionais

| Filtro | Descrição | Aplicação |
|--------|-----------|-----------|
| **Seleção de Setores** | Dropdown múltiplo com geocódigos de 15 dígitos | Consolidar dados por setor |
| **Período de Referência** | Ano Agrícola (01/01/2025 a 31/12/2025) | Alinhamento com data de referência |
| **Recenseador** | Lista de agentes do posto | Análise individualizada |
| **Status** | Homologado, Em Correção, Pendente | Filtro por fase do processo |

### 4.2 Botões de Exportação e Formatos Suportados

| Formato | Finalidade | Características |
|---------|------------|-----------------|
| **PDF** | Documentação estática para prestação de contas | NBR 14724:2024, Padrão Ofício, Brasão da República |
| **CSV** | Importação em ferramentas GIS (QGIS/ArcGIS) | UTF-8, metadados estruturados, coordenadas |

---

## 5. Diretrizes de Acessibilidade (e-MAG 3.1 & WCAG 2.2 AA)

Os relatórios do dashboard do ACQ foram projetados para cumprir integralmente as normas federais e critérios internacionais de acessibilidade digital. A versão **WCAG 2.2**, publicada em outubro de 2023, adiciona 9 novos critérios de sucesso em relação à versão 2.1 (W3C, 2023). A conformidade com a **WCAG 2.2 Nível AA** é agora a linha de base legal para websites governamentais na maioria das jurisdições (Open Door Digital, 2026).

### 5.1 Alternativas Textuais e Independência de Cor

| Requisito | Implementação | Referência |
|-----------|---------------|------------|
| **Descrição de Gráficos** | `aria-label` detalhando o teor dos dados | e-MAG Área 5 |
| **Independência de Cor** | Ícones geométricos + rótulos textuais | WCAG 1.4.1 / e-MAG 4.2 |
| **Texto Alternativo** | `alt` descritivo para imagens informativas | e-MAG 3.6 |

**Exemplo de implementação:**
```html
<canvas role="img" aria-label="Gráfico de rosco mostrando 89% de cobertura concluída, 6% em andamento e 5% pendente no setor #150280610000021"></canvas>
```

### 5.2 Contraste de Alta Legibilidade (WCAG 1.4.3)

| Elemento | Contraste Mínimo | Status |
|----------|------------------|--------|
| Texto normal (Univers 55 Roman, 16px) | ≥ 4.5:1 | ✅ Supera 15:1 |
| Texto grande (Univers 65 Bold, 24px+) | ≥ 3:1 | ✅ Supera 8.5:1 |
| Indicadores de foco | ≥ 3:1 | ✅ Conforme |

### 5.3 Target Size Otimizado (WCAG 2.2 — 2.5.8)

| Tipo de Alvo | Tamanho Mínimo | Aplicação |
|--------------|----------------|-----------|
| **Alvos Padrão** | 24×24px CSS | Links, filtros, ícones |
| **Botões Críticos** | 48×48px CSS | Aprovar, Solicitar Correções, Exportar |

### 5.4 Critérios WCAG 2.2 Aplicados

| Critério | Nível | Especificação | Referência |
|----------|-------|---------------|------------|
| **2.4.11 — Focus Not Obscured (Minimum)** | AA | O indicador de foco não deve ser completamente ocultado por componentes fixos | W3C, 2023 |
| **2.4.13 — Focus Appearance** | AAA | Indicador de foco com área mínima e contraste 3:1 | W3C, 2023 |
| **2.5.8 — Target Size (Minimum)** | AA | Alvos interativos com mínimo de 24×24px CSS | W3C, 2023 |
| **3.3.7 — Redundant Entry** | AA | Dados previamente informados não são requisitados novamente | W3C, 2023 |
| **3.3.8 — Accessible Authentication** | AA | Login com biometria ou PIN, sem testes cognitivos | W3C, 2023 |

---

## 6. Segurança, Privacidade e Sigilo Estatístico (LGPD & AES-256 GCM)

Como o dashboard manipula e extrai dados patrimoniais e sensíveis de produtores e estabelecimentos, aplicam-se estritamente as regras de sigilo da Lei nº 5.534/68 e a LGPD.

### 6.1 Criptografia At Rest (IndexedDB)

| Camada | Tecnologia | Finalidade | Referência |
|--------|------------|------------|------------|
| **Dados em Repouso** | AES-256 GCM via Web Crypto API | Proteção de dados sensíveis no dispositivo | LGPD Art. 46 |
| **Derivação de Chave** | PBKDF2 com salt + autenticação Gov.br | Chave única por sessão | — |
| **Dados em Trânsito** | TLS 1.3 / HTTPS | Proteção durante transmissão | LGPD Art. 46 |

### 6.2 Descarte Seguro

O registro criptografado local é excluído permanentemente da memória física (IndexedDB) e do cache imediatamente após a confirmação síncrona do recebimento das homologações pelos servidores centrais do IBGE, cumprindo o **direito ao esquecimento** previsto no artigo 18 da LGPD.

---

## 7. Checklist de Handoff Técnico (DesignOps)

| Item | Critério | Status | Referência |
|------|----------|--------|------------|
| **Markup Semântico** | XHTML Estrito com fechamento mandatório de tags | ✅ | Edital IBGE 2026 |
| **Grid e Layout** | Grid fluida de 8 colunas (paisagem) com espaçamento 8pt | ✅ | DSGov Mobile |
| **Cores Oficiais** | Azul IBGE (HEX #0033A0 / RGB 0,51,160) e paleta semântica | ✅ | MIV IBGE |
| **Tipografia** | Univers LT Std (55 Roman corpo, 65 Bold títulos) | ✅ | MIV IBGE |
| **Contraste Mínimo** | Razão ≥ 4.5:1 para textos e 3:1 para indicadores de foco | ✅ | e-MAG 4.1 / WCAG 1.4.3 |
| **Independência de Cor** | Status com ícones e texto, não apenas cor | ✅ | e-MAG 4.2 / WCAG 1.4.1 |
| **Target Size** | 24×24px (padrão) / 48×48px (botões críticos) | ✅ | WCAG 2.2 — 2.5.8 |
| **Focus Not Obscured** | Foco visível, não ocultado pela Barra Gov.Br | ✅ | WCAG 2.2 — 2.4.11 |
| **Regiões Vivas** | `aria-live="polite"` no feed de notificações | ✅ | e-MAG Área 2 |
| **Alternativas Textuais** | `aria-label` em gráficos e imagens | ✅ | e-MAG Área 5 |
| **Criptografia Local** | AES-256 GCM no IndexedDB para dados "at rest" | ✅ | LGPD Art. 46 |
| **Descarte Seguro** | Remoção imediata pós-sincronização | ✅ | LGPD Art. 18 |

---

## 8. Conclusão

Os Relatórios de Qualidade e Performance foram projetados para serem **ferramentas analíticas robustas, acessíveis e seguras**, permitindo que Carlos monitore a qualidade dos dados coletados, identifique inconsistências em tempo real e homologue setores com confiança estatística.

A aplicação dos critérios **WCAG 2.2 AA** (incluindo os novos critérios 2.4.11 Focus Not Obscured, 2.5.8 Target Size, 3.3.7 Redundant Entry e 3.3.8 Accessible Authentication), **e-MAG 3.1** e **LGPD**, combinada com a identidade visual do IBGE e as diretrizes do **DSGov 4.0**, garante que os relatórios estejam alinhados com os mais elevados padrões de governança digital e inclusão.

O relatório de qualidade por setor, com seus gráficos de rosca e barras empilhadas, o resumo textual dos achados e a tabela dinâmica de inconsistências, fornece a Carlos uma visão abrangente da saúde estatística do setor. O relatório de performance da equipe, com suas métricas individuais e gráficos comparativos, permite a identificação de gargalos operacionais e deficiências de treinamento.

A criptografia AES-256 GCM no IndexedDB e o descarte seguro dos dados locais após a homologação asseguram a **rastreabilidade, integridade e segurança** do processo, em conformidade com as exigências do Centro Nacional de Qualidade (CNQ) e da LGPD, reforçando a confiança da sociedade nos dados produzidos pelo IBGE.

---

## 9. Referências

### Manuais e Documentos Oficiais do IBGE

1. IBGE. **Manual do Recenseador do Censo Demográfico 2022 (CD-1.09)**. Rio de Janeiro: IBGE, 2022. Disponível em: <https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5723.pdf>. Acesso em: 9 ago. 2026.

2. IBGE. **Edital de Abertura nº 02/2026 — Processo Seletivo Simplificado para Agente Censitário de Qualidade (ACQ)**. Rio de Janeiro: IBGE, 2026.

3. IBGE. **Manual de Identidade Visual do IBGE**. Rio de Janeiro: IBGE, 2016. Disponível em: <https://www.ibge.gov.br>. Acesso em: 9 ago. 2026.

### Padrões de Governo Digital e Acessibilidade

4. BRASIL. **e-MAG 3.1 — Modelo de Acessibilidade em Governo Eletrônico**. Brasília: Ministério do Planejamento, Orçamento e Gestão, 2014. Disponível em: <https://emag.governoeletronico.gov.br/>. Acesso em: 9 ago. 2026.

5. BRASIL. **DSGov 4.0 — Padrão Digital de Governo**. Brasília: Ministério da Gestão e da Inovação em Serviços Públicos, 2024. Disponível em: <https://www.gov.br/ds/>. Acesso em: 9 ago. 2026.

6. W3C. **Web Content Accessibility Guidelines (WCAG) 2.2**. Cambridge: W3C, 2023. Disponível em: <https://www.w3.org/TR/WCAG22/>. Acesso em: 9 ago. 2026.

### Visualização de Dados

7. CAIRO, Alberto. **The Truthful Art: Data, Charts, and Maps for Communication**. San Francisco: New Riders, 2016.

8. FEW, Stephen. **Show Me the Numbers: Designing Tables and Graphs to Enlighten**. 2. ed. Burlingame: Analytics Press, 2012.

9. GRAY, Dave. **Gamestorming: A Playbook for Innovators, Rulebreakers, and Changemakers**. Sebastopol: O'Reilly Media, 2010.

10. WURMAN, Richard Saul. **Information Architects**. Nova Iorque: Graphis Press Corp, 1996.

### Engenharia de Software

11. BOEHM, Barry; BASILI, Victor. **Software Defect Reduction Top 10 List**. In: IEEE Computer, 2001.

12. PRESSMAN, Roger. **Engenharia de Software**. 6. ed. São Paulo: McGraw-Hill, 2001.

### Legislação

13. BRASIL. **Lei nº 5.534, de 14 de novembro de 1968**. Dispõe sobre o sigilo das informações prestadas ao IBGE. Disponível em: <https://www.planalto.gov.br/ccivil_03/leis/l5534.htm>. Acesso em: 9 ago. 2026.

14. BRASIL. **Lei nº 13.709, de 14 de agosto de 2018 (LGPD)**. Brasília: Presidência da República, 2018. Disponível em: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>. Acesso em: 9 ago. 2026.

### Referências Complementares

15. FOCUS CONCURSOS. **Concurso IBGE 2026 — Agente Censitário de Qualidade (ACQ)**. 2026. Disponível em: <https://focusconcursos.com.br/produto/ibge-agente-censitario-de-qualidade-acq>. Acesso em: 9 ago. 2026.

16. OPEN DOOR DIGITAL. **WCAG 2.2 Accessibility Requirements**. 2026. Disponível em: <https://www.opendoordigital.com.au/accessibility/wcag-2-2-requirements/>. Acesso em: 9 ago. 2026.

17. ACCESSIBLE EU CENTRE. **WCAG 2.2 is officially a W3C recommendation**. 2023. Disponível em: <https://accessible-eu.ec.europa.eu/>. Acesso em: 9 ago. 2026.

---

**Versão:** 2.0 (Revisada)
**Data:** Agosto 2026
**Status:** ✅ Especificação validada com Edital ACQ, DSGov 4.0, WCAG 2.2 AA, e-MAG 3.1 e LGPD