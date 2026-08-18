# 🗺️ Jornada Digital #01: Seu José (Produtor Rural)

A jornada do Seu José é marcada pela dualidade entre a necessidade de visibilidade para obter crédito rural (PRONAF) e o medo de fiscalização ou perda de benefícios sociais.

#### 1. Sensibilização e Descoberta (Contexto Social)
*   **Ação:** Seu José toma conhecimento do Censo através de um carro de som na vila ou pela visita da recenseadora Mariana em sua porteira.
*   **Insight de UX:** O primeiro contato deve enfatizar o **Sigilo Estatístico (Lei nº 5.534/68)** e a **LGPD** para mitigar a desconfiança inicial.
*   **Ponto de Dor:** Receio de que declarar sua produção de subsistência (milho e feijão para a família) resulte em novos impostos.
*   **Oportunidade:** Mostrar que o preenchimento garante a atualização do cadastro de estabelecimentos rurais, facilitando o acesso ao **PRONAF**.

#### 2. Acesso e Autenticação (Fronteira Tecnológica — Online)
*   **Ação:** Ele abre o aplicativo em seu smartphone Android básico. O sistema solicita login via **Gov.br**.
*   **Insight Técnico:** Para evitar a frustração com senhas complexas, o sistema oferece autenticação por **PIN numérico** ou biometria (conforme WCAG 2.2, critério 3.3.8, que veda testes cognitivos).
*   **Ponto de Dor:** O sinal 3G oscila bruscamente. Ele precisa subir até o "alto do morro" para validar o acesso inicial.

#### 3. Coleta e Preenchimento (Arquitetura Instrucional — Offline)
*   **Ação:** Com o login validado, o sistema entra em modo **Offline-First**. Seu José responde ao **Questionário Básico**.
*   **Insight de Design:** O app diferencia **"Propriedade Rural"** (onde ele mora) de **"Estabelecimento Agropecuário"** (onde ele produz), usando um glossário que traduz hectares para medidas locais como **"tarefas"** ou **"alqueires"**.
*   **Acessibilidade:** Os botões possuem alvos de toque amplos (**48x48 pixels**) para facilitar o uso por mãos calejadas, e o contraste é de **4.5:1** para leitura sob o sol forte do sertão baiano.

#### 4. Validação e Captura de Coordenadas (Georreferenciamento)
*   **Ação:** O sistema utiliza o componente **br-gnss-tracker** para registrar a localização da sede da pequena fazenda.
*   **Insight de Engenharia:** O app exibe um indicador visual: se a incerteza da coordenada (**\\(\sigma_h\\)**) for maior que **5,0 metros**, ele orienta o Seu José a se afastar de árvores ou muros altos para melhorar a recepção do satélite.
*   **Segurança:** Cada resposta é encriptada imediatamente com **AES-256** no banco de dados local (**IndexedDB**) do celular.

#### 5. Finalização e Alívio (Sincronização e Sigilo)
*   **Ação:** Ele encerra o preenchimento e recebe um **Recibo Digital**.
*   **Insight de Sincronia:** O sistema aguarda silenciosamente. Quando Seu José vai à sede do município na feira semanal, o **Background Sync** detecta internet e transmite os dados via **TLS 1.3**.
*   **Emoção:** Sensação de dever cumprido e segurança de que seus dados foram protegidos e entregues ao "governo" para garantir as melhorias na região.

---

### 💡 Matriz de Sucesso para a Persona
Para que esta jornada seja bem-sucedida no contexto do concurso IBGE 2026, o projeto deve garantir:
1.  **Linguagem Simples:** Abstração de termos jurídicos em favor de orientações diretas.
2.  **Robustez Offline:** O formulário nunca deve perder dados se o app fechar ou a bateria acabar.
3.  **Identidade Visual:** Uso da família **Univers LT Std** e do **Azul IBGE (#0033A0)** para transmitir a autoridade e seriedade da instituição.
Com base nos manuais técnicos do IBGE, no regime jurídico da Lei nº 8.745/93 e nas diretrizes de engenharia do desafio "Censo Fácil", apresento a jornada detalhada da recenseadora **Mariana**, enriquecida com requisitos técnicos e operacionais críticos para o sucesso da operação em campo.

---

# 🗺️ Jornada Digital #02: Mariana (Recenseadora)

A jornada de Mariana é regida pela busca por eficiência, visto que sua remuneração é calculada estritamente **por produção** (quantidade de estabelecimentos visitados e questionários aplicados).

#### 1. Preparação e Planejamento (Posto Censitário — Online)
*   **Ação:** Mariana comparece ao Posto Censitário, sua base operacional física. Ela recebe as orientações técnicas e materiais de seu Agente Censitário Supervisor (ACS).
*   **Insight Técnico:** No DMC, ela realiza a carga digital do **Setor Censitário** designado. Ela deve consultar o **Mapa Municipal Estatístico (MME)** fixado no posto para planejar a rota de acesso e os meios de transporte adequados para chegar à área rural.
*   **Ponto de Dor:** Pressão para iniciar a coleta rapidamente para garantir rendimento financeiro.

#### 2. Navegação e Reconhecimento (Campo — Offline)
*   **Ação:** Mariana inicia o percurso pelo ponto inicial definido no **Descritivo do Setor**. Ela deve seguir uma varredura ordenada (espiral ou zigue-zague) para evitar omissões ou duplicidade de visitas.
*   **Insight Geográfico:** Ela utiliza a **Escala Gráfica** do mapa digital para estimar distâncias reais (ex: 3cm no mapa 1:50.000 = 1,5 km) e gerenciar a autonomia da bateria do DMC e do combustível.
*   **Desafio:** Identificar "linhas secas" (limites imaginários não materializados no terreno) e gerenciar o acesso a Áreas de Interesse Operacional (AIOs) de Povos e Comunidades Tradicionais, que podem exigir guias-intérpretes.

#### 3. Abordagem e Coleta de Dados (Campo — Offline)
*   **Ação:** Ao chegar a uma propriedade, deve distinguir se é apenas uma residência ou um **Estabelecimento Agropecuário** (unidade com produção para venda ou subsistência).
*   **Captura GNSS:** Mariana deve se posicionar na sede ou entrada principal. O sistema "Censo Fácil" (br-gnss-tracker) fornece feedback visual do **HDOP**: ela só registra o ponto se a incerteza (\\(\sigma_h\\)) for **inferior a 5,0 metros**.
*   **Entrevista:** Aplica o Questionário Básico ou Completo conforme o perfil produtivo.
*   **Insight de UX:** A interface deve ter alto contraste (**4.5:1**) e tipografia **Univers LT Std** para legibilidade sob sol forte, com botões de no mínimo **24x24 pixels** para facilitar o uso com mãos calejadas ou em movimento.

#### 4. Gestão de Conflitos e Atualização Cadastral (Campo — Offline)
*   **Situações Especiais:**
    *   **Ausência:** Se não encontrar ninguém, deve realizar pelo menos **3 tentativas** em horários alternados antes de reportar a pendência ao ACS.
    *   **Recusa:** Mariana não deve ser hostil. Deve registrar a recusa no DMC para que o ACS realize uma visita de sensibilização posterior.
*   **Conformidade:** Os dados são salvos com criptografia **AES-256** no armazenamento local (IndexedDB) para garantir o sigilo estatístico e conformidade com a **LGPD**.

#### 5. Transmissão e Homologação (Posto Censitário — Sync)
*   **Ação:** Ao retornar à base ou encontrar sinal, o **Background Sync** transmite os dados via TLS 1.3 para os servidores do IBGE.
*   **Insight de Auditoria:** Mariana apresenta o trabalho ao ACS. Se houver falhas de cobertura ou inconsistências graves (ex: área declarada maior que a do setor), o supervisor exige o retorno imediato a campo para correção.
*   **Emoção:** "Dever cumprido" e confirmação da produtividade para fins de pagamento.

---

### ✅ Matriz de Desempenho da Jornada
Para Mariana ter um alto desempenho, o sistema deve garantir:
1.  **Operação 100% Offline:** Mapas e regras de consistência devem estar na memória física do dispositivo.
2.  **Rigor de Endereçamento:** Registro seguindo o padrão CNEFE, incluindo pontos de referência rurais (ex: "após a porteira azul").
3.  **Segurança Híbrida:** Integração com login **Gov.br** (nível prata/ouro), mas com contingência via PIN para áreas sem torre de celular.

---- 

# 🗺️ Jornada Digital #03: Carlos (ACQ)

A jornada de Carlos é pautada pelo rigor normativo e pela estabilidade institucional garantida pela **Lei nº 8.112/90**. Diferente dos contratados temporários, sua função exige uma visão de longo prazo sobre a consistência dos dados que comporão as estatísticas oficiais do país.

#### 1. Preparação e Monitoramento em Tempo Real (Online — CEQ)
*   **Ação:** Carlos inicia seu expediente acessando o painel do **SIGC** (Sistema de Indicadores de Desempenho) em sua estação de trabalho no Centro Estadual de Qualidade (CEQ).
*   **Insight de Auditoria:** Ele monitora o ritmo de coleta da equipe em campo. O sistema "Censo Fácil" permite que ele visualize mapas de calor de produtividade e identifique gargalos operacionais em tempo real.
*   **Foco Técnico:** Carlos verifica se o cronograma de carga e transmissão de setores está alinhado às metas nacionais coordenadas pelo CNQ.

#### 2. Auditoria de Precisão Geográfica (Georreferenciamento)
*   **Ação:** O ACQ seleciona amostras de endereços capturados para validar as coordenadas GNSS registradas nos DMCs.
*   **Insight de Engenharia:** Ele analisa o índice de incerteza da coordenada (\\(\sigma_h\\)). Conforme as normas técnicas, o registro só é válido se a precisão horizontal for estritamente **inferior a 5,0 metros**.
*   **Análise Espacial:** Através de imagens orbitais, ele confirma se o ponto georreferenciado respeita a **"Regra da Sede"**, garantindo que propriedades multissetoriais sejam contabilizadas no setor correto.

#### 3. Cruzamento de Consistência Temática (Lógica Censitária)
*   **Ação:** Carlos examina os Questionários Básico e Completo, verificando a completude e padronização das respostas.
*   **Insight de Consistência:** Ele utiliza algoritmos para detectar discrepâncias lógicas, como a relação entre a área total declarada e o efetivo da pecuária ou volume de colheita.
*   **Diferencial Profissional:** Ele gerencia situações de **PEUV** (Pendente de Espécie da Unidade Visitada) para assegurar que estabelecimentos rurais não sejam classificados erroneamente como domicílios comuns.

#### 4. Mediação Técnica e Gestão de Erros (Supervisão)
*   **Ação:** Ao detectar falhas recorrentes, Carlos orienta o Agente Censitário Supervisor (ACS) sobre a necessidade de reforço no treinamento dos recenseadores.
*   **Ponto de Decisão:** Ele avalia as justificativas inseridas para casos de **recusa** ou **ausência**, confirmando se foram realizadas as 3 tentativas obrigatórias em horários alternados antes de aceitar o encerramento da pendência.

#### 5. Homologação Final e Transmissão (Encerramento)
*   **Ação:** Após a validação de todas as correções, Carlos realiza a **homologação** definitiva do setor censitário para a base nacional.
*   **Insight de Governança:** O ACQ assegura que toda a produção documentária do censo respeite as normas da **ABNT** (como a NBR 14724) e os padrões de identidade visual do instituto.
*   **Segurança:** Garante que o fluxo de dados respeite o sigilo estatístico e a **LGPD**, validando o descarte seguro dos dados locais após a sincronização.

---

### 💡 Matriz de Sucesso para o ACQ
Para que Carlos desempenhe sua função com excelência, o sistema "Censo Fácil" deve oferecer:
1.  **Visão Lado a Lado:** Comparação entre dados declarados e imagens de satélite para auditoria geográfica.
2.  **Alertas Hierarquizados:** Notificações automáticas de inconsistências graves baseadas em algoritmos de validação.
3.  **Rigor Tipográfico:** Uso das famílias **Univers LT Std** e **FALse positiVe Round BRK** (esta restrita à marca do Censo Agro) para garantir a credibilidade institucional.