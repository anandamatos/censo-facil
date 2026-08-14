#!/usr/bin/env python3
"""
Script para criar as Stories da Fase 1 do Projeto "Censo Fácil"
Baseado na estrutura de épicos e stories validada
"""

import os
import sys
import time
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
    print("❌ ERRO: GITHUB_TOKEN não encontrado!")
    print("   Verifique o arquivo .env na raiz do projeto")
    sys.exit(1)

HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

BASE_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"

# ============================================
# DEFINIÇÃO DAS STORIES - FASE 1
# ============================================

STORIES = [
    # ============================================================
    # EPIC-F1-UX-001: Pesquisa, Personas e Jornadas do Usuário
    # ============================================================
    
    {
        'id': 'STORY-F1-UX-001.1',
        'title': 'Criação da Persona "Seu José" (Produtor Rural)',
        'epic_id': 'EPIC-F1-UX-001',
        'epic_title': 'Pesquisa, Personas e Jornadas do Usuário',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'ux-research', 'doc'],
        'story_points': 3,
        'body': '''## 📖 User Story
Como UX Researcher, quero criar uma persona detalhada do produtor rural para orientar as decisões de design do "Censo Fácil", garantindo que a solução atenda às necessidades reais do público-alvo do Censo Agropecuário.

## ✅ Critérios de Aceite
- [ ] Persona com nome, idade, ocupação e escolaridade definidos
- [ ] Nível de alfabetização digital mapeado (smartphone básico, uso limitado de apps)
- [ ] Dores e necessidades no contexto do Censo identificadas
- [ ] Mapeamento nos 5 planos de Garrett (Estratégia, Escopo, Estrutura, Esqueleto, Superfície)
- [ ] Card da persona criado com foto, citação, bio, objetivos e frustrações
- [ ] Persona validada com stakeholders do IBGE/SGD

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-001.1.1: Levantamento de dados demográficos do produtor rural (IBGE, Censo Agropecuário anterior)
- [ ] TASK-F1-UX-001.1.2: Definição do perfil tecnológico (smartphone básico, conectividade limitada)
- [ ] TASK-F1-UX-001.1.3: Mapeamento de dores e necessidades no contexto do Censo
- [ ] TASK-F1-UX-001.1.4: Aplicação dos 5 planos de Garrett (Estratégia → Superfície)
- [ ] TASK-F1-UX-001.1.5: Criação do card da persona (nome, foto, citação, bio, objetivos, frustrações)
- [ ] TASK-F1-UX-001.1.6: Validação com stakeholders do IBGE

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-001.1
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 3 Story Points
**Prioridade:** P0
**Épico:** EPIC-F1-UX-001
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-research` `doc`

## 📚 Referências e Links de Estudo
- [Manual do Recenseador do Censo Agropecuário (CD-1.09)](https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5723.pdf)
- [Censo Agropecuário 2017 – Resultados Preliminares](https://censoagro2017.ibge.gov.br/)
- [5 Planos de Garrett (The Elements of User Experience)](https://www.jjg.net/elements/)
- [Política Nacional de Desenvolvimento Sustentável dos Povos e Comunidades Tradicionais](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/decreto/d6040.htm)'''
    },
    {
        'id': 'STORY-F1-UX-001.2',
        'title': 'Criação da Persona "Mariana" (Recenseadora)',
        'epic_id': 'EPIC-F1-UX-001',
        'epic_title': 'Pesquisa, Personas e Jornadas do Usuário',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'ux-research', 'doc'],
        'story_points': 3,
        'body': '''## 📖 User Story
Como UX Researcher, quero criar uma persona detalhada da recenseadora para orientar as decisões de design do "Censo Fácil", considerando seu regime de contratação temporária (Lei 8.745/93) e os desafios do trabalho de campo.

## ✅ Critérios de Aceite
- [ ] Persona com nome, idade, perfil profissional definidos
- [ ] Regime de contratação (Lei 8.745/93) contextualizado
- [ ] Fluxo de trabalho em campo mapeado (DMC, setor censitário, entrevistas)
- [ ] Desafios operacionais identificados (offline, navegação, recusas)
- [ ] Mapeamento nos 5 planos de Garrett
- [ ] Card da persona criado e validado

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-001.2.1: Levantamento do perfil do recenseador (contratação temporária - Lei 8.745/93)
- [ ] TASK-F1-UX-001.2.2: Mapeamento do fluxo de trabalho em campo (DMC, setor censitário, entrevistas)
- [ ] TASK-F1-UX-001.2.3: Identificação de desafios operacionais (offline, navegação, recusas)
- [ ] TASK-F1-UX-001.2.4: Aplicação dos 5 planos de Garrett
- [ ] TASK-F1-UX-001.2.5: Criação do card da persona
- [ ] TASK-F1-UX-001.2.6: Validação com stakeholders do IBGE

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-001.2
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 3 Story Points
**Prioridade:** P0
**Épico:** EPIC-F1-UX-001
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-research` `doc`

## 📚 Referências e Links de Estudo
- [Manual do Recenseador do Censo Agropecuário (CD-1.09)](https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5723.pdf)
- [Lei nº 8.745/93 – Contratação Temporária](https://www2.camara.leg.br/legin/fed/lei/1993/lei-8745-9-dezembro-1993-363171-publicacaooriginal-1-pl.html)'''
    },
    {
        'id': 'STORY-F1-UX-001.3',
        'title': 'Criação da Persona "Carlos" (Agente Censitário de Qualidade - ACQ)',
        'epic_id': 'EPIC-F1-UX-001',
        'epic_title': 'Pesquisa, Personas e Jornadas do Usuário',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'ux-research', 'doc'],
        'story_points': 3,
        'body': '''## 📖 User Story
Como UX Researcher, quero criar uma persona detalhada do Agente Censitário de Qualidade (ACQ) para orientar as decisões de design do módulo de auditoria do "Censo Fácil", considerando seu regime como servidor efetivo (Lei 8.112/90).

## ✅ Critérios de Aceite
- [ ] Persona com nome, idade, perfil profissional definidos
- [ ] Regime de servidor efetivo (Lei 8.112/90) contextualizado
- [ ] Fluxo de auditoria e validação de dados mapeado
- [ ] Necessidades de relatórios e indicadores identificadas
- [ ] Mapeamento nos 5 planos de Garrett
- [ ] Card da persona criado e validado

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-001.3.1: Levantamento do perfil do ACQ (servidor efetivo - Lei 8.112/90)
- [ ] TASK-F1-UX-001.3.2: Mapeamento do fluxo de auditoria e validação de dados
- [ ] TASK-F1-UX-001.3.3: Identificação de necessidades de relatórios e indicadores
- [ ] TASK-F1-UX-001.3.4: Aplicação dos 5 planos de Garrett
- [ ] TASK-F1-UX-001.3.5: Criação do card da persona
- [ ] TASK-F1-UX-001.3.6: Validação com stakeholders do IBGE

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-001.3
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 3 Story Points
**Prioridade:** P0
**Épico:** EPIC-F1-UX-001
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-research` `doc`

## 📚 Referências e Links de Estudo
- [Manual do Agente Censitário Supervisor (ACS)](https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5726.pdf)
- [Lei nº 8.112/90 – Regime Jurídico dos Servidores Públicos](https://www2.camara.leg.br/legin/fed/lei/1990/lei-8112-11-dezembro-1990-322161-publicacaooriginal-1-pl.html)'''
    },
    {
        'id': 'STORY-F1-UX-001.4',
        'title': 'Validação das Personas com Stakeholders',
        'epic_id': 'EPIC-F1-UX-001',
        'epic_title': 'Pesquisa, Personas e Jornadas do Usuário',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'ux-research', 'doc'],
        'story_points': 2,
        'body': '''## 📖 User Story
Como UX Researcher, quero validar as personas criadas com stakeholders do IBGE e da SGD/MGI para garantir que estejam alinhadas com a realidade do Censo Agropecuário.

## ✅ Critérios de Aceite
- [ ] Preparação da apresentação das personas
- [ ] Sessão de validação com stakeholders (IBGE/SGD)
- [ ] Coleta de feedback e ajustes
- [ ] Aprovação final das personas

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-001.4.1: Preparação da apresentação das personas
- [ ] TASK-F1-UX-001.4.2: Sessão de validação com stakeholders (IBGE/SGD)
- [ ] TASK-F1-UX-001.4.3: Coleta de feedback e ajustes
- [ ] TASK-F1-UX-001.4.4: Aprovação final das personas

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-001.4
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 2 Story Points
**Prioridade:** P0
**Épico:** EPIC-F1-UX-001
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-research` `doc`'''
    },

    # ============================================================
    # EPIC-F1-UX-002: Jornadas do Usuário e Heurísticas de Nielsen
    # ============================================================

    {
        'id': 'STORY-F1-UX-002.1',
        'title': 'Mapeamento da Jornada do Produtor Rural',
        'epic_id': 'EPIC-F1-UX-002',
        'epic_title': 'Jornadas do Usuário e Heurísticas de Nielsen',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'ux-research', 'doc'],
        'story_points': 2,
        'body': '''## 📖 User Story
Como UX Researcher, quero mapear a jornada do produtor rural no "Censo Fácil" para identificar pontos de contato, emoções e oportunidades de melhoria.

## ✅ Critérios de Aceite
- [ ] Touchpoints do produtor com o sistema identificados
- [ ] Etapas mapeadas: descoberta → login → preenchimento → finalização
- [ ] Diferenciação de estados online/offline
- [ ] Emoções e pontos de dor identificados em cada etapa
- [ ] Mapa da jornada visual criado

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-002.1.1: Identificação dos touchpoints do produtor
- [ ] TASK-F1-UX-002.1.2: Mapeamento das etapas da jornada
- [ ] TASK-F1-UX-002.1.3: Diferenciação de estados online/offline
- [ ] TASK-F1-UX-002.1.4: Identificação de emoções e pontos de dor
- [ ] TASK-F1-UX-002.1.5: Criação do mapa da jornada (visual)

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-002.1
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 2 Story Points
**Prioridade:** P1
**Épico:** EPIC-F1-UX-002
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-research` `doc`

## 📚 Referências e Links de Estudo
- [Manual do Recenseador (CD-1.09)](https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5723.pdf)
- [5 Planos de Garrett (The Elements of User Experience)](https://www.jjg.net/elements/)'''
    },
    {
        'id': 'STORY-F1-UX-002.2',
        'title': 'Mapeamento da Jornada do Recenseador',
        'epic_id': 'EPIC-F1-UX-002',
        'epic_title': 'Jornadas do Usuário e Heurísticas de Nielsen',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'ux-research', 'doc'],
        'story_points': 2,
        'body': '''## 📖 User Story
Como UX Researcher, quero mapear a jornada do recenseador no "Censo Fácil" para identificar pontos de contato, emoções e oportunidades de melhoria.

## ✅ Critérios de Aceite
- [ ] Touchpoints do recenseador com o sistema identificados
- [ ] Etapas mapeadas: login → navegação no setor → entrevista → sincronização
- [ ] Diferenciação de estados online/offline
- [ ] Emoções e pontos de dor identificados em cada etapa
- [ ] Mapa da jornada visual criado

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-002.2.1: Identificação dos touchpoints do recenseador
- [ ] TASK-F1-UX-002.2.2: Mapeamento das etapas da jornada
- [ ] TASK-F1-UX-002.2.3: Diferenciação de estados online/offline
- [ ] TASK-F1-UX-002.2.4: Identificação de emoções e pontos de dor
- [ ] TASK-F1-UX-002.2.5: Criação do mapa da jornada (visual)

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-002.2
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 2 Story Points
**Prioridade:** P1
**Épico:** EPIC-F1-UX-002
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-research` `doc`

## 📚 Referências e Links de Estudo
- [Manual do Recenseador (CD-1.09)](https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5723.pdf)'''
    },
    {
        'id': 'STORY-F1-UX-002.3',
        'title': 'Mapeamento da Jornada do ACQ',
        'epic_id': 'EPIC-F1-UX-002',
        'epic_title': 'Jornadas do Usuário e Heurísticas de Nielsen',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'ux-research', 'doc'],
        'story_points': 2,
        'body': '''## 📖 User Story
Como UX Researcher, quero mapear a jornada do Agente Censitário de Qualidade (ACQ) no módulo de auditoria do "Censo Fácil" para identificar oportunidades de melhoria na validação de dados.

## ✅ Critérios de Aceite
- [ ] Touchpoints do ACQ com o sistema identificados
- [ ] Etapas mapeadas: login → auditoria → validação → aprovação
- [ ] Emoções e pontos de dor identificados em cada etapa
- [ ] Mapa da jornada visual criado

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-002.3.1: Identificação dos touchpoints do ACQ
- [ ] TASK-F1-UX-002.3.2: Mapeamento das etapas da jornada
- [ ] TASK-F1-UX-002.3.3: Identificação de emoções e pontos de dor
- [ ] TASK-F1-UX-002.3.4: Criação do mapa da jornada (visual)

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-002.3
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 2 Story Points
**Prioridade:** P1
**Épico:** EPIC-F1-UX-002
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-research` `doc`

## 📚 Referências e Links de Estudo
- [Manual do Agente Censitário Supervisor (ACS)](https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5726.pdf)'''
    },
    {
        'id': 'STORY-F1-UX-002.4',
        'title': 'Análise das 10 Heurísticas de Nielsen',
        'epic_id': 'EPIC-F1-UX-002',
        'epic_title': 'Jornadas do Usuário e Heurísticas de Nielsen',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'ux-design', 'doc'],
        'story_points': 3,
        'body': '''## 📖 User Story
Como UX Designer, quero avaliar o fluxo do "Censo Fácil" sob as 10 heurísticas de Nielsen para identificar pontos de fricção e definir ações preventivas de design.

## ✅ Critérios de Aceite
- [ ] Aplicação das 10 heurísticas ao fluxo do "Censo Fácil"
- [ ] Identificação de pontos de fricção
- [ ] Definição de ações preventivas de design
- [ ] Relatório consolidado com recomendações

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-002.4.1: Aplicação da Heurística 1: Visibilidade do status
- [ ] TASK-F1-UX-002.4.2: Aplicação da Heurística 2: Correspondência com mundo real
- [ ] TASK-F1-UX-002.4.3: Aplicação da Heurística 3: Controle do usuário
- [ ] TASK-F1-UX-002.4.4: Aplicação da Heurística 4: Consistência
- [ ] TASK-F1-UX-002.4.5: Aplicação da Heurística 5: Prevenção de erros
- [ ] TASK-F1-UX-002.4.6: Aplicação da Heurística 6: Reconhecimento
- [ ] TASK-F1-UX-002.4.7: Aplicação da Heurística 7: Flexibilidade
- [ ] TASK-F1-UX-002.4.8: Aplicação da Heurística 8: Design minimalista
- [ ] TASK-F1-UX-002.4.9: Aplicação da Heurística 9: Diagnóstico de erros
- [ ] TASK-F1-UX-002.4.10: Aplicação da Heurística 10: Ajuda e documentação
- [ ] TASK-F1-UX-002.4.11: Relatório consolidado com recomendações

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-002.4
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 3 Story Points
**Prioridade:** P1
**Épico:** EPIC-F1-UX-002
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-design` `doc`

## 📚 Referências e Links de Estudo
- [10 Heurísticas de Nielsen – NN/g](https://www.nngroup.com/articles/ten-usability-heuristics/)
- [UX Research em Governo Eletrônico (ESDI/UERJ)](https://www.esdi.uerj.br/assets/60131c71d30a78161ca77a0b959818e4/da35ec6b6c8982bcfd253b2c78eb9def.pdf)'''
    },

    # ============================================================
    # EPIC-F1-UX-003: Arquitetura da Informação (LATCH e Gestalt)
    # ============================================================

    {
        'id': 'STORY-F1-UX-003.1',
        'title': 'Mapeamento dos Sistemas de Organização, Rotulagem e Navegação',
        'epic_id': 'EPIC-F1-UX-003',
        'epic_title': 'Arquitetura da Informação (LATCH e Gestalt)',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'ux-design', 'doc'],
        'story_points': 2,
        'body': '''## 📖 User Story
Como UX Designer, quero mapear os sistemas de organização, rotulagem e navegação do questionário do Censo Agropecuário para estruturar a informação de forma lógica e compreensível.

## ✅ Critérios de Aceite
- [ ] Sistemas de Organização (exatos e ambíguos) mapeados
- [ ] Sistemas de Rotulagem definidos (rótulos compreensíveis)
- [ ] Sistemas de Navegação estruturados (posição relativa)
- [ ] Sistemas de Busca especificados (metadados e indexação)

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-003.1.1: Mapeamento dos Sistemas de Organização
- [ ] TASK-F1-UX-003.1.2: Definição dos Sistemas de Rotulagem
- [ ] TASK-F1-UX-003.1.3: Estruturação dos Sistemas de Navegação
- [ ] TASK-F1-UX-003.1.4: Especificação dos Sistemas de Busca

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-003.1
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 2 Story Points
**Prioridade:** P1
**Épico:** EPIC-F1-UX-003
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-design` `doc`

## 📚 Referências e Links de Estudo
- [Information Architecture (Rosenfeld, Morville, Arango)](https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/)
- [Arquitetura da Informação – Sistemas de Organização](https://www.nngroup.com/articles/information-architecture/)'''
    },
    {
        'id': 'STORY-F1-UX-003.2',
        'title': 'Aplicação do Método LATCH ao Questionário',
        'epic_id': 'EPIC-F1-UX-003',
        'epic_title': 'Arquitetura da Informação (LATCH e Gestalt)',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'ux-design', 'doc'],
        'story_points': 3,
        'body': '''## 📖 User Story
Como UX Designer, quero aplicar o método LATCH (Localização, Alfabeto, Tempo, Categoria, Hierarquia) para estruturar os dados do questionário do Censo Agropecuário, otimizando a navegação e compreensão do usuário.

## ✅ Critérios de Aceite
- [ ] Organização dos dados por Localização (espaço geográfico)
- [ ] Organização dos dados por Alfabeto (ordem alfabética)
- [ ] Organização dos dados por Tempo (cronologia)
- [ ] Organização dos dados por Categoria (afinidade temática)
- [ ] Organização dos dados por Hierarquia (importância)
- [ ] Matriz LATCH consolidada criada

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-003.2.1: Organização por Localização
- [ ] TASK-F1-UX-003.2.2: Organização por Alfabeto
- [ ] TASK-F1-UX-003.2.3: Organização por Tempo
- [ ] TASK-F1-UX-003.2.4: Organização por Categoria
- [ ] TASK-F1-UX-003.2.5: Organização por Hierarquia
- [ ] TASK-F1-UX-003.2.6: Criação da Matriz LATCH consolidada

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-003.2
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 3 Story Points
**Prioridade:** P1
**Épico:** EPIC-F1-UX-003
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-design` `doc`

## 📚 Referências e Links de Estudo
- [Método LATCH – Evernote](https://evernote.com/learn/what-is-the-latch-method-method-a-practical-guide)
- [Organizing Things – Dave Gray](https://medium.com/@davegray/organizing-things-1dbc6faf5d79)'''
    },
    {
        'id': 'STORY-F1-UX-003.3',
        'title': 'Aplicação das Leis da Gestalt ao Layout do Formulário',
        'epic_id': 'EPIC-F1-UX-003',
        'epic_title': 'Arquitetura da Informação (LATCH e Gestalt)',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'ux-design', 'doc'],
        'story_points': 2,
        'body': '''## 📖 User Story
Como UX Designer, quero aplicar as leis da Gestalt ao layout do formulário do Censo Agropecuário para otimizar o agrupamento visual de campos complexos e facilitar a compreensão do usuário.

## ✅ Critérios de Aceite
- [ ] Lei da Proximidade aplicada ao layout
- [ ] Lei da Semelhança aplicada ao layout
- [ ] Lei do Fechamento aplicada ao layout
- [ ] Lei da Continuidade aplicada ao layout
- [ ] Lei da Figura-Fundo aplicada ao layout
- [ ] Justificativa técnica de cada escolha documentada

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-003.3.1: Aplicação da Lei da Proximidade
- [ ] TASK-F1-UX-003.3.2: Aplicação da Lei da Semelhança
- [ ] TASK-F1-UX-003.3.3: Aplicação da Lei do Fechamento
- [ ] TASK-F1-UX-003.3.4: Aplicação da Lei da Continuidade
- [ ] TASK-F1-UX-003.3.5: Aplicação da Lei da Figura-Fundo
- [ ] TASK-F1-UX-003.3.6: Justificativa técnica das escolhas

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-003.3
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 2 Story Points
**Prioridade:** P1
**Épico:** EPIC-F1-UX-003
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-design` `doc`

## 📚 Referências e Links de Estudo
- [Design Principles: Visual Perception and Gestalt – Smashing Magazine](https://www.smashingmagazine.com/2014/03/design-principles-visual-perception-and-the-principles-of-gestalt/)
- [Gestalt Principles for Visual UI Design – UX Tigers](https://www.uxtigers.com/post/gestalt-principles)'''
    },
    {
        'id': 'STORY-F1-UX-003.4',
        'title': 'Validação da Arquitetura da Informação com Stakeholders',
        'epic_id': 'EPIC-F1-UX-003',
        'epic_title': 'Arquitetura da Informação (LATCH e Gestalt)',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'ux-research', 'doc'],
        'story_points': 2,
        'body': '''## 📖 User Story
Como UX Designer, quero validar a Arquitetura da Informação do "Censo Fácil" com stakeholders do IBGE para garantir que a estruturação dos dados esteja alinhada com as necessidades do Censo Agropecuário.

## ✅ Critérios de Aceite
- [ ] Preparação da apresentação da Arquitetura da Informação
- [ ] Sessão de validação com stakeholders (IBGE/SGD)
- [ ] Coleta de feedback e ajustes
- [ ] Aprovação final da Arquitetura da Informação

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-003.4.1: Preparação da apresentação
- [ ] TASK-F1-UX-003.4.2: Sessão de validação com stakeholders
- [ ] TASK-F1-UX-003.4.3: Coleta de feedback e ajustes
- [ ] TASK-F1-UX-003.4.4: Aprovação final

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-003.4
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 2 Story Points
**Prioridade:** P1
**Épico:** EPIC-F1-UX-003
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-research` `doc`'''
    },

    # ============================================================
    # EPIC-F1-UX-004: Acessibilidade (e-MAG 3.1 e WCAG 2.2 AA)
    # ============================================================

    {
        'id': 'STORY-F1-UX-004.1',
        'title': 'Auditoria de Acessibilidade – Área de Marcação (e-MAG)',
        'epic_id': 'EPIC-F1-UX-004',
        'epic_title': 'Acessibilidade (e-MAG 3.1 e WCAG 2.2 AA)',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'ux-design', 'test'],
        'story_points': 2,
        'body': '''## 📖 User Story
Como UX Designer, quero realizar uma auditoria na Área de Marcação do e-MAG 3.1 para garantir que o "Censo Fácil" utilize HTML semântico e atributos de acessibilidade corretamente.

## ✅ Critérios de Aceite
- [ ] Uso de elementos HTML semânticos verificado
- [ ] Código válido conforme padrões W3C verificado
- [ ] Uso correto de atributos de acessibilidade verificado
- [ ] Estrutura hierárquica de cabeçalhos verificada
- [ ] IDs únicos e labels associados verificados

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-004.1.1: Verificação de uso de HTML semântico
- [ ] TASK-F1-UX-004.1.2: Verificação de código válido W3C
- [ ] TASK-F1-UX-004.1.3: Verificação de atributos (alt, title, aria-*)
- [ ] TASK-F1-UX-004.1.4: Verificação de hierarquia de cabeçalhos
- [ ] TASK-F1-UX-004.1.5: Verificação de IDs e labels associados

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-004.1
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 2 Story Points
**Prioridade:** P0
**Épico:** EPIC-F1-UX-004
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-design` `test`

## 📚 Referências e Links de Estudo
- [e-MAG 3.1 – Área de Marcação](https://emag.governoeletronico.gov.br/)
- [W3C HTML Validation](https://validator.w3.org/)'''
    },
    {
        'id': 'STORY-F1-UX-004.2',
        'title': 'Auditoria de Acessibilidade – Área de Comportamento (e-MAG)',
        'epic_id': 'EPIC-F1-UX-004',
        'epic_title': 'Acessibilidade (e-MAG 3.1 e WCAG 2.2 AA)',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'ux-design', 'test'],
        'story_points': 2,
        'body': '''## 📖 User Story
Como UX Designer, quero realizar uma auditoria na Área de Comportamento do e-MAG 3.1 para garantir que o "Censo Fácil" seja operável por teclado e forneça feedback claro para ações do usuário.

## ✅ Critérios de Aceite
- [ ] Operabilidade por teclado verificada
- [ ] Feedback para ações do usuário verificado
- [ ] Ausência de conteúdo que pisca rapidamente verificada
- [ ] Visibilidade e lógica do foco de teclado verificada
- [ ] Uso de WAI-ARIA verificado

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-004.2.1: Verificação de operabilidade por teclado
- [ ] TASK-F1-UX-004.2.2: Verificação de feedback visual
- [ ] TASK-F1-UX-004.2.3: Verificação de ausência de piscadas (>3Hz)
- [ ] TASK-F1-UX-004.2.4: Verificação de visibilidade do foco
- [ ] TASK-F1-UX-004.2.5: Verificação de WAI-ARIA

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-004.2
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 2 Story Points
**Prioridade:** P0
**Épico:** EPIC-F1-UX-004
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-design` `test`

## 📚 Referências e Links de Estudo
- [e-MAG 3.1 – Área de Comportamento](https://emag.governoeletronico.gov.br/)
- [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)'''
    },
    {
        'id': 'STORY-F1-UX-004.3',
        'title': 'Auditoria de Acessibilidade – Área de Conteúdo/Informação (e-MAG)',
        'epic_id': 'EPIC-F1-UX-004',
        'epic_title': 'Acessibilidade (e-MAG 3.1 e WCAG 2.2 AA)',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'ux-writing', 'test'],
        'story_points': 1,
        'body': '''## 📖 User Story
Como UX Writer, quero realizar uma auditoria na Área de Conteúdo/Informação do e-MAG 3.1 para garantir que o "Censo Fácil" utilize linguagem clara e forneça alternativas textuais para conteúdos não textuais.

## ✅ Critérios de Aceite
- [ ] Linguagem clara e objetiva verificada
- [ ] Alternativas textuais para conteúdos não textuais verificadas
- [ ] Estrutura lógica do conteúdo verificada
- [ ] Significado não dependente apenas de cor verificado
- [ ] Títulos descritivos para páginas e seções verificados

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-004.3.1: Verificação de linguagem clara
- [ ] TASK-F1-UX-004.3.2: Verificação de alternativas textuais
- [ ] TASK-F1-UX-004.3.3: Verificação de estrutura lógica
- [ ] TASK-F1-UX-004.3.4: Verificação de não dependência de cor
- [ ] TASK-F1-UX-004.3.5: Verificação de títulos descritivos

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-004.3
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 1 Story Point
**Prioridade:** P0
**Épico:** EPIC-F1-UX-004
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-writing` `test`

## 📚 Referências e Links de Estudo
- [e-MAG 3.1 – Área de Conteúdo/Informação](https://emag.governoeletronico.gov.br/)'''
    },
    {
        'id': 'STORY-F1-UX-004.4',
        'title': 'Auditoria de Acessibilidade – Área de Apresentação/Design (e-MAG)',
        'epic_id': 'EPIC-F1-UX-004',
        'epic_title': 'Acessibilidade (e-MAG 3.1 e WCAG 2.2 AA)',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'ux-design', 'test'],
        'story_points': 2,
        'body': '''## 📖 User Story
Como UX Designer, quero realizar uma auditoria na Área de Apresentação/Design do e-MAG 3.1 para garantir contraste mínimo de 4.5:1, redimensionamento de texto e design responsivo.

## ✅ Critérios de Aceite
- [ ] Contraste mínimo 4.5:1 para textos normais verificado
- [ ] Contraste mínimo 3:1 para textos grandes verificado
- [ ] Redimensionamento de texto até 200% verificado
- [ ] Design responsivo para dispositivos verificado
- [ ] Opções de alto contraste disponíveis

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-004.4.1: Verificação de contraste 4.5:1
- [ ] TASK-F1-UX-004.4.2: Verificação de contraste 3:1 (textos grandes)
- [ ] TASK-F1-UX-004.4.3: Verificação de redimensionamento 200%
- [ ] TASK-F1-UX-004.4.4: Verificação de design responsivo
- [ ] TASK-F1-UX-004.4.5: Verificação de opções de alto contraste

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-004.4
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 2 Story Points
**Prioridade:** P0
**Épico:** EPIC-F1-UX-004
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-design` `test`

## 📚 Referências e Links de Estudo
- [e-MAG 3.1 – Área de Apresentação/Design](https://emag.governoeletronico.gov.br/)
- [WCAG 2.2 – Contraste (1.4.3)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum)'''
    },
    {
        'id': 'STORY-F1-UX-004.5',
        'title': 'Auditoria de Acessibilidade – Área de Multimídia (e-MAG)',
        'epic_id': 'EPIC-F1-UX-004',
        'epic_title': 'Acessibilidade (e-MAG 3.1 e WCAG 2.2 AA)',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'ux-design', 'test'],
        'story_points': 1,
        'body': '''## 📖 User Story
Como UX Designer, quero realizar uma auditoria na Área de Multimídia do e-MAG 3.1 para garantir que imagens, vídeos e áudio do "Censo Fácil" sejam acessíveis.

## ✅ Critérios de Aceite
- [ ] Alt descritivos para imagens verificados
- [ ] Legendas e audiodescrição para vídeos verificados
- [ ] Transcrições para áudio verificadas
- [ ] Controles de reprodução para mídias animadas verificados
- [ ] Ausência de reprodução automática verificada

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-004.5.1: Verificação de alt descritivos
- [ ] TASK-F1-UX-004.5.2: Verificação de legendas/vídeos
- [ ] TASK-F1-UX-004.5.3: Verificação de transcrições/áudio
- [ ] TASK-F1-UX-004.5.4: Verificação de controles de reprodução
- [ ] TASK-F1-UX-004.5.5: Verificação de ausência de autoplay

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-004.5
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 1 Story Point
**Prioridade:** P0
**Épico:** EPIC-F1-UX-004
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-design` `test`

## 📚 Referências e Links de Estudo
- [e-MAG 3.1 – Área de Multimídia](https://emag.governoeletronico.gov.br/)'''
    },
    {
        'id': 'STORY-F1-UX-004.6',
        'title': 'Auditoria de Acessibilidade – Área de Formulário (e-MAG)',
        'epic_id': 'EPIC-F1-UX-004',
        'epic_title': 'Acessibilidade (e-MAG 3.1 e WCAG 2.2 AA)',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'ux-design', 'test'],
        'story_points': 2,
        'body': '''## 📖 User Story
Como UX Designer, quero realizar uma auditoria na Área de Formulário do e-MAG 3.1 para garantir que os formulários do "Censo Fácil" tenham rótulos associados, instruções claras e mensagens de erro compreensíveis.

## ✅ Critérios de Aceite
- [ ] Rótulos associados corretamente aos campos verificados
- [ ] Instruções claras para preenchimento verificadas
- [ ] Mensagens de erro compreensíveis verificadas
- [ ] Agrupamento de campos relacionados verificado
- [ ] Navegação lógica entre campos verificada

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-004.6.1: Verificação de rótulos associados
- [ ] TASK-F1-UX-004.6.2: Verificação de instruções claras
- [ ] TASK-F1-UX-004.6.3: Verificação de mensagens de erro
- [ ] TASK-F1-UX-004.6.4: Verificação de agrupamento de campos
- [ ] TASK-F1-UX-004.6.5: Verificação de navegação lógica

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-004.6
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 2 Story Points
**Prioridade:** P0
**Épico:** EPIC-F1-UX-004
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-design` `test`

## 📚 Referências e Links de Estudo
- [e-MAG 3.1 – Área de Formulário](https://emag.governoeletronico.gov.br/)'''
    },
    {
        'id': 'STORY-F1-UX-004.7',
        'title': 'Verificação de Critérios Específicos WCAG 2.2 AA',
        'epic_id': 'EPIC-F1-UX-004',
        'epic_title': 'Acessibilidade (e-MAG 3.1 e WCAG 2.2 AA)',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'ux-design', 'test'],
        'story_points': 2,
        'body': '''## 📖 User Story
Como UX Designer, quero verificar a conformidade do "Censo Fácil" com os critérios específicos da WCAG 2.2 Nível AA, incluindo Target Size, Focus Not Obscured e Accessible Authentication.

## ✅ Critérios de Aceite
- [ ] Critério 2.5.8 (Target Size - 24x24px) verificado
- [ ] Critério 2.4.11 (Focus Not Obscured) verificado
- [ ] Critério 3.3.8 (Accessible Authentication) verificado
- [ ] Critério 3.3.7 (Redundant Entry) verificado
- [ ] Matriz de Conformidade consolidada criada

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-UX-004.7.1: Verificação do Critério 2.5.8
- [ ] TASK-F1-UX-004.7.2: Verificação do Critério 2.4.11
- [ ] TASK-F1-UX-004.7.3: Verificação do Critério 3.3.8
- [ ] TASK-F1-UX-004.7.4: Verificação do Critério 3.3.7
- [ ] TASK-F1-UX-004.7.5: Elaboração da Matriz de Conformidade

---
## 🏷️ Metadados
**ID:** STORY-F1-UX-004.7
**Squad:** UX & Experience
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 2 Story Points
**Prioridade:** P0
**Épico:** EPIC-F1-UX-004
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `ux-design` `test`

## 📚 Referências e Links de Estudo
- [WCAG 2.2 – Critério 2.5.8 (Target Size)](https://www.w3.org/TR/WCAG22/#target-size-minimum)
- [WCAG 2.2 – Critério 2.4.11 (Focus Not Obscured)](https://www.w3.org/TR/WCAG22/#focus-not-obscured-minimum)
- [WCAG 2.2 – Critério 3.3.8 (Accessible Authentication)](https://www.w3.org/TR/WCAG22/#accessible-authentication-minimum)
- [WCAG 2.2 – Critério 3.3.7 (Redundant Entry)](https://www.w3.org/TR/WCAG22/#redundant-entry)'''
    },

    # ============================================================
    # EPIC-F1-ALL-005: Consolidação da Fase 1
    # ============================================================

    {
        'id': 'STORY-F1-ALL-005.1',
        'title': 'Consolidação dos Entregáveis da Fase 1',
        'epic_id': 'EPIC-F1-ALL-005',
        'epic_title': 'Consolidação da Fase 1',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'doc'],
        'story_points': 2,
        'body': '''## 📖 User Story
Como coordenador do projeto, quero consolidar todos os entregáveis da Fase 1 em um relatório único para apresentação aos stakeholders e alinhamento para início da Fase 2.

## ✅ Critérios de Aceite
- [ ] Revisão de todos os documentos da Fase 1 realizada
- [ ] Inconsistências ou lacunas identificadas
- [ ] Relatório Consolidado da Fase 1 elaborado
- [ ] Apresentação preparada para stakeholders

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-ALL-005.1.1: Revisão de todos os documentos
- [ ] TASK-F1-ALL-005.1.2: Identificação de inconsistências/lacunas
- [ ] TASK-F1-ALL-005.1.3: Elaboração do Relatório Consolidado
- [ ] TASK-F1-ALL-005.1.4: Preparação da apresentação

---
## 🏷️ Metadados
**ID:** STORY-F1-ALL-005.1
**Squad:** All Squads
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 2 Story Points
**Prioridade:** P1
**Épico:** EPIC-F1-ALL-005
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `doc`'''
    },
    {
        'id': 'STORY-F1-ALL-005.2',
        'title': 'Revisão e Alinhamento com Stakeholders',
        'epic_id': 'EPIC-F1-ALL-005',
        'epic_title': 'Consolidação da Fase 1',
        'milestone': 'M1 - Fase 1: Pesquisa e Estratégia',
        'labels': ['story', 'fase-1', 'doc'],
        'story_points': 1,
        'body': '''## 📖 User Story
Como coordenador do projeto, quero apresentar o Relatório Consolidado da Fase 1 para stakeholders do IBGE e SGD/MGI para obter aprovação e alinhamento para a Fase 2.

## ✅ Critérios de Aceite
- [ ] Apresentação do Relatório Consolidado para stakeholders
- [ ] Coleta de feedback e ajustes
- [ ] Aprovação final da estratégia de design
- [ ] Handoff para a Fase 2

## 📋 Tarefas (Checklist)
- [ ] TASK-F1-ALL-005.2.1: Apresentação do Relatório
- [ ] TASK-F1-ALL-005.2.2: Coleta de feedback e ajustes
- [ ] TASK-F1-ALL-005.2.3: Aprovação final
- [ ] TASK-F1-ALL-005.2.4: Handoff para a Fase 2

---
## 🏷️ Metadados
**ID:** STORY-F1-ALL-005.2
**Squad:** All Squads
**Fase:** Fase 1
**Tipo:** Story
**Estimativa:** 1 Story Point
**Prioridade:** P1
**Épico:** EPIC-F1-ALL-005
**Responsável:** @executor-unico
**Labels:** `story` `fase-1` `doc`'''
    }
]

# ============================================================
# FUNÇÕES DA API
# ============================================================

def get_milestone_number(title):
    """Busca o número do milestone pelo título"""
    url = f"{BASE_URL}/milestones"
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        for ms in r.json():
            if ms['title'] == title:
                return ms['number']
    return None

def get_epic_number_by_id(epic_id):
    """Busca o número da issue do épico pelo ID"""
    url = f"{BASE_URL}/issues?state=open"
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        for issue in r.json():
            if epic_id in issue['title']:
                return issue['number']
    return None

def create_issue(title, body, labels, milestone_number):
    """Cria uma issue no repositório"""
    url = f"{BASE_URL}/issues"
    data = {
        'title': title,
        'body': body,
        'labels': labels,
        'milestone': milestone_number
    }
    r = requests.post(url, headers=HEADERS, json=data)
    return r

def add_comment(issue_number, body):
    """Adiciona um comentário à issue"""
    url = f"{BASE_URL}/issues/{issue_number}/comments"
    data = {'body': body}
    r = requests.post(url, headers=HEADERS, json=data)
    return r

# ============================================================
# FUNÇÃO PRINCIPAL
# ============================================================

def main():
    print("""
    🚀 ==============================================
       CRIAÇÃO DE STORIES - FASE 1
       Projeto "Censo Fácil" – IBGE 2026
    ==============================================
    """)
    
    print(f"📋 Repositório: {REPO_OWNER}/{REPO_NAME}")
    print(f"📊 Total de Stories: {len(STORIES)}\n")
    
    # Cache
    milestone_cache = {}
    epic_cache = {}
    
    created = 0
    skipped = 0
    
    for story in STORIES:
        print(f"\n📖 Processando: {story['id']}")
        
        # Busca milestone
        if story['milestone'] not in milestone_cache:
            milestone_cache[story['milestone']] = get_milestone_number(story['milestone'])
        
        milestone_number = milestone_cache[story['milestone']]
        if not milestone_number:
            print(f"   ⚠️ Milestone '{story['milestone']}' não encontrado!")
            continue
        
        # Busca épico
        if story['epic_id'] not in epic_cache:
            epic_cache[story['epic_id']] = get_epic_number_by_id(story['epic_id'])
        
        epic_number = epic_cache[story['epic_id']]
        if not epic_number:
            print(f"   ⚠️ Épico '{story['epic_id']}' não encontrado!")
            continue
        
        # Título com ID
        full_title = f"[{story['id']}] {story['title']}"
        
        # Cria a story
        result = create_issue(
            title=full_title,
            body=story['body'],
            labels=story['labels'],
            milestone_number=milestone_number
        )
        
        if result.status_code == 201:
            issue_number = result.json()['number']
            print(f"   ✅ Story criada: #{issue_number} - {full_title}")
            created += 1
            
            # Comentário vinculando ao épico
            comment_body = f"🔗 Esta Story faz parte do Épico #{epic_number} - {story['epic_title']}"
            add_comment(issue_number, comment_body)
            
            time.sleep(1)
            
        elif result.status_code == 422:
            print(f"   ℹ️ Story já existe ou erro de validação")
            skipped += 1
        else:
            print(f"   ❌ Erro ao criar story: {result.status_code}")
            print(f"   {result.text[:200]}")
        
        time.sleep(0.5)
    
    print(f"""
    ==============================================
    ✅ CRIAÇÃO CONCLUÍDA - FASE 1!
    ==============================================
    
    📊 Resumo:
       Stories criadas: {created}
       Stories ignoradas: {skipped}
    
    🔗 Acesse as issues:
    https://github.com/{REPO_OWNER}/{REPO_NAME}/issues
    """)

if __name__ == "__main__":
    main()