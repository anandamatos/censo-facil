# 🗂️ Card da Persona: Carlos

**Nome Completo:** Carlos Eduardo Mendes  
**Idade:** 45 anos  
**Ocupação:** Agente Censitário de Qualidade (ACQ) — Servidor Efetivo (**Lei nº 8.112/90**)  
**Formação:** Graduação em Engenharia Cartográfica com Especialização em Ciência de Dados.  
**Localização:** Superintendência Estadual do IBGE (SES), atuando no Centro Estadual de Qualidade (CEQ).  
**Citação:** *"Meu trabalho é garantir que os números reflitam a verdade do campo; um dado sem consistência geográfica é apenas um palpite, não estatística."*

#### 📖 Biografia e Trajetória Profissional
Carlos ingressou no IBGE via concurso público há 15 anos. Como servidor efetivo sob o regime da **Lei nº 8.112/90**, ele possui estabilidade e uma visão de longo prazo sobre as séries históricas do Instituto. Já participou de três operações censitárias e hoje lidera equipes de auditoria, sendo o responsável final pela homologação de setores complexos. Ele valoriza a precisão técnica e o rigor normativo, sendo exigente quanto ao cumprimento do **Manual do Recenseador** e das normas da **ABNT** na documentação técnica.

#### 📱 Perfil Tecnológico e Necessidades
*   **Ferramentas:** Opera estações de trabalho de alto desempenho com softwares de **Geoprocessamento** (QGIS, ArcGIS) e o dashboard de controle do **SIGC** (Sistema de Indicadores de Desempenho).
*   **Habilidades:** Especialista em análise de **coordenadas geográficas**, detecção de erros de consistência (ex: área declarada vs. produção colhida) e manipulação de bases de dados **SQL**.
*   **Necessidades:** Precisa de uma interface que centralize alertas de inconsistência e permita a visualização de mapas de calor sobre a cobertura dos setores em tempo real.

#### ⚠️ Responsabilidades e Critérios de Qualidade
*   **Auditoria Geográfica:** Validar se as capturas de coordenadas no DMC respeitam o limite de incerteza (**σₕ < 5,0m**) e o índice **HDOP** aceitável.
*   **Consistência Temática:** Cruzar dados de **produção de subsistência** com a estrutura fundiária da região para evitar subnotificações.
*   **Homologação:** Decidir sobre a necessidade de revisitas em campo ou se o setor pode ser encerrado e transmitido para a base nacional.

---

### 🏗️ Aplicação dos 5 Planos de Garrett (Foco: Auditoria e Validação)

Carlos exige que o sistema "Censo Fácil" ofereça suporte à sua função crítica de controle:

1.  **Estratégia (Metas de Qualidade):**
    *   **Objetivo:** Reduzir o índice de erro de omissão e garantir a integridade dos dados conforme a **LGPD**.
    *   **KPIs:** Taxa de setores homologados na primeira análise e precisão do georreferenciamento.

2.  **Escopo (Funcionalidades de Auditoria):**
    *   **Dashboards de Desempenho:** Visualização de indicadores de cobertura e produtividade por agente.
    *   **Filtros de Inconsistência:** Ferramenta para gerenciar situações de **PEUV** (Pendente de Espécie da Unidade Visitada) e recusas.

3.  **Estrutura (Fluxo de Validação):**
    *   **Workflow Linear:** Recebimento dos dados do ACS → Análise de inconsistências → Aprovação ou solicitação de correção (retorno ao campo) → Homologação final.

4.  **Esqueleto (Análise Eficiente):**
    *   **Interface Baseada em Mapas:** Disposição de dados lado a lado com a imagem de satélite para validar a "Regra da Sede" em propriedades multissetoriais.
    *   **Hierarquia de Alertas:** Destaque visual para erros críticos que impedem a homologação.

5.  **Superfície (Visualização de Dados):**
    *   **Design Tokens:** Uso estrito do **Azul IBGE (Pantone 286 C)** e tipografia **Univers LT Std** para relatórios oficiais.
    *   **Acessibilidade:** Gráficos e tabelas densas com contraste e legibilidade otimizados para sessões longas de análise.

---

### ✅ Validação e Conformidade Normativa
Esta persona foi estruturada respeitando a distinção entre os regimes jurídicos presentes nas fontes: enquanto a Mariana (Recenseadora) é regida pelo contrato temporário da **Lei nº 8.745/93**, Carlos personifica a governança do servidor estável da **Lei nº 8.112/90**, sendo o guardião da memória técnica do IBGE. O projeto prático no Dia 08 do cronograma focará especificamente no desenvolvimento das interfaces que Carlos utilizará para manter os padrões de qualidade do 12º Censo Agropecuário.