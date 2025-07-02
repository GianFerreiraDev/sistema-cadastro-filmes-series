# Bibliotecas
from time import sleep as pause
from os import system, name

# Lista onde vamos armazenar os títulos cadastrados
titulos = []


# Funções do programa
def limpar_tela():
    #verifica o sistema operacional e executa o comando adequado
    system("cls" if name == "nt" else "clear")


 cadastrar_titulos():
    limpar_tela()
    nome = str(input("Nome do título: ")).strip().title()
    tipo = str(input("Tipo (Filme/Serie): ")).strip().title()
    ano = int(input("Ano de lançamento: "))
    
    titulo = {
        "nome": nome,
        "tipo": tipo,
        "ano": ano
    }
    
    titulos.append(titulo)
    print(f"✅ '{nome}' cadastrado com sucesso!")
    pause(2)


def exibir_menu():
    limpar_tela()
    print("\n🎬 Sistema de cadastro de Filmes e Séries 🎬 ")
    print("1 - Cadastrar novo título")
    print("2 - Listar todos os títulos")
    print("3 - Atualizar um título")
    print("4 - Remover um título")
    print("5 - Sair")


def main():
    while True:
        exibir_menu()
        opcao = int(input("Escolha uma opção de 1 a 5: "))
        if opcao == 1:
            print("Opção de cadastrar títulos selecionada.")
            pause(2)
            cadastrar_titulos()
        elif opcao == 2:
            print("Opção de listar títulos selecionada.")
            pause(2)
        elif opcao == 3:
            print("Opção de atulizar título selecionada.")
            pause(2)
        elif opcao == 4:
            print("Opção de remover título selecionada.")
            pause(2)
        elif opcao == 5:
            print("Opção de sair selecionada.")
            pause(2)
            break
        else:
            print("Opção inválida. Tente novamente!")
            pause(2)
def cadastrar_titulo():
    nome = str(input("Nome do titulo: ")).strip().title()
    tipo = str(input("Tipo (Filme/série): ")).strip().title()
    ano = int(input("Ano de lançamento: "))


# Programa princial
main()
