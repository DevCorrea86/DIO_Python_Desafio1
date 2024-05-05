import os

menu = '''
|------------------|
|       MENU       |
|------------------|
| [1] DEPÓSITO     |
| [2] SAQUE        |
| [3] EXTRATO      |
| [4] SAIR         |
|------------------|
'''

saldo = 0
extrato = """
|-------------------|
|      EXTRATO      |
|-------------------|
"""
limite = 500
n_saques = 0
LIMITE_SAQUES = 3
SIFRAO = "R$"

while True:
    print(menu)
    opcao = input("Opção do menu: ")

    if opcao == "1":
        deposito = float(input("Informe valor a ser depositado (MAX: R$ 500.00): "))
        if deposito > 500 or deposito <= 0:
            print("Valor deve ser positivo e menor que R$500.00")
        else:
            saldo += deposito
            extrato += f"| Depós: {SIFRAO:>}{deposito:<9.2f}|\n"

    elif opcao == "2":
        saque = float(input("Informe o valor a ser sacado: "))
        if saque > saldo:
            print("Valor excede o valor do saldo!")
        elif n_saques > LIMITE_SAQUES:
            print("Limites de saques diários excedido.")
        else:
            saldo -= saque
            limite += 1
            extrato += f"| Saque: {SIFRAO:>}{saque:<9.2f}|\n"
    elif opcao == "3":
        extrato += f"| Saldo: {SIFRAO:>}{saldo:<9.2f}|\n|-------------------|"
        print(extrato)

    elif opcao == "4":
        break

    else:
        print("Informe uma opção válida!")
