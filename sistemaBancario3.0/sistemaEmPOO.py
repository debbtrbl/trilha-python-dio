from abc import ABC, abstractmethod
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_deposito(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nasc, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nasc = data_nasc


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def criar_conta(cls, numero, cliente):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self._saldo
        if valor > saldo:
            print("Saldo insuficiente para saque.")
            return False
        elif valor <= 0:
            print("Valor inválido para saque. Tente novamente.")
            return False
        else:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            return True

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            return True
        else:
            print("Valor inválido para depósito. Tente novamente.")
            return False


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = 0
        for transacao in self.historico.transacoes:
            if isinstance(transacao, Saque):
                numero_saques += 1

        if valor > self._saldo:
            print("Saldo insuficiente para saque.")
            return False
        elif valor > self.limite:
            print(f"Valor do saque excede o limite de R$ {self.limite:.2f}.")
            return False
        elif numero_saques >= self.limite_saques:
            print(f"Limite de saques diários atingido ({self.limite_saques} saques).")
            return False
        elif valor <= 0:
            print("Valor inválido para saque. Tente novamente.")
            return False
        else:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            return True

    def __str__(self):
        return f"""
            Agência: {self.agencia}
            Conta: {self.numero}
            Titular: {self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

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

    @classmethod
    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


clientes = []
contas = []


def buscar_cliente_por_cpf(cpf):
    for cliente in clientes:
        if cliente._cpf == cpf:
            return cliente
    return None


def buscar_conta_por_cpf(cpf):
    for conta in contas:
        if conta.cliente._cpf == cpf:
            return conta
    return None


def menu():
    return """
    ======= Banco Debgital - Menu =======
    [1] Depositar
    [2] Sacar
    [3] Ver Extrato
    [4] Criar usuário
    [5] Criar conta
    [6] Listar usuários
    [7] Listar contas
    [0] Sair
    => """


while True:
    opcao = input(menu())

    match opcao:
        case "1":
            cpf = input("Informe o CPF do cliente: ")
            conta = buscar_conta_por_cpf(cpf)
            if conta:
                valor = float(input("Valor do depósito: R$ "))
                transacao = Deposito(valor)
                transacao.registrar(conta)
            else:
                print("Conta não encontrada.")

        case "2":
            cpf = input("Informe o CPF do cliente: ")
            conta = buscar_conta_por_cpf(cpf)
            if conta:
                valor = float(input("Valor do saque: R$ "))
                transacao = Saque(valor)
                transacao.registrar(conta)
            else:
                print("Conta não encontrada.")

        case "3":
            cpf = input("Informe o CPF do cliente: ")
            conta = buscar_conta_por_cpf(cpf)
            if conta:
                print("=== Extrato ===")
                for t in conta.historico.transacoes:
                    print(f"{t['tipo']}: R$ {t['valor']:.2f} em {t['data']}")
                print(f"Saldo atual: R$ {conta.saldo:.2f}")
            else:
                print("Conta não encontrada.")

        case "4":
            nome = input("Nome: ")
            data_nasc = input("Data de nascimento (DD/MM/AAAA): ")
            cpf = input("CPF: ")
            endereco = input("Endereço (rua, número, bairro, cidade - UF): ")

            if buscar_cliente_por_cpf(cpf):
                print("Já existe cliente com esse CPF.")
            else:
                cliente = PessoaFisica(cpf, nome, data_nasc, endereco)
                clientes.append(cliente)
                print("Cliente criado com sucesso.")

        case "5":
            cpf = input("CPF do cliente: ")
            cliente = buscar_cliente_por_cpf(cpf)
            if cliente:
                numero = len(contas) + 1
                conta = ContaCorrente(numero, cliente)
                cliente.adicionar_conta(conta)
                contas.append(conta)
                print("Conta criada com sucesso.")
            else:
                print("Cliente não encontrado.")

        case "6":
            if not clientes:
                print("Nenhum cliente cadastrado.")
            else:
                print("=== Clientes ===")
                for c in clientes:
                    print(
                        f"{c._nome} - CPF: {c._cpf} - Nasc: {c._data_nasc} - Endereço: {c._endereco}"
                    )

        case "7":
            if not contas:
                print("Nenhuma conta cadastrada.")
            else:
                print("=== Contas ===")
                for conta in contas:
                    print(
                        f"Agência: {conta.agencia} | Conta: {conta.numero} | Cliente: {conta.cliente._nome}"
                    )

        case "0":
            print("Saindo...")
            break

        case _:
            print("Opção inválida. Tente novamente.")

    print()
