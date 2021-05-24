""" 04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA 
e devolva uma string no formato DD de mesPorExtenso de AAAA. 
Opcional: valide a data e retorne 'data inválida' caso a data seja inválida. """

def date_on(x,y,z): #FUNÇÃO CRIADA PARA FAZER A FORMATAÇÃO DA DATA, RECEBENDO COMO PARÂMETRO: 
#X PARA DIA, Y PARA MES E Z PARA ANO.
    diaList = list() #LISTA PARA ARMAZENAR OS DIAS VÁLIDOS DE 1 À 31.
    mesList = list() #LISTA PARA ARMAZENAR OS MESES VÁLIDOS DE 1 À 12.
    for a in range(1,32): #NESTA ESTRUTURA DE REPETIÇÃO O for IRÁ ADICIONA A LISTA DE DIAS... TODOS OS DIAS VÁLIDOS (1 à 31)
        diaList.append(a)
    if x not in diaList: #SEO DIA DIGITADO NÃO ESTIVER NA LISTA DE DIAS VÁLIDOS...
        print('Dia inválido')
    else:
        for b in range(1,13): #NESTA ESTRUTURA DE REPETIÇÃO O for IRÁ ADICIONA A LISTA DE MESES... TODOS OS MESES VÁLIDOS (1 à 12)
            mesList.append(b)
        if y not in mesList: #SE O MÊS DIGITADO NÃO ESTIVER NA LISTA DE MESES VÁLIDOS...
            print('Mês inválido')
        else:
            if len(z) != 4: #SE O ANO DIGITADO NÃO TIVER 4 CARACTERES...
                print('Ano inválido')
            else: # SE TUDO ESTIVER OK, O PRINT ABAIXO IRA FAZER A FORMATAÇÃO DA DATA DE ACORDO COM O ÍNDICE DA LISTA ABAIXO:
                meses = [0,'janeiro','fevereiro','março','abril','maio','junho',
                'julho','agosto','setembro','outubro','novembro','dezembro']
                print('{} de {} de {}'.format(x,meses[y],z))
print('-=-'*20)
print('Digite uma data no formato DD/MM/AAAA : ')
dia = int(input('Dia (DD) --> : '))
mes = int(input('Mês (MM) --> : '))
ano = input('Ano (AAAA) --> : ')
print('-=-'*20)
date_on(dia,mes,ano) #AQUI APÓS O INPUT, NÓS CHAMAMOS A FUNÇÃO CRIADA ACIMA.
print('-=-'*20)