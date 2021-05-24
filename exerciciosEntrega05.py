""" 05 - Refatore o exercício 2, para que uma função receba a frase, 
faça todo o tratamento necessário e retorne o resultado. 
Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original. """

from unidecode import unidecode #FUNÇÃO RESPONSÁVEL POR REMOVER OS ACENTOS DAS VOGAIS
def d(): #FUNÇÃO CRIADA PARA CHAMAR UMA DECORAÇÃO DE TEXTO SIMPLES.
   print('-=-'*20)
def fra():
    #INPUT PARA RECEBER A FRASE DO USUÁRIO.
    frase = str(input('''Digite uma frase qualquer 
    --> : ''')).upper()#TRANSFORMA A FRASE EM MAIUSCULO
    frase = unidecode(frase)#AQUI REMOVE OS ACENTOS
    vogais = 'AEIOU' #VARIÁVEL PARA ARMAZENAR AS VOGAIS
    lista_de_vogais = list() #LISTA PARA ARMAZENAR AS VOGAIS RETIRADAS DO INPUT
    #VARIÁVEIS ABAIXO SERVEM PARA CONTAGEM DAS LETRAS.
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    #NESSE for A ESTRUTURA IRÁ VERIFICAR CADA LETRA DA FRASE A PROCURA DE VOGAIS...
    for v in frase:
    #SE A LETRA EM QUE O for ESTIVER FOR UM "A" ELEL IRÁ CONTAR MAIS UM NA VARIÁVEL a. E ASSIM POR DIANTE...
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
    # NESTE for A ESTRUTURA IRÁ PERCORRER A FRASE RECEBIDA PELO INPUT.
    for r in frase:
        #SE A LETRA QUE ESTIVER SENDO PECORRIDA ESTIVER NA VARIÁVEL DAS VOGAIS...
        if r in vogais:
            #E SE ESSA LETRA NÃO ESTIVER NA LISTA DE VOGAIS... A FUNÇÃO .append IRÁ ADICIONAR À MESMA.
            if r not in lista_de_vogais: #ESTA CONDIÇÃO SERVE PARA NÃO SE REPETIR VOGAIS NA LISTA DE VOGAIS ENCONTRADAS NA FRASE.
                lista_de_vogais.append(r)
    #NESTE for A ESTRUTURA IRÁ PERCORRER A VARIÁVEL VOGAIS...
    for p in vogais:
        frase = frase.replace(p, '') #A CADA VOGAL PECORRIDA A FUNÇÃO .replace IRÁ SUBSTITUIR A LETRA NA FRASA DO USUÁRIO POR UMA STR VAZIA.        
    d()
    print('''As vogais nessa frase foram:
    --> {}'''.format(sorted(lista_de_vogais))) #NESTE print, A FUNÇÃO sorted ORDENA AS VOGAIS ENCONTRADAS NA FRASE EM ORDEM ALFABÉTICA.
    d()
    #AQUI NESSE PRINT ABAIXO, SERVE PARA INFORMAR QUANTAS LETRAS DE CADA VOGAL FORAM ENCONTRADAS NA FRASE
    print('''Foram {} letras "A",
    {} letras "E",
    {} letras "I",
    {} letras "O",
    e {} letras "U"'''.format(a,e,i,o,u))
    d()
    print('''A frsae sem as vogais fica assim:
    --> {}'''.format(frase))
    d()
    print('Foram retiradas {} letras da frase original'.format(a+e+i+o+u)) #input FORMATADO PARA CONTAR QUANTAS LETRAS FORAM TIRADAS DA FRASE ORIGINAL.
    d()
fra()