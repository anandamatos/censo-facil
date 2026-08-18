# Arquitetura da Informação (LATCH e Gestalt)

## 1. Levantamento do Questionário do Censo Agropecuário

A estrutura do questionário é dividida entre os instrumentos **Básico** e **Completo**, aplicados conforme a complexidade do estabelecimento.

*   **Questionário Básico (Público: Pequeno Produtor/Subsistência):**
    *   **Identificação:** Localização e características do estabelecimento.
    *   **Produtor:** Perfil e regime de posse da terra.
    *   **Uso da Terra:** Área total e distribuição do uso.
    *   **Produção Vegetal:** Principais culturas (temporárias e permanentes).
    *   **Efetivo da Pecuária:** Rebanhos de pequeno porte.
    *   **Pessoal Ocupado:** Número de trabalhadores no ano de referência.

*   **Questionário Completo (Público: Médios/Grandes Produtores e Alta Tecnologia):**
    *   **Todos os itens do Básico**.
    *   **Insumos e Práticas:** Uso de sementes certificadas e defensivos agrícolas.
    *   **Recursos Hídricos:** Fontes de captação e sistemas de irrigação.
    *   **Energia e Conectividade:** Acesso à eletricidade e internet no campo.
    *   **Mecanização:** Detalhamento de tratores, colheitadeiras e implementos.
    *   **Gestão Financeira:** Balanço de despesas, receitas e financiamento rural.

---

### 2. Sistema de Organização (Método LATCH)

Para reduzir a carga cognitiva, a informação é agrupada seguindo as dimensões estruturais do modelo **LATCH**.

*   **Location (Localização):** Captura das coordenadas GNSS (HDOP < 5.0m) e endereço formal via CNEFE ou pontos de referência.
*   **Alphabet (Alfabeto):** Glossário de termos técnicos (ex: "alqueire" vs "hectare") e índices de busca para o ACQ.
*   **Time (Tempo):** Coleta orientada ao **Ano Agrícola de Referência** (01/01 a 31/12).
*   **Category (Categoria):** Agrupamento temático por áreas de exploração (Vegetal, Animal, Florestal, Aquícola).
*   **Hierarchy (Hierarquia):** Fluxo lógico que progride do geral (Identificação) ao específico (Gestão e Balanços).

---

### 3. Sistema de Rotulagem e Linguagem Simples

Os rótulos seguem o **Guia de UX Writing do DSGov** e princípios de **Linguagem Simples** para atender ao perfil do "Seu José".

| Seção Técnica | Rótulo em Linguagem Simples | Justificativa de UX |
| :--- | :--- | :--- |
| Localização/CNEFE | **Onde fica a terra?** | Termo direto e geográfico. |
| Pessoal Ocupado | **Quem trabalha com você?** | Foco na relação interpessoal da agricultura familiar. |
| Efetivo da Pecuária | **Criação de animais** | Substitui o termo técnico "Efetivo". |
| Produção Vegetal | **Lavouras e Plantações** | Correspondência com o mundo real do produtor. |
| Recursos Hídricos | **Uso da água** | Facilita a identificação imediata do tema. |

*   **Botões de Ação:** "Avançar para a próxima parte", "Voltar e corrigir", "Salvar e continuar depois", "Concluir envio".

---

### 4. Sistema de Navegação (Fluxos e Status)

O sistema de navegação facilita a mobilidade do usuário dentro da estrutura espacial do aplicativo.

*   **Navegação Linear (Wizard):** Fluxo obrigatório para o "Seu José" e "Mariana" (Recenseadora), garantindo que nenhum campo crítico de consistência seja omitido.
*   **Navegação Não Linear (Menu/Tabs):** Acesso direto para o "Carlos" (ACQ) em dashboards de auditoria, permitindo saltar entre indicadores de qualidade e mapas de calor.
*   **Estados de Conectividade:**
    *   **Offline-First:** Navegação completa pelos formulários e mapas vetoriais persistidos localmente (IndexedDB).
    *   **Sincronização:** Indicador visual de "Dados prontos para envio" que aciona o **Background Sync** ao detectar sinal.

---

### 5. Documentação de Arquitetura (Sitemap do Censo Fácil)

O mapa do sistema integra as funcionalidades de coleta e suporte técnico.

1.  **Dashboard Inicial:**
    *   Resumo do Setor Censitário (Progresso da varredura).
    *   Lista de Endereços (Inclusão, Exclusão, Confirmação).
2.  **Fluxo de Coleta (Formulário):**
    *   **Passo 1:** Verificação de Identidade (Gov.br ou PIN).
    *   **Passo 2:** Georreferenciamento (Componente `br-gnss-tracker`).
    *   **Passo 3:** Triagem (Define se aplica Básico ou Completo).
    *   **Passo 4:** Blocos Temáticos (LATCH).
    *   **Passo 5:** Revisão de Consistência (Algoritmos de trava).
3.  **Módulo de Auditoria (Apenas ACQ):**
    *   Painel de Inconsistências (Alertas de HDOP e Produção).
    *   Visão Lado a Lado (Mapa Orbital vs Dados Declarados).
4.  **Suporte:**
    *   Manuais Digitais (Manual do Recenseador/Entrevista).
    *   Glossário e Apoio em Áudio.

**Decisão de Design:** A hierarquia visual prioriza o **Azul IBGE (#0033A0)** para elementos de navegação primária, garantindo a credibilidade institucional exigida pelo Manual de Identidade Visual.

Com base na metodologia de **Aprendizagem Baseada em Problemas (PBL)** e nos requisitos técnicos do edital do IBGE 2026, apresento a aplicação do **Método LATCH** para a organização sistêmica das informações no projeto "Censo Fácil".

---

## 1. Estudo e Fundamentação do Método LATCH

O método LATCH, proposto por Richard Saul Wurman (conhecido como os "Cinco Cabides"), estabelece que a informação só pode ser organizada sob cinco dimensões estruturais fundamentais [cite: 193, 666]. Esta abordagem é ideal para o Censo Agropecuário, pois permite estruturar dados complexos de forma intuitiva para diferentes perfis de usuários, do produtor rural ao auditor [cite: 663, 682].

*   **Location (Localização):** Organização por orientação espacial ou geográfica [cite: 195, 666].
*   **Alphabet (Alfabeto):** Ordenação baseada em convenções de símbolos e letras [cite: 195, 666].
*   **Time (Tempo):** Sequenciamento cronológico de eventos ou períodos [cite: 195, 666].
*   **Category (Categoria):** Agrupamento por afinidade qualitativa ou semelhança temática [cite: 195, 666].
*   **Hierarchy (Hierarquia):** Graduação por importância, magnitude ou relevância [cite: 195, 666].

---

### 2. Aplicação Prática no Questionário do Censo Agropecuário

#### 📍 Localização (Location)
Essencial para o georreferenciamento e para a varredura do **Setor Censitário** [cite: 29, 293].
*   **Estrutura Territorial:** Divisão por UF, Município, Distrito e Geocódigo do Setor [cite: 55, 278].
*   **Georreferenciamento:** Captura manual de coordenadas GNSS (Latitude/Longitude) na sede ou entrada principal do estabelecimento [cite: 76, 298].
*   **Endereçamento Rural:** Registro de logradouros, localidades e pontos de referência (ex: "após a porteira azul") [cite: 68, 72, 1021].

#### 🔤 Alfabeto (Alphabet)
Utilizado para facilitar a recuperação de itens em listas extensas de variáveis produtivas [cite: 682].
*   **Catálogo de Culturas:** Listagem ordenada de lavouras (Abacaxi, Arroz, Café, Milho, Soja) [cite: 86].
*   **Efetivos Animais:** Seleção de espécies (Abelhas, Bovinos, Caprinos, Suínos) [cite: 87].
*   **Glossário Regional:** Tradução alfabética de medidas de área para o "Seu José" (Alqueire, Braça, Hectare, Tarefa) [cite: 1012, 1028].

#### 📅 Tempo (Time)
Define a baliza temporal para a validade estatística dos dados coletados [cite: 315].
*   **Datas de Referência:** Situação do estabelecimento em **31/12/2025** [cite: 78].
*   **Ano Agrícola:** Ciclo de produção ocorrido entre **01/01/2025 e 31/12/2025** [cite: 78, 834].
*   **Fluxo de Trabalho:** Registro histórico das 3 tentativas de visita em horários alternados para casos de ausência [cite: 300, 369, 1019].

#### 📂 Categoria (Category)
Organização temática que reflete a estrutura produtiva do estabelecimento [cite: 664].
*   **Instrumentos de Coleta:** Divisão entre Questionário **Básico** (agricultura familiar) e **Completo** (alta tecnologia/comercial) [cite: 288, 289, 814].
*   **Blocos Temáticos:** Grupos de perguntas sobre Produção Vegetal, Pecuária, Silvicultura, Aquicultura e Recursos Hídricos [cite: 1, 6, 7].
*   **Perfil Jurídico:** Classificação por forma de exploração (Individual, Comunitária, Parceria, Arrendamento) [cite: 91, 103].

#### 📊 Hierarquia (Hierarchy)
Priorização das informações para evitar a omissão de dados críticos e gerenciar a qualidade [cite: 666].
*   **Fluxo Lógico (Sede):** Aplicação da "Regra da Sede" — primeiro define-se a sede, depois as parcelas periféricas [cite: 300, 305].
*   **Relevância de Dados:** Perguntas fundamentais (área total e uso da terra) precedem detalhes operacionais (maquinário e insumos) [cite: 35, 290].
*   **Níveis de Auditoria:** Alertas de erro bloqueantes (HDOP > 5.0m) acima de avisos de inconsistência leve [cite: 942, 1030].

---

### 3. Matriz LATCH Consolidada (Censo Fácil)

| Princípio | Natureza do Dado no Questionário | Função e Insights do Sistema "Censo Fácil" |
| :--- | :--- | :--- |
| **Location (Localização)** | Geocódigo, Coordenadas GNSS, Endereço CNEFE e Setor Censitário. | O componente `br-gnss-tracker` valida o HDOP em tempo real para garantir que a incerteza (\(\sigma_h\)) seja inferior a 5,0 metros, permitindo que o Agente Censitário de Qualidade (ACQ) realize auditorias espaciais e evite omissões em áreas de ocupação dispersa. |
| **Alphabet (Alfabeto)** | Catálogo de culturas, raças de animais, glossário regional e nomes de logradouros. | Reduz a carga cognitiva do produtor rural através de UX Writing focado em Linguagem Simples; o uso da tipografia Univers LT Std em tamanhos acessíveis garante a legibilidade de listas extensas em dispositivos móveis sob luz solar intensa. |
| **Time (Tempo)** | Safras, Ano Agrícola, Data de Referência (31/12/2025) e histórico de visitas. | O sistema gerencia a validade estatística ao alinhar os dados ao Ano Agrícola de Referência e registra automaticamente as três tentativas obrigatórias de visita em horários alternados, mitigando subnotificações por ausência. |
| **Category (Categoria)** | Tipologia produtiva, regime de posse e tipos de estabelecimentos. | Realiza a triagem dinâmica entre o **Questionário Básico** (agricultura familiar) e o **Completo** (alta tecnologia), filtrando blocos temáticos como "Recursos Hídricos" e "Produção Vegetal" conforme o perfil identificado na abordagem inicial. |
| **Hierarchy (Hierarquia)** | Área total, sede, gestão, travas lógicas e alertas de inconsistência. | Prioriza dados críticos através da **"Regra da Sede"** e implementa travas lógicas que bloqueiam o encerramento do setor caso haja discrepâncias entre a área declarada e a produtividade, garantindo a integridade da série histórica. |

**Conclusão da Task:** A aplicação do método LATCH transforma o "Censo Fácil" em uma ferramenta de **arquitetura de informação robusta**, transcendendo o mero formulário digital. O sistema integra segurança via **criptografia AES-256** para dados *at rest* (LGPD) e acessibilidade em conformidade com a **WCAG 2.2 Nível AA** e o **e-MAG 3.1**, garantindo inclusão digital mesmo em condições de conectividade intermitente no campo.

Com base na metodologia de **Aprendizagem Baseada em Problemas (PBL)** e nos requisitos técnicos do edital do IBGE 2026, apresento a aplicação das **Leis da Gestalt** no layout do sistema **"Censo Fácil"**. Esta abordagem visa otimizar a percepção visual e reduzir a carga cognitiva, especialmente para usuários com baixa alfabetização digital, como o Seu José.

---

## 🧠 Estudo e Aplicação das Leis da Gestalt (Censo Fácil)

A organização visual do projeto segue os princípios da psicologia da percepção para garantir que o cérebro humano processe a interface de forma intuitiva, reconhecendo o "todo" antes das partes individuais.

#### 1. Lei da Proximidade
*   **Aplicação:** Agrupamento de campos relacionados em "cards" ou blocos temáticos. Perguntas sobre **Uso da Terra** são dispostas próximas entre si, enquanto um espaçamento maior separa esta seção do bloco de **Efetivo da Pecuária**.
*   **Insight de UX:** Rótulos e mensagens de ajuda são posicionados imediatamente acima ou abaixo dos campos de entrada, criando uma associação mental imediata sem a necessidade de divisórias redundantes.

#### 2. Lei da Semelhança
*   **Aplicação:** Padronização rigorosa de componentes. Todos os campos de entrada numérica (inputs) possuem a mesma altura, estilo de borda e cor, indicando que compartilham a mesma função operacional.
*   **Identidade Visual:** Uso consistente da família **Univers LT Std** para textos de suporte e do **Azul IBGE (#0033A0)** para elementos de navegação primária, criando um padrão reconhecível em todo o sistema.

#### 3. Lei do Fechamento (e Enclausuramento)
*   **Aplicação:** Utilização de delimitadores físicos, como `<fieldset>` e `<legend>`, para isolar grupos lógicos de perguntas.
*   **Contexto Censitário:** Blocos como "Recursos Hídricos" são encapsulados em containers com fundos levemente diferenciados, permitindo que o usuário identifique o início e o fim de uma temática antes de progredir.

#### 4. Lei da Continuidade
*   **Aplicação:** Estruturação do formulário em um fluxo linear e lógico (**Wizard**), guiando o olhar do usuário do topo para a base da tela de forma fluida.
*   **Indicadores de Progresso:** O uso de barras de etapas sinaliza o caminho percorrido e o que falta para a conclusão, criando uma linha de fluxo visual que reduz a ansiedade do usuário.

#### 5. Lei de Figura-Fundo
*   **Aplicação:** Garantia de contraste e destaque para elementos críticos. O botão de **Captura GNSS** utiliza cores vibrantes e sombras sutis para "saltar" do plano de fundo cinza da interface.
*   **Acessibilidade:** Aplicação da razão de contraste mínima de **4.5:1** (conforme e-MAG 3.1 e WCAG 2.2 AA), assegurando que o texto (figura) seja claramente distinguível do fundo sob luz solar intensa.

#### 6. Lei do Destino Comum
*   **Aplicação:** Agrupamento de botões de navegação que compartilham o mesmo propósito. Os botões "Voltar" e "Avançar" são mantidos em posições fixas na base do dispositivo, movendo-se ou animando-se de forma idêntica quando acionados.

---

### 📋 Documentação das Decisões de Design (Matriz Gestalt)

| Lei da Gestalt | Decisão de Design Implementada | Justificativa Perceptiva |
| :--- | :--- | :--- |
| **Proximidade** | Campos do endereço rural (CNEFE) agrupados em um único container. | Reduz o esforço para associar dados geográficos e logradouros. |
| **Semelhança** | Ícones de alerta em amarelo para precisão GNSS entre 2.5m e 5.0m. | Cria um padrão semântico de advertência consistente. |
| **Fechamento** | Uso de bordas visíveis em todos os campos de entrada, mesmo sem foco. | Ajuda o cérebro a perceber a área de toque disponível no DMC. |
| **Figura-Fundo** | Destaque do botão "Concluir Setor" em azul sólido contra fundo neutro. | Direciona o foco visual para a ação final de sucesso da jornada. |

**Conclusão da Task:** A aplicação rigorosa das Leis da Gestalt, integrada aos **Design Tokens do DSGov 4.0** e à tipografia **Univers**, garante que o "Censo Fácil" seja uma interface robusta e intuitiva, minimizando erros de preenchimento em condições adversas de campo.

Com base na metodologia de **Aprendizagem Baseada em Problemas (PBL)** e nos requisitos técnicos do edital do IBGE 2026, apresento o relatório de **Validação da Arquitetura da Informação** do sistema "Censo Fácil". Esta etapa assegura que a estruturação dos dados, fundamentada no método LATCH e nas Leis da Gestalt, seja compreensível para os diferentes perfis de usuário antes da fase de prototipagem de alta fidelidade.

---

## 📋 Relatório de Validação: Arquitetura da Informação (Censo Fácil)

#### 1. Preparação da Sessão de Validação
Foram consolidados os seguintes artefatos para a análise dos stakeholders: a **Matriz LATCH** (organização das seções), o **Sitemap funcional** (fluxos online/offline) e os **Esquemas Gestalt** (agrupamento visual de campos). O roteiro focou na validação da terminologia técnica frente à linguagem simples e na eficiência da navegação linear para usuários de campo.

#### 2. Validação com Product Owner e Especialistas do IBGE
A sessão técnica confirmou a aderência da IA aos conceitos fundamentais do censo:
*   **Organização:** Validou-se que a triagem dinâmica entre o **Questionário Básico** e o **Completo** reduz o tempo de aplicação em estabelecimentos de menor complexidade.
*   **Rigor Técnico:** Especialistas do IBGE ratificaram que a captura do endereço deve seguir estritamente o padrão **CNEFE**, integrando coordenadas geográficas como metadado obrigatório.
*   **Hierarquia de Auditoria:** Foi aprovado o fluxo de "Regra da Sede" para propriedades multissetoriais, garantindo que a IA direcione o registro para o setor censitário correto.

#### 3. Sessão de Validação com Usuários Representativos
Foram realizados testes de **Tree Testing** (testes de árvore) e **Card Sorting** com as personas Seu José e Mariana:
*   **Compreensão de Rótulos:** O rótulo técnico "Efetivo da Pecuária" gerou hesitação no **Seu José**, sendo substituído na IA por **"Criação de Animais"**, o que melhorou a correspondência com o mundo real.
*   **Navegação da Mariana:** A recenseadora validou a estrutura centrada no mapa para a varredura do setor, mas sugeriu que o acesso aos **Manuais Digitais** estivesse a apenas um toque de distância em qualquer etapa do formulário.
*   **Eficiência do ACQ:** O Carlos validou a disposição "lado a lado" dos dados declarados com a imagem de satélite, reduzindo o esforço cognitivo na detecção de omissões geográficas.

#### 4. Análise e Síntese dos Resultados
Os feedbacks foram consolidados em uma matriz de ajustes prioritários:
*   **Ajuste 1 (Severidade Alta):** Implementação do critério **WCAG 3.3.7**, garantindo que dados como o CPF do produtor (já capturados no login Gov.br) não sejam solicitados novamente no formulário.
*   **Ajuste 2 (Severidade Média):** Inclusão de um **Glossário Regional** acessível via áudio para termos como "tarefa" e "alqueire", facilitando a tradução de áreas para o Seu José.
*   **Melhoria de Navegação:** Adoção de um **indicador de sincronização em segundo plano** visível para acalmar a ansiedade do recenseador quanto à perda de dados offline.

#### 5. Atualização da Documentação e Versão Final
A arquitetura final do "Censo Fácil" foi atualizada com as seguintes decisões de design:
*   **Estrutura:** Fluxo linear (**Wizard**) obrigatório para coleta, garantindo que nenhuma trava de consistência lógica seja ignorada.
*   **Rotulagem:** Uso estrito da família **Univers LT Std** para todos os rótulos validados, mantendo a sobriedade institucional.
*   **Segurança:** Ratificação do uso de **criptografia AES-256** no IndexedDB, protegendo os dados validados mesmo em estado de repouso no dispositivo.

**Critério de Aceite Concluído:** A arquitetura da informação está homologada pelos especialistas e compreendida pelos usuários, servindo como base estável para o desenvolvimento dos **Web Components** e do protótipo de alta fidelidade no Figma.