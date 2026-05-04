import textwrap 
from abc import ABC, abstractmethod
from datetime import datetime

#################################################################
#####------------------------CLASSES------------------------#####
#################################################################

class Conta:
    def __init__(self, cliente, numero):
        self._saldo = 0
        self._cliente = cliente
        self._agencia = "0001"
        self._numero = numero
        self._historico = Historico()
        self._saques_realizados = 0

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)    

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):

        if not isinstance(valor, (int, float)):
            raise ValueError("Favor inserir um número")

        if self._saldo < 0:
            self._saldo = 0

        valor = float(valor)            
        self._saldo = valor

    @property
    def numero_conta(self):        
        return f"{self._agencia}/{self._numero}"
    
    def sacar(self, valor):
        if self._saldo < valor:
            print("\n❌ Operação negada: Saldo insuficiente para realizar este saque.")
            return False

        if self._saldo > valor:
            self._saldo -= valor
            print(f"\n✅ Saque no valor de R${valor:.2f} realizado com sucesso!")
            self._saques_realizados +=1
            return True
        
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n✅ Depósito realizado com sucesso!")
            return True
        else:
            print("\n❌ Valor inválido. Por favor, insira um valor positivo.")
            return False

    def __str__(self):
        return f"""\
            Agência:\t{self._agencia}
            C/C:\t\t{self._numero}
            Titular:\t{self._cliente.nome}
        """

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite, limite_saques):
        super().__init__(cliente, numero)
        self._limite = limite
        self._limite_saques = limite_saques
    @classmethod
    def nova_conta(cls, cliente, numero, limite = 500, limite_saques=3):
        return cls(cliente, numero, limite, limite_saques)

    def sacar(self, valor):
        
        if valor > self._limite:
            print("\n❌ Operação negada: Limite da conta insuficiente para realizar este saque.")
            return False        

        if self._saques_realizados >= self._limite_saques:
            print("\n❌ Operação negada: Sem saques restantes")
            return False
        
        return super().sacar(valor)       
        

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self, valor):
        if len(valor) < 5:
            raise ValueError(f"{valor} é muito curto. Por favor, informe o endereço completo (Rua, número, bairro, cidade e estado)")
        if not any(char.isdigit() for char in valor):
            raise ValueError("Endereço incompleto. Por favor, inclua o número do logradouro")
        self._endereco = valor

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, endereco, nome, cpf, data_nascimento):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
    
    @property
    def cpf(self):
        if len(self._cpf) != 11:
            return "CPF Inválido - formato esperado: 11 dígitos numéricos"
        
        return f"{self._cpf[:3]}.{self._cpf[3:6]}.{self._cpf[6:9]}-{self._cpf[9:]}"

    @cpf.setter
    def cpf(self, valor):
        if len(valor) != 11:
            raise ValueError(f"CPF inválido. Digite exatamente 11 dígitos numéricos, sem pontos ou traços. Valor informado: {valor}")
        if not valor.isdigit():
            raise ValueError("CPF inválido. Use apenas números, sem pontos, traços ou espaços")
        self._cpf = valor

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        if len(valor) <= 2:
            raise ValueError("Nome muito curto. Digite seu nome completo (mínimo 3 caracteres)")
        if not all(c.isalpha() or c.isspace() for c in valor):
            raise ValueError("Nome inválido. Use apenas letras e espaços, sem números ou caracteres especiais")
        self._nome = valor

    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, valor):
        if len(valor) != 8:
            raise ValueError("Data inválida. Use o formato DDMMAAAA (exemplo: 15031990)")
        if int(valor[4:]) > (datetime.today().year - 18):
            raise ValueError("Idade insuficiente. É necessário ter no mínimo 18 anos para abrir uma conta")
        self._data_nascimento = f"{valor[0:2]}/{valor[2:4]}/{valor[4:8]}"

class Historico:
    def __init__(self):
        self.transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    @transacoes.setter
    def transacoes(self, valor):
        self._transacoes = valor
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, valor):
        if valor < 0:
            raise ValueError("Valor de saque inválido. O valor deve ser positivo")
        
    def registrar(self, conta):
        sucesso = conta.sacar(self._valor)
        if sucesso:
            conta._historico.adicionar_transacao(self)
            return "Saque realizado com sucesso!"
        else :
            return "Não foi possível realizar o saque"

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, valor):
        if valor < 0:
            raise ValueError("Valor de depósito inválido. O valor deve ser positivo")
        
    def registrar(self, conta):
        sucesso = conta.depositar(self._valor)
        if sucesso:
            conta._historico.adicionar_transacao(self)
            return "Depósito realizado com sucesso!"
        else:
            return "Não foi possível realizar o depósito"
        
#################################################################
#####----------------------UTILIÁRIOS-----------------------#####
#################################################################
def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def filtrar_conta_numero(numero_buscado, lista_contas):

    for conta in lista_contas:

        if str(conta._numero) == str(numero_buscado):
            return conta
        
    return None

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

def depositar(conta):
    valor = float(input("💰 Qual valor deseja depositar? R$ "))
    __autorizacao_deposito = input(f'''
╔════════════════════════════════════════╗
║       CONFIRMAÇÃO DE DEPÓSITO          ║
╠════════════════════════════════════════╣
║  Valor: R$ {valor:>28.2f} ║
╠════════════════════════════════════════╣
║  [1] Confirmar operação                ║
║  [2] Cancelar e digitar novo valor     ║
╚════════════════════════════════════════╝
Sua escolha: ''')
    match __autorizacao_deposito: 
        case "1":
            transacao = Deposito(valor)
            transacao.registrar(conta)
            return True
        case "2":
            return False
        case _:
            print("\n⚠️  Opção inválida selecionada")
            return True

def sacar(conta):
        valor = float(input("💵 Qual valor deseja sacar? R$ "))
        __autorizacao_saque = input(f'''
╔════════════════════════════════════════╗
║         CONFIRMAÇÃO DE SAQUE           ║
╠════════════════════════════════════════╣
║  Valor: R$ {valor:>28.2f} ║
╠════════════════════════════════════════╣
║  [1] Confirmar operação                ║
║  [2] Cancelar e digitar novo valor     ║
╚════════════════════════════════════════╝
Sua escolha: ''')
        match __autorizacao_saque: 
            case "1":
                transacao = Saque(valor)
                transacao.registrar(conta)
                return True
            case "2":
                return False
        
def exibir_extrato(conta):
    print('''
╔════════════════════════════════════════╗
║          EXTRATO BANCÁRIO              ║
╠════════════════════════════════════════╣''')
    
    transacoes = conta._historico._transacoes
    
    if not transacoes:
        print('''║                                        ║
║  📭 Nenhuma movimentação realizada     ║
║                                        ║''')
    else:
        for transacao in transacoes:
            tipo = transacao["tipo"]
            valor = transacao["valor"]
            data = transacao["data"]
            
            if tipo == "Saque":
                print(f'''║                                        ║
║  💵 Saque                              ║
║  Valor: R$ {valor:>5.2f} ║
║  Data: {data:<29} ║''')
            else:
                print(f'''║                                        ║
║  💰 Depósito                           ║
║  Valor: R$ {valor:>5.2f} ║
║  Data: {data:<29} ║''')
    
    print(f'''╠════════════════════════════════════════╣
║  💳 Saldo atual: R$ {conta.saldo:>17.2f} ║
╚════════════════════════════════════════╝
''')    