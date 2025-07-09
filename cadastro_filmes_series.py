# Bibliotecas
from time import sleep as pause
from os import system, name
from banco import conectar_banco, inserir_titulo, buscar_todos_titulos, atualizar_titulo

# Conexão com o banco de dados
conexao, cursor = conectar_banco()

# Lista onde vamos armazenar os títulos cadastrados
titulos = []

# Funções do programa
def limpar_tela():
    # Verifica o sistema operacional e executa o comando adequado
    system("cls" if name == "nt" else "clear")


def cadastrar_titulos(conexao, cursor):
    # Cadastra filmes e series
    limpar_tela()
    while True:
        print("{}".format("Cadastro de novo titulo"))
        while True:
            nome = input("Nome do título: ").strip().title()
            if len(nome) < 1:
                print("Digite um nome valido. Tente novamente!")
            else:
                break
        
        while True:
            tipo = input("Tipo (Filme/Serie): ").strip().title()
            if tipo in ("Filme", "Serie"):
                break
            else:
                print("Digite um tipo valido. Tente novamente!")
    
        while True:
            try:
                ano = int(input("Ano de lançamento: "))
                if ano > 1894:
                    break
                else:
                    print("⚠️ Use um ano apos 1894.")
            except ValueError:
                print("⚠️ Ano inválido. Use uma data válida.")
    
        try:
            inserir_titulo(conexao, cursor, nome, tipo, ano)
            print(f"✅ '{nome}' cadastrado com sucesso no banco de dados!")
            pause(2)
        except Exception as erro:
            print(f"Erro ao salvar no banco de dados: {erro}")

        while True:
            opc = input("Cadastrar um novo título? (Sim/Não): ").strip().lower()
            if opc in ("sim", "s", "não", "nao", "n"):
                break
            print("Opção inválida. Tente novamente.")
            
        if opc in ("não", "nao", "n"):
            print("Retornando ao menu principal")
            pause(2)
            break
        # Obs: usei break aqui porque essa função é chamada exclusivamente pelo menu principal...
# Caso futuramente seja chamada por outros módulos, trocar por return para garantir o encerramento imediato...


def listar_titulos():
    # Lista todos os titulos salvos
    limpar_tela()
    resultados = buscar_todos_titulos(cursor)
    if not resultados:
        print("📪 Nenhum título cadastrado ainda.")
        pause(2)
        return
      
    print(f"{'📋 Lista de Títulos Cadastrados':^50}")
    print("-" * 50)
    print(f"{'Nº':>2}   {'Título':<25} | {'Tipo':<8} | Ano")
    print("-" * 50)
    for i, (id, nome, tipo, ano) in enumerate(resultados, start=1):
        print(f"{i:>2}.  {nome:<25} | {tipo:<8} | {ano}")
    print("-" * 50)
    while True:
        opc = str(input("\nVoltar para o menu principai? (Sim): ")).strip().lower()
        if opc in ("sim", "s"):
            break
        else:
            print("Opção invalida. Tente novamente.")


def atualizar_titulos():
    # Atualiza os titulos salvos
    while True:
        limpar_tela()
        resultados = buscar_todos_titulos(cursor)
        if not resultados:
            print("📪 Nenhum título cadastrado ainda.")
            pause(2)
            return
        print(f"{'📋 Lista de Títulos Cadastrados':^50}")
        print("-" * 50)
        print(f"{'ID':>2}   {'Título':<25} | {'Tipo':<8} | Ano")
        print("-" * 50)
        for i, (id, nome, tipo, ano) in enumerate(resultados):
            print(f"{id:>2}.  {nome:<25} | {tipo:<8} | {ano}")
        print("-" * 50)
        while True:
            try:
                id_escolhido = int(input("Digite o ID do titulo que deseja atualizar: "))
                ids_disponiveis = [id for (id, _, _, _) in resultados]
                if id_escolhido in ids_disponiveis:
                    print("Deixe em branco para manter o valor atual.")
                    novo_nome = str(input("Novo nome: ")).strip().title()
                    novo_tipo = str(input("Novo tipo (Filme/Serie): ")).strip().title()
                    while True:
                        novo_ano = input("Novo ano de lançamento: ")
                        if novo_ano.strip() == "":
                            novo_ano = None
                            break
                        else:
                            try:
                                novo_ano = int(novo_ano)
                                if novo_ano > 1894:
                                    break
                                else:
                                    print("⚠️ Use um ano apos 1894.")
                            except ValueError:
                                print("⚠️ Ano inválido. Use uma data válida.")
                    sucesso = atualizar_titulo(cursor, conexao, id_escolhido, novo_nome or None, novo_tipo or None, novo_ano)
                    if sucesso:
                        print("✅ Titulo atualizado com sucesso!")
                        pause(2)
                        break
                    else:
                        print("⚠️ Nenhuma alteração feita.")
                        break
                else:
                    print("❌ ID não encontrado. Verifique e tente novamente.")
                    pause(2)
            except ValueError:
                print("⚠️ Entrada invalida. Use apenas números.")
                pause(2)
        while True:
            opc = input("Atualizar utro título? (Sim/Não): ").strip().lower()
            if opc in ("sim", "s", "não", "nao", "n"):
                break
            print("⚠️Opção inválida. Tente novamente.")
        if opc in ("não", "nao", "n"):
            print("Retornando ao menu principal")
            pause(2)
            break


def remover_titulos():
    # Remove titulos salvos
    limpar_tela()
    global titulos
    if not titulos:
        print("📪 Nenhum título cadastrado ainda.")
        pause(2)
        return
    listar_titulos()
    try:
        indice = int(input("Digite o número do titulo que deseja removerr: ")) - 1
        if 0 <= indice < len(titulos):
            titulo_removido = titulos.pop(indice)
            print(f"🗑️'{titulo_removido['nome']}' removido com seucesso!")
            pause(2)
        else:
            print("❌ Número invalido.")
            pause(2)
    except ValueError:
        print("⚠️ Entrada invalida. Use apenas números.")
        pause(2)


def exibir_menu():
    # Menu principal do sistema
    limpar_tela()
    print("\n🎬 Sistema de cadastro de Filmes e Séries 🎬 ")
    print("1 - Cadastrar novo título")
    print("2 - Listar todos os títulos")
    print("3 - Atualizar um título")
    print("4 - Remover um título")
    print("5 - Sair")


def main():
    # Programa principal
    while True:
        exibir_menu()
        opcao = int(input("Escolha uma opção de 1 a 5: "))
        if opcao == 1:
            print("Opção de cadastrar títulos selecionada.")
            pause(2)
            cadastrar_titulos(conexao, cursor)
        elif opcao == 2:
            print("Opção de listar títulos selecionada.")
            pause(2)
            listar_titulos()
        elif opcao == 3:
            print("Opção de atulizar título selecionada.")
            pause(2)
            atualizar_titulos()
        elif opcao == 4:
            print("Opção de remover título selecionada.")
            pause(2)
            remover_titulos()
        elif opcao == 5:
            print("Opção de sair selecionada.")
            pause(2)
            break
        else:
            print("Opção inválida. Tente novamente!")
            pause(2)


# Programa princial
main()
