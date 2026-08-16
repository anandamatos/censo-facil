# 📑 Guia Prático: Implementação das Diretrizes de Marcação (e-MAG 3.1 + XHTML Estrito)

## Com DSGov e Exemplos Interativos

---

## 1. ESTRUTURA HTML SEMÂNTICA E HIERARQUIA

### 1.1 Elementos de Região e Landmarks

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" 
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" 
      xml:lang="pt" 
      lang="pt">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <title>Censo Fácil – Coleta de Dados</title>
  <!-- DSGov CSS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@govbr-ds/core@latest/dist/core.min.css" />
</head>
<body>
  <!-- HEADER com role="banner" -->
  <header role="banner" class="br-header">
    <div class="container">
      <div class="header-logo">
        <img src="logo-ibge.png" alt="IBGE – Instituto Brasileiro de Geografia e Estatística" />
      </div>
      <!-- Barra Gov.Br integrada -->
      <div class="header-govbr">
        <govbr-bar></govbr-bar>
      </div>
    </div>
  </header>

  <!-- NAVEGAÇÃO com role="navigation" -->
  <nav role="navigation" aria-label="Navegação principal" class="br-navigation">
    <ul>
      <li><a href="#dashboard">Dashboard</a></li>
      <li><a href="#coleta">Coleta</a></li>
      <li><a href="#auditoria">Auditoria</a></li>
    </ul>
  </nav>

  <!-- CONTEÚDO PRINCIPAL com role="main" -->
  <main role="main" id="conteudo-principal" class="container">
    <h1>Censo Agropecuário 2026</h1>
    
    <!-- Seção de Coleta -->
    <section aria-labelledby="titulo-coleta">
      <h2 id="titulo-coleta">Coleta de Dados</h2>
      <!-- Conteúdo da coleta -->
    </section>
  </main>

  <!-- FOOTER com role="contentinfo" -->
  <footer role="contentinfo" class="br-footer">
    <p>© 2026 IBGE – Todos os direitos reservados</p>
  </footer>
</body>
</html>
```

**Explicação:**
- `<header role="banner">`: Define o cabeçalho da página, identificado como região de banner por leitores de tela.
- `<nav role="navigation">`: Marca a área de navegação principal, permitindo que usuários de leitores de tela pulem diretamente para ela.
- `<main role="main">`: Indica o conteúdo principal da página; deve haver apenas um por documento.
- `<footer role="contentinfo">`: Identifica informações de rodapé como metadados da página.
- **`<section aria-labelledby="...">`**: Agrupa conteúdo temático com um título referenciado por `aria-labelledby`, melhorando a navegação por regiões.

---

### 1.2 Hierarquia de Títulos

```html
<!-- ✅ CORRETO – Hierarquia lógica sem saltos -->
<main role="main">
  <h1>Censo Agropecuário 2026</h1>
  <!-- Título principal da página -->
  
  <section aria-labelledby="section1">
    <h2 id="section1">1. Identificação do Estabelecimento</h2>
    <!-- Subtítulo de primeiro nível -->
    
    <article>
      <h3>1.1 Dados do Produtor</h3>
      <!-- Subtítulo de segundo nível -->
      
      <h4>1.1.1 Informações Pessoais</h4>
      <!-- Subtítulo de terceiro nível -->
    </article>
  </section>
  
  <section aria-labelledby="section2">
    <h2 id="section2">2. Uso da Terra</h2>
    <!-- Outro subtítulo de primeiro nível -->
  </section>
</main>
```
```
<!-- ❌ INCORRETO – Saltos de nível -->
<main>
  <h1>Censo Agropecuário 2026</h1>
  <h3>1. Identificação do Estabelecimento</h3>
  <!-- Saltou do h1 para o h3 – confunde leitores de tela -->
  
  <h5>1.1 Dados do Produtor</h5>
  <!-- Saltos adicionais – estrutura quebrada -->
</main>
```

**Explicação:**
- **Hierarquia lógica**: h1 → h2 → h3 → h4 → h5 → h6, sem saltos.
- **Benefício**: Leitores de tela geram um índice da página baseado nos headings, permitindo navegação rápida.
- **Uso de `aria-labelledby`**: Conecta a seção ao seu título, melhorando a compreensão contextual.

---

## 2. LABELS E ASSOCIAÇÕES EM FORMULÁRIOS

### 2.1 Associação Explícita (for/id)

```html
<!-- ✅ CORRETO – Associação explícita com for/id -->
<form id="formulario-coleta" action="#" method="post">
  <!-- Campo de texto -->
  <div class="br-form-group">
    <label for="nome-produtor">Nome completo do produtor</label>
    <input type="text" 
           id="nome-produtor" 
           name="nome_produtor" 
           class="br-input" 
           required="required" 
           aria-required="true" />
  </div>
  
  <!-- Campo de seleção -->
  <div class="br-form-group">
    <label for="tipo-produtor">Tipo de produtor</label>
    <select id="tipo-produtor" name="tipo_produtor" class="br-select">
      <option value="">Selecione...</option>
      <option value="familiar">Agricultura Familiar</option>
      <option value="patronal">Agricultura Patronal</option>
    </select>
  </div>
  
  <!-- Campo com instrução adicional (aria-describedby) -->
  <div class="br-form-group">
    <label for="area-total">Área total do estabelecimento (hectares)</label>
    <span id="instrucao-area" class="br-help-text">
      Informe a área total em hectares. Exemplo: 50,5
    </span>
    <input type="number" 
           id="area-total" 
           name="area_total" 
           class="br-input" 
           step="0.1" 
           aria-describedby="instrucao-area" 
           required="required" />
  </div>
</form>
```
```
<!-- ❌ INCORRETO – Placeholder como único label -->
<div class="br-form-group">
  <input type="text" 
         placeholder="Nome completo do produtor" 
         class="br-input" />
  <!-- ❌ O placeholder desaparece ao digitar e não é vocalizado -->
</div>
```

**Explicação:**
- **`<label for="...">`**: Associa explicitamente o rótulo ao campo; ao clicar no label, o campo recebe foco.
- **`aria-describedby`**: Conecta uma instrução adicional ao campo, lida por leitores de tela.
- **`aria-required="true"`**: Indica campo obrigatório para tecnologias assistivas.
- **Placeholder não substitui label**: O placeholder não é vocalizado consistentemente e desaparece ao digitar.

---

## 3. RIGOR SINTÁTICO E VALIDAÇÃO (XHTML STRICT)

### 3.1 Estrutura XHTML com Fechamento de Tags

```html
<!-- ✅ CORRETO – XHTML Strict com fechamento adequado -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" 
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" 
      xml:lang="pt" 
      lang="pt">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <title>XHTML Strict – Exemplo</title>
</head>
<body>
  <div id="app">
    <!-- Tags de fechamento automático -->
    <img src="icone.png" alt="Ícone de localização" />
    <br />
    <hr />
    
    <!-- Inputs com fechamento -->
    <input type="text" 
           id="nome" 
           name="nome" 
           value="" 
           disabled="disabled" 
           readonly="readonly" />
    <input type="checkbox" 
           id="termos" 
           name="termos" 
           checked="checked" />
    
    <!-- Elementos aninhados corretamente -->
    <ul>
      <li>Item 1</li>
      <li>Item 2</li>
    </ul>
  </div>
</body>
</html>
```
```
<!-- ❌ INCORRETO – HTML permissivo -->
<img src="icone.png" alt="Ícone">
<br>
<input type="text" disabled>
<ul>
  <li>Item 1
  <li>Item 2
</ul>
```

**Explicação:**
- **Fechamento de tags vazias**: `/>` (ex: `<img />`, `<br />`, `<input />`).
- **Atributos booleanos explícitos**: `disabled="disabled"`, `checked="checked"`.
- **Case-sensitive**: Todas as tags e atributos em **letras minúsculas**.
- **Aninhamento correto**: Tags abertas e fechadas na ordem inversa (ex: `<ul><li>...</li></ul>`).

---

### 3.2 Seções CDATA para Scripts

```html
<!-- ✅ CORRETO – Script com CDATA protegido -->
<script type="text/javascript">
/* <![CDATA[ */
  // O parser XML trata a seção CDATA como texto literal
  function validarPrecisao(HDOP) {
    // Operadores < e && não causam erro no parser XML
    if (HDOP < 5.0 && HDOP > 0) {
      console.log("Precisão ótima: " + HDOP);
    } else {
      console.log("Precisão insuficiente: " + HDOP);
    }
  }
/* ]]> */
</script>
```
```
<!-- ❌ INCORRETO – Script sem CDATA -->
<script type="text/javascript">
  // O parser XML interpreta o '<' como início de uma tag
  if (HDOP < 5.0 && HDOP > 0) {
    // ❌ ERRO: '>' e '<' causam falha de parsing
  }
</script>
```

**Explicação:**
- **CDATA protege caracteres especiais**: `<`, `>`, `&` são interpretados como texto literal.
- **Comentários `/* ... */`**: Ocultam as tags CDATA de navegadores que não as reconhecem.
- **Necessário para XHTML**: Evita erros fatais de parsing no motor XML.

---

## 4. ATRIBUTOS DE ACESSIBILIDADE (WAI-ARIA)

### 4.1 Componente br-gnss-tracker com Região Viva (`aria-live`)

```html
<!-- Componente de captura GNSS com ARIA -->
<div class="br-card" role="region" aria-labelledby="gnss-title">
  <h3 id="gnss-title">Captura de Coordenadas GNSS</h3>
  
  <!-- Região viva para atualizações de precisão -->
  <div aria-live="polite" aria-atomic="true" class="gnss-status">
    <span id="status-hdop" class="status-indicator status-ok">
      ✅ Precisão: Ótima (HDOP: 2.1)
    </span>
  </div>
  
  <!-- Barra de progresso com ARIA -->
  <div role="progressbar" 
       aria-valuenow="85" 
       aria-valuemin="0" 
       aria-valuemax="100" 
       class="progress-bar"
       aria-label="Progresso da captura de sinal">
    <span class="progress-fill" style="width:85%"></span>
    <span class="progress-text">85%</span>
  </div>
  
  <!-- Botão com ARIA -->
  <button type="button" 
          class="br-button primary" 
          aria-label="Iniciar captura de coordenadas" 
          id="btn-capturar">
    📡 Capturar
  </button>
</div>
```

**Explicação:**
- **`aria-live="polite"`**: Atualizações são anunciadas após a conclusão da interação atual.
- **`aria-atomic="true"`**: A região inteira é lida quando atualizada.
- **`role="progressbar"`**: Identifica o elemento como barra de progresso.
- **`aria-valuenow` / `aria-valuemin` / `aria-valuemax`**: Valores numéricos da barra de progresso.
- **`aria-label`**: Fornece um nome acessível para elementos sem texto visível.

---

### 4.2 Componente Expansível com `aria-expanded`

```html
<!-- Componente de ajuda expansível -->
<div class="br-accordion">
  <button type="button" 
          class="br-accordion-header" 
          aria-expanded="false" 
          aria-controls="ajuda-gnss" 
          id="btn-ajuda-gnss">
    📖 Como funciona a captura de coordenadas?
  </button>
  
  <div class="br-accordion-content" 
       id="ajuda-gnss" 
       role="region" 
       aria-labelledby="btn-ajuda-gnss" 
       hidden="hidden">
    <p>A captura de coordenadas utiliza o receptor GNSS integrado ao DMC.</p>
    <ul>
      <li><strong>HDOP &lt; 5.0</strong>: Precisão ótima (verde)</li>
      <li><strong>HDOP 5.0-10.0</strong>: Precisão aceitável (amarelo)</li>
      <li><strong>HDOP &gt; 10.0</strong>: Precisão insuficiente (vermelho)</li>
    </ul>
  </div>
</div>

<script>
  // Controle do estado expansível com ARIA
  const btn = document.getElementById('btn-ajuda-gnss');
  const content = document.getElementById('ajuda-gnss');
  
  btn.addEventListener('click', function() {
    const expanded = this.getAttribute('aria-expanded') === 'true';
    this.setAttribute('aria-expanded', !expanded);
    content.hidden = expanded;
  });
</script>
```

**Explicação:**
- **`aria-expanded`**: Indica se o conteúdo expansível está visível (`true`) ou oculto (`false`).
- **`aria-controls`**: Conecta o botão ao conteúdo que ele controla.
- **`role="region"`**: Identifica a área do conteúdo expansível.
- **`aria-labelledby`**: Associado ao botão que controla a região.

---

## 5. RESUMO: CHECKLIST DE MARCAÇÃO

| Diretriz | Critério | Status |
|----------|----------|--------|
| **Declaração de Idioma** | `lang` e `xml:lang` no `<html>` | ✅ Conforme |
| **Estrutura de Regiões** | `<header>`, `<nav>`, `<main>`, `<footer>` | ✅ Conforme |
| **Landmarks** | `role="banner"`, `role="navigation"`, `role="main"`, `role="contentinfo"` | ✅ Conforme |
| **Hierarquia de Títulos** | h1 → h2 → h3... sem saltos | ✅ Conforme |
| **Encapsulamento de Texto** | Texto em `<p>` ou `<div>`, não diretamente no `<body>` | ✅ Conforme |
| **Fechamento de Tags** | `<br />`, `<img />`, `<input />` | ✅ Conforme |
| **Case Sensitivity** | Tags e atributos em minúsculas | ✅ Conforme |
| **Atributos Booleanos** | `disabled="disabled"`, `checked="checked"` | ✅ Conforme |
| **Associação Label/ID** | `<label for="id">` e `<input id="id">` | ✅ Conforme |
| **Vedação de Placeholders** | `placeholder` não substitui label | ✅ Conforme |
| **Agrupamento Lógico** | `<fieldset>` e `<legend>` para grupos | ✅ Conforme |
| **Seções CDATA** | Scripts com `/* <![CDATA[ */` | ✅ Conforme |
| **WAI-ARIA** | `aria-live`, `aria-expanded`, `aria-controls`, `role` | ✅ Conforme |
| **Unicidade de IDs** | IDs únicos em todo o documento | ✅ Conforme |

---

## 📚 Referências

| Documento | Link |
|-----------|------|
| **e-MAG 3.1 – Área de Marcação** | https://emag.governoeletronico.gov.br/ |
| **DSGov – Componentes** | https://www.gov.br/ds/componentes/visao-geral |
| **WCAG 2.2 – Guideline 1.3** | https://www.w3.org/TR/WCAG22/#adaptable |
| **W3C XHTML 1.0 Strict** | https://www.w3.org/TR/xhtml1/ |
| **WAI-ARIA Authoring Practices** | https://www.w3.org/WAI/ARIA/apg/ |

---

*Este guia serve como referência prática para a implementação das diretrizes de marcação do e-MAG 3.1 no "Censo Fácil", garantindo conformidade com o edital do IBGE 2026 e acessibilidade para todos os usuários.*