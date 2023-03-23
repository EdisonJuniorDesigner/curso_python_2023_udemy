"""
Iterando strings com while
"""

nome = "Luiz Otávio" #Iteráveis
tamanho_nome = len(nome)
contador = 0

while tamanho_nome > contador:
    print("*"+nome[contador], end="")
    contador += 1
    if contador == tamanho_nome:
        print("*")
