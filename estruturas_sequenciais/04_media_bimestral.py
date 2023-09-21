# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

# pedindo as notas bimestrais
nota_1 = float(input('Nota da 1ª prova: '))
nota_2 = float(input('Nota da 2ª prova: '))
nota_3 = float(input('Nota da 3ª prova: '))
nota_4 = float(input('Nota da 4ª prova: '))

# printa a nota média:
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

# printando a média
print(f'A nota média é {media}.')
