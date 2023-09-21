# Faça um Programa que peça dois números e imprima a soma.

# pedindo o primeiro e o segundo número

# Obs.: Cuidado! A função input só retorna `str` (texto),
# ou seja, se o usuário digitar o número 2, o programa vai
# retorna o texto 2 não o número 2. Para transformar o tipo.

num_1_texto = input('Digite o primeiro número: ')
num_2_texto = input('Digite o segundo número: ')

# transformando em número
num_1 = float(num_1_texto)
num_2 = float(num_2_texto)

# calculando a soma
soma = num_1 + num_2 

# printando a soma
print(f'A soma de {num_1} e {num_2} é igual a {soma}.')
