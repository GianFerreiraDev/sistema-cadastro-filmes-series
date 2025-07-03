# Bibliotecas
from time import sleep as pause
from os import system, name

# Lista onde vamos armazenar os títulos cadastrados
titulos = []


# Funções do programa
def limpar_tela():
    # Verifica o sistema operacional e executa o comando adequado
    system("cls" if name == "nt" else "clear")


def cadastrar_titulos():
    # Cadastra filmes e series
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
    while True:
        pause(2)
        opc = str(input("Cadastrar um novo título? (Sim/Nao): ")).strip().lower()
        if opc == "nao":
            print("Retornando ao menu principal")
            pause(2)
            break
        elif opc == "sim":
            print("Cadastrando um novo titulo.")
            pause(2)
            cadastrar_titulos()
        else:
            print("Opção invalida. Tente novamente.")


def listar_titulos():
    # Lista todos os titulos salvos
    limpar_tela()
    global titulos
    if not titulos:
        print("📪 Nenhum título cadastrado ainda.")
        pause(2)
        return
        
    print("📋 Lista de Títulos Cadastrados")
    for i, titulo in enumerate(titulos, start=1):
        print(f"{i}. {titulo['nome']} ({titulo['tipo']}, {titulo['ano']})")
    while True:
        opc = str(input("Voltar para o menu principai? (Sim): ")).strip().lower()
        if opc == "sim":
            break
        else:
            print("Opção invalida. Tente novamente.")


def atualizar_titulos():
    # Atualiza os titulos salvos
    limpar_tela()
    global titulos
    if not titulos:
        print("📪 Nenhum título cadastrado ainda.")
        pause(2)
        return
    listar_titulos()
    try:
        indice = int(input("Digite o número do titulo que deseja atualizar: ")) - 1
        print(indice)
        if 0 <= indice < len(titulos):
            print("Deixe em branco se não quiser alterar aquele campo.")
            novo_nome = str(input("Novo nome: ")).strip().title()
            novo_tipo = str(input("Novo tipo (Filme/Serie): ")).strip().title()
            novo_ano = input("Novo ano: ").strip()
            if novo_ano:
                novo_ano = int(novo_ano)
            else:
                novo_ano = None
            
            if novo_nome:
                titulos[indice]["nome"] = novo_nome
            if novo_tipo:
                titulos[indice]["tipo"] = novo_tipo
            if novo_ano is not None:
                titulos[indice]["ano"] = novo_ano
            print("✅ Titulo atualizado com sucesso!")
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
            cadastrar_titulos()
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
        elif opcao == 5:
            print("Opção de sair selecionada.")
            pause(2)
            break
        else:
            print("Opção inválida. Tente novamente!")
            pause(2)


# Programa princial
main()
