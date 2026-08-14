#!/usr/bin/env python3
"""
Script para sincronizar labels do repositório com o GitHub Projects V2
Cria as mesmas labels dentro do Project (para boards que não herdam do repositório)
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
PROJECT_NUMBER = int(os.environ.get('PROJECT_NUMBER', 8))

# Verificar se o token está configurado
if not GITHUB_TOKEN:
    print('❌ GITHUB_TOKEN não encontrado no .env')
    print('   Certifique-se de que o arquivo .env contém:')
    print('   GITHUB_TOKEN=seu_token_aqui')
    sys.exit(1)

# ============================================
# LISTA DE LABELS (mesma estrutura do repositório)
# ============================================

LABELS = [
    # ===== TIPO =====
    {'name': 'epic', 'color': 'FF6B6B', 'description': 'Épico - Grande marco do projeto (Fase)'},
    {'name': 'story', 'color': '4ECDC4', 'description': 'Story - Funcionalidade/Entrega'},
    {'name': 'task', 'color': '45B7D1', 'description': 'Task - Entregável/Artefato'},
    {'name': 'discovery', 'color': 'F9CA24', 'description': 'Discovery - Pesquisa e validação (UX Research)'},
    {'name': 'measurement', 'color': 'F0932B', 'description': 'Measurement - Métricas e avaliação (UX Metrics)'},
    {'name': 'delivery', 'color': '6AB04C', 'description': 'Delivery - Implementação e entrega'},

    # ===== FASE =====
    {'name': 'fase-1', 'color': 'E8F5E9', 'description': 'Fase 1: Pesquisa, Estratégia, AI e Acessibilidade'},
    {'name': 'fase-2', 'color': 'E3F2FD', 'description': 'Fase 2: Design Visual, Prototipagem e Design System'},
    {'name': 'fase-3', 'color': 'FFF3E0', 'description': 'Fase 3: Engenharia Frontend, Web Components e Integração'},
    {'name': 'fase-4', 'color': 'FCE4EC', 'description': 'Fase 4: Testes, Governança DesignOps e Documentação'},

    # ===== SQUAD / PAPEL =====
    {'name': 'ux-research', 'color': '9B59B6', 'description': 'UX Research - Pesquisa com usuários, personas, jornadas'},
    {'name': 'ux-design', 'color': '3498DB', 'description': 'UX Design - Prototipagem, Design System, DSGov'},
    {'name': 'ux-writing', 'color': '1ABC9C', 'description': 'UX Writing - Microcopy, linguagem simples, redação oficial'},
    {'name': 'frontend', 'color': 'E74C3C', 'description': 'Frontend - XHTML, CSS, Web Components, acessibilidade'},
    {'name': 'backend', 'color': '2ECC71', 'description': 'Backend - APIs, integração Gov.br, criptografia, LGPD'},
    {'name': 'designops', 'color': 'F39C12', 'description': 'DesignOps - Governança, fluxo de trabalho, métricas'},
    {'name': 'qa', 'color': '8E44AD', 'description': 'QA - Testes de usabilidade, matriz de severidade, validação'},

    # ===== STATUS =====
    {'name': 'backlog', 'color': '95A5A6', 'description': 'Backlog - Pendente, aguardando início'},
    {'name': 'in-progress', 'color': '3498DB', 'description': 'In Progress - Em andamento'},
    {'name': 'review', 'color': 'F39C12', 'description': 'Review - Aguardando revisão/validação'},
    {'name': 'done', 'color': '2ECC71', 'description': 'Done - Concluído'},
    {'name': 'blocked', 'color': 'E74C3C', 'description': 'Blocked - Bloqueado, aguardando dependência'},

    # ===== PRIORIDADE =====
    {'name': 'P0', 'color': 'E74C3C', 'description': 'Prioridade 0 - Crítico, bloqueia outras entregas'},
    {'name': 'P1', 'color': 'F39C12', 'description': 'Prioridade 1 - Alta, essencial para o MVP'},
    {'name': 'P2', 'color': '3498DB', 'description': 'Prioridade 2 - Média, melhoria ou refinamento'},

    # ===== ENTREGÁVEIS =====
    {'name': 'doc', 'color': '8E44AD', 'description': 'Documentação - Relatórios, manuais, guias'},
    {'name': 'prototipo', 'color': 'E67E22', 'description': 'Protótipo - Figma, fluxos, telas'},
    {'name': 'code', 'color': '2ECC71', 'description': 'Código - Implementação técnica'},
    {'name': 'ds', 'color': '3498DB', 'description': 'Design System - Componentes, tokens, DSGov'},
    {'name': 'test', 'color': '9B59B6', 'description': 'Testes - Usabilidade, QA, validação'},
    {'name': 'slides', 'color': 'F1C40F', 'description': 'Apresentação - Deck executivo, slides'},
]

# ============================================
# FUNÇÕES GRAPHQL PARA PROJECTS V2
# ============================================

def get_project_id():
    """Busca o ID do Project V2 usando GraphQL"""
    query = """
    {
      repository(owner: "%s", name: "%s") {
        projectsV2(first: 10) {
          nodes {
            id
            title
            number
          }
        }
      }
    }
    """ % (REPO_OWNER, REPO_NAME)

    headers = {
        'Authorization': f'Bearer {GITHUB_TOKEN}',
        'Content-Type': 'application/json',
    }

    response = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)

    if response.status_code != 200:
        print(f'❌ Erro ao buscar projeto: {response.status_code}')
        print(f'   {response.text[:200]}...')
        return None

    data = response.json()

    if 'errors' in data:
        print(f'❌ Erro GraphQL: {data["errors"]}')
        return None

    for project in data.get('data', {}).get('repository', {}).get('projectsV2', {}).get('nodes', []):
        if project['number'] == PROJECT_NUMBER:
            return project['id']

    print(f'❌ Projeto #{PROJECT_NUMBER} não encontrado')
    return None


def get_existing_project_labels(project_id):
    """Busca labels existentes no Project V2"""
    query = """
    {
      node(id: "%s") {
        ... on ProjectV2 {
          labels(first: 50) {
            nodes {
              id
              name
            }
          }
        }
      }
    }
    """ % project_id

    headers = {
        'Authorization': f'Bearer {GITHUB_TOKEN}',
        'Content-Type': 'application/json',
    }

    response = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)

    if response.status_code != 200:
        print(f'❌ Erro ao buscar labels do projeto: {response.status_code}')
        return []

    data = response.json()

    if 'errors' in data:
        print(f'❌ Erro GraphQL: {data["errors"]}')
        return []

    labels = data.get('data', {}).get('node', {}).get('labels', {}).get('nodes', [])
    return [label['name'] for label in labels if label]


def create_project_label(project_id, name, color, description):
    """Cria uma label dentro do Project V2 via GraphQL"""
    mutation = """
    mutation {
      createProjectV2Label(input: {
        projectId: "%s"
        name: "%s"
        color: "%s"
        description: "%s"
      }) {
        label {
          id
          name
        }
      }
    }
    """ % (project_id, name, color, description)

    headers = {
        'Authorization': f'Bearer {GITHUB_TOKEN}',
        'Content-Type': 'application/json',
    }

    response = requests.post('https://api.github.com/graphql', json={'query': mutation}, headers=headers)

    if response.status_code != 200:
        print(f'❌ Erro HTTP ao criar {name}: {response.status_code}')
        return False

    data = response.json()

    if 'errors' in data:
        # Verifica se o erro é de label duplicada
        for error in data['errors']:
            if 'already exists' in error.get('message', '').lower():
                print(f'⚠️ Label já existe: {name}')
                return True
        print(f'❌ Erro GraphQL ao criar {name}: {data["errors"]}')
        return False

    print(f'✅ Criada no Project: {name}')
    return True


# ============================================
# FUNÇÃO PRINCIPAL
# ============================================

def main():
    """Função principal"""
    print('🚀 Iniciando sincronização de labels para o GitHub Projects V2...')
    print(f'📁 Repositório: {REPO_OWNER}/{REPO_NAME}')
    print(f'📋 Projeto #: {PROJECT_NUMBER}')
    print(f'🔑 Token: {GITHUB_TOKEN[:10]}...')
    print()

    # 1. Buscar ID do projeto
    project_id = get_project_id()
    if not project_id:
        print('❌ Não foi possível obter o ID do projeto. Abortando.')
        sys.exit(1)

    print(f'📌 Projeto encontrado: ID {project_id}')
    print()

    # 2. Buscar labels existentes no projeto
    existing_labels = get_existing_project_labels(project_id)
    print(f'📊 Labels existentes no projeto: {len(existing_labels)}')
    print()

    # 3. Criar labels que não existem
    print('📌 Criando labels no Project...')
    print('-' * 60)

    created_count = 0
    skipped_count = 0

    for label in LABELS:
        if label['name'] in existing_labels:
            print(f'⏭️  Pulando (já existe): {label["name"]}')
            skipped_count += 1
            continue

        if create_project_label(
            project_id,
            label['name'],
            label['color'],
            label['description']
        ):
            created_count += 1

    print('-' * 60)
    print(f'✅ Labels criadas: {created_count}')
    print(f'⏭️  Labels já existentes: {skipped_count}')
    print(f'📊 Total de labels no projeto: {len(existing_labels) + created_count}')
    print()
    print('🔗 Acesse o projeto em:')
    print(f'   https://github.com/users/{REPO_OWNER}/projects/{PROJECT_NUMBER}')


if __name__ == '__main__':
    main()