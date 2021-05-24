""" 06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
   "Telefonou para a vítima?"
   "Esteve no local do crime?"
   "Mora perto da vítima?"
   "Devia para a vítima?"
   "Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   Caso contrário, ele será classificado como "Inocente". """

print('RESPONDA APENAS COM "SIM" OU "NAO":')
print('-=-'*15)
p1 = input('Telefonou para a vítima?  ').lower() 
p2 = input('Esteve no local do crime?  ').lower()
p3 = input('Mora perto da vítima?  ').lower()
p4 = input('Devia para a vítima?  ').lower()
p5 = input('Já trabalhou com a vítima?  ').lower()
respostas = [p1,p2,p3,p4,p5]
contar = respostas.count('sim')
print('-=-'*15)
if contar == 2:
    print('Você é um SUSPEITO!')
else:
    if contar == 3 or contar == 4:
        print('Você é um CÚMPLICE!')
    else:
        if contar == 5:
            print('Você é um ASSASSINO!')
        else:
            print('Você é INOCENTE!')
print('-=-'*15)