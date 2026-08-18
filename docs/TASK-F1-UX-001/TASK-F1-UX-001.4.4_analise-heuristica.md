# 📊 Análise Heurística Expandida: Sistema Censo Fácil

#### 1. Visibilidade do Status do Sistema
O sistema deve informar claramente o estado de conectividade e a precisão da coleta geográfica.
*   **Aplicação no Projeto:** O componente `br-gnss-tracker` utiliza indicadores visuais de cores baseados no **HDOP**: verde para sinal ótimo (≤ 2.5m), amarelo para aceitável (≤ 5.0m) e vermelho para sinal bloqueado (> 5.0m). 
*   **Insight:** Um indicador de sincronização em segundo plano (**Background Sync**) informa à Mariana se os dados já foram transmitidos via TLS 1.3 ou se permanecem apenas no armazenamento local criptografado.

#### 2. Correspondência entre o Sistema e o Mundo Real
A linguagem deve ser familiar ao produtor rural e respeitar a terminologia técnica do IBGE.
*   **Aplicação no Projeto:** Uso de um **Glossário Agropecuário** que traduz termos técnicos para medidas locais, como "alqueires" ou "tarefas", facilitando a compreensão do Seu José.
*   **Insight:** A interface utiliza ícones e metáforas baseadas no **Manual do Recenseador**, como a distinção visual clara entre "Residência" e "Estabelecimento Agropecuário".

#### 3. Controle e Liberdade do Usuário
O usuário deve ser capaz de desfazer ações, especialmente em formulários longos.
*   **Aplicação no Projeto:** Implementação de salvamento automático em **IndexedDB**, permitindo que o Seu José saia do app e retorne exatamente de onde parou sem perda de dados, essencial para dispositivos com pouca memória.
*   **Insight:** Mariana pode editar coordenadas geográficas antes da homologação final, caso perceba que o ponto foi capturado longe da "Regra da Sede".

#### 4. Consistência e Padrões
Aderência estrita à Identidade Visual do IBGE e ao Design System do Governo Federal.
*   **Aplicação no Projeto:** Uso obrigatório da família tipográfica **Univers LT Std** para interfaces e do **Azul IBGE (Pantone 286 C / #0033A0)**.
*   **Insight:** O sistema segue as grids fluidas do **DSGov Mobile**: 4 colunas para smartphones (Seu José) e 8 colunas para tablets (Mariana/Carlos).

#### 5. Prevenção de Erros
O DMC deve atuar como a primeira barreira contra dados inconsistentes.
*   **Aplicação no Projeto:** Travas de segurança lógica impedem o registro de dados fisicamente impossíveis, como um efetivo de pecuária maior do que a capacidade da área de pastagem declarada.
*   **Insight:** O sistema bloqueia a finalização do questionário se o índice **HDOP** for superior a 5,0 metros, prevenindo erros de georreferenciamento que seriam rejeitados pelo Carlos (ACQ).

#### 6. Reconhecimento em vez de Memorização
Redução da carga cognitiva através da visibilidade de contexto e dados persistentes.
*   **Aplicação no Projeto:** Implementação do critério **WCAG 3.3.7 (Redundant Entry)**, que evita que o Seu José tenha que digitar novamente informações já capturadas pelo sistema ou pelo login do Gov.br.
*   **Insight:** O cabeçalho do formulário mantém visível o nome do produtor e o código do setor censitário, evitando que a Mariana se perca durante a varredura do terreno.

#### 7. Flexibilidade e Eficiência de Uso
Atender tanto ao usuário leigo (Seu José) quanto ao profissional técnico (Carlos).
*   **Aplicação no Projeto:** Fluxo simplificado passo a passo (**Wizard**) para o produtor e dashboards densos com filtros de inconsistência avançados para o ACQ.
*   **Insight:** Alvos interativos com tamanho mínimo de **24x24 pixels** (WCAG 2.5.8), otimizados para uso em campo sob condições de trepidação ou mãos calejadas.

#### 8. Estética e Design Minimalista
Foco na legibilidade e na tarefa principal, eliminando ruídos visuais.
*   **Aplicação no Projeto:** Design baseado no **DSGov 4.0**, priorizando alto contraste (mínimo de 4.5:1) para leitura sob a luz solar intensa das áreas rurais.
*   **Insight:** A tipografia **Neuropolitical** é utilizada estritamente na logomarca, mantendo a interface limpa com a família Univers.

#### 9. Ajuda para Reconhecer, Diagnosticar e Recuperar de Erros
Mensagens de erro claras e orientações de correção imediata.
*   **Aplicação no Projeto:** Em caso de baixa precisão GNSS, o sistema exibe um alerta explicativo sugerindo que o agente se afaste de obstáculos físicos (copas de árvores ou muros).
*   **Insight:** Microcopy de tratamento de erros seguindo os princípios de **Linguagem Simples**, explicando o "porquê" do erro em vez de códigos de sistema genéricos.

#### 10. Ajuda e Documentação
Suporte acessível a qualquer momento durante a operação.
*   **Aplicação no Projeto:** Acesso direto ao **Manual do Recenseador** e ao **Manual de Entrevista** em formato digital dentro do próprio DMC.
*   **Insight:** Inclusão de botões de áudio para leitura de instruções, auxiliando o Seu José em casos de baixa alfabetização ou dificuldades de leitura.

---

### 🛡️ Matriz de Severidade Aplicada (LGPD)
Com base na auditoria do briefing, o maior risco identificado é a omissão de segurança em dados offline. 
*   **Recomendação Crítica:** É obrigatório o uso de criptografia simétrica **AES-256** no IndexedDB via Web Crypto API para todos os dados "at rest" no dispositivo, garantindo a conformidade com a **LGPD** e o sigilo estatístico da Lei nº 5.534/68.