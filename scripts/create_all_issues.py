#!/usr/bin/env python3
"""
Script unificado para criar Labels e Épicos no GitHub Projects
"""

import os
import sys
import subprocess

def main():
    """Função principal"""
    print('🚀 Iniciando configuração completa do GitHub Projects...')
    print()

    # 1. Criar Labels
    print('📌 Passo 1: Criando Labels...')
    print('-' * 60)
    result = subprocess.run(
        [sys.executable, 'scripts/create_labels.py'],
        capture_output=False
    )
    if result.returncode != 0:
        print('❌ Erro ao criar labels. Abortando.')
        sys.exit(1)
    print()

    # 2. Criar Épicos
    print('📌 Passo 2: Criando Épicos...')
    print('-' * 60)
    result = subprocess.run(
        [sys.executable, 'scripts/create_epic_issues.py'],
        capture_output=False
    )
    if result.returncode != 0:
        print('❌ Erro ao criar épicos. Abortando.')
        sys.exit(1)

    print()
    print('-' * 60)
    print('✅ Configuração completa finalizada!')
    print('🔗 Acesse o projeto em:')
    print('   https://github.com/users/anandamatos/projects/8')


if __name__ == '__main__':
    main()