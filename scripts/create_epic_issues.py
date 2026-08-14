#!/usr/bin/env python3
"""
Script para criar os 4 Épicos (1 por Fase) no GitHub Projects
"""

import os
import sys
import requests
from dotenv import load_dotenv

# ============================================
# CARREGAR CONFIGURAÇÕES DO .ENV
# ============================================

load_dotenv()

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
REPO_OWNER = os.environ.get('REPO_OWNER', 'anandamatos')
REPO_NAME = os.environ.get('REPO_NAME', 'censo-facil')

if not GITHUB_TOKEN:
    print('❌ GITHUB_TOKEN não encontrado no .env')
    sys.exit(1)

HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

BASE_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"

# ============================================
# ESTRUTURA DOS ÉPICOS (1 POR FASE)
# ============================================

EPICS = [
    {
        'id': 'EPIC-F1-UX-001',
        'title': 'Fase 1: Pesquisa, Estratégia, Arquitetura da Informação e Acessibilidade',
        'fase': 'Fase 1',
        'labels': ['epic', 'fase-1'],
        'description': '''## 🎯 Objetivo do Épico

Estabelecer a base conceitual e normativa do "Censo Fácil", alinhada ao edital do IBGE 2026, mapeando as necessidades dos usuários, estruturando a informação e garantindo conformidade com acessibilidade.

## 👥 Squad Responsável
- **UX & Experience** (executor único)

## 📌 Definition of Done
- [ ] Personas validadas com stakeholders
- [ ] Jornadas do usuário mapeadas com transições online/offline
- [ ] Matriz LATCH e princípios da Gestalt aplicados
- [ ] Auditoria de acessibilidade (e-MAG 3.1 e WCAG 2.2 AA) concluída
- [ ] Relatório consolidado da Fase 1 aprovado
- [ ] Alinhamento estratégico para início da Fase 2

## 🔍 Tarefas de Discovery (UX Research)
- [ ] DISCOVERY-F1-UX-001: Realizar pesquisa etnográfica com produtores rurais (persona "Seu José")
- [ ] DISCOVERY-F1-UX-002: Conduzir entrevistas com recenseadores para mapear fluxo de campo (persona "Mariana")
- [ ] DISCOVERY-F1-UX-003: Analisar necessidades de auditoria com Agentes Censitários de Qualidade (persona "Carlos")
- [ ] DISCOVERY-F1-UX-004: Mapear a jornada do usuário em cenários offline-first
- [ ] DISCOVERY-F1-UX-005: Avaliar os sistemas de organização, rotulagem e navegação do questionário
- [ ] DISCOVERY-F1-UX-006: Aplicar o método LATCH para estruturação dos dados do censo
- [ ] DISCOVERY-F1-UX-007: Identificar barreiras de acessibilidade em campo (baixa visão, baixa alfabetização digital)

## 📊 Tarefas de Mensuração (UX Metrics)
- [ ] MEASUREMENT-F1-UX-001: Definir KPIs de usabilidade para o "Censo Fácil" (taxa de conclusão, tempo de tarefa)
- [ ] MEASUREMENT-F1-UX-002: Estabelecer critérios de sucesso para cada persona (ex: produtor conclui questionário em <20min)
- [ ] MEASUREMENT-F1-UX-003: Criar baseline de acessibilidade com base no e-MAG 3.1
- [ ] MEASUREMENT-F1-UX-004: Definir métricas de contraste e legibilidade (4.5:1)
- [ ] MEASUREMENT-F1-UX-005: Alinhar KPIs com a Ferramenta de Avaliação de Serviços Digitais do Gov.br

## 📋 Stories Relacionadas (21 stories)
- STORY-F1-UX-001.1: Criação da Persona "Seu José" (Produtor Rural)
- STORY-F1-UX-001.2: Criação da Persona "Mariana" (Recenseadora)
- STORY-F1-UX-001.3: Criação da Persona "Carlos" (ACQ)
- STORY-F1-UX-001.4: Validação das Personas com Stakeholders
- STORY-F1-UX-002.1: Mapeamento da Jornada do Produtor Rural
- STORY-F1-UX-002.2: Mapeamento da Jornada do Recenseador
- STORY-F1-UX-002.3: Mapeamento da Jornada do ACQ
- STORY-F1-UX-002.4: Análise das 10 Heurísticas de Nielsen
- STORY-F1-UX-003.1: Mapeamento dos Sistemas de Organização, Rotulagem e Navegação
- STORY-F1-UX-003.2: Aplicação do Método LATCH
- STORY-F1-UX-003.3: Aplicação das Leis da Gestalt
- STORY-F1-UX-003.4: Validação da Arquitetura da Informação
- STORY-F1-UX-004.1: Auditoria – Área de Marcação (e-MAG)
- STORY-F1-UX-004.2: Auditoria – Área de Comportamento (e-MAG)
- STORY-F1-UX-004.3: Auditoria – Área de Conteúdo (e-MAG)
- STORY-F1-UX-004.4: Auditoria – Área de Apresentação (e-MAG)
- STORY-F1-UX-004.5: Auditoria – Área de Multimídia (e-MAG)
- STORY-F1-UX-004.6: Auditoria – Área de Formulário (e-MAG)
- STORY-F1-UX-004.7: Critérios Específicos WCAG 2.2 AA
- STORY-F1-ALL-005.1: Consolidação dos Entregáveis da Fase 1
- STORY-F1-ALL-005.2: Revisão e Alinhamento com Stakeholders

## 🏷️ Metadados
**ID:** EPIC-F1-UX-001
**Fase:** 1
**Tipo:** Épico
**Track:** Discovery & Mensuração (UX Research)
**Responsável:** @executor-unico''',
    },
    {
        'id': 'EPIC-F2-UX-001',
        'title': 'Fase 2: Design Visual, Prototipagem e Design System',
        'fase': 'Fase 2',
        'labels': ['epic', 'fase-2'],
        'description': '''## 🎯 Objetivo do Épico

Materializar o design do "Censo Fácil" em protótipos de alta fidelidade, aplicando a Identidade Visual do IBGE, adaptando o DSGov 4.0 e documentando componentes customizados.

## 👥 Squad Responsável
- **UX & Experience** (executor único)

## 📌 Definition of Done
- [ ] Design Tokens do DSGov mapeados e adaptados
- [ ] Componente `br-gnss-tracker` documentado em Custom Elements Manifest
- [ ] Protótipo Figma navegável com fluxos de coleta e auditoria
- [ ] Tipografia oficial (Neuropolitical/Univers) aplicada
- [ ] UX Writing e microcopy padronizados
- [ ] Kit de UI DSGov Mobile validado

## 🔍 Tarefas de Discovery (Design Validation)
- [ ] DISCOVERY-F2-UX-001: Avaliar aderência do protótipo ao DSGov 4.0
- [ ] DISCOVERY-F2-UX-002: Testar usabilidade do componente `br-gnss-tracker`
- [ ] DISCOVERY-F2-UX-003: Validar clareza da UX Writing com produtores rurais
- [ ] DISCOVERY-F2-UX-004: Verificar aplicação da tipografia Univers e Neuropolitical
- [ ] DISCOVERY-F2-UX-005: Avaliar consistência do Design System

## 📊 Tarefas de Mensuração (Design Quality)
- [ ] MEASUREMENT-F2-UX-001: Medir taxa de sucesso no protótipo
- [ ] MEASUREMENT-F2-UX-002: Coletar feedback qualitativo
- [ ] MEASUREMENT-F2-UX-003: Verificar conformidade com cores oficiais
- [ ] MEASUREMENT-F2-UX-004: Avaliar acessibilidade visual
- [ ] MEASUREMENT-F2-UX-005: Estabelecer baseline de satisfação (SUS)

## 📋 Stories Relacionadas
- STORY-F2-UX-001.1: Mapeamento dos Design Tokens do DSGov Mobile
- STORY-F2-UX-001.2: Definição das Grids Móveis (4 colunas / 8 colunas)
- STORY-F2-UX-001.3: Especificação do Componente br-gnss-tracker
- STORY-F2-UX-001.4: Documentação do Componente (CEM)
- STORY-F2-UX-002.1: Prototipagem – Fluxo de Login (Gov.br + Offline)
- STORY-F2-UX-002.2: Prototipagem – Dashboard e Mapa do Setor
- STORY-F2-UX-002.3: Prototipagem – Formulário e Captura GNSS
- STORY-F2-UX-002.4: Prototipagem – Encerramento e Sincronização
- STORY-F2-UX-003.1: Prototipagem – Dashboard de Auditoria do ACQ
- STORY-F2-UX-003.2: Prototipagem – Validação de Consistência de Dados
- STORY-F2-UX-003.3: Prototipagem – Gestão de Pendentes e Ocorrências
- STORY-F2-UX-003.4: Prototipagem – Relatórios de Qualidade
- STORY-F2-ALL-004.1: Consolidação dos Entregáveis da Fase 2
- STORY-F2-ALL-004.2: Revisão e Alinhamento com Stakeholders

## 🏷️ Metadados
**ID:** EPIC-F2-UX-001
**Fase:** 2
**Tipo:** Épico
**Track:** Discovery & Mensuração (Design Validation)
**Responsável:** @executor-unico''',
    },
    {
        'id': 'EPIC-F3-FND-001',
        'title': 'Fase 3: Engenharia Frontend, Web Components e Integração',
        'fase': 'Fase 3',
        'labels': ['epic', 'fase-3'],
        'description': '''## 🎯 Objetivo do Épico

Implementar a solução técnica do "Censo Fácil" com conformidade XHTML, Web Components, integração Gov.br e garantia de segurança e acessibilidade.

## 👥 Squad Responsável
- **Foundation & Core Business** (executor único)

## 📌 Definition of Done
- [ ] Componente `br-gnss-tracker` implementado em XHTML com Shadow DOM
- [ ] Módulo ES6 de validação geodésica (HDOP) funcional
- [ ] Service Worker configurado para offline-first
- [ ] Criptografia AES-256 implementada no IndexedDB (LGPD)
- [ ] Barra Gov.Br integrada e fluxo OIDC funcional
- [ ] Código validado conforme XHTML Estrito e e-MAG
- [ ] Relatório técnico consolidado

## 🔍 Tarefas de Discovery (Technical Validation)
- [ ] DISCOVERY-F3-FND-001: Validar estrutura do Web Component com @govbr-ds/webcomponents
- [ ] DISCOVERY-F3-FND-002: Testar precisão do cálculo de HDOP
- [ ] DISCOVERY-F3-FND-003: Verificar eficácia do Service Worker
- [ ] DISCOVERY-F3-FND-004: Validar integração da Barra Gov.Br
- [ ] DISCOVERY-F3-FND-005: Avaliar conformidade com LGPD

## 📊 Tarefas de Mensuração (Technical Quality)
- [ ] MEASUREMENT-F3-FND-001: Medir performance de carregamento (Lighthouse)
- [ ] MEASUREMENT-F3-FND-002: Verificar conformidade com Gov.br
- [ ] MEASUREMENT-F3-FND-003: Avaliar cobertura de testes
- [ ] MEASUREMENT-F3-FND-004: Monitorar tempo de sincronização
- [ ] MEASUREMENT-F3-FND-005: Verificar segurança dos dados

## 📋 Stories Relacionadas
- STORY-F3-FND-001.1: Implementação do Componente br-gnss-tracker
- STORY-F3-FND-001.2: Validação Geodésica (ES6)
- STORY-F3-FND-001.3: Service Worker e Offline
- STORY-F3-FND-001.4: Criptografia AES-256
- STORY-F3-FND-001.5: CSS Responsivo e Acessível
- STORY-F3-FND-002.1: Integração da Barra Gov.Br
- STORY-F3-FND-002.2: Autenticação OIDC (Gov.br)
- STORY-F3-FND-002.3: Manual de Replicabilidade Institucional
- STORY-F3-ALL-003.1: Testes de Integração
- STORY-F3-ALL-003.2: Revisão de Código

## 🏷️ Metadados
**ID:** EPIC-F3-FND-001
**Fase:** 3
**Tipo:** Épico
**Track:** Discovery & Mensuração (Technical Validation)
**Responsável:** @executor-unico''',
    },
    {
        'id': 'EPIC-F4-ALL-001',
        'title': 'Fase 4: Testes, Governança DesignOps e Documentação',
        'fase': 'Fase 4',
        'labels': ['epic', 'fase-4'],
        'description': '''## 🎯 Objetivo do Épico

Validar o "Censo Fácil" com usuários reais, estabelecer governança DesignOps e documentar a solução final para entrega e escalabilidade.

## 👥 Squad Responsável
- **All Squads** (executor único)

## 📌 Definition of Done
- [ ] Plano de Testes de Usabilidade executado
- [ ] Matriz de Severidade e recomendações de redesign
- [ ] Documento de DesignOps e estratégia de evolução
- [ ] Manual de Identidade Visual do "Censo Fácil"
- [ ] Deck Executivo para SGD/MGI
- [ ] Conformidade com a Ferramenta de Avaliação de Serviços Digitais do Gov.br atestada

## 🔍 Tarefas de Discovery (User Validation)
- [ ] DISCOVERY-F4-UX-001: Recrutar participantes para testes
- [ ] DISCOVERY-F4-UX-002: Conduzir sessões de teste de usabilidade
- [ ] DISCOVERY-F4-UX-003: Coletar feedback qualitativo
- [ ] DISCOVERY-F4-UX-004: Identificar pontos de fricção
- [ ] DISCOVERY-F4-UX-005: Documentar lições aprendidas

## 📊 Tarefas de Mensuração (Quality Assurance)
- [ ] MEASUREMENT-F4-UX-001: Calcular Taxa de Conclusão (TCT)
- [ ] MEASUREMENT-F4-UX-002: Medir Tempo Médio (TME)
- [ ] MEASUREMENT-F4-UX-003: Aplicar Escala SUS
- [ ] MEASUREMENT-F4-UX-004: Classificar problemas (Matriz de Severidade)
- [ ] MEASUREMENT-F4-UX-005: Validar conformidade com Gov.br
- [ ] MEASUREMENT-F4-UX-006: Estabelecer métricas de DesignOps

## 📋 Stories Relacionadas
- STORY-F4-UX-001.1: Elaboração do Plano de Testes de Usabilidade
- STORY-F4-UX-001.2: Execução de Testes com Personas
- STORY-F4-UX-001.3: Matriz de Severidade e Recomendações
- STORY-F4-ALL-002.1: Documento de DesignOps
- STORY-F4-ALL-002.2: Estratégia de Iteração e Evolução
- STORY-F4-ALL-003.1: Manual de Identidade Visual
- STORY-F4-ALL-003.2: Apresentação Executiva

## 🏷️ Metadados
**ID:** EPIC-F4-ALL-001
**Fase:** 4
**Tipo:** Épico
**Track:** Discovery & Mensuração (User Validation / QA)
**Responsável:** @executor-unico''',
    }
]

# ============================================
# FUNÇÕES
# ============================================

def create_github_issue(title, body, labels):
    """Cria uma issue no GitHub"""
    url = f"{BASE_URL}/issues"
    data = {
        'title': title,
        'body': body,
        'labels': labels,
    }
    response = requests.post(url, headers=HEADERS, json=data)
    
    if response.status_code == 201:
        issue = response.json()
        print(f'✅ Criado: {title} (##{issue["number"]})')
        return issue
    else:
        print(f'❌ Erro ao criar {title}: {response.status_code}')
        return None

# ============================================
# MAIN
# ============================================

def main():
    print('🚀 Criando os 4 Épicos do Projeto "Censo Fácil"...')
    print(f'📁 Repositório: {REPO_OWNER}/{REPO_NAME}\n')
    
    for epic in EPICS:
        title = f'[{epic["id"]}] {epic["title"]}'
        create_github_issue(title, epic['description'], epic['labels'])
        print()
    
    print('✅ Todos os 4 Épicos foram criados!')
    print('🔗 https://github.com/anandamatos/censo-facil/issues')

if __name__ == '__main__':
    main()