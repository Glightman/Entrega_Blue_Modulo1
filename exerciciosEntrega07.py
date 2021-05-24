""" 07 - Crie um programa onde o usuário possa digitar sete numeroses numéricos e 
cadastre-os em uma lista única que mantenha separados os numeroses pares e ímpares. 
No final, mostre os numeroses pares e ímpares em ordem crescente. """
numeros = [[],[]]
for n in range(1,8):
	num = int(input('Digite o {}° número: '.format(n)))
	if num%2 == 0:
		numeros[0].append(num)
	else:
		numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print('-=-'*10)
print(f'''Pares {numeros[0]}
Impares {numeros[1]}''')
print('-=-'*10)
