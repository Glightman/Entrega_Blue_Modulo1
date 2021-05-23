#01 - Utilizando estruturas condicionais faça um programa
# que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, 
   # divida pelo resultado da divisão inteira e mostre o resultado na tela. 
   # Se não, mostre que a multiplicação não foi maior que 40.

def d():
   print('-=-'*20)
d()
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
d()
print('--> A soma desses números é igua a {}'.format(num1+num2))
print('--> A multiplicação entre esses números é igual a {}'.format(num1*num2))
d()
if num1>num2:
   print('--> O {} é o maior'.format(num1))
   print('--> A divisão inteira do primeiro número pelo segundo é igual a {}'.format(num1//num2))
   resultado = (num1*num2)/(num1//num2)
else:
   print('--> O {} é o maior'.format(num2))
   print('--> A divisão inteira do segundo número pelo primeiro é igual a {}'.format(num2//num1))
   resultado = (num1*num2)/(num2//num1)
if (num1+num2)%2==0:
   print('--> A soma entre os dois números é par')
else:
   print('A soma entre os dois números é ímpar')
if num1*num2>40:
   print('''--> O resultado da divisão entre 
   a multiplicação dos dois números e a divisão inteira dos mesmos é igual a {}'''.format(resultado))
else:
   print('--> A multiplicação entre os números não foi maior que 40')
d()
