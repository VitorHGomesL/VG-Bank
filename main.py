from Cliente import *
import random

def menu_acessar_cliente():

    print('''
╔════════════════════════════════════════╗
║         ACESSO À SUA CONTA             ║
╠════════════════════════════════════════╣
║  Como deseja realizar o acesso?        ║
║                                        ║
║  [1] Por CPF                           ║
║  [2] Por número da conta               ║
║  [3] Retornar ao Menu inicial          ║
╚════════════════════════════════════════╝''')
    __acesso = input("Sua escolha: ").strip()

    if __acesso == "1":
        while True:
            print("\n📋 Informe seu CPF (apenas números):")
            cpf = input("CPF: ").strip()
            _cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            cliente = filtrar_cliente(_cpf_formatado, lista_clientes)
            if cliente:
                print(f"\n✅ Acesso realizado com sucesso!\n👤 Bem-vindo(a), {cliente.nome}!")
                return True
            else:
                print("\n❌ Cliente não encontrado. Verifique o CPF e tente novamente.")
    
    if __acesso == "2":
        menu_acessar_conta()

    if __acesso == "3":
        selecao_menu("IN")
def menu_acessar_conta():
    while True:
        numero_conta = input("\n🔢 Informe o número da conta (apenas números): ")
        conta = filtrar_conta_numero(numero_conta, contas)
        if conta:
            print("\n✅ Acesso realizado com sucesso!")
            return conta
        else:
            print("\n❌ Conta não encontrada. Verifique o número e tente novamente.")
            selecao_menu("CL")
            break      

def menu_primeiro_acesso():

    print('''
╔════════════════════════════════════════╗
║         ABERTURA DE CONTA              ║
╠════════════════════════════════════════╣
║  Selecione o tipo de conta:            ║
║                                        ║
║  [1] Pessoa Física                     ║
║  [2] Pessoa Jurídica (em breve)        ║
╚════════════════════════════════════════╝''')

    __acesso = input("Sua escolha: ").strip()
    match __acesso:
        case "1":
            while True:
                try:
                    nome = input("\n👤 Nome completo: ")
                    cpf = input("📋 CPF (apenas números): ")
                    endereco = input("🏠 Endereço completo: ")
                    data_nascimento = input("📅 Data de nascimento (DDMMAAAA): ")
                    novo_usuario = PessoaFisica(endereco = endereco, nome = nome, cpf = cpf, data_nascimento = data_nascimento)
                    print(f'''
╔════════════════════════════════════════╗
║      CONFIRMAÇÃO DE CADASTRO           ║
╠════════════════════════════════════════╣
║  Nome: {novo_usuario.nome:<32} ║
║  CPF: {novo_usuario.cpf:<33} ║
║  Data de Nascimento: {novo_usuario.data_nascimento:<20} ║
║  Endereço: {novo_usuario.endereco[:29]:<29} ║
╠════════════════════════════════════════╣
║  Os dados estão corretos?              ║
║                                        ║
║  [1] Sim, confirmar cadastro           ║
║  [2] Não, corrigir informações         ║
╚════════════════════════════════════════╝''')
                    __confirmacao = input("Sua escolha: ").strip()
                    match __confirmacao:
                        case "1":
                            lista_clientes.append(novo_usuario)
                            print("\n✅ Cadastro realizado com sucesso!")
                            break
                        case "2":
                            pass
                except ValueError as e:
                    print(f"\n⚠️  ATENÇÃO! {str(e).upper()}")
        case _:
            print("\n❌ Opção inválida. Por favor, tente novamente.")


def menu_cliente():

    while True:
        print('''
╔════════════════════════════════════════╗
║           ÁREA DO CLIENTE              ║
╠════════════════════════════════════════╣
║  O que deseja fazer?                   ║
║                                        ║
║  [1] Acessar conta existente           ║
║  [2] Abrir nova conta                  ║
║  [3] Voltar ao menu principal          ║
╚════════════════════════════════════════╝''')
        
        __acesso = input("Sua escolha: ").strip()

        match __acesso:
            case "1": 
                conta = menu_acessar_conta()
                if conta:
                    menu_transacoes(conta)
                break
            case "2": 
                numero = random.randint(10000, 99999)
                criar_conta(numero_conta = numero, contas = contas, clientes = lista_clientes)
            case "3":
                selecao_menu("IN")

def menu_transacoes(conta):
    while True:
        print(f'''
    ╔════════════════════════════════════════╗
    ║            MENU DE OPERAÇÕES           ║
    ╠════════════════════════════════════════╣
    ║💰 Saldo atual: R$ {conta.saldo:>18.2f} ║
    ╠════════════════════════════════════════╣
    ║  Selecione a operação desejada:        ║
    ║                                        ║
    ║  [1] 💳 Realizar depósito              ║
    ║  [2] 💵 Realizar saque                 ║ 
    ║  [3] 🔄 Exibir extrato                 ║                
    ║  [4] 🔄 Transferência (em breve)       ║
    ║  [5] ⬅️  Voltar                        ║
    ╚════════════════════════════════════════╝''')
        __acesso = input("Sua escolha: ").strip()
        match __acesso:
            case "1":
                sucesso_deposito = depositar(conta = conta)
                if sucesso_deposito:
                    print(f"\n✅ Depósito de R$ {conta.saldo:.2f} realizado com sucesso!")
                elif not sucesso_deposito:
                    print("\n⚠️  Operação cancelada pelo usuário")
                else:
                    print("\n❌ Não foi possível concluir o depósito. Por favor, tente novamente.")
            case "2":
                sucesso_saque = sacar(conta = conta)
                if sucesso_saque:
                    print(f"\n✅ Saldo restante: {conta.saldo:.2f}")
                elif not sucesso_saque:
                    print("\n⚠️  Operação cancelada pelo usuário")
                else:
                    print(sucesso_saque)
            case "3":
                exibir_extrato(conta)
            case "4":
                print("\n⚙️  Funcionalidade em desenvolvimento. Aguarde as próximas atualizações!")
                selecao_menu("TR", conta)
            case "5":
                print("\n↩️  Retornando ao menu anterior...")
                selecao_menu("CL")

def menu_inicial():
    menu_selecionado = "IN"

    while True:
            
            print('''
╔════════════════════════════════════════╗
║                                        ║
║          🏦  VG BANK  🏦               ║
║                                        ║
║      Bem-vindo ao seu banco digital!   ║
║                                        ║
╠════════════════════════════════════════╣
║           MENU PRINCIPAL               ║
╠════════════════════════════════════════╣
║  Como deseja acessar o sistema?        ║
║                                        ║
║  [1] 👤 Área do Cliente                ║
║  [2] 🔧 Área Administrativa            ║
║  [0] 🚪 Sair do sistema                ║
╚════════════════════════════════════════╝''')

            menu_selecionado = input("Sua escolha: ").strip()

            match menu_selecionado:
                case "1":
                    print('''
╔════════════════════════════════════════╗
║           ÁREA DO CLIENTE              ║
╠════════════════════════════════════════╣
║  Você já é nosso cliente?              ║
║                                        ║
║  [1] Não, desejo abrir uma conta      ║
║  [2] Sim, já possuo cadastro          ║
╚════════════════════════════════════════╝''')
                    acesso_cliente = input("Sua escolha: ")
                    match acesso_cliente:
                        case "1":
                            menu_primeiro_acesso()
                        
                        case "2":
                            sucesso = menu_acessar_cliente()
                            if sucesso:
                                menu_cliente()
                            else: 
                                print("\n❌ Dados inválidos. Por favor, tente novamente.")
                case "2":
                    acesso_administrador = "0"
                    print('''
╔════════════════════════════════════════╗
║        ÁREA ADMINISTRATIVA             ║
╠════════════════════════════════════════╣
║  Acesso autorizado                     ║
║                                        ║
║  [1] 📋 Listar clientes cadastrados    ║
║  [2] 🗑️  Remover cliente (em breve)    ║
╚════════════════════════════════════════╝''')
                    acesso_administrador = input("Sua escolha: ")
                    if acesso_administrador == "1":
                        print("\n" + "="*50)
                        print("           LISTA DE CLIENTES CADASTRADOS")
                        print("="*50)
                        for cliente in lista_clientes:
                            print(f"\n👤 Nome: {cliente.nome}")
                            print(f"📋 CPF: {cliente.cpf}")
                            print(f"📅 Data de Nascimento: {cliente.data_nascimento}")
                            print("-"*50)
                    elif acesso_administrador == "2":
                        pass
                
                case "0":
                    print("\n👋 Encerrando sistema... Até logo!")
                    break
                case _:
                    print("\n❌ Opção inválida. Por favor, selecione uma opção válida.")

def selecao_menu(menu_selecionado, conta=None):
    match menu_selecionado:
        case "IN":
            menu_inicial()
            
        case "PA":
            menu_primeiro_acesso()
            
        case "CL":
            return menu_acessar_cliente()
            
        case "CO":
            return menu_acessar_conta()
            
        case "TR":
            if conta:
                menu_transacoes(conta)
            else:
                print("\n❌ Erro: É necessário estar logado em uma conta para realizar operações.")
                
        case "AD":
            print("\n⚙️  Acessando área administrativa... (em desenvolvimento)")
            
        case _:
            print("\n❌ Código de menu inexistente.")


    

lista_clientes = []
contas = []
cliente = ""
menu_selecionado = "IN"
'''
═══════════════════════════════════════════════════════════
                    ÍNDICE DE MENUS
═══════════════════════════════════════════════════════════
IN  - Menu Inicial (Principal)
PA  - Menu de Primeiro Acesso (Cadastro)
CL  - Menu de Acesso por Cliente
CO  - Menu de Acesso por Conta
TR  - Menu de Transações (Operações Bancárias)
AD  - Menu Administrativo (em desenvolvimento)
═══════════════════════════════════════════════════════════
'''
tester = PessoaFisica(endereco = "Rua do Teste nº 50", nome = "Testador", cpf = "12345678900", data_nascimento = "01012001")
lista_clientes.append(tester)

menu_inicial()
