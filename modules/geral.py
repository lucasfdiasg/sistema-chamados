import os
import json

### GERAL ###

## Caminho para o banco de dados
DB = "database/chamados.json"



def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho():
    print('''
==========================================
===         SISTEMA DE CHAMADOS        ===
==========================================''')



def cadastrar_chamados():
    clear_terminal()
    cabecalho()
    print("=== Cadastro de Chamados ===")

    descricao = input("Descrição do chamado: ")
    
    prioridade = ''
    while prioridade not in ('1', '2', '3', '4'):
        prioridade = input("Prioridade ([1] Alta, [2] Média, [3] Normal, [4] Baixa): ").strip()

    prioridades_opcoes = {"1": "ALta",
                          "2": "Média",
                          "3": "Normal",
                          "4": "Baixa"}
    prioridade = prioridades_opcoes[prioridade]    

    try:
        with open(DB, "r", encoding="utf-8") as file:
            chamados = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        chamados = []

    novo_chamado = {
        "id": len(chamados) + 1,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": "aberto"
    }

    chamados.append(novo_chamado)

    with open(DB, "w", encoding="utf-8") as file:
        json.dump(chamados, file, indent=4, ensure_ascii=False)

    print("\n✅ Chamado cadastrado com sucesso!\n")
    input("Pressione Enter para continuar...")

def buscar_chamados():
    clear_terminal()
    cabecalho()
    print("=== Buscar Chamados ===")

    termo = input("Digite o ID ou parte da descrição: ").strip()

    try:
        with open(DB, "r", encoding="utf-8") as file:
            chamados = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        chamados = []

    resultados = [c for c in chamados if termo in str(c["id"]) or termo.lower() in c["descricao"].lower()]

    if not resultados:
        print("\n⚠ Nenhum chamado encontrado.")
        input("\nPressione Enter para continuar...")
        return

    print("\n🔍 Resultados encontrados:")
    for chamado in resultados:
        print(f"ID: {chamado['id']} | {chamado['descricao']} | Prioridade: {chamado['prioridade']} | Status: {chamado['status']}")

    opcao = input("\nDigite o ID do chamado para editar ou pressione Enter para voltar: ").strip()
    
    if not opcao.isdigit():
        return

    id_escolhido = int(opcao)
    chamado_selecionado = next((c for c in chamados if c["id"] == id_escolhido), None)

    if not chamado_selecionado:
        print("\n⚠ ID não encontrado.")
        input("\nPressione Enter para continuar...")
        return

    print(f"\n✏ Editando Chamado ID {chamado_selecionado['id']}")
    print(f"Descrição atual: {chamado_selecionado['descricao']}")
    nova_descricao = input("Nova descrição (ou pressione Enter para manter): ").strip()

    if nova_descricao:
        chamado_selecionado["descricao"] = nova_descricao

    print("\n[1] Em andamento")
    print("[2] Finalizado")
    print("[0] Manter status atual")

    novo_status = input("\nEscolha uma opção para o status: ").strip()

    status_opcoes = {"1": "Em andamento", "2": "Finalizado"}
    if novo_status in status_opcoes:
        chamado_selecionado["status"] = status_opcoes[novo_status]

    # Salvar alterações
    with open(DB, "w", encoding="utf-8") as file:
        json.dump(chamados, file, indent=4, ensure_ascii=False)

    print("\n✅ Chamado atualizado com sucesso!")
    input("\nPressione Enter para continuar...")



def remover_chamados_finalizados():
    clear_terminal()
    cabecalho()
    print("=== Remover Chamados Finalizados ===")

    try:
        with open(DB, "r", encoding="utf-8") as file:
            chamados = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        chamados = []

    chamados_finalizados = [c for c in chamados if c["status"] == "Finalizado"]

    if not chamados_finalizados:
        print("\n⚠ Nenhum chamado finalizado encontrado.")
        input("\nPressione Enter para continuar...")
        return

    print("\n🔍 Chamados finalizados encontrados:")
    for chamado in chamados_finalizados:
        print(f"ID: {chamado['id']} | {chamado['descricao']} | Prioridade: {chamado['prioridade']}")

    confirmar = input("\nTem certeza que deseja remover TODOS os chamados finalizados? (S/N): ").strip().lower()
    if confirmar != "s":
        print("\n❌ Ação cancelada.")
        input("\nPressione Enter para continuar...")
        return

    # Remove apenas os chamados finalizados
    chamados = [c for c in chamados if c["status"] != "Finalizado"]

    # Atualiza o arquivo JSON
    with open(DB, "w", encoding="utf-8") as file:
        json.dump(chamados, file, indent=4, ensure_ascii=False)

    print("\n✅ Chamados finalizados removidos com sucesso!")
    input("\nPressione Enter para continuar...")


def listar_chamados_por_prioridade():
    clear_terminal()
    cabecalho()
    print("=== Lista de Chamados por Prioridade ===")

    try:
        with open(DB, "r", encoding="utf-8") as file:
            chamados = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        chamados = []

    if not chamados:
        print("\n⚠ Nenhum chamado cadastrado.")
        input("\nPressione Enter para continuar...")
        return

    # Definição da ordem de prioridade
    prioridade_ordem = {"Alta": 1, "Média": 2, "Normal": 3, "Baixa": 4}
    
    # Ordenação dos chamados pela prioridade
    chamados.sort(key=lambda c: prioridade_ordem[c["prioridade"]])

    print("\n🔍 Chamados ordenados por prioridade:\n")
    for chamado in chamados:
        print(f"ID: {chamado['id']} | {chamado['descricao']} | Prioridade: {chamado['prioridade']} | Status: {chamado['status']}")

    input("\nPressione Enter para continuar...")


def exibir_estatisticas():
    clear_terminal()
    cabecalho()
    print("=== Estatísticas dos Chamados ===")

    try:
        with open(DB, "r", encoding="utf-8") as file:
            chamados = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        chamados = []

    total_chamados = len(chamados)

    if total_chamados == 0:
        print("\n⚠ Nenhum chamado cadastrado.")
        input("\nPressione Enter para continuar...")
        return

    # Contadores
    finalizados = sum(1 for c in chamados if c["status"] == "Finalizado")
    em_andamento = sum(1 for c in chamados if c["status"] == "Em Andamento")
    abertos = sum(1 for c in chamados if c["status"] == "aberto")

    prioridade_contagem = {
        "Alta": sum(1 for c in chamados if c["prioridade"] == "Alta"),
        "Média": sum(1 for c in chamados if c["prioridade"] == "Média"),
        "Normal": sum(1 for c in chamados if c["prioridade"] == "Normal"),
        "Baixa": sum(1 for c in chamados if c["prioridade"] == "Baixa"),
    }

    # Cálculo de percentuais
    perc_finalizados = (finalizados / total_chamados) * 100
    perc_andamento = (em_andamento / total_chamados) * 100
    perc_abertos = (abertos / total_chamados) * 100

    print("\n📊 Estatísticas Gerais:")
    print(f"🔹 Total de Chamados: {total_chamados}")
    print(f"✅ Finalizados: {finalizados} ({perc_finalizados:.2f}%)")
    print(f"⏳ Em Andamento: {em_andamento} ({perc_andamento:.2f}%)")
    print(f"📂 Abertos: {abertos} ({perc_abertos:.2f}%)")

    print("\n🎯 Estatísticas por Prioridade:")
    for prioridade, quantidade in prioridade_contagem.items():
        percentual = (quantidade / total_chamados) * 100
        print(f"🔸 {prioridade}: {quantidade} ({percentual:.2f}%)")

    input("\nPressione Enter para continuar...")


def reverter_ou_limpar_lista():
    clear_terminal()
    cabecalho()
    print("=== Reverter ou Limpar Lista de Chamados ===")

    try:
        with open(DB, "r", encoding="utf-8") as file:
            chamados = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        chamados = []

    if not chamados:
        print("\n⚠ Nenhum chamado cadastrado.")
        input("\nPressione Enter para continuar...")
        return

    print("\n🔄 O que deseja fazer?")
    print("[1] Reverter a ordem dos chamados")
    print("[2] Limpar todos os chamados")
    print("[0] Cancelar")

    opcao = input("\nDigite sua opção: ").strip()

    if opcao == "1":
        chamados.reverse()
        print("\n✅ Lista de chamados revertida com sucesso!")

    elif opcao == "2":
        confirmacao = input("\n❗ Tem certeza que deseja excluir TODOS os chamados? (S/N): ").strip().lower()
        if confirmacao == "s":
            chamados = []
            print("\n🗑️ Lista de chamados apagada com sucesso!")
        else:
            print("\n❌ Operação cancelada.")

    elif opcao == "0":
        print("\n🔙 Operação cancelada.")

    else:
        print("\n⚠ Opção inválida!")

    # Salvar as mudanças no arquivo JSON
    with open(DB, "w", encoding="utf-8") as file:
        json.dump(chamados, file, indent=4, ensure_ascii=False)

    input("\nPressione Enter para continuar...")


#V.2025.02.24