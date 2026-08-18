# 📊 Diagramas de Arquitetura da Informação – Projeto "Censo Fácil"

## Visualização Estrutural dos Sistemas de Organização, Rotulagem e Navegação

---

## 1. DIAGRAMA DE HIERARQUIA DO QUESTIONÁRIO

### 1.1 Estrutura Geral do Questionário

```mermaid
graph TD
    subgraph "Questionário Censo Agropecuário"
        A[Início da Coleta] --> B{Classificação do Estabelecimento}
        B -->|Pequeno/Subsistência| C[Questionário Básico]
        B -->|Médio/Grande/ Alta Tecnologia| D[Questionário Completo]
        
        C --> C1[Identificação]
        C --> C2[Produtor e Posse]
        C --> C3[Uso da Terra]
        C --> C4[Produção Vegetal]
        C --> C5[Efetivo da Pecuária]
        C --> C6[Pessoal Ocupado]
        
        D --> D1[Identificação]
        D --> D2[Produtor e Posse]
        D --> D3[Uso da Terra]
        D --> D4[Produção Vegetal]
        D --> D5[Efetivo da Pecuária]
        D --> D6[Pessoal Ocupado]
        D --> D7[Insumos e Práticas]
        D --> D8[Recursos Hídricos]
        D --> D9[Energia e Conectividade]
        D --> D10[Mecanização]
        D --> D11[Gestão Financeira]
    end
    
    style A fill:#0033A0,color:#fff
    style B fill:#f5a623,color:#fff
    style C fill:#4CAF50,color:#fff
    style D fill:#2196F3,color:#fff
```

### 1.2 Detalhamento dos Módulos do Questionário Completo

```mermaid
graph LR
    subgraph "Módulos do Questionário Completo"
        QC1[Identificação<br/>e Localização] --> QC2[Produtor<br/>e Posse]
        QC2 --> QC3[Uso da Terra<br/>e Culturas]
        QC3 --> QC4[Pecuária<br/>e Extrativismo]
        QC4 --> QC5[Insumos e<br/>Práticas Agrícolas]
        QC5 --> QC6[Recursos<br/>Hídricos]
        QC6 --> QC7[Energia e<br/>Conectividade]
        QC7 --> QC8[Mecanização<br/>e Maquinário]
        QC8 --> QC9[Gestão<br/>Financeira]
    end
    
    style QC1 fill:#0033A0,color:#fff
    style QC2 fill:#0033A0,color:#fff
    style QC3 fill:#0033A0,color:#fff
    style QC4 fill:#0033A0,color:#fff
    style QC5 fill:#0033A0,color:#fff
    style QC6 fill:#0033A0,color:#fff
    style QC7 fill:#0033A0,color:#fff
    style QC8 fill:#0033A0,color:#fff
    style QC9 fill:#0033A0,color:#fff
```

---

## 2. MATRIZ LATCH – ORGANIZAÇÃO DOS DADOS

### 2.1 Diagrama dos 5 Princípios LATCH

```mermaid
mindmap
  root((LATCH<br/>Organização))
    Location
      Coordenadas GNSS
      Endereço formal
      Setor censitário
      Município/UF
    Alphabet
      Glossário de termos
      Índice de busca ACQ
      Lista de culturas
      Lista de insumos
    Time
      Ano agrícola de referência
      Safras e períodos
      Histórico de produção
    Category
      Produção Vegetal
      Produção Animal
      Produção Florestal
      Produção Aquícola
    Hierarchy
      Identificação → Geral
      Uso da terra → Detalhamento
      Insumos → Gestão
      Balanços → Financeiro
```

### 2.2 Aplicação Prática do LATCH no Questionário

```mermaid
graph TD
    subgraph "Aplicação LATCH por Tipo de Dado"
        D1[Dados de Localização] --> L1[Location]
        D2[Listas e Catálogos] --> L2[Alphabet]
        D3[Dados Temporais] --> L3[Time]
        D4[Agrupamentos Temáticos] --> L4[Category]
        D5[Fluxo de Preenchimento] --> L5[Hierarchy]
    end
    
    L1 --> A[Coordenadas GNSS]
    L1 --> B[Endereço e CNEFE]
    
    L2 --> C[Culturas e Insumos]
    L2 --> D[Glossário de Termos]
    
    L3 --> E[Ano Agrícola]
    L3 --> F[Períodos de Safra]
    
    L4 --> G[Vegetal / Animal]
    L4 --> H[Florestal / Aquícola]
    
    L5 --> I[Identificação → Uso → Gestão]
    L5 --> J[Geral → Específico]
    
    style L1 fill:#0033A0,color:#fff
    style L2 fill:#0033A0,color:#fff
    style L3 fill:#0033A0,color:#fff
    style L4 fill:#0033A0,color:#fff
    style L5 fill:#0033A0,color:#fff
```

---

## 3. SISTEMA DE ROTULAGEM – TRADUÇÃO PARA LINGUAGEM SIMPLES

### 3.1 Mapeamento de Rótulos Técnicos → Linguagem Simples

```mermaid
graph TD
    subgraph "Tradução de Rótulos"
        T1[Localização/CNEFE] -->|Linguagem Simples| R1["📍 Onde fica a terra?"]
        T2[Pessoal Ocupado] -->|Linguagem Simples| R2["👨‍🌾 Quem trabalha com você?"]
        T3[Efetivo da Pecuária] -->|Linguagem Simples| R3["🐄 Criação de animais"]
        T4[Produção Vegetal] -->|Linguagem Simples| R4["🌱 Lavouras e Plantações"]
        T5[Recursos Hídricos] -->|Linguagem Simples| R5["💧 Uso da água"]
        T6[Gestão Financeira] -->|Linguagem Simples| R6["💰 Contas e receitas"]
        T7[Insumos e Práticas] -->|Linguagem Simples| R7["🧪 Como você planta?"]
    end
    
    style T1 fill:#4a5568,color:#fff
    style T2 fill:#4a5568,color:#fff
    style T3 fill:#4a5568,color:#fff
    style T4 fill:#4a5568,color:#fff
    style T5 fill:#4a5568,color:#fff
    style T6 fill:#4a5568,color:#fff
    style T7 fill:#4a5568,color:#fff
    
    style R1 fill:#0033A0,color:#fff
    style R2 fill:#0033A0,color:#fff
    style R3 fill:#0033A0,color:#fff
    style R4 fill:#0033A0,color:#fff
    style R5 fill:#0033A0,color:#fff
    style R6 fill:#0033A0,color:#fff
    style R7 fill:#0033A0,color:#fff
```

### 3.2 Glossário de Termos Técnicos

```mermaid
flowchart LR
    subgraph "Glossário de Termos"
        G1[EFETIVO] -->|Significa| G1R["Cabeças de animais<br/>(gado, porcos, aves)"]
        G2[CNEFE] -->|Significa| G2R["Cadastro Nacional<br/>de Endereços"]
        G3[HDOP] -->|Significa| G3R["Precisão do sinal<br/>de satélite"]
        G4[ALQUEIRE] -->|Significa| G4R["Medida de terra<br/>(~2,42 hectares)"]
        G5[MÓDULO FISCAL] -->|Significa| G5R["Tamanho mínimo<br/>de terra produtiva"]
    end
    
    style G1 fill:#4a5568,color:#fff
    style G2 fill:#4a5568,color:#fff
    style G3 fill:#4a5568,color:#fff
    style G4 fill:#4a5568,color:#fff
    style G5 fill:#4a5568,color:#fff
    
    style G1R fill:#0033A0,color:#fff
    style G2R fill:#0033A0,color:#fff
    style G3R fill:#0033A0,color:#fff
    style G4R fill:#0033A0,color:#fff
    style G5R fill:#0033A0,color:#fff
```

---

## 4. SISTEMA DE NAVEGAÇÃO – FLUXOS E ESTADOS

### 4.1 Navegação Linear (Wizard) – Perfil do Produtor

```mermaid
graph LR
    subgraph "Fluxo Linear - Produtor Rural"
        S1[Login<br/>Gov.br/PIN] --> S2[Georreferenciamento<br/>Coordenadas GNSS]
        S2 --> S3[Triagem<br/>Básico ou Completo]
        S3 --> S4[Bloco 1<br/>Identificação]
        S4 --> S5[Bloco 2<br/>Uso da Terra]
        S5 --> S6[Bloco 3<br/>Produção]
        S6 --> S7[Bloco 4<br/>Revisão]
        S7 --> S8[Conclusão<br/>Envio]
    end
    
    style S1 fill:#0033A0,color:#fff
    style S2 fill:#0033A0,color:#fff
    style S3 fill:#f5a623,color:#fff
    style S4 fill:#4CAF50,color:#fff
    style S5 fill:#4CAF50,color:#fff
    style S6 fill:#4CAF50,color:#fff
    style S7 fill:#4CAF50,color:#fff
    style S8 fill:#0033A0,color:#fff
```

### 4.2 Navegação Não Linear (Menu) – Perfil ACQ

```mermaid
graph TD
    subgraph "Fluxo Não Linear - ACQ"
        M1[Dashboard<br/>Visão Geral] --> M2[Mapa de Calor<br/>Cobertura]
        M1 --> M3[Painel de<br/>Inconsistências]
        M1 --> M4[Relatórios de<br/>Qualidade]
        M1 --> M5[Auditoria<br/>por Agente]
        
        M3 --> M3A[Alertas HDOP]
        M3 --> M3B[Alertas Produção]
        M3 --> M3C[Pendentes PEUV]
        
        M4 --> M4A[Exportar PDF]
        M4 --> M4B[Exportar CSV]
        M4 --> M4C[Histórico]
    end
    
    style M1 fill:#0033A0,color:#fff
    style M2 fill:#2196F3,color:#fff
    style M3 fill:#2196F3,color:#fff
    style M4 fill:#2196F3,color:#fff
    style M5 fill:#2196F3,color:#fff
    style M3A fill:#f5a623,color:#fff
    style M3B fill:#f5a623,color:#fff
    style M3C fill:#f5a623,color:#fff
    style M4A fill:#4CAF50,color:#fff
    style M4B fill:#4CAF50,color:#fff
    style M4C fill:#4CAF50,color:#fff
```

### 4.3 Estados de Conectividade (Online/Offline)

```mermaid
stateDiagram-v2
    [*] --> Offline
    
    Offline --> Offline: Navegação local<br/>Formulários cache
    Offline --> Online: Sinal detectado
    
    state Offline {
        [*] --> IndexedDB
        IndexedDB --> Formulário
        Formulário --> Dados_Salvos
        Dados_Salvos --> Pendente_Sincronizacao
    }
    
    Online --> Offline: Sinal perdido
    Online --> Sincronizado: Backgroung Sync
    
    state Online {
        [*] --> Autenticação_Govbr
        Autenticação_Govbr --> API_IBGE
        API_IBGE --> Validação
        Validação --> Envio
    }
    
    Sincronizado --> [*]
```

---

## 5. SITEMAP COMPLETO DO CENSO FÁCIL

### 5.1 Estrutura de Telas e Navegação

```mermaid
graph TD
    subgraph "Sitemap - Censo Fácil"
        H[Dashboard Inicial] --> L[Login Gov.br]
        H --> S[Seleção Setor]
        H --> E[Lista de Endereços]
        H --> A[Módulo Auditoria]
        H --> U[Suporte]
        
        L --> G[Georreferenciamento]
        G --> T[Triagem Básico/Completo]
        T --> Q[Questionário]
        
        Q --> B1[Bloco: Identificação]
        Q --> B2[Bloco: Uso da Terra]
        Q --> B3[Bloco: Produção]
        Q --> B4[Bloco: Insumos]
        Q --> B5[Bloco: Gestão]
        Q --> R[Revisão Final]
        
        R --> ENV[Envio Sincronizado]
        
        A --> A1[Mapa de Calor]
        A --> A2[Inconsistências]
        A --> A3[Relatórios]
        
        U --> U1[Manuais]
        U --> U2[Glossário]
        U --> U3[Apoio Áudio]
    end
    
    style H fill:#0033A0,color:#fff
    style L fill:#f5a623,color:#fff
    style S fill:#f5a623,color:#fff
    style E fill:#f5a623,color:#fff
    style A fill:#2196F3,color:#fff
    style U fill:#4CAF50,color:#fff
    style G fill:#f5a623,color:#fff
    style T fill:#f5a623,color:#fff
    style Q fill:#4CAF50,color:#fff
    style B1 fill:#4CAF50,color:#fff
    style B2 fill:#4CAF50,color:#fff
    style B3 fill:#4CAF50,color:#fff
    style B4 fill:#4CAF50,color:#fff
    style B5 fill:#4CAF50,color:#fff
    style R fill:#f5a623,color:#fff
    style ENV fill:#0033A0,color:#fff
```

### 5.2 Fluxo de Telas (Wireframe Conceitual)

```mermaid
flowchart TB
    subgraph "Fluxo de Telas por Perfil"
        direction TB
        
        subgraph "Produtor Rural"
            P1[Login] --> P2[Dashboard]
            P2 --> P3[Formulário]
            P3 --> P4[Revisão]
            P4 --> P5[Envio]
        end
        
        subgraph "Recenseador"
            R1[Login] --> R2[Setor]
            R2 --> R3[Lista Endereços]
            R3 --> R4[Coleta]
            R4 --> R5[Sincronização]
        end
        
        subgraph "ACQ"
            A1[Login] --> A2[Dashboard]
            A2 --> A3[Auditoria]
            A3 --> A4[Relatórios]
            A4 --> A5[Validação]
        end
    end
    
    style P1 fill:#0033A0,color:#fff
    style P2 fill:#0033A0,color:#fff
    style P3 fill:#4CAF50,color:#fff
    style P4 fill:#f5a623,color:#fff
    style P5 fill:#0033A0,color:#fff
    
    style R1 fill:#0033A0,color:#fff
    style R2 fill:#0033A0,color:#fff
    style R3 fill:#4CAF50,color:#fff
    style R4 fill:#4CAF50,color:#fff
    style R5 fill:#0033A0,color:#fff
    
    style A1 fill:#0033A0,color:#fff
    style A2 fill:#0033A0,color:#fff
    style A3 fill:#2196F3,color:#fff
    style A4 fill:#2196F3,color:#fff
    style A5 fill:#0033A0,color:#fff
```

---

## 6. DECISÃO DE DESIGN – HIERARQUIA VISUAL

### 6.1 Cores e Identidade Visual

```mermaid
flowchart LR
    subgraph "Paleta de Cores do Censo Fácil"
        C1[Azul IBGE<br/>#0033A0<br/>Pantone 286 C] --> USO1[Navegação Primária<br/>Botões Principais<br/>Cabeçalhos]
        
        C2[Branco<br/>#FFFFFF] --> USO2[Fundo de Telas<br/>Áreas de Conteúdo]
        
        C3[Cinza Claro<br/>#F5F5F5] --> USO3[Card<br/>Áreas Secundárias<br/>Separadores]
        
        C4[Verde<br/>#4CAF50] --> USO4[Confirmar<br/>Sucesso<br/>Concluir]
        
        C5[Amarelo<br/>#F5A623] --> USO5[Atenção<br/>Alertas<br/>Pendências]
        
        C6[Vermelho<br/>#E53935] --> USO6[Erro<br/>Recusa<br/>Bloqueio]
    end
    
    style C1 fill:#0033A0,color:#fff
    style C2 fill:#FFFFFF,color:#000
    style C3 fill:#F5F5F5,color:#000
    style C4 fill:#4CAF50,color:#fff
    style C5 fill:#F5A623,color:#fff
    style C6 fill:#E53935,color:#fff
```

### 6.2 Aplicação da Tipografia Oficial

```mermaid
flowchart TD
    subgraph "Tipografia do Censo Fácil"
        TIPO1[Neuropolitical] --> APLIC1[Logomarca Censo<br/>Uso Restrito ao Logo]
        TIPO2[Univers LT Std<br/>55 Roman] --> APLIC2[Corpo de Texto<br/>Parágrafos]
        TIPO3[Univers LT Std<br/>65 Bold] --> APLIC3[Títulos<br/>Destaques]
        TIPO4[Univers LT Std<br/>55 Oblique] --> APLIC4[Citações<br/>Notas]
    end
    
    style TIPO1 fill:#0033A0,color:#fff
    style TIPO2 fill:#0033A0,color:#fff
    style TIPO3 fill:#0033A0,color:#fff
    style TIPO4 fill:#0033A0,color:#fff
```

---

## 📌 LEGENDA DOS DIAGRAMAS

| Cor | Significado |
|-----|-------------|
| 🔵 **Azul IBGE (#0033A0)** | Navegação primária, elementos principais, títulos |
| 🟢 **Verde (#4CAF50)** | Confirmar, sucesso, concluir, módulos ativos |
| 🟡 **Amarelo (#F5A623)** | Atenção, alertas, pendências, triagem |
| 🔴 **Vermelho (#E53935)** | Erro, recusa, bloqueio |
| 🔷 **Azul Claro (#2196F3)** | Módulos secundários, auditoria, relatórios |
| ⚪ **Cinza (#4A5568)** | Rótulos técnicos originais |

---

## 💡 COMO UTILIZAR ESTES DIAGRAMAS

| Tipo de Diagrama | Quando Usar | Para Quê |
|------------------|-------------|----------|
| **Hierarquia** | Fase 1 – Estrutura | Entender a relação entre seções do questionário |
| **LATCH** | Fase 1 – Organização | Visualizar como os dados são organizados |
| **Rotulagem** | Fase 2 – UX Writing | Traduzir termos técnicos para linguagem simples |
| **Navegação** | Fase 2 – Prototipagem | Mapear fluxos de tela e transições |
| **Sitemap** | Fase 2 – Arquitetura | Ter visão completa do sistema |
| **Cores/Tipografia** | Fase 2 – Design System | Aplicar identidade visual consistente |

---

*Documento base para a criação dos diagramas de arquitetura da informação do "Censo Fácil". Os diagramas devem ser utilizados como referência durante as fases de design e desenvolvimento.*