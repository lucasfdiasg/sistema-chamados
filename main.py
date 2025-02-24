import json
from modules.geral import *

sair = False

def menu():
    clear_terminal()
    cabecalho()
    opcoes = ["1", "2", "3", "4", "5", "6", "0"] 

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
        input("Pressione Enter para continuar...")
        return False

    if opcao == "1":
        cadastrar_chamados()
    elif opcao == "2":
        buscar_chamados()
    elif opcao == "3":
        remover_chamados_finalizados()
    elif opcao == "4":
        listar_chamados_por_prioridade()
    elif opcao == "5":
        exibir_estatisticas()
    elif opcao == "6":
        reverter_ou_limpar_lista()
    elif opcao == "0":
        return True

    return False

while not sair:
    sair = menu()
