# Bibliotecas
from time import sleep as pause

def exibir_menu():
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

main()
