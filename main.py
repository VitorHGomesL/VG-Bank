
from Cliente import *
from Administrador import listar_clientes, deletar_cliente
import random


#Inicia o aplicativo e apresenta as opções para o usuário
def bem_vindo():
    print("")
    print(("#").center(30, "#"))
    print(("BEM VINDO AO VG BANK").center(30, " "))
    print(("#").center(30, "#"))
    print(" ")

#Roda a aplicação enquanto a opção de saída ("0") não é selecionada

def primeiro_acesso():

    while True:
        print('''
Selecione uma das opções:
[1] - Pessoa Física
[2] - Pessoa Jurídica (!!!!!!WYP!!!!!)''')

        __acesso = input("").strip()
        match __acesso:
            case "1":
                try:
                    nome = input("Insira seu nome completo: ")
                    cpf = input("Insira seu CPF (apenas números): ")
                    endereco = input("Insira seu endereço: ")
                    data_nascimento = input("Informe sua data de nascimento: ")
                    numero = random.randint(10000, 99999)
                    novo_usuario = pessoaFisica(endereco, nome, cpf, data_nascimento)
                    print(f'''
Bem vindo, {novo_usuario.nome}!
foram coletados os seguintes dados:
Endereço: {novo_usuario.endereco}
Data de Nascimento: {novo_usuario.data_nascimento}
CPF: {novo_usuario.cpf}
                        
Deseja confirmar?
[1] - Sim, confirmo as informações inseridas
[2] - Desejo retornar para confirmar os dados''')
                    __confirmacao = input("").strip()
                    match __confirmacao:
                        case "1":
                            clientes.append(pessoaFisica.salvar_cliente_PF(novo_usuario.nome, novo_usuario.cpf,novo_usuario.data_nascimento, novo_usuario.endereco))
                            print(f'''
Dados confirmados com sucesso!
Sua conta foi criada sob o número: {numero}''')
                            break
                        case "2":
                            pass
                except ValueError as e:
                    print(f"ATENÇÃO! ERRO!{e.upper()}")
            case _:
                print("Parámetros inválidos, por favor, tente novamente")


def acesso():
    print('''
Deseja realizar o acesso pelo número da conta ou CPF?
[1] - CPF
[2] - Número da conta 
''')
    __acesso = input("").strip()

    if __acesso == "1":
        print("Informe seu CPF(Apenas números):")
        cpf = input("").strip()


def menu_cliente():


    print('''
O que deseja fazer?
[1] - Entrar em uma conta existente
[2] - Criar uma nova conta 
''')
    
    __acesso = input("").strip()

    match __acesso:
        case "1": 
            print ("Entrou em conta existente")
        case "2": 
            pass

def menu_inicial():
    #define as variáveis necessárias para execução da classe main
    acesso = 0

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
                    print("Já é nosso cliente ou deseja abrir uma conta?")
                    print("[1] - Ainda não sou cliente")
                    print("[2] - Já sou cliente")
                    acesso_cliente = input("")
                    match acesso_cliente:
                        case "1":
                            primeiro_acesso()
                        
                        case "2":
                            menu_cliente()
#
#
#
#
#
#
#
#
#
#
#
#
#
#

            #Acesso de administrador("Separado" do resto do código pois será uma implementação futura, para facilitar a visualização das etapas acima)
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

clientes = []
contas = []
bem_vindo()
menu_inicial()
