class Cliente:
    def __init__ (self, nome, sobrenome, email, telefone, saldo = 0):
        self.nome = nome
        self.sobrenome = sobrenome
        self.saldo = saldo
        self.email = email
        self.telefone = telefone

def primeiro_acesso():
    nome = input("Insira seu nome: ")
    sobrenome = input("Insira seu sobrenome: ")
    email = input("Insira seu e-mail: ")
    telefone = input("Insira seu telefone: ")
    novo_usuario = Cliente(nome, sobrenome, email, telefone)
    dados_para_salvar = (f"{novo_usuario.nome}, {novo_usuario.sobrenome}, {novo_usuario.email}, {novo_usuario.telefone}, R${novo_usuario.saldo}\n")
    with open ("usuarios.txt", "a") as arquivo:
        arquivo.write(dados_para_salvar)
    

    return novo_usuario

