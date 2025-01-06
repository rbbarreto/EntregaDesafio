# AND = para ser True tudo te  que ser true
# OR = Para ser true apenas um tem que ser true
saldo = 1000
saque = 250
limite = 200

conta_especial = True

print(saldo >= saque and saldo <= limite)
print(saldo >= saque or saldo <= limite)

exp = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(exp)


