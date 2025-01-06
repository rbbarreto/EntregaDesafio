def exibir_poema(data_extenso, *arg , **Kwargs):
    texto = "\n".join(arg)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in Kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Domingo, 10 de novembro de 2024",
    "Zen of python",
    "Beautiful is better than ugly",
    "Explicit is better than complex",
    autor="Tim peter",
    ano=1999)    