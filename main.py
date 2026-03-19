
from Cliente import Cliente, primeiro_acesso
from Administrador import listar_clientes, deletar_cliente

#define as variáveis necessárias para execução da classe main

acesso = 0

#Inicia o aplicativo e apresenta as opções para o usuário
print("--------------------")
print("BEM VINDO AO VG BANK")
print("--------------------")
print(" ")


while acesso != "1" and acesso != "2":
    
        print("Deseja realizar o acesso como Cliente, ou administrador?")
        print("(1) - Cliente")
        print("(2) - administrador")
        acesso = input("").strip()
        if acesso == "1":
            novo_usuario = primeiro_acesso()
            print(f"Bem vindo, {novo_usuario.nome}, foi registrado o e-mail {novo_usuario.email} e o telefone {novo_usuario.telefone}")
            print(f"Seu saldo é de R${novo_usuario.saldo}")
        elif acesso == "2":
            acesso_administrador = "0"
            print("Acesso de administrador realizado")
            print("O que deseja fazer?")
            print("(1) Listar usuários")
            print("(2) Deletar cliente")
            acesso_administrador = input("")
            if acesso_administrador == "1":
                listar_clientes()
            elif acesso_administrador == "2":
                deletar_cliente()
        else:
            print("Parámetros inválidos, tente novamente")
            print("")

