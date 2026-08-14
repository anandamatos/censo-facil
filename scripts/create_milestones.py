#!/usr/bin/env python3
"""
Script para criar Milestones no repositório GitHub
Os milestones são herdados pelo Projects V2 automaticamente
"""

import os
import sys
import requests
from datetime import datetime, timedelta
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

# ============================================
# ESTRUTURA DOS MILESTONES
# ============================================

# Data base: 1º dia do projeto (ajuste conforme necessário)
START_DATE = datetime(2026, 8, 11)  # Data de início do desafio

MILESTONES = [
    {
        'title': 'M1 - Fase 1: Pesquisa e Estratégia',
        'description': '''
## 🎯 Objetivo do Milestone

Concluir a Fase 1 do projeto "Censo Fácil", estabelecendo a base conceitual e normativa.

## 📋 Entregáveis
- Personas validadas (Seu José, Mariana, Carlos)
- Jornadas do usuário mapeadas
- Matriz LATCH e princípios da Gestalt
- Auditoria de acessibilidade (e-MAG 3.1 e WCAG 2.2 AA)
- Relatório consolidado da Fase 1

## 🔗 Issues Relacionadas
- EPIC-F1-UX-001: Pesquisa, Personas e Jornadas
- EPIC-F1-UX-002: Jornadas e Heurísticas
- EPIC-F1-UX-003: Arquitetura da Informação
- EPIC-F1-UX-004: Acessibilidade (e-MAG/WCAG)
- EPIC-F1-ALL-005: Consolidação da Fase 1

## 📅 Prazo
Dia 5 do projeto
''',
        'due_date': START_DATE + timedelta(days=5)
    },
    {
        'title': 'M2 - Fase 2: Design e Prototipagem',
        'description': '''
## 🎯 Objetivo do Milestone

Concluir a Fase 2 do projeto "Censo Fácil", materializando o design em protótipos de alta fidelidade.

## 📋 Entregáveis
- Design Tokens do DSGov mapeados
- Componente br-gnss-tracker documentado
- Protótipo Figma navegável (coleta e auditoria)
- Tipografia oficial aplicada (Neuropolitical/Univers)
- UX Writing e microcopy padronizados
- Kit de UI DSGov Mobile validado

## 🔗 Issues Relacionadas
- EPIC-F2-UX-001: DSGov e Componentes
- EPIC-F2-UX-002: Protótipo Fluxo de Coleta
- EPIC-F2-UX-003: Protótipo Fluxo de Auditoria
- EPIC-F2-ALL-004: Consolidação da Fase 2

## 📅 Prazo
Dia 10 do projeto
''',
        'due_date': START_DATE + timedelta(days=10)
    },
    {
        'title': 'M3 - Fase 3: Engenharia e Integração',
        'description': '''
## 🎯 Objetivo do Milestone

Concluir a Fase 3 do projeto "Censo Fácil", implementando a solução técnica completa.

## 📋 Entregáveis
- Componente br-gnss-tracker em XHTML com Shadow DOM
- Módulo ES6 de validação geodésica (HDOP)
- Service Worker para offline-first
- Criptografia AES-256 no IndexedDB (LGPD)
- Barra Gov.Br integrada e fluxo OIDC
- Código validado conforme XHTML Estrito e e-MAG

## 🔗 Issues Relacionadas
- EPIC-F3-FND-001: Web Components e XHTML
- EPIC-F3-FND-002: Integração Gov.br
- EPIC-F3-ALL-003: Revisão Técnica

## 📅 Prazo
Dia 15 do projeto
''',
        'due_date': START_DATE + timedelta(days=15)
    },
    {
        'title': 'M4 - Fase 4: Testes e Documentação',
        'description': '''
## 🎯 Objetivo do Milestone

Concluir a Fase 4 do projeto "Censo Fácil", validando a solução e entregando a documentação final.

## 📋 Entregáveis
- Plano de Testes de Usabilidade executado
- Matriz de Severidade e recomendações
- Documento de DesignOps e estratégia de evolução
- Manual de Identidade Visual do "Censo Fácil"
- Deck Executivo para SGD/MGI
- Conformidade com a Ferramenta de Avaliação de Serviços Digitais do Gov.br

## 🔗 Issues Relacionadas
- EPIC-F4-UX-001: Plano de Testes
- EPIC-F4-ALL-002: DesignOps e Governança
- EPIC-F4-ALL-003: Documentação Final

## 📅 Prazo
Dia 20 do projeto
''',
        'due_date': START_DATE + timedelta(days=20)
    }
]

# ============================================
# FUNÇÕES
# ============================================

def create_github_milestone(title, description, due_date):
    """Cria um milestone no repositório GitHub"""
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/milestones'

    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
        'Content-Type': 'application/json',
    }

    data = {
        'title': title,
        'description': description,
        'due_on': due_date.isoformat() + 'Z',
        'state': 'open',
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        milestone = response.json()
        print(f'✅ Criado: {title} (#{milestone["number"]})')
        print(f'   📅 Prazo: {due_date.strftime("%d/%m/%Y")}')
        return milestone
    elif response.status_code == 422:
        # Milestone já existe
        print(f'⚠️ Já existe: {title}')
        return None
    else:
        print(f'❌ Erro ao criar {title}: {response.status_code}')
        print(f'   {response.text[:200]}...')
        return None


def main():
    print('🚀 Criando Milestones no repositório...')
    print(f'📁 {REPO_OWNER}/{REPO_NAME}')
    print(f'📅 Data de início: {START_DATE.strftime("%d/%m/%Y")}')
    print()

    created = 0
    for milestone in MILESTONES:
        result = create_github_milestone(
            milestone['title'],
            milestone['description'],
            milestone['due_date']
        )
        if result:
            created += 1
        print()

    print(f'✅ Milestones criados/verificados: {created}/{len(MILESTONES)}')
    print()
    print('📌 Os milestones agora estão disponíveis no repositório e no Projects V2!')
    print(f'🔗 https://github.com/{REPO_OWNER}/{REPO_NAME}/milestones')


if __name__ == '__main__':
    main()