
from Cliente import Cliente, cadastrar_usuario
from Administrador import listar_clientes, deletar_cliente

#define as variáveis necessárias para execução da classe main

acesso = 0

#Inicia o aplicativo e apresenta as opções para o usuário
print("")
print(("#").center(30, "#"))
print(("BEM VINDO AO VG BANK").center(30, " "))
print(("#").center(30, "#"))
print(" ")

#Roda a aplicação enquanto a opção de saída ("0") não é selecionada
while acesso != "0":
        
        #Imprime as opções de acesso ao aplicativo e opção de saída
        print(f'''Deseja realizar o acesso como Cliente ou administrador?
[1] - Cliente
[2] - administrador
[0] - Sair''')

        #Coleta a opção selecionada pelo usuário
        acesso = input("").strip()

        #Acesso de cliente
        match acesso:
            case "1":
            #Imprime as opções de usuário(Abrir conta / Realizar acesso)
                print("Deseja abrir uma conta conosco ou entrar em uma conta existente?")
                print("[1] - Abrir conta")
                print("[2] - Entrar em conta existente")
                acesso_cliente = input("")
                match acesso_cliente:
                    case "1":
                        #Executa a função de primeiro acesso do arquivo "Cliente.py", que realiza a coleta dos dados do usuário para preenchimento da classe "cliente"
                        
                        nome = input("Insira seu nome: ")
                        sobrenome = input("Insira seu sobrenome: ")
                        email = input("Insira seu e-mail: ")
                        telefone = input("Insira seu telefone: ")
                        novo_usuario = cadastrar_usuario(nome, sobrenome, email, telefone)
                        
                        #Imprime os dados registrados pelo usuário, e seu saldo(0 por padrão na criação da conta)
                        print(f"Bem vindo, {novo_usuario.nome}, foi registrado o e-mail {novo_usuario.email} e o telefone {novo_usuario.telefone}")
                        print(f"Seu saldo é de R${novo_usuario.saldo}")
                    
                    case "2":
                        print("Acesso de cliente realizado (WIP)")
        
        #Acesso de administrador
            case "2":
                acesso_administrador = "0"
                #Imprime as opções de administrador
                print("Acesso de administrador realizado")
                print("O que deseja fazer?")
                print("(1) Listar usuários")
                print("(2) Deletar cliente")
                acesso_administrador = input("") #Coleta qual opcao de administrador o usuário quer realizar
                if acesso_administrador == "1":
                    listar_clientes()
                elif acesso_administrador == "2":
                    deletar_cliente()
            
            case "0":
                  print("Acesso encerrado")
                  SystemExit
            case _:
                print("Parámetros inválidos, tente novamente")
                print("")

