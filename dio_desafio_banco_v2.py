## Sistema bancário Versão 2:
#
import datetime
import textwrap #

def menu():
    menu = """\n
    ### DIOBank - Menu ###
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tSaldo
    [5]\tNovo usuário
    [6]\tNova conta
    [7]\tListar contas
    [0]\tSair
    """
    return input(textwrap.dedent(menu))

def continuar():
    return

menu2 = """
Efetuar nova transação?
[S] Sim
[N] Não

Informe a opção desejada: """

def sacar (*, saldo, valor, extrato, limite, numero_saques, limite_saques, moeda):
    excedeu_saldo = valor >= saldo
    excedeu_limite = valor >= limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Saldo em conta insuficiente.")
    elif excedeu_limite:
        print("Valor limite de saque excecido.")
    elif excedeu_saques:
        print ("Número de saques diário excedido.")
    elif valor > 0:
        saldo -= valor
        data_transacao = datetime.datetime.now()
        data_lancamento = data_transacao.strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"{data_lancamento} Saque: {moeda:>8}{valor:>12.2f}\n"
        numero_saques += 1
        print ("Saque realizado, por favor retire seu dinheiro no caixa")
    return saldo, extrato

def depositar (saldo, valor, extrato, /, moeda):
    if valor > 0:
        saldo += valor
        data_transacao = datetime.datetime.now()
        data_lancamento = data_transacao.strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"{data_lancamento} Depósito: {moeda:>5}{valor:>12.2f}\n"
        print ("Valor depositado com sucesso!")
    else:
        print("Valor inválido, tente novamente")
            
    return saldo, extrato

def exibir_saldo (saldo):
    print (f"Seu saldo atual é R$ {saldo:>12.2f}")
    return saldo

def exibir_extrato (saldo, /, *, extrato, moeda):
    texto = " DIO BANK - EXTRATO "
    print (f"\n{texto:#^48}")
    print ("Não foram realizadas movimentações" if not extrato else extrato)
    print (f"Saldo em conta {moeda:>19} {saldo:>12.2f}")
    print ("================================================")

def criar_usuario (usuarios):
    # função criar usuário: lista com nome, data de nascimento, cpf e endereço (logradouro, nro - bairro - cidade/sigla estado), somente os números do CPF deve ser armazenado e não podemos ter dois cadastros com o mesmo CPF
    cpf = input("Informe o CPF: (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF")
        return
    nome = input("informe o nome completo: ")
    data_nascimento = input ("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input ("Informe o endereço (logradourom nro - bairro - cidade/sigla estado): ")

    usuarios.append(({"nome" : nome, "data_nascimento": data_nascimento, "cpf" : cpf, "endereco": endereco}))
    
    print ("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta (agencia, numero_conta, usuarios):
    # função criar conta: armazenar contas em uma lista, conta = Agência (0001), número da conta (sequencial iniciada por 1)e usuário (pode ter mais de 1 usuário mas a conta só pode ter 1 usuário)
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia" : agencia, "numero_conta" : numero_conta, "usuario" : usuario}

def listar_contas (contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        
        print(textwrap.dedent(linha))

def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    moeda = "R$"
    
    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "2":
            print ("Saque")
            valor = float(input("Informe o valor a ser sacado:"))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
            
        elif opcao == "3":
            exibir_extrato(saldo, extrato = extrato)
            
        elif opcao == "4":
            exibir_saldo(saldo)

        elif opcao == "5":
            criar_usuario(usuarios)

        elif opcao == "6":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "7":
            listar_contas(contas)

        elif opcao == "0":
            print ("Obrigado por utilizar nosso sistema!")
            break
        else:
            print ("Opção inválida, por favor selecionar novamente a operação desejada.")

main()
