#!/usr/bin/env python3
"""
Script para atualizar as stories da Fase 1 para a Opção 4
- Fecha as 4 stories existentes com comentário
- Cria as 4 novas stories (agrupadas)
- Mantém o histórico
"""

import os
import sys
import time
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
REPO_OWNER = os.environ.get('REPO_OWNER', 'anandamatos')
REPO_NAME = os.environ.get('REPO_NAME', 'censo-facil')

if not GITHUB_TOKEN:
    print('❌ GITHUB_TOKEN não encontrado')
    sys.exit(1)

HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

BASE_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"

# ============================================================
# NOVAS STORIES (OPÇÃO 4)
# ============================================================

NEW_STORIES = [
    {
        'id': 'STORY-F1-UX-001',
        'title': 'Personas e Jornadas do Usuário',
        'epic_id': 'EPIC-F1-UX-001',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'ux-research', 'doc'],
        'story_points': 8,
        'body': '''## 📖 User Story
Como UX Researcher, quero criar as personas e mapear as jornadas dos usuários do "Censo Fácil" para orientar as decisões de design do projeto.

## ✅ Critérios de Aceite
- [ ] Personas validadas: Seu José, Mariana, Carlos
- [ ] Jornadas mapeadas com transições online/offline
- [ ] Análise das 10 Heurísticas de Nielsen
- [ ] Documentação consolidada

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-001.1: Criação da Persona "Seu José" (2 SP)
- [ ] TASK-F1-UX-001.2: Criação da Persona "Mariana" (2 SP)
- [ ] TASK-F1-UX-001.3: Criação da Persona "Carlos" (2 SP)
- [ ] TASK-F1-UX-001.4: Jornadas e Heurísticas (2 SP)

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-001
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 8 Story Points
**Prioridade:** P0
**Épico:** EPIC-F1-UX-001
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-research` `doc`

## 📚 Referências
- [Manual do Recenseador](https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5723.pdf)
- [10 Heurísticas de Nielsen](https://www.nngroup.com/articles/ten-usability-heuristics/)
- [5 Planos de Garrett](https://www.jjg.net/elements/)'''
    },
    {
        'id': 'STORY-F1-UX-002',
        'title': 'Arquitetura da Informação (LATCH e Gestalt)',
        'epic_id': 'EPIC-F1-UX-001',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'ux-design', 'doc'],
        'story_points': 8,
        'body': '''## 📖 User Story
Como UX Designer, quero estruturar a Arquitetura da Informação do "Censo Fácil" usando o método LATCH e os princípios da Gestalt para otimizar a navegação e compreensão do usuário.

## ✅ Critérios de Aceite
- [ ] Matriz LATCH aplicada ao questionário
- [ ] Princípios da Gestalt aplicados ao layout
- [ ] Sistemas de organização, rotulagem e navegação mapeados
- [ ] Validação com stakeholders

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-002.1: Sistemas de Organização, Rotulagem e Navegação (2 SP)
- [ ] TASK-F1-UX-002.2: Aplicação do Método LATCH (2 SP)
- [ ] TASK-F1-UX-002.3: Aplicação das Leis da Gestalt (2 SP)
- [ ] TASK-F1-UX-002.4: Validação da Arquitetura da Informação (2 SP)

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-002
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 8 Story Points
**Prioridade:** P1
**Épico:** EPIC-F1-UX-001
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-design` `doc`

## 📚 Referências
- [Método LATCH](https://evernote.com/learn/what-is-the-latch-method-method-a-practical-guide)
- [Gestalt Principles](https://www.smashingmagazine.com/2014/03/design-principles-visual-perception-and-the-principles-of-gestalt/)'''
    },
    {
        'id': 'STORY-F1-UX-003',
        'title': 'Auditoria de Acessibilidade (e-MAG 3.1 e WCAG 2.2 AA)',
        'epic_id': 'EPIC-F1-UX-001',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'ux-design', 'test'],
        'story_points': 8,
        'body': '''## 📖 User Story
Como UX Designer, quero realizar uma auditoria completa de acessibilidade do "Censo Fácil" com base no e-MAG 3.1 e WCAG 2.2 AA, garantindo conformidade com os padrões de Governo Digital.

## ✅ Critérios de Aceite
- [ ] 6 áreas do e-MAG auditadas
- [ ] Critérios WCAG 2.2 AA verificados
- [ ] Matriz de conformidade consolidada
- [ ] Plano de mitigação de barreiras

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-003.1: e-MAG - Marcação (1 SP)
- [ ] TASK-F1-UX-003.2: e-MAG - Comportamento (1 SP)
- [ ] TASK-F1-UX-003.3: e-MAG - Conteúdo (1 SP)
- [ ] TASK-F1-UX-003.4: e-MAG - Apresentação/Design (1 SP)
- [ ] TASK-F1-UX-003.5: e-MAG - Multimídia (1 SP)
- [ ] TASK-F1-UX-003.6: e-MAG - Formulário (1 SP)
- [ ] TASK-F1-UX-003.7: WCAG 2.2 AA (2 SP)

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-003
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 8 Story Points
**Prioridade:** P0
**Épico:** EPIC-F1-UX-001
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-design` `test`

## 📚 Referências
- [e-MAG 3.1](https://emag.governoeletronico.gov.br/)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [Ferramenta de Avaliação Gov.br](https://www.gov.br/governodigital/pt-br/plataformas-e-servicos-digitais/ferramenta-de-avaliacao)'''
    },
    {
        'id': 'STORY-F1-ALL-004',
        'title': 'Consolidação e Apresentação da Fase 1',
        'epic_id': 'EPIC-F1-UX-001',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'doc', 'slides'],
        'story_points': 8,
        'body': '''## 📖 User Story
Como coordenador do projeto, quero consolidar todos os entregáveis da Fase 1 em um relatório final e apresentar os resultados para os stakeholders, garantindo alinhamento para a Fase 2.

## ✅ Critérios de Aceite
- [ ] Relatório Consolidado da Fase 1 elaborado
- [ ] Apresentação Executiva preparada
- [ ] Aprovação dos stakeholders (IBGE/SGD)
- [ ] Handoff para a Fase 2

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-ALL-004.1: Elaboração do Relatório Final (4 SP)
- [ ] TASK-F1-ALL-004.2: Apresentação e Validação com Stakeholders (4 SP)

---
## 🏷️ Metadados
**ID:** STORY-F1-ALL-004
**Squad:** All Squads
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 8 Story Points
**Prioridade:** P1
**Épico:** EPIC-F1-UX-001
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `doc` `slides`

## 📚 Referências
- [Ferramenta de Avaliação Gov.br](https://www.gov.br/governodigital/pt-br/plataformas-e-servicos-digitais/ferramenta-de-avaliacao)'''
    }
]

# ============================================================
# FUNÇÕES
# ============================================================

def get_issue_by_title(title):
    """Busca uma issue pelo título"""
    url = f"{BASE_URL}/issues?state=all"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        for issue in response.json():
            if issue['title'] == title:
                return issue
    return None

def close_issue(issue_number, comment):
    """Fecha uma issue com um comentário"""
    # Adicionar comentário
    comment_url = f"{BASE_URL}/issues/{issue_number}/comments"
    requests.post(comment_url, headers=HEADERS, json={'body': comment})
    
    # Fechar a issue
    close_url = f"{BASE_URL}/issues/{issue_number}"
    response = requests.patch(close_url, headers=HEADERS, json={'state': 'closed'})
    return response.status_code == 200

def create_new_issue(title, body, labels, milestone):
    """Cria uma nova issue"""
    url = f"{BASE_URL}/issues"
    
    # Buscar milestone number
    milestone_number = None
    ms_url = f"{BASE_URL}/milestones"
    ms_response = requests.get(ms_url, headers=HEADERS)
    if ms_response.status_code == 200:
        for ms in ms_response.json():
            if ms['title'] == milestone:
                milestone_number = ms['number']
                break
    
    data = {
        'title': title,
        'body': body,
        'labels': labels,
        'milestone': milestone_number
    }
    response = requests.post(url, headers=HEADERS, json=data)
    return response

# ============================================================
# MAIN
# ============================================================

def main():
    print("""
    🔄 ==============================================
       REESCRITA DE STORIES - FASE 1
       De 21 micro-stories → 4 stories de 8 SP
    ==============================================
    """)
    
    # 1. Identificar stories antigas
    old_stories = [
        '[STORY-F1-UX-001.1] Criação da Persona "Seu José" (Produtor Rural)',
        '[STORY-F1-UX-001.2] Criação da Persona "Mariana" (Recenseadora)',
        '[STORY-F1-UX-001.3] Criação da Persona "Carlos" (Agente Censitário de Qualidade - ACQ)',
        '[STORY-F1-UX-001.4] Validação das Personas com Stakeholders',
    ]
    
    print('📌 Passo 1: Fechando stories antigas...')
    print('-' * 60)
    
    for old_title in old_stories:
        issue = get_issue_by_title(old_title)
        if issue:
            comment = f"""
🔁 **ESTA ISSUE FOI REESCRITA**

A estrutura da Fase 1 foi refinada para melhor adequação ao cronograma.

**Nova estrutura:**
- STORY-F1-UX-001: Personas e Jornadas (8 SP)
- STORY-F1-UX-002: Arquitetura da Informação (8 SP)
- STORY-F1-UX-003: Acessibilidade (8 SP)
- STORY-F1-ALL-004: Consolidação (8 SP)

🔗 Consulte as novas issues para continuar o trabalho.
"""
            if close_issue(issue['number'], comment):
                print(f'   ✅ Fechada: #{issue["number"]} - {old_title}')
            else:
                print(f'   ❌ Erro ao fechar: #{issue["number"]}')
        else:
            print(f'   ⚠️ Issue não encontrada: {old_title}')
        time.sleep(0.5)
    
    print()
    print('📌 Passo 2: Criando novas stories (Opção 4)...')
    print('-' * 60)
    
    for story in NEW_STORIES:
        title = f'[{story["id"]}] {story["title"]}'
        result = create_new_issue(
            title=title,
            body=story['body'],
            labels=story['labels'],
            milestone=story['milestone']
        )
        
        if result.status_code == 201:
            print(f'   ✅ Criada: #{result.json()["number"]} - {title}')
        elif result.status_code == 422:
            print(f'   ⚠️ Já existe: {title}')
        else:
            print(f'   ❌ Erro: {result.status_code}')
        time.sleep(0.5)
    
    print()
    print('-' * 60)
    print('✅ REESCRITA CONCLUÍDA!')
    print()
    print('📊 Nova estrutura:')
    print('   ├── STORY-F1-UX-001: Personas e Jornadas (8 SP)')
    print('   ├── STORY-F1-UX-002: Arquitetura da Informação (8 SP)')
    print('   ├── STORY-F1-UX-003: Acessibilidade (8 SP)')
    print('   └── STORY-F1-ALL-004: Consolidação (8 SP)')
    print()
    print('🔗 https://github.com/anandamatos/censo-facil/issues')

if __name__ == '__main__':
    main()