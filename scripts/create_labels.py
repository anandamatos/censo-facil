#!/usr/bin/env python3
"""
Script para criar Labels no GitHub (Repositório)
As labels criadas no repositório são automaticamente herdadas pelo Projects V2
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

# ============================================
# LISTA DE LABELS
# ============================================

LABELS = [
    # ===== TIPO =====
    {'name': 'epic', 'color': 'FF6B6B', 'description': 'Épico - Grande marco do projeto (Fase)'},
    {'name': 'story', 'color': '4ECDC4', 'description': 'Story - Funcionalidade/Entrega'},
    {'name': 'task', 'color': '45B7D1', 'description': 'Task - Entregável/Artefato'},
    {'name': 'discovery', 'color': 'F9CA24', 'description': 'Discovery - Pesquisa e validação (UX Research)'},
    {'name': 'measurement', 'color': 'F0932B', 'description': 'Measurement - Métricas e avaliação'},
    {'name': 'delivery', 'color': '6AB04C', 'description': 'Delivery - Implementação e entrega'},

    # ===== FASE =====
    {'name': 'fase-1', 'color': 'E8F5E9', 'description': 'Fase 1: Pesquisa, Estratégia, AI e Acessibilidade'},
    {'name': 'fase-2', 'color': 'E3F2FD', 'description': 'Fase 2: Design Visual, Prototipagem e Design System'},
    {'name': 'fase-3', 'color': 'FFF3E0', 'description': 'Fase 3: Engenharia Frontend, Web Components e Integração'},
    {'name': 'fase-4', 'color': 'FCE4EC', 'description': 'Fase 4: Testes, Governança DesignOps e Documentação'},

    # ===== SQUAD / PAPEL =====
    {'name': 'ux-research', 'color': '9B59B6', 'description': 'UX Research'},
    {'name': 'ux-design', 'color': '3498DB', 'description': 'UX Design'},
    {'name': 'ux-writing', 'color': '1ABC9C', 'description': 'UX Writing'},
    {'name': 'frontend', 'color': 'E74C3C', 'description': 'Frontend'},
    {'name': 'backend', 'color': '2ECC71', 'description': 'Backend'},
    {'name': 'designops', 'color': 'F39C12', 'description': 'DesignOps'},
    {'name': 'qa', 'color': '8E44AD', 'description': 'QA - Testes e Validação'},

    # ===== STATUS =====
    {'name': 'backlog', 'color': '95A5A6', 'description': 'Backlog - Pendente'},
    {'name': 'in-progress', 'color': '3498DB', 'description': 'In Progress - Em andamento'},
    {'name': 'review', 'color': 'F39C12', 'description': 'Review - Aguardando revisão'},
    {'name': 'done', 'color': '2ECC71', 'description': 'Done - Concluído'},
    {'name': 'blocked', 'color': 'E74C3C', 'description': 'Blocked - Bloqueado'},

    # ===== PRIORIDADE =====
    {'name': 'P0', 'color': 'E74C3C', 'description': 'Prioridade 0 - Crítico'},
    {'name': 'P1', 'color': 'F39C12', 'description': 'Prioridade 1 - Alta'},
    {'name': 'P2', 'color': '3498DB', 'description': 'Prioridade 2 - Média'},

    # ===== ENTREGÁVEIS =====
    {'name': 'doc', 'color': '8E44AD', 'description': 'Documentação'},
    {'name': 'prototipo', 'color': 'E67E22', 'description': 'Protótipo'},
    {'name': 'code', 'color': '2ECC71', 'description': 'Código'},
    {'name': 'ds', 'color': '3498DB', 'description': 'Design System'},
    {'name': 'test', 'color': '9B59B6', 'description': 'Testes'},
    {'name': 'slides', 'color': 'F1C40F', 'description': 'Apresentação'},
]

# ============================================
# FUNÇÕES
# ============================================

def create_github_label(name, color, description):
    """Cria uma label no repositório GitHub"""
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/labels'

    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
    }

    data = {
        'name': name,
        'color': color,
        'description': description,
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f'✅ Criada: {name}')
        return True
    elif response.status_code == 422:
        # Label já existe
        print(f'⚠️ Já existe: {name}')
        return True
    else:
        print(f'❌ Erro ao criar {name}: {response.status_code}')
        return False


def main():
    print('🚀 Criando labels no repositório...')
    print(f'📁 {REPO_OWNER}/{REPO_NAME}')
    print()

    created = 0
    for label in LABELS:
        if create_github_label(label['name'], label['color'], label['description']):
            created += 1

    print()
    print(f'✅ Labels criadas/verificadas: {created}/{len(LABELS)}')
    print('📌 As labels agora estão disponíveis no Projects V2!')

if __name__ == '__main__':
    main()