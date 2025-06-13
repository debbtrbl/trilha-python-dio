menu = '''
Bem-vindo ao Sistema Bancário!
Selecione uma opção:
1. Depositar
2. Sacar
3. Extrato
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
            valor = float(input("Valor do depósito: R$ "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Valor inválido para depósito. Tente novamente.")
        case "2":
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
        case "3":
            print("=========================================")
            print("Extrato:")
            if not extrato:
                print("Nenhum movimento encontrado.")
            else:
                print(extrato)
            print(f"Saldo atual: R$ {saldo:.2f}")
            print("=========================================")
        case "0":
            print("Saindo...")
            break
        case _:
            print("Opção inválida. Tente novamente.")
    print() 
