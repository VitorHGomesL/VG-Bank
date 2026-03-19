from Cliente import Cliente


def listar_clientes():
    with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

def deletar_cliente():
    print("Teste de deletar")