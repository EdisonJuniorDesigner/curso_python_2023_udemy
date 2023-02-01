# Operadores lógicos
# and (e) or(ou) not(não)

# Exemplo AND
entrada = input('[E}ntra [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# ---------------

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)