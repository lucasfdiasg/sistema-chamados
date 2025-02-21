import os
import json

### GERAL ###

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho():
    print('''
==========================================
===         SISTEMA DE CHAMADOS        ===
==========================================''')

def menu():
    clear_terminal()
    cabecalho()
    opcoes = [1, 2, 3, 4, 5, 0]
    clear_terminal()
    cabecalho()
    print('''\
==| 1 | CADASTRAR CHAMADOS              ==
==| 2 | BUSCAR CHAMADOS                 ==
==| 3 | REMOVER CHAMADOS FINALIZADOS    ==
==| 4 | LISTAR CHAMADOS POR PRIORIDADES ==
==| 5 | EXIBIR ESTATISTICAS             ==
==| 6 | REVERTER OU LIMPAR LISTA        ==
==| 0 | SAIR                            ==
==========================================''')
    
    opcao = input("\n>>>> Escolha uma opção: ")

    
    if opcao not in opcoes:
        print("Opção Inválida!")

    if opcao == 1:
        cadastrar_chamados()
    elif opcao == 2:
        buscar_chamados()
    elif opcao == 3:
        remover_chamados_finalizados()
    elif opcao == 4:
        listar_chamados_por_prioridade()
    elif opcao == 5:
        reverter_ou_limpar_lista()
    elif opcao == 0:
        return

def cadastrar_chamados():
    cabecalho()
    print('''\
===        Cadastro de Chamados        ===
==========================================''')
    

def buscar_chamados():
    ...

def remover_chamados_finalizados():
    ...

def listar_chamados_por_prioridade():
    ...

def exibir_estatisticas():
    ...

def reverter_ou_limpar_lista():
    ...
    

