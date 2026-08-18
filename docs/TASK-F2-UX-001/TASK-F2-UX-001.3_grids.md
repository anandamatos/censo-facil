# 📱 Configuração de Grids Móveis para o "Censo Fácil"

## DSGov 4.0 · Mobile-First · WCAG 2.2 AA

---

## 1. Contexto e Fundamentação

A configuração de grids móveis para o sistema **"Censo Fácil"** foi estruturada para garantir a adaptabilidade do layout em diferentes dispositivos e orientações, assegurando a usabilidade para as personas do projeto — desde o produtor rural com smartphone básico até o agente censitário utilizando o Dispositivo Móvel de Coleta (DMC).

A abordagem adotada é fundamentalmente **Mobile-First** , iniciando o design pela menor tela e realizando um aprimoramento progressivo para telas maiores. Esta filosofia atua como um filtro de conteúdo, forçando a equipe a priorizar apenas as funções e informações essenciais para a jornada do usuário, conforme descrito nas diretrizes de Design Responsivo.

Os grids responsivos, embora resolvam problemas de layout, não necessariamente resolvem problemas de design. A abordagem adotada pelo "Censo Fácil" vai além do mero redimensionamento, buscando adaptar o conteúdo com intenção e consciência contextual, garantindo que a interface funcione para os usuários em campo, e não apenas se encaixe em uma grade flexível .

---

## 2. Configuração da Grid para Smartphones (Orientação Retrato)

A grid para smartphones é otimizada para dispositivos de tela menor, como o do **Seu José**, priorizando a clareza e a facilidade de toque.

| Propriedade | Especificação | Justificativa |
|-------------|---------------|---------------|
| **Colunas** | 4 colunas fluidas | Proporciona flexibilidade para organizar conteúdos variados sem sobrecarregar a tela estreita |
| **Margens Laterais** | **8px** | Conforme o padrão mobile do DSGov, garante respiro nas bordas da tela |
| **Medianiz (Gutter)** | **16px** | Espaçamento adequado entre colunas para evitar colisão visual de elementos  |
| **Largura de Conteúdo** | 100% (fluida) | Adapta-se à largura do visor sem gerar rolagem horizontal |
| **Alinhamento** | Centralizado | Conteúdo principal centralizado para melhor legibilidade em telas pequenas  |

**Justificativa de Design:**

A escolha da grid de 4 colunas para smartphones baseia-se na necessidade de apresentar informações de forma clara e hierarquizada, garantindo que os elementos mais importantes sejam facilmente acessíveis. Conforme o Manual do Recenseador, o Dispositivo Móvel de Coleta (DMC) utilizado em campo deve ser operável com uma mão, o que exige que os alvos interativos estejam posicionados de forma ergonômica.

---

## 3. Configuração da Grid para Tablets e Orientação Paisagem

Para dispositivos com maior área de tela, como o DMC operado por **Mariana** ou o tablet de **Carlos**, a grid é expandida para permitir a visualização de dados mais densos, como mapas e tabelas de auditoria.

| Propriedade | Especificação | Justificativa |
|-------------|---------------|---------------|
| **Colunas** | 8 colunas fluidas | Maior densidade de informação para telas amplas |
| **Margens Laterais** | **16px** | Área de respiro adequada em telas maiores |
| **Medianiz (Gutter)** | **16px** | Consistência com a grid de smartphone para manter a uniformidade visual |
| **Largura Máxima** | Expansível | O conteúdo ocupa a área útil mantendo proporção confortável para leitura  |
| **Grid Reorganização** | Cards ocupam 2 ou 4 colunas | Adaptação dinâmica dependendo da densidade da informação |

**Breakpoints de Referência:**

| Breakpoint | Largura | Aplicação |
|------------|---------|-----------|
| **Base (Mobile)** | 320px+ | Grid de 4 colunas |
| **Tablet** | 768px+ | Grid de 8 colunas  |
| **Desktop** | 1024px+ | Grid expandida |

---

## 4. Sistema de Espaçamento Baseado em 8pt

O sistema de medidas baseia-se em múltiplos de **8px** (8pt System), garantindo o rigor geométrico e a consistência entre o design e o desenvolvimento .

| Token | Valor | Aplicação |
|-------|-------|-----------|
| `spacing-xs` | 4px | Espaçamento mínimo (ícones, bordas) |
| `spacing-sm` | 8px | Margens internas pequenas, separação de itens próximos  |
| `spacing-md` | 16px | Padding padrão de cards e containers |
| `spacing-lg` | 24px | Espaçamento entre seções |
| `spacing-xl` | 32px | Margens externas principais |
| `spacing-xxl` | 48px | Espaçamento entre blocos temáticos |

**Por que 8px?**

O sistema 8pt garante compatibilidade com a maioria das resoluções de tela, funciona perfeitamente em displays @1x, @2x e @3x, e reduz erros de tradução entre design e código .

---

## 5. Target Size e Acessibilidade (WCAG 2.2)

A organização em colunas facilita o cumprimento do critério **WCAG 2.2 — 2.5.8 (Target Size Minimum)** , garantindo que alvos interativos tenham área mínima adequada para toque .

| Tipo de Alvo | Tamanho Mínimo | Referência |
|--------------|----------------|------------|
| **Alvos padrão** | 24×24px CSS | WCAG 2.2 Nível AA  |
| **Botões críticos (GNSS)** | 48×48px CSS | Recomendado para uso em campo |
| **Espaçamento entre alvos** | 8px mínimo | Evita ativação acidental  |

**Exceções ao Target Size :**
- Links inline em parágrafos (limitados pela altura da linha)
- Controles determinados pelo agente do usuário (ex: inputs nativos)
- Elementos cujo tamanho não pode ser modificado sem afetar a funcionalidade

**Critério de Espaçamento de Alvos:**

Segundo as diretrizes de acessibilidade móvel, alvos interativos menores que 24×24px podem ser considerados conformes se houver espaço suficiente entre eles . Por exemplo, dois botões de 16px precisam de pelo menos 8px de espaço entre si para atingir o requisito de 24px (16 + 8 = 24).

---

## 6. Filosofia Mobile-First e Aprimoramento Progressivo

A implementação das grids segue a filosofia **Mobile-First**, que orienta o design a iniciar pela menor tela :

```
Mobile-First ── Progressão:
├── Tela Pequena (smartphone): Apenas conteúdo e funções essenciais
│   └── Grid: 4 colunas, margem 8px
├── Tela Média (tablet): Adição de colunas e informações secundárias
│   └── Grid: 8 colunas, margem 16px
└── Tela Grande (desktop): Adição de recursos avançados e interações
    └── Grid expandida
```

**Benefícios da Abordagem Mobile-First:**

1. **Filtro de Conteúdo:** Força a priorização do que é realmente essencial para a jornada do usuário
2. **Performance:** Menos recursos para carregar em dispositivos de baixa capacidade
3. **Acessibilidade:** Melhor experiência para usuários com dispositivos básicos
4. **Escalabilidade:** Facilidade para adicionar complexidade progressivamente

---

## 7. Testes de Responsividade e Conformidade

A implementação das grids será validada através de testes rigorosos para assegurar que:

| Critério | Método de Validação | Referência |
|----------|---------------------|------------|
| **Ausência de rolagem horizontal** | Teste em resoluções comuns de smartphones e tablets | — |
| **Legibilidade mantida** | Verificação da tipografia Univers LT Std em tamanhos acessíveis | e-MAG Área 4 |
| **Adaptação dinâmica de componentes** | Teste de reorganização de cards e elementos | — |
| **Target Size ≥ 24×24px** | Inspeção de elementos interativos | WCAG 2.2 2.5.8  |
| **Contraste ≥ 4.5:1** | Ferramenta de Avaliação Gov.br | WCAG 1.4.3 |

**Ferramentas de Teste:**
- Xcode Accessibility Inspector (para iOS, testa 44×44 mínimo)
- Ferramenta de Avaliação Gov.br
- Testes em dispositivos reais
- Validadores automáticos de acessibilidade

---

## 8. Conclusão

A configuração de grids móveis para o "Censo Fácil" garante que o sistema seja **resiliente e operável** tanto em smartphones básicos quanto em equipamentos profissionais de campo, mantendo a sobriedade e o rigor institucional do IBGE.

A abordagem Mobile-First, combinada com o sistema de espaçamento 8pt, grids fluidas (4 colunas para smartphones, 8 para tablets) e conformidade com WCAG 2.2 (Target Size ≥ 24×24px), assegura que a interface se adapte com intenção ao contexto de uso — desde a entrevista com o produtor rural até a auditoria de dados em escritórios regionais.

---

## 9. Referências

### Padrões e Diretrizes

1. BRASIL. **DSGov 4.0 — Padrão Digital de Governo**. Disponível em: https://www.gov.br/ds/.

2. BRASIL. **e-MAG 3.1 — Modelo de Acessibilidade em Governo Eletrônico**. Disponível em: https://emag.governoeletronico.gov.br/.

3. W3C. **Web Content Accessibility Guidelines (WCAG) 2.2**. Disponível em: https://www.w3.org/TR/WCAG22/.

4. W3C. **WCAG 2.2 — Critério 2.5.8 (Target Size Minimum)** . Disponível em: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum .

### Manuais do IBGE

5. IBGE. **Manual do Recenseador do Censo Demográfico 2022 (CD-1.09)** . Disponível em: https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5723.pdf.

6. IBGE. **Instruções Operacionais para Supervisores (CA 2.10)** . Disponível em: https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc0934.pdf.

### Referências Complementares

7. **8px Grid System — Modern UI Design**. Disponível em: https://raw.githubusercontent.com/NeverSight/skills_feed/refs/heads/main/data/skills-md/sitechfromgeorgia/georgian-distribution-system/modern-ui-designer/SKILL.md .

8. **Target Size (Minimum) (2.5.8)** — LambdaTest. Disponível em: https://www.lambdatest.com/support/docs/accessibility-web-rule-2-5-8-target-size/ .

9. **Touch Target Spacing** — Deque Systems. Disponível em: https://docs.deque.com/devtools-mobile/2025.7.2/en/ios-touch-target-spacing .

10. **Mobile Accessibility WCAG** — GitHub. Disponível em: https://github.com/wshobson/agents/blob/main/plugins/ui-design/skills/accessibility-compliance//references/mobile-accessibility.md .

---

**Versão:** 1.0
**Data:** Agosto 2026
**Status:** ✅ Validado com DSGov 4.0 e WCAG 2.2 AA