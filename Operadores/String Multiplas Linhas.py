# Strings de múltiplas linhas são definidas informado 3 aspas
# simples ou dupas durante a atribuição. Elas podem ocupar 
# Várias linhas do código, e todos os espaços em branco são 
# incluídos na string final.

Nome = "RICARDO"

mensagem = f'''
    Olá, meu nome {Nome},
 Eu estou aprendendo Python
       Essa mensagem tem diferentes recuos.  
'''
mensagem2 = f"""
Olá, meu nome {Nome},
Eu estou aprendendo Python
Essa mensagem tem diferentes recuos.  
"""

tela = f'''
  ======================Menu==========================
       1: cadastro 
       2: financeiro
       3: relatorio
       4: Sair
  ======================Menu==========================
'''


print(mensagem2)
print(mensagem)
print(tela)


