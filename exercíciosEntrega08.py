""" 08 - Crie um programa que leia nome, 
ano de nascimento e carteira de trabalho e 
cadastre-os (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de 0, 
o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar. 
Considere que o trabalhador deve contribuir por 35 anos para se aposentar. """

cadastro = dict() #DICIONÁRIO PARA ARMAZENAR OS DADOS DO CADASTRO
nome = input('Seu nome: ')
ano = int(input('Seu ano de nascimento: '))
ctps = float(input('Numero da CTPS: '))
cadastro['nome'] = nome
cadastro['idade'] = 2021-ano
cadastro['ctps'] = ctps
if ctps != 0:
    ano2 = int(input('Ano de contratação: '))
    salário = float(input('Seu salário: '))
    cadastro['Ano de contratação'] = ano2
    cadastro['Salário'] = salário
    cadastro['Idade de aposentadoria'] = (ano2 - ano) + 35
print(cadastro)