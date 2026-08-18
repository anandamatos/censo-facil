# 🎨 Mapeamento de Design Tokens para o "Censo Fácil"

## DSGov 4.0, Manual de Identidade Visual IBGE e Acessibilidade

---

## 1. Contexto e Fundamentação

O mapeamento de Design Tokens para o sistema **"Censo Fácil"** estabelece a ponte entre a identidade visual institucional do IBGE e os padrões de Governo Digital, materializando a conformidade com o **Manual de Identidade Visual (MIV) do IBGE** e as diretrizes do **DSGov 4.0**.

O IBGE, como instituição produtora de estatísticas oficiais que retratam a realidade brasileira, exige que sua identidade visual transmita **seriedade, precisão e credibilidade** — atributos essenciais para manter a confiança da população nos dados coletados. A aplicação uniforme dos elementos visuais torna a imagem do Instituto familiar aos usuários, fortalecendo sua presença institucional .

A base deste mapeamento considera três pilares fundamentais:

| Pilar | Referência | Impacto no Design System |
|-------|------------|--------------------------|
| **Identidade Institucional** | Manual de Identidade Visual do IBGE | Cores, tipografia e elementos de marca |
| **Padrões de Governo Digital** | DSGov 4.0 | Componentes reutilizáveis, grids e acessibilidade |
| **Acessibilidade e Inclusão** | e-MAG 3.1 e WCAG 2.2 AA | Contraste, legibilidade e operabilidade |
| **Privacidade e Sigilo** | Lei nº 5.534/68 e LGPD | Proteção de dados e sigilo estatístico |

A **Lei nº 5.534/68** estabelece o caráter sigiloso das informações prestadas ao IBGE, que serão usadas exclusivamente para fins estatísticos e não poderão servir de prova em processos administrativos, fiscais ou judiciais . Este princípio orienta a abordagem de segurança dos dados no Design System, garantindo que a interface reflita o compromisso institucional com a confidencialidade.

---

## 2. Mapeamento de Cores

### 2.1 Paleta Institucional Primária

A cor primária absoluta do sistema é o **Azul IBGE**, fundamental para transmitir a credibilidade e autoridade do Instituto em campo .

| Token | Referência IBGE | Valor | Aplicação DSGov |
|-------|-----------------|-------|-----------------|
| `color-primary-pure` | **Azul IBGE 286 C** | HEX `#0033A0` | Navegação primária, botões de ação, títulos institucionais |
| `color-primary-dark` | Azul IBGE 286 C (escuro) | HEX `#002680` | Hover e estados ativos |
| `color-primary-light` | Azul IBGE 286 C (claro) | HEX `#3366CC` | Fundos de destaque e elementos secundários |

**Especificações Técnicas:**
- **Pantone:** 286 C
- **CMYK:** 100/80/0/12
- **RGB:** 0/51/160
- **HEX:** `#0033A0`

### 2.2 Paleta Neutra e Funcional

| Token | Valor HEX | Aplicação |
|-------|-----------|-----------|
| `color-secondary-pure` | `#FFFFFF` | Fundo de telas, áreas de conteúdo limpo |
| `color-neutral-light` | `#F5F5F5` | Fundo de cards, separadores secundários |
| `color-neutral-medium` | `#C5D4EB` | Bordas, divisores e áreas inativas |
| `color-neutral-dark` | `#071D41` | Textos principais e cabeçalhos |
| `color-text-primary` | `#1C1C1E` | Corpo de texto principal (contraste ≥ 4.5:1) |
| `color-text-secondary` | `#555770` | Textos auxiliares e legendas |

### 2.3 Paleta Semântica (Feedback e Estados)

| Token | Cor | HEX | Aplicação |
|-------|-----|-----|-----------|
| `color-success` | Verde IBGE | `#4CAF50` | Indicador de precisão GNSS ótima (HDOP ≤ 2.5m), confirmações |
| `color-warning` | Amarelo | `#F5A623` | Alertas de precisão aceitável, pendências de coleta |
| `color-error` | Vermelho | `#E53935` | Erros críticos, bloqueio de registro GNSS (HDOP > 5.0m) |
| `color-info` | Azul Claro | `#2196F3` | Informações contextuais e dicas |

**Critério de Contraste:**
Todos os tokens de texto devem respeitar a razão mínima de **4.5:1** contra o fundo, garantindo a legibilidade em condições de luz solar intensa, conforme exigido pelo e-MAG 3.1 (Área de Apresentação/Design) e pela WCAG 2.2 (Critério 1.4.3).

---

## 3. Mapeamento de Tipografia

### 3.1 Família Tipográfica Oficial

Conforme o Manual de Identidade Visual do IBGE, o sistema utiliza a família **Univers** para toda a interface de usuário, reservando fontes específicas apenas para a marca gráfica do projeto .

| Token de Família | Peso / Estilo | Aplicação na UI |
|------------------|---------------|-----------------|
| `font-family-base` | **Univers 55 Roman** | Corpo de texto, parágrafos, legendas informativas |
| `font-family-bold` | **Univers 65 Bold** | Títulos de seções, rótulos de campos, botões |
| `font-family-italic` | **Univers 55 Oblique** | Notas explicativas, citações de manuais |
| `font-family-bold-italic` | **Univers 65 Bold Oblique** | Títulos com ênfase adicional |

### 3.2 Escala Tipográfica

A escala tipográfica foi definida com base nas diretrizes de legibilidade do e-MAG e nas recomendações do DSGov para interfaces governamentais:

| Token | Tamanho | Peso | Aplicação |
|-------|---------|------|-----------|
| `text-heading-1` | 2.5rem (40px) | Bold | Títulos de página (h1) |
| `text-heading-2` | 1.5rem (24px) | Bold | Títulos de seção (h2) |
| `text-heading-3` | 1.125rem (18px) | Bold | Subtítulos (h3) |
| `text-body-large` | 1rem (16px) | Regular | Corpo de texto principal |
| `text-body-small` | 0.875rem (14px) | Regular | Textos auxiliares, legendas |
| `text-label` | 0.75rem (12px) | Medium | Rótulos de campos e botões |
| `text-caption` | 0.625rem (10px) | Regular | Informações complementares |

**Legibilidade Mínima:** O texto corporal utiliza o tamanho de **16px (1rem)** para assegurar a legibilidade mínima exigida pelo e-MAG .

### 3.3 Família da Logomarca

A tipografia **Neuropolitical** é utilizada **exclusivamente** na logomarca do IBGE e suas variações, conferindo à marca um caráter técnico e contemporâneo, mas com uso restrito ao logotipo, não devendo ser aplicada em textos ou elementos gráficos complementares.

---

## 4. Espaçamento e Grid

### 4.1 Sistema de Medidas (8pt System)

O sistema de medidas baseia-se em múltiplos de **8px** (8pt System), garantindo o rigor geométrico e a consistência entre o design e o desenvolvimento .

| Token | Valor | Aplicação |
|-------|-------|-----------|
| `spacing-xs` | 4px | Espaçamento mínimo entre elementos |
| `spacing-sm` | 8px | Margens internas pequenas |
| `spacing-md` | 16px | Padding padrão de cards e containers |
| `spacing-lg` | 24px | Espaçamento entre seções |
| `spacing-xl` | 32px | Margens externas principais |
| `spacing-xxl` | 48px | Espaçamento entre blocos temáticos |

### 4.2 Grids Responsivas

| Dispositivo | Colunas | Margem Lateral | Medianiz | Aplicação |
|-------------|---------|----------------|----------|-----------|
| **Smartphone (retrato)** | 4 | 8px | 16px | Produtor rural (Seu José) |
| **Tablet (paisagem)** | 8 | 16px | 16px | Recenseadora (Mariana) / ACQ (Carlos) |

### 4.3 Target Size (Área de Toque)

Conforme o critério **WCAG 2.2 (2.5.8 – Target Size)** , os alvos interativos devem ter:

| Tipo | Tamanho Mínimo | Observação |
|------|----------------|------------|
| **Alvos padrão** | 24x24px CSS | Mínimo exigido pela WCAG |
| **Botões críticos no DMC** | 48x48px | Recomendado para facilitar o uso em campo |

---

## 5. Estados de Interação e Acessibilidade

### 5.1 Estados de Interação

| Estado | Token | Aplicação |
|--------|-------|-----------|
| **Default** | `color-primary-pure` | Estado padrão de botões e links |
| **Hover** | `color-primary-dark` | Indicação de interatividade ao passar o mouse |
| **Focus** | Indicador com contraste 3:1 | Visibilidade do foco de teclado (WCAG 2.4.11) |
| **Active** | `color-primary-light` | Estado durante o clique/toque |
| **Disabled** | Opacidade reduzida (40%) | Campos e botões desativados |
| **Loading** | Indicador de progresso | Feedback de processamento |

### 5.2 Acessibilidade Visual

| Critério | Especificação | Referência |
|----------|---------------|------------|
| **Contraste mínimo** | 4.5:1 para texto normal | WCAG 1.4.3 |
| **Contraste mínimo** | 3:1 para texto grande (≥18pt) | WCAG 1.4.3 |
| **Foco visível** | Indicador com contraste ≥ 3:1 | WCAG 2.4.11 |
| **Não obscurecimento** | Foco não ocultado pela Barra Gov.Br | WCAG 2.4.11 |

### 5.3 Elevação e Sombras

| Token | Valor | Aplicação |
|-------|-------|-----------|
| `elevation-sm` | Box-shadow: 0 2px 4px rgba(0,0,0,0.08) | Cards e containers |
| `elevation-md` | Box-shadow: 0 4px 12px rgba(19,81,180,0.08) | Cards em hover |
| `elevation-lg` | Box-shadow: 0 8px 24px rgba(0,0,0,0.12) | Modais e overlays |

---

## 6. Validação e Conformidade

### 6.1 Critérios de Validação

| Critério | Ferramenta/Método | Frequência |
|----------|-------------------|------------|
| **Contraste de cores** | Ferramenta de Avaliação Gov.br | Por sprint |
| **Conformidade DSGov** | Revisão manual + ferramenta | Por release |
| **Acessibilidade** | Testes com leitores de tela (NVDA, JAWS) | Por sprint |
| **LGPD e Sigilo** | Auditoria de dados | Por release |

### 6.2 Justificativa de Decisões de Design

As decisões de Design Tokens foram orientadas pelos seguintes princípios:

1. **Identidade Institucional:** Manutenção do Azul IBGE como cor primária, transmitindo credibilidade e autoridade.
2. **Padronização:** Adoção do sistema 8pt para garantir consistência entre design e desenvolvimento.
3. **Acessibilidade:** Priorização de contraste mínimo e áreas de toque adequadas para usuários com baixa visão e em condições de campo.
4. **Conformidade Legal:** Alinhamento com a Lei nº 5.534/68 (sigilo estatístico) e com a LGPD .

### 6.3 Entrega e Documentação

Os tokens foram consolidados para implementação via:

- **Web Components nativos:** Utilizando o manifesto CEM para documentação técnica
- **Figma:** Tokens disponíveis como variáveis de design
- **CSS:** Tokens disponíveis como variáveis CSS customizadas (`var(--color-primary-pure)`)

A conformidade final deve ser validada com a **Ferramenta de Avaliação Gov.br**, garantindo a aderência aos padrões de acessibilidade e sigilo estatístico exigidos pelo IBGE.

---

## 7. Referências

### Documentos Institucionais
1. IBGE. **Manual de Identidade Visual do IBGE**. Disponível em: https://www.ibge.gov.br.
2. IBGE. **Política de Comunicação do IBGE (2ª edição, 2016)**. Disponível em: https://www.ibge.gov.br/np_download/novoportal/documentos_institucionais/politica_de_comunicacao_2ed_2016.pdf.

### Padrões de Governo Digital
3. BRASIL. **DSGov 4.0 – Padrão Digital de Governo**. Disponível em: https://www.gov.br/ds/.
4. BRASIL. **e-MAG 3.1 – Modelo de Acessibilidade em Governo Eletrônico**. Disponível em: https://emag.governoeletronico.gov.br/.

### Normas de Acessibilidade
5. W3C. **Web Content Accessibility Guidelines (WCAG) 2.2**. Disponível em: https://www.w3.org/TR/WCAG22/.

### Legislação
6. BRASIL. **Lei nº 5.534, de 14 de novembro de 1968**. Dispõe sobre o sigilo das informações prestadas ao IBGE. Disponível em: https://www.planalto.gov.br/ccivil_03/leis/l5534.htm.
7. BRASIL. **Lei nº 13.709, de 14 de agosto de 2018 (LGPD)**. Lei Geral de Proteção de Dados Pessoais. Disponível em: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm.

### Referências Complementares
8. **IBGE – Sala de Acesso a Dados Restritos (SAR)**. Disponível em: https://www.ibge.gov.br/acesso-informacao/sala-de-acesso-a-dados-restritos.html.
9. **Custom Elements Manifest Specification**. Disponível em: https://github.com/webcomponents/custom-elements-manifest.

---

**Versão:** 1.0
**Data:** Agosto 2026
**Status:** ✅ Validado com DSGov 4.0 e Manual de Identidade Visual do IBGE