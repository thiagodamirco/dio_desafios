## Sistema bancário:
#
import datetime

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Saldo
[0] Sair

Informe a opção desejada: """

menu2 = """
Continuar?
[S] Sim
[N] Não

Informe a opção desejada: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
moeda = "R$"

def sacar (valor):
    if saldo >= valor:
        print ("valor sacado")

while True:
    opcao = input (menu)

    if opcao == "1":
        deposito = float(input("Informe o valor do depósito: "))
        if deposito > 0:
            saldo += deposito
            data_transacao = datetime.datetime.now()
            data_lancamento = data_transacao.strftime("%d/%m/%Y %H:%M:%S")
            extrato += f"{data_lancamento} Depósito: {moeda:>5}{deposito:>12.2f}\n"
            print ("Valor depositado com sucesso!")
            continuar = str.upper(input(menu2))
            if continuar == "N":
                print ("obrigado por utilizar nosso banco!")
                break
        else:
            print("Valor inválido, tente novamente")
        
    elif opcao == "2":
        print ("Saque")
        saque = float(input("Informe o valor a ser sacado:"))

        excedeu_saldo = saque >= saldo

        excedeu_limite = saque >= limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo em conta insuficiente.")
        elif excedeu_limite:
            print("Valor limite de saque excecido.")
        elif excedeu_saques:
            print ("Número de saques diário excedido.")

        elif saque > 0:
            saldo -= saque
            data_transacao = datetime.datetime.now()
            data_lancamento = data_transacao.strftime("%d/%m/%Y %H:%M:%S")
            extrato += f"{data_lancamento} Saque: {moeda:>8}{saque:>12.2f}\n"
            numero_saques += 1
            print ("Saque realizado, por favor retire seu dinheiro no caixa")
            continuar = str.upper(input(menu2))
            if continuar == "N":
                print ("obrigado por utilizar nosso banco!")
        else:
            print ("Informação inválida, tente novamente")

    elif opcao == "3":
        texto = " DIO BANK - EXTRATO "
        print (f"\n{texto:#^48}")
        print ("Não foram realizadas movimentações" if not extrato else extrato)
        print (f"Saldo em conta {moeda:>19} {saldo:>12.2f}")
        print ("================================================")
    
    elif opcao == "4":
        print (f"Seu saldo atual é R$ {saldo:>12.2f}")

    elif opcao == "0":
        print ("Obrigado por utilizar nosso sistema!")
        break
    else:
        print ("Opção inválida, por favor selecionar novamente a operação desejada.")



