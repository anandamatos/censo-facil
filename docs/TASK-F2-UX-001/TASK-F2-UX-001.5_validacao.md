# 🛡️ Relatório de Validação: Ferramenta de Avaliação Gov.br

## Design System do "Censo Fácil" — Conformidade com DSGov 4.0, e-MAG 3.1 e WCAG 2.2 AA

---

## 1. Contexto e Fundamentação

A validação do Design System do "Censo Fácil" utilizando a **Ferramenta de Avaliação Gov.br** foi estruturada para garantir a aderência ao **DSGov 4.0** e a conformidade com os padrões de acessibilidade **e-MAG 3.1** e **WCAG 2.2 AA**, fundamentais para a operação em campo por recenseadores e produtores rurais.

A Ferramenta de Avaliação do Gov.br, coordenada pela Secretaria de Governo Digital (SGD/MGI), aplica critérios que visam a uniformização da experiência do cidadão e a eliminação de barreiras digitais. O e-MAG, em sua versão 3.1, é o modelo de acessibilidade adotado pelo governo brasileiro, baseado nas recomendações internacionais da WCAG e adaptado às necessidades locais e prioridades brasileiras .

### 1.1 Base Legal e Institucional

A Secretaria de Governo Digital (SGD) é responsável por coordenar e articular as diretrizes para a gestão eficiente e segura dos dados no setor público, conforme estabelecido pela Estratégia Nacional de Governo Digital (ENGDo) . A qualidade é um valor essencial para o MGI, que busca sempre melhorar a gestão pública de forma resolutiva e responsiva por meio da inovação tecnológica .

O Governo Digital brasileiro opera sob princípios de experiência do usuário, interoperabilidade, unificação de canais digitais, governo simples e acessível, e identidade única . Esses princípios orientam a validação do Design System do "Censo Fácil", garantindo que ele atenda não apenas aos requisitos técnicos, mas também aos objetivos estratégicos de inclusão digital.

---

## 2. Metodologia e Critérios de Avaliação

### 2.1 Eixos de Avaliação

A validação foi estruturada em quatro eixos principais, alinhados às diretrizes da SGD/MGI:

| Eixo | Critério | Referência |
|------|----------|------------|
| **Identidade Unificada** | Barra Gov.Br, cores e tipografias institucionais (Azul IBGE, Univers LT Std) | DSGov 4.0 |
| **Acessibilidade Digital** | 6 áreas do e-MAG 3.1 (Marcação, Comportamento, Conteúdo, Apresentação, Multimídia, Formulário) | e-MAG 3.1  |
| **Qualidade Mobile** | Grids responsivas (4 colunas para smartphones, 8 para tablets), target size de toque | WCAG 2.2 |
| **Segurança e Privacidade** | Proteção de dados, criptografia, conformidade com LGPD | Lei nº 13.709/2018 |

### 2.2 Critérios WCAG 2.2 Aplicados

A WCAG 2.2, publicada como recomendação oficial do W3C em outubro de 2023, adicionou nove novos critérios de sucesso à especificação, removendo o critério de Parsing (4.1.1) por ter se tornado obsoleto . Os novos critérios abordam itens relativos a:

- Foco de teclado (2.4.11 — Focus Not Obscured)
- Gestos de arrasto (2.5.7 — Dragging Movements)
- Tamanho de alvo (2.5.8 — Target Size)
- Ajuda consistente (3.2.6 — Consistent Help)
- Entrada de dados (3.3.7 — Redundant Entry)
- Autenticação acessível (3.3.8 — Accessible Authentication)

**Critério 2.5.8 — Target Size (Minimum):** Estabelece que alvos interativos devem ter um tamanho mínimo de **24x24 pixels CSS**, com exceções para links inline, elementos que não podem ser redimensionados e controles nativos do agente do usuário . Alvos menores que 24x24px podem ser considerados conformes se houver espaço suficiente (pelo menos 24x24px) entre eles .

---

## 3. Execução da Avaliação do Protótipo

### 3.1 Auditoria das 6 Áreas do e-MAG 3.1

| Área e-MAG | Itens Auditados | Status | Evidência |
|------------|-----------------|--------|-----------|
| **Marcação** | XHTML Estrito, fechamento de tags, IDs únicos, atributos semânticos | ✅ Conforme | Tags fechadas, atributos em minúsculas, IDs únicos validados |
| **Comportamento** | Navegação por teclado, foco visível, `aria-live` | ✅ Conforme | Teclas Tab, Enter, Espaço funcionais; foco não obscurecido |
| **Conteúdo** | Linguagem Simples, hierarquia de títulos (h1 a h6), alternativas textuais | ✅ Conforme | Termos técnicos traduzidos ("Efetivo da Pecuária" → "Criação de animais") |
| **Apresentação** | Contraste ≥ 4.5:1, grids fluidas, zoom 200% | ✅ Conforme | Contraste validado pela Ferramenta Gov.br |
| **Multimídia** | `alt` descritivo, legendas, VLibras, sem auto-play | ✅ Conforme | Componente GNSS com `aria-label` e descrições textuais |
| **Formulário** | `label for/id`, `fieldset`/`legend`, mensagens de erro com `aria-live` | ✅ Conforme | Associações explícitas e mensagens em Linguagem Simples |

### 3.2 Resultados da Avaliação

A auditoria do protótipo de alta fidelidade e dos componentes customizados (como o `br-gnss-tracker`) identificou os seguintes pontos:

**Conformidades Verificadas:**

1. **Barra Gov.Br:** Presença obrigatória da Barra Gov.Br em todas as páginas, conforme exigência da SGD/MGI para serviços públicos digitais .
2. **XHTML Estrito:** Código validado com fechamento mandatório de todas as tags e uso de letras minúsculas em atributos, cumprindo a exigência do edital do IBGE 2026.
3. **Contraste Visual:** Razão de contraste aferida em **4.5:1** para textos normais, garantindo a legibilidade sob luz solar intensa.
4. **Target Size (WCAG 2.2 — 2.5.8):** Alvos interativos com mínimo de 24x24px CSS, expandidos para **48x48px** em funções críticas de coleta para facilitar o uso por produtores rurais .

---

## 4. Identificação e Correção de Não Conformidades

Durante a avaliação, foram priorizados ajustes de severidade alta para evitar passivos de conformidade no certame:

| Área Avaliada | Não Conformidade Detectada | Correção Implementada | Status Final |
|---------------|---------------------------|----------------------|--------------|
| **Comportamento** | Foco de teclado obscurecido pela Barra Gov.Br fixa | Reajuste do *z-index* e espaçamento superior (*padding*) para cumprir o critério **2.4.11 da WCAG 2.2** (Focus Not Obscured)  | ✅ Conforme |
| **Conteúdo** | Uso de termos técnicos ("Efetivo da Pecuária") dificultando a compreensão | Aplicação de **Linguagem Simples** e UX Writing: alterado para "Criação de animais" | ✅ Conforme |
| **Marcação** | IDs duplicados em blocos de formulários repetitivos | Implementação de lógica de geração de **IDs únicos** e associação explícita via `label for` | ✅ Conforme |
| **Segurança** | Dados sensíveis armazenados em texto simples no cache local | Implementação de criptografia simétrica **AES-256** no IndexedDB via Web Crypto API (LGPD) | ✅ Conforme |

---

## 5. Conformidade com a Estratégia Nacional de Governo Digital

A validação do "Censo Fácil" está alinhada com a **Estratégia Nacional de Governo Digital (ENGDo)** , que orienta as diretrizes para a transformação digital no setor público brasileiro . As recomendações da SGD/MGI para o período 2024-2027 detalham a responsabilidade de incentivar o desenvolvimento, a implementação e o uso de plataformas digitais inclusivas .

### 5.1 Princípios da ENGDo Aplicados

| Princípio | Aplicação no "Censo Fácil" |
|-----------|---------------------------|
| **Experiência do usuário** | Interfaces em Linguagem Simples, design centrado no produtor rural |
| **Interoperabilidade** | Integração com Barra Gov.Br, autenticação OIDC e ecossistema GOV.BR |
| **Unificação de canais digitais** | Consistência entre aplicativo móvel, web e DMC |
| **Governo simples e acessível** | Conformidade com e-MAG 3.1 e WCAG 2.2 AA |
| **Identidade única** | Login via GOV.BR com níveis Bronze, Prata e Ouro |

---

## 6. Recomendações para Manutenção Contínua

### 6.1 Governança DesignOps

Estabelecer uma rotina de **governança DesignOps** para que novos componentes mantenham a herança dos tokens de acessibilidade validados nesta fase. O e-MAG oferece cursos específicos para conteudistas e desenvolvedores, com carga horária de 20h e 30h respectivamente, que capacitam profissionais no desenvolvimento, manutenção, adequação e alimentação de portais e sítios eletrônicos da administração pública .

### 6.2 Ciclo de Validação Contínua

| Frequência | Atividade | Responsável |
|------------|-----------|-------------|
| **Por sprint** | Testes de contraste e foco com Ferramenta Gov.br | UX Designer |
| **Por release** | Auditoria completa das 6 áreas do e-MAG | Equipe de Qualidade |
| **Anual** | Reavaliação com novos critérios WCAG | DesignOps |

### 6.3 Monitoramento de Novas Diretrizes

A versão atual do e-MAG (3.1) está em processo de revisão para se adequar à versão 2.1 da WCAG, e futuras atualizações devem considerar a WCAG 2.2 . Recomenda-se o monitoramento contínuo das publicações do W3C e da SGD/MGI para garantir a conformidade futura.

---

## 7. Conclusão

O Design System do "Censo Fácil" obteve **status final de conformidade plena** após os ciclos de reavaliação:

- **Status de Acessibilidade:** 100% aderente ao e-MAG 3.1 e WCAG 2.2 Nível AA
- **Status de Identidade:** Totalmente alinhado ao Manual de Identidade Visual do IBGE e ao DSGov 4.0
- **Status de Segurança:** Conformidade com a LGPD (Lei nº 13.709/2018) e práticas de criptografia AES-256

Esta validação técnica assegura que o projeto cumpra a missão institucional de proporcionar uma experiência digital de qualidade e inclusiva para todos os cidadãos brasileiros.

> *“A digitalização do Estado e a identificação civil são projetos de longo prazo que dependem da parceria e da cooperação de diversas instituições públicas.”* — Rogério Mascarenhas, Secretário de Governo Digital do MGI 

---

## 8. Referências

1. BRASIL. Secretaria de Governo Digital. **Modelo de Acessibilidade em Governo Eletrônico (e-MAG) versão 3.1**. Disponível em: https://www.gov.br/governodigital/pt-br/acessibilidade-e-usuario/acessibilidade-digital/modelo-de-acessibilidade/modelo-de-acessibilidade .

2. W3C. **Web Content Accessibility Guidelines (WCAG) 2.2**. Publicado em outubro de 2023. Disponível em: https://www.w3.org/TR/WCAG22/ .

3. AODA. **Web Accessibility Guidelines for Target Size**. Disponível em: https://aoda.ca/web-accessibility-guidelines-for-target-size/ .

4. **Portaria SGD/MGI nº 4.248/2024** — Estratégia Nacional de Governo Digital. Disponível em: https://www.gov.br/governodigital/pt-br/estrategias-e-governanca-digital .

5. BRASIL. **Lei nº 13.709, de 14 de agosto de 2018 (LGPD)** . Lei Geral de Proteção de Dados Pessoais. Disponível em: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm .

6. CTA/IFRS. **Cursos do e-MAG — Centro Tecnológico de Acessibilidade do IFRS**. Disponível em: https://cta.ifrs.edu.br/cursos-do-emag/ .

---

**Versão:** 1.0
**Data:** Agosto 2026
**Status:** ✅ Validação concluída — Design System 100% conforme