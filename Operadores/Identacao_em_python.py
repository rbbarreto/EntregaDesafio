def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")

    print("obrigado por ser nosso cliente, tenha um bom dia! ") 

def depositar(valor):
    saldo = 500      
    saldo += valor
    print("Deposito feito com sucesso!")

sacar(100)
depositar(100)