#02 - Utilizando estruturas de repetição com variável de controle, 
# faça um programa que receba uma string com uma frase informada pelo usuário e 
# conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, 
# depois mostre na tela essa mesma frase sem nenhuma vogal.
from unidecode import unidecode
def d(): #FUNÇÃO CRIADA PARA CHAMAR UMA DECORAÇÃO DE TEXTO SIMPLES.
   print('-=-'*20)
frase = str(input('''Digite uma frase qualquer 
--> : ''')).upper()
frase = unidecode(frase)
vogais = 'AEIOU'
vogais2 = list()
a = 0
e = 0
i = 0
o = 0
u = 0
for v in frase:
    if v == 'A':
        a+=1
    if v == 'E':
        e+=1
    if v == 'I':
        i+=1
    if v == 'O':
        o+=1
    if v == 'U':
        u+=1
for r in frase:
    if r in vogais:
        if r not in vogais2:
            vogais2.append(r)
for p in vogais:
    frase = frase.replace(p, '')        
d()
print('''As vogais nessa frase foram:
--> {}'''.format(sorted(vogais2)))
d()
print('''Foram {} letras "A",
{} letras "E",
{} letras "I",
{} letras "O",
e {} letras "U"'''.format(a,e,i,o,u))
d()
print('''A frsae sem as vogais fica assim:
--> {}'''.format(frase))
d()