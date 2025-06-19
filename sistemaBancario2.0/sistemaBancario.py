clientes = []
contas = []

def sacar(*, saldo, valor, limite, numSaques, lIMITE_SAQUES, extrato):
    valor = float(input("Valor do saque: R$ "))
    if valor > saldo:
        print("Saldo insuficiente para saque.")
    elif valor > limite:
        print(f"Valor do saque excede o limite de R$ {limite:.2f}.")
    elif numSaques >= LIMITE_SAQUES:
        print(f"Limite de saques diários atingido ({LIMITE_SAQUES} saques).")
    elif valor <= 0:
        print("Valor inválido para saque. Tente novamente.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numSaques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

def depositar(saldo, valor, extrato):
    valor = float(input("Valor do depósito: R$ "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito. Tente novamente.")

def extrato(saldo, /, extrato):
    print("=========================================")
    print("Extrato:")
    if not extrato:
        print("Nenhum movimento encontrado.")
    else:
        print(extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=========================================")

def criar_usuario():
    nome = input(str("Nome: "))
    data_nasc = input(str("Data de nascimento (DD/MM/AAAA):  "))
    cpf = input(str("CPF: "))
    endereco = input(str("Endereço: (Rua n° bairro cidade/sigla estado) "))

    if any(cliente['cpf'] == cpf for cliente in clientes):
        print("CPF já cadastrado. Tente novamente.")

    cliente = {
        'nome': nome,
        'data_nasc': data_nasc,
        'cpf': cpf,
        'endereco': endereco
    }
    clientes.append(cliente)
    print("Usuário criado com sucesso!")

def criar_conta():
    agencia = "0001"
    numConta = len(contas) + 1
    cpf = input("CPF do cliente: ")
    dono = None
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            dono = cliente
            break
    if dono:
        nova_conta = {
            'agencia': agencia,
            'numConta': numConta,
            'Cliente': dono
        }
        contas.append(nova_conta)
        print("Conta criada com sucesso!")

def listar_usuarios():
    if not clientes:
        print("Nenhum usuário cadastrado.")
    else:
        print("Usuários cadastrados:")
        for cliente in clientes:
            print(f"Nome: {cliente['nome']}, CPF: {cliente['cpf']}, Data de Nascimento: {cliente['data_nasc']}, Endereço: {cliente['endereco']}")

def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        print("Contas cadastradas:")
        for conta in contas:
            print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numConta']}, Cliente: {conta['Cliente']['nome']}")

menu = '''
Bem-vindo ao Sistema Bancário!
Selecione uma opção:
1. Depositar
2. Sacar
3. Extrato
4. Criar usuário
5. Criar conta
6. Listar usuários
7. Listar contas
0. Sair
'''

saldo = 0.0
limite = 500.0
extrato = ""
numSaques = 0
LIMITE_SAQUES = 3

while True:
    op = input(menu)

    match op:
        case "1":
            sacar(saldo=saldo, valor=0, limite=limite, numSaques=numSaques, lIMITE_SAQUES=LIMITE_SAQUES, extrato=extrato)
        case "2":
            valor = input("Valor do depósito: R$ ")
            depositar(saldo, valor, extrato)
        case "3":
            extrato(saldo, extrato=extrato)
        case "4":
            criar_usuario()
        case "5":
            criar_conta()
        case "6":
            listar_usuarios()
        case "7":
            listar_contas()
        case "0":
            print("Saindo...")
            break
        case _:
            print("Opção inválida. Tente novamente.")
    print() 
