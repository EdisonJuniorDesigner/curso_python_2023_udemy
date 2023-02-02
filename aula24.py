# Operadores in e not in
# String são iteráveis
#  0 1 2 3 4 5
#  o t á v i o
# -6-5-4-3-2-1

# nome = 'Edison'
# print(nome[2])
# print(nome[-4])
# print('son' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('son' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

variavel_a = 1 or 0
variavel_b = 0 or 1
print(variavel_a, variavel_a)