"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# Exercício 01 concluído

valor = input('Digite um número interio: ')

try:
    valor_int = int(valor)
    valor_par = valor_int % 2 == 0
    valor_impar = valor_int % 2 != 0
    
    valor_nome = 'Ímpar'
    
    if valor_par:
        valor_nome = 'Par'
    
    print(f'O número que você digitou é {valor_nome}.')
except:
    print('Você não digitou um número inteiro')

# ----------

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# Exercício 02 concluído

horario = input('Qual o horário atual: ')

try:
    horario_int = int(horario)
    
    bom_dia = horario_int >= 0 and horario_int <= 11
    boa_tarde = horario_int >= 12 and horario_int <= 17
    boa_noite = horario_int >= 18 and horario_int <= 23
    
    if bom_dia:
        print("Bom dia")
    elif boa_tarde:
        print("Boa tarde")
    elif boa_noite:
        print("Boa noite")
    else:
        print("Não conheço essa hora")
except:
    print('Você não digitou um número inteiro')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# Exerício 03 concluído

nome = input("Digite seu primeiro nome: ")
tamanho_nome = len(nome)

if tamanho_nome > 1:
    valor_nome = ""

    if tamanho_nome <= 4:
        valor_nome = "curto"
    elif tamanho_nome <= 6:
        valor_nome = "normal"
    else:
        valor_nome = "muito grande"

    print(f"Seu nome é {valor_nome}")
else:
    print("Por favor, digite mais de uma letra")
