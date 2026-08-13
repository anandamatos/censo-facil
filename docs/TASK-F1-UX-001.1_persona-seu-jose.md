# 🗂️ Card da Persona: Seu José

**Nome Completo:** José dos Santos
**Idade:** 62 anos
**Ocupação:** Agricultor Familiar (Policultura de Subsistência).
**Escolaridade:** Ensino Fundamental Incompleto.
**Localização:** Minifúndio em área rural de ocupação dispersa, interior da Bahia.
**Citação:** *"Eu só quero que o governo saiba que a gente existe aqui, sem complicação e sem medo de perder o que é nosso."*

#### 📖 Biografia e Contexto Socioeconômico
Seu José nasceu e cresceu na lida do campo, vivendo em uma pequena propriedade onde cultiva milho e feijão para sustento de sua família. Ele representa a **Agricultura Familiar**, pilar essencial para a segurança alimentar, e depende de políticas como o **PRONAF** para manter sua produtividade. Sua rotina é marcada pelo trabalho braçal pesado, e ele possui uma visão pragmática da terra, vendo o Censo como uma forma de garantir acesso a créditos rurais.

#### 📱 Perfil Tecnológico e Conectividade
*   **Dispositivo:** Smartphone Android básico com memória e processamento limitados.
*   **Alfabetização Digital:** **Baixa**. Ele utiliza majoritariamente o WhatsApp para áudios, sentindo-se intimidado por interfaces com termos técnicos ou muitos botões.
*   **Conectividade:** **Internet intermitente**. O sinal de dados só é estável em pontos específicos do terreno ou na sede do município.

#### ⚠️ Dores e Necessidades (Contexto do Censo)
*   **Desconfiança:** Medo de que os dados coletados sejam usados para fiscalização tributária ou perda de benefícios.
*   **Complexidade:** Dificuldade em compreender conceitos como **"Estabelecimento Agropecuário"** ou unidades de medida em hectares.
*   **Frustração:** Aplicativos que exigem conexão constante ou logins complexos que ele não consegue memorizar.

---

### 🏗️ Aplicação dos 5 Planos de Garrett (Projeto Censo Fácil)

Para atender ao Seu José sob o rigor do edital, o projeto deve seguir:

1.  **Estratégia (Necessidades do Usuário e Objetivos do Negócio):**
    *   **Usuário:** Garantir a declaração de sua produção para manter acesso a créditos rurais.
    *   **IBGE:** Capturar dados precisos de **produção de subsistência** em áreas remotas com o mínimo de omissão.

2.  **Escopo (Especificações Funcionais):**
    *   **Coleta Offline-First:** Persistência de dados encriptados (**AES-256**) no **IndexedDB** do navegador para garantir segurança sob a **LGPD** enquanto não houver sinal.
    *   **Login Acessível:** Autenticação sem testes cognitivos complexos (WCAG 2.2 - Critério 3.3.8).

3.  **Estrutura (Arquitetura da Informação):**
    *   **Método LATCH:** Organização do questionário por **Categoria** (Pecuária, Lavoura, Água) para facilitar a memorização do progresso.
    *   **Fluxo Linear:** Guia passo a passo para evitar que o usuário se perca em menus complexos.

4.  **Esqueleto (Design de Interface):**
    *   **Target Size:** Alvos interativos com no mínimo **24x24 pixels** para facilitar o toque (WCAG 2.2).
    *   **Leis da Gestalt:** Uso da **Proximidade** para agrupar campos relacionados, reduzindo a carga cognitiva.

5.  **Superfície (Design Visual):**
    *   **Cores e Contraste:** Uso do **Azul IBGE (HEX #0033A0)** com razão de contraste mínima de **4.5:1** para leitura sob o sol.
    *   **Tipografia:** Família **Univers LT Std** (55 Roman e 65 Bold) para todos os textos de interface, garantindo legibilidade.

---

### ✅ Validação e Documentação
Esta persona foi validada cruzando dados do **Relatório de Personas da Fase 1** com os procedimentos de campo descritos no **Manual do Recenseador**. O desenvolvimento técnico deve ignorar a permissividade do HTML5 moderno em favor do **XHTML Estrito** exigido pelo edital para garantir a integridade dos dados XML.