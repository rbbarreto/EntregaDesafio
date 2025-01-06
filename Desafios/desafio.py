menu = """

[d] Depositor
[s] Sacar
[e] Extrato
[q] Sair

"""


saldo = 0
limite = 500
Extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True :

    opcao = input(menu)     

    if opcao == "d":
        valor = float(input("informe o valor de deposito: "))   

        if valor > 0:
            saldo += valor
            Extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("operação falhou! O Valor informado e inválido.")

    elif opcao == "s":
        valor = float(input("informe o valor de saque: "))   

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operaçao falhou! você não tem saldo suficiente.")

        if excedeu_limite:
            print("Operaçao falhou! o valor do saque excede o limite.")

        if excedeu_saques:
            print("Operaçao falhou! número máximo de saque excedido.")

        elif valor > 0:
                saldo -= valor
                Extrato += f"Saque R$ {valor:.2f}\n"
                numero_saques += 1
        else:
            print("operação falhou! o valor informado é inválido.")    


    elif opcao == "e":
        print("\n================================Extrato================================")
        print("Não foram realizadas movimentações. " if not Extrato else Extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("=============================================")

    elif opcao == "q":
        break;

    else:
        print("operação inválida, por favor selecione novamente a operação desejada.")



