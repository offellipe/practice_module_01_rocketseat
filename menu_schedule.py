import json  # Para salvar e carregar dados em um arquivo


def mostrar_menu():
    print("1. Adicionar Contato | \n"
          "2. Visualizar Contatos | \n"
          "3. Editar Contato | \n"
          "4. Marcar/Desmarcar Favorito | \n"
          "5. Visualizar Favoritos | \n"
          "6. Apagar Contato | \n"
          "0. Sair\n"
          )


def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    favorito = input("Favorito (S/N): ").upper()

    contato = {
        "Nome": nome,
        "Telefone": telefone,
        "Email": email,
        "Favorito": favorito == "S"
        }
    contatos.append(contato)
    print("Contato adicionado com sucesso!")


def visualizar_contatos():
    for i, contato in enumerate(contatos):
        print(f"{i + 1}. {contato['Nome']} - "
              f"{contato['Telefone']} - "
              f"{contato['Email']} - "
              f"{'Favorito' if contato['Favorito'] else ''}\n")


def salvar_contatos():
    with open("contatos.json", "w") as arquivo:
        json.dump(contatos, arquivo)


def carregar_contatos():
    try:
        with open("contatos.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


contatos = carregar_contatos()


def editar_contato():
    visualizar_contatos()
    indice_contato = int(
        input("Digite o número do contato que deseja editar: ")) - 1

    if 0 <= indice_contato < len(contatos):
        novo_nome = input("Novo Nome: ")
        novo_telefone = input("Novo Telefone: ")
        novo_email = input("Novo Email: ")

        contatos[indice_contato]["Nome"] = novo_nome
        contatos[indice_contato]["Telefone"] = novo_telefone
        contatos[indice_contato]["Email"] = novo_email

        print("Contato editado com sucesso!")
        salvar_contatos()
    else:
        print("Índice de contato inválido.")


def marcar_desmarcar_favorito():
    visualizar_contatos()
    indice_contato = int(input("Digite o número do contato que deseja marcar/"
                               "desmarcar como favorito: ")) - 1

    if 0 <= indice_contato < len(contatos):
        contatos[indice_contato]["Favorito"] = not contatos[indice_contato]
        ["Favorito"]
        print("Contato marcado/desmarcado como favorito com sucesso!")
        salvar_contatos()
    else:
        print("Índice de contato inválido.")


def visualizar_favoritos():
    favoritos = [contato for contato in contatos if contato["Favorito"]]
    if favoritos:
        print("Contatos Favoritos:")
        for i, contato in enumerate(favoritos):
            print(f"{i + 1}. {contato['Nome']} - "
                  f"{contato['Telefone']} - "
                  f"{contato['Email']} - "
                  f"{'Favorito' if contato['Favorito'] else ''}\n")
    else:
        print("Nenhum contato favorito.")


def apagar_contato():
    visualizar_contatos()
    indice_contato = int(input(
        "Digite o número do contato que deseja apagar: ")) - 1

    if 0 <= indice_contato < len(contatos):
        del contatos[indice_contato]
        print("Contato apagado com sucesso!")
        salvar_contatos()
    else:
        print("Índice de contato inválido.")


while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        adicionar_contato()
        salvar_contatos()
    elif escolha == "2":
        visualizar_contatos()
    elif escolha == "3":
        editar_contato()
    elif escolha == "4":
        marcar_desmarcar_favorito()
    elif escolha == "5":
        visualizar_favoritos()
    elif escolha == "6":
        apagar_contato()
    elif escolha == "0":
        print("Encerrando o programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
