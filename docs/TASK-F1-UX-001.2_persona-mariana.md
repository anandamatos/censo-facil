# 🗂️ Card da Persona: Mariana

**Nome Completo:** Mariana Silva Silveira
**Idade:** 26 anos
**Ocupação:** Recenseadora (Contratada temporária sob a **Lei nº 8.745/93**)
**Escolaridade:** Superior Completo (Recém-formada em Ciências Sociais)
**Localização:** Atua em setores censitários rurais de difícil acesso
**Citação:** *"Meu objetivo é cumprir a meta do dia com precisão, mas as estradas e a falta de sinal tornam cada entrevista um desafio de logística."*

#### 📖 Biografia e Contexto Profissional
Mariana é uma jovem profissional que viu no Processo Seletivo Simplificado do IBGE uma oportunidade de aplicar seus conhecimentos acadêmicos e obter renda. Como contratada temporária, seu vínculo tem duração prevista de até **12 meses**, sem estabilidade, e sua remuneração é estritamente baseada na **produção** (quantidade de estabelecimentos visitados e questionários aplicados). Ela é dedicada e entende a importância da missão institucional de "retratar o Brasil", mas sente a pressão de prazos e a necessidade de eficiência para garantir seus rendimentos.

#### 📱 Perfil Tecnológico e Equipamento
*   **Equipamento:** Opera o **Dispositivo Móvel de Coleta (DMC)**, um tablet que integra mapas digitais, lista de endereços e questionários.
*   **Habilidades:** Alta alfabetização digital, mas utiliza o dispositivo em condições adversas (sol forte, chuva, poeira).
*   **Uso de Dados:** Depende criticamente das funcionalidades **offline** do sistema, realizando a sincronização dos dados apenas ao retornar ao Posto Censitário ou encontrar sinal estável.

#### ⚠️ Desafios Operacionais em Campo
*   **Navegação:** Enfrenta dificuldades com limites de setores mal definidos fisicamente e estradas vicinais sem sinalização.
*   **Logística:** Necessita de autonomia de bateria e GPS (GNSS) preciso para georreferenciar as sedes dos estabelecimentos.
*   **Situações Especiais:** Lida diariamente com a **ausência de informantes** (exigindo retorno em horários alternados) e **recusas** que demandam habilidades de convencimento e mediação.

---

### 🏗️ Aplicação dos 5 Planos de Garrett (Foco: Eficiência em Campo)

Para atender Mariana, o "Censo Fácil" deve ser estruturado conforme o modelo de Garrett:

1.  **Estratégia (Necessidades e Objetivos):**
    *   **Usuário:** Maximizar a coleta diária com o mínimo de retrabalho ou erros de consistência.
    *   **IBGE:** Garantir a cobertura total do setor e a integridade dos dados sob a LGPD.

2.  **Escopo (Especificações Funcionais):**
    *   **Offline-First:** Mapas vetoriais e questionários carregados localmente com criptografia **AES-256**.
    *   **GNSS Tracker:** Indicador visual de precisão (HDOP) para garantir capturas válidas.

3.  **Estrutura (Arquitetura da Informação):**
    *   **Fluxo de Trabalho:** Organização clara das etapas: Preparação → Coleta → Transmissão.
    *   **Navegação:** Interface centrada no mapa para facilitar a varredura do terreno e evitar omissões.

4.  **Esqueleto (Design de Interface):**
    *   **Target Size:** Alvos de toque de no mínimo **24x24 pixels** para uso em movimento.
    *   **Feedback Imediato:** Alertas de consistência em tempo real para evitar a necessidade de revisitas.

5.  **Superfície (Design Visual):**
    *   **Identidade:** Uso do **Azul IBGE (#0033A0)** e tipografia **Univers LT Std**.
    *   **Acessibilidade:** Alto contraste para leitura sob luz solar intensa, seguindo o **e-MAG 3.1**.

---

### ✅ Validação e Suporte
Mariana reporta-se diretamente ao **Agente Censitário Supervisor (ACS)**, que avalia a qualidade de seu trabalho e gerencia a cobertura do setor. O sucesso da Mariana depende de uma interface que minimize a carga cognitiva e automatize tarefas repetitivas, permitindo que ela foque na interação humana com os produtores rurais.