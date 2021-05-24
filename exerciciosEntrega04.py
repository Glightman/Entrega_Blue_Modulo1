#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA 
# e devolva uma string no formato DD de mesPorExtenso de AAAA. 
# Opcional: valide a data e retorne 'data inválida' caso a data seja inválida.

def date_on(x,y,z):
    diaList = list()
    mesList = list()
    dia1 = int(x)
    mes1 = int(y)
    for a in range(1,32):
        diaList.append(a)
    if dia1 not in diaList:
        print('Dia inválido')
    else:
        for b in range(1,13):
            mesList.append(b)
        if mes1 not in mesList:
            print('Mês inválido')
        else:
            if len(z) != 4:
                print('Ano inválido')
            else:
                meses = [0,'janeiro','fevereiro','março','abril','maio','junho',
                'julho','agosto','setembro','outubro','novembro','dezembro']
                print('{} de {} de {}'.format(dia1,meses[mes1],z))
print('-=-'*20)
print('Digite uma data no formato DD/MM/AAAA : ')
dia = input('Dia (DD) --> : ')
mes = input('Mês (MM) --> : ')
ano = input('Ano (AAAA) --> : ')
print('-=-'*20)
date_on(dia,mes,ano)
print('-=-'*20)