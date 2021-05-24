#05 - Refatore o exercício 2, para que uma função receba a frase, 
# faça todo o tratamento necessário e retorne o resultado. 
# Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.

from unidecode import unidecode
def d(): #FUNÇÃO CRIADA PARA CHAMAR UMA DECORAÇÃO DE TEXTO SIMPLES.
   print('-=-'*20)
frase = str(input('''Digite uma frase qualquer 
--> : ''')).upper()
def vog(x):
    x = unidecode(x)
    vogais = 'AEIOU'
    vogais2 = list()
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for v in x:
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
    for r in x:
        if r in vogais:
            if r not in vogais2:
                vogais2.append(r)
    for p in vogais:
        x = x.replace(p, '')        
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
    print('''A frase sem as vogais fica assim:
    --> {}'''.format(x))
    d()
    print('Foram retiradas {} letras da frase original'.format(a+e+i+o+u))
    d()
vog(frase)