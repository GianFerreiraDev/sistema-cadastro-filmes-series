# Bibliotecas
import re
from getpass import getpass
from time import sleep as pause
from os import system, name
from banco import conectar_banco, inserir_titulo, buscar_todos_titulos, atualizar_titulo, remover_titulo, cadastrar_usuario

# Conexão com o banco de dados
conexao, cursor = conectar_banco()


# Funções do programa
def limpar_tela():
    # Verifica o sistema operacional e executa o comando adequado
    system("cls" if name == "nt" else "clear")


def cabecalho(mensagem):
    # Exibe o cabeçalho com a mensagem centralizada
    limpar_tela()
    print("-" * 50)
    print(f"{mensagem:^50}")
    print("-" * 50)


def cadastrar_titulos_ui(conexao, cursor):
    # Cadastra filmes e series
    while True:
        cabecalho("Cadastro de novo título")
        while True:
            nome = input("Nome do título: ").strip().title()
            if len(nome) < 1:
                print("⚠️ Digite um nome valido. Tente novamente!")
                pause(2)
            else:
                break
        
        while True:
            tipo = input("Tipo (Filme/Serie): ").strip().title()
            if tipo in ("Filme", "Serie"):
                break
            else:
                print("Digite um tipo valido. Tente novamente!")
                pause(2)
    
        while True:
            try:
                ano = int(input("Ano de lançamento: "))
                if ano > 1894:
                    break
                else:
                    print("⚠️ Use um ano apos 1894.")
                    pause(2)
            except ValueError:
                print("⚠️ Ano inválido. Use uma data válida.")
                pause(2)
    
        try:
            inserir_titulo(conexao, cursor, nome, tipo, ano)
            print(f"✅ '{nome}' cadastrado com sucesso no banco de dados!")
            pause(2)
        except Exception as erro:
            print(f"Erro ao salvar no banco de dados: {erro}")
            pause(2)

        while True:
            opc = input("Cadastrar um novo título? (Sim/Não): ").strip().lower()
            if opc in ("sim", "s", "yes", "y", "não", "nao", "not", "no", "n"):
                break
            print("⚠️ Opção inválida. Tente novamente.")
            pause(2)
            
        if opc in ("não", "nao", "not", "no", "n"):
            print("Retornando ao menu principal")
            pause(2)
            break
        # Obs: usei break aqui porque essa função é chamada exclusivamente pelo menu principal...
# Caso futuramente seja chamada por outros módulos, trocar por return para garantir o encerramento imediato...


def listar_titulos_ui():
    # Lista todos os titulos salvos
    resultados = buscar_todos_titulos(cursor)

    cabecalho("📋 Lista de Títulos Cadastrados")
    if not resultados:
        print("📪 Nenhum título cadastrado ainda.")
        pause(2)
        return
    print(f"{'Nº':>2}   {'Título':<25} | {'Tipo':<8} | Ano")
    print("-" * 50)
    for (id, nome, tipo, ano) in resultados:
        print(f"{id:>2}.  {nome:<25} | {tipo:<8} | {ano}")
    print("-" * 50)
    while True:
        opc = str(input("\nVoltar para o menu principal? (Sim): ")).strip().lower()
        if opc in ("sim", "s", "yes", "y"):
            print("Retornando ao menu principal")
            pause(2)
            break
        print("⚠️ Opção invalida. Tente novamente.")
        pause(2)


def atualizar_titulos_ui():
    # Atualiza os titulos salvos
    while True:
        limpar_tela()
        resultados = buscar_todos_titulos(cursor)

        cabecalho("📋 Lista de Títulos Cadastrados")
        if not resultados:
            print("📪 Nenhum título cadastrado ainda.")
            pause(2)
            return
        print(f"{'ID':>2}   {'Título':<25} | {'Tipo':<8} | Ano")
        print("-" * 50)
        for (id, nome, tipo, ano) in resultados:
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
                        pause(2)
                        break
                else:
                    print("❌ ID não encontrado. Verifique e tente novamente.")
                    pause(2)
            except ValueError:
                print("⚠️ Entrada invalida. Use apenas números.")
                pause(2)
        while True:
            opc = input("Atualizar outro título? (Sim/Não): ").strip().lower()
            if opc in ("sim", "s", "yes", "y", "não", "nao", "not", "no", "n"):
                break
            print("⚠️Opção inválida. Tente novamente.")
        if opc in ("não", "nao", "not", "no", "n"):
            print("Retornando ao menu principal")
            pause(2)
            break


def remover_titulos_ui():
    # Remove titulos salvos
    while True:
        resultados = buscar_todos_titulos(cursor)
        try:
            cabecalho("📋 Lista de Títulos Cadastrados")
            if not resultados:
                print("📪 Nenhum título para remover.")
                pause(2)
                return
            
            print(f"{'ID':>2}   {'Título':<25} | {'Tipo':<8} | Ano")
            print("-" * 50)
            
            for (id, nome, tipo, ano) in resultados:
                print(f"{id:>2}.  {nome:<25} | {tipo:<8} | {ano}")
            print("-" * 50)
            indice = int(input("Digite o ID do titulo que deseja remover: "))
            while True:
                confirmação = input(f"Tem certeza que deseja remover o título com ID {indice}? (Sim/Não): ").strip().lower()
                if confirmação in ("sim", "s", "yes", "y", "não", "nao", "not", "no", "n"):
                    break
                print("⚠️ Opção inválida. Tente novamente.")
            if confirmação in ("não", "nao", "n"):
                print("❌ Operação cancelada. Retornando ao menu principal.")
                pause(2)
                return
            if remover_titulo(cursor, conexao, indice):
                print(f"🗑️ Título removido com sucesso!")
                pause(2)
                while True:
                    opc = input("Remover outro título? (Sim/Não): ").strip().lower()
                    if opc in ("sim", "s", "yes", "y", "não", "nao", "not", "no", "n"):
                        break
                    print("⚠️Opção inválida. Tente novamente.")
                    pause(2)
                if opc in ("não", "nao", "n"):
                    print("Retornando ao menu principal")
                    pause(2)
                    return
            else:
                print("❌ ID não encontrado. Verifique e tente novamente.")
                pause(2)
        except ValueError:
            print("⚠️ Entrada invalida. Use apenas números.")
            pause(2)


def cadastrar_usuarios_ui():
    # Função para cadastrar novos usuários

    # Expressão regular para validar e-mail simples e senhas padrão
    padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    padrao_senha = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'

    while True:
        cabecalho("Cadastro de novo usuário")
        
        while True:
            nome = input("Nome do usuário: ").strip().title()
            if len(nome) < 1:
                print("Digite um nome valido. Tente novamente!")
                pause(2)
            else:
                break
        
        while True:
            email = input("E-mail do usuário: ").strip().lower()
            if re.match(padrao_email, email):
                break
            else:
                print("⚠️ E-mail inválido. Tente novamente.")
                pause(2)
        
        while True:
            senha = getpass("Senha do usuário: ").strip()
            if re.match(padrao_senha, senha):
                break
            else:
                print("Senha fraca. A senha precisa ter pelo menos:")
                print("- 8 caracteres")
                print("- 1 letra maiúscula")
                print("- 1 letra minúscula")
                print("- 1 número")
                print("- 1 caractere especial (!@#$...)")
                pause(2)
        while True:
            resp = input("É administrador? (Sim/Não): ").strip().lower()
            if resp in ("sim", "s", "yes", "y"):
                is_admin = True
                break
            elif resp in ("não", "nao", "not", "no", "n"):
                is_admin = False
                break
            else:
                print("⚠️ Opção invalida. Apenas (Sim/Não).")
                pause(2)

        sucesso = cadastrar_usuario(cursor, conexao, nome, email, senha, is_admin)
        if sucesso:
            print(f"✅ Usuário '{nome}' cadastrado com sucesso!")
            pause(2)
        else:
            print(f"❌ Falha: Email já está cadastrado")
            pause(2)
        
        while True:
            opc = input("Cadastrar outro usuário? (Sim/Não): ").strip().lower()
            if opc in ("sim", "s", "yes", "y", "não", "nao", "not", "no", "n"):
                break
            print("⚠️ Opção inválida. Tente novamente.")
            pause(2)
        
        if opc in ("não", "nao", "not", "no", "n"):
            print("Retornando ao menu principal")
            pause(2)
            break


def exibir_menu():
    # Menu principal do sistema
    cabecalho("🎬 Sistema de cadastro de Filmes e Séries 🎬")
    print("1 - Cadastrar novo título")
    print("2 - Listar todos os títulos")
    print("3 - Atualizar um título")
    print("4 - Remover um título")
    print("5 - Cadastrar um usuário")
    print("6 - Sair")


def main():
    # Programa principal
    while True:
        exibir_menu()
        try:
            opcao = int(input("Escolha uma opção de 1 a 6: "))
            if opcao == 1:
                print("Opção de cadastrar títulos selecionada.")
                pause(2)
                cadastrar_titulos_ui(conexao, cursor)
            elif opcao == 2:
                print("Opção de listar títulos selecionada.")
                pause(2)
                listar_titulos_ui()
            elif opcao == 3:
                print("Opção de atualizar título selecionada.")
                pause(2)
                atualizar_titulos_ui()
            elif opcao == 4:
                print("Opção de remover título selecionada.")
                pause(2)
                remover_titulos_ui()
            elif opcao == 5:
                print("Opção de cadastrar usuario selecionada.")
                pause(2)
                cadastrar_usuarios_ui()
            elif opcao == 6:
                print("Encerrando o sistema. Até logo!")
                pause(2)
                break
            else:
                print("Opção inválida. Tente novamente!")
                pause(2)
        except ValueError:
            print("digite um numero inteiro.")
            pause(2)


# Programa principal
main()
