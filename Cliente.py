from abc import ABC, abstractmethod
from datetime import date

class Conta:
    def __init__(self, conta, numero):
        self._saldo = 0
        self._conta = conta
        self._agencia = "0001"
        self._numero = numero
        self._historico = Historico()
        

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        
        if isinstance(valor, int):
            valor = float(valor)
            self._saldo = valor
        elif not isinstance(valor, (int, float)):
            raise ValueError("Favor inserir um número")
        else:
            self._saldo = valor

    @property
    def numero_conta(self):
        numero_conta = f"{self._agencia}/{self._numero}"
        return numero_conta


class contaCorrente(Conta):
    def __init__(self, limite, limite_saques):
        self._limite = limite
        self._limite_saques = limite_saques
    


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao():
        pass
    def adicionar_conta(self, Conta = Conta):
        pass


class pessoaFisica(Cliente):
    def __init__(self, endereco, nome, cpf, data_nascimento):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
    
    @property
    def cpf(self):
        if len(self._cpf) != 11:
            return f"CPF Inválido, favor inserir 11 digitos, sem . ou -"
        
        return f"{self._cpf[:3]}.{self._cpf[3:6]}.{self._cpf[6:9]}-{self._cpf[9:]}"

    @cpf.setter
    def cpf(self, valor):
        if len(valor) != 11:
            raise ValueError(f"CPF Inválido, favor selecione 2 abaixo e retorne, digite apenas os 11 digitos, sem . ou -, valor inserido: {self._cpf}")
        if not valor.isdigit():
            raise ValueError("Insira somente números no CPF")
        self._cpf = valor

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        if len(valor) <= 2:
            raise ValueError("Mínimo de 3 letras no nome")
        if not all(c.isalpha() or c.isspace() for c in valor):
            raise ValueError("Cáracteres especiais não são aceitos")
        self._nome = valor

    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, valor):
        if len(valor) != 8:
            raise ValueError("Insira uma data válida")
        if int(valor[4:]) > (date.today().year - 18):
            raise ValueError("Muito novo para abrir uma conta")
        if len(valor) == 8:
            self._data_nascimento = f"{valor[0:2]}/{valor[2:4]}/{valor[4:8]}"

    
    def salvar_cliente_PF(nome, cpf, data_nascimento, endereco):
        dados_para_salvar = f'"nome":{nome}, "cpf":{cpf}, "data_nascimento":{data_nascimento}, "endereco":{endereco}, "numero": {Conta().numero_conta}'
        return dados_para_salvar


class Historico:
    pass

class Transacao(ABC):
    pass

class Saque(Transacao):
    pass

class Deposito(Transacao):
    pass