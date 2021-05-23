#03 - Utilizando estruturas de repetição com teste lógico, 
#faça um programa que peça uma senha para iniciar seu processamento, 
#só deixe o usuário continuar se a senha estiver correta, 
#após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, 
#onde o computador vai “pensar” em um número entre 0 e 10. 
#O jogador vai tentar adivinhar qual número foi escolhido até acertar, 
#a cada palpite do usuário diga a ele se o número escolhido pelo computador 
#é maior ou menor ao que ele palpitou, no final mostre quantos palpites foram necessários para vencer.

from random import randint #AQUI EU IMPORTO A A FUNÇÃO randint RESPONÁSAVEL POR GERAR NÚMEROS ALEATÓRIOS.
from time import sleep #A FUNÇÃO  sleep SERVE PARA GERAR UM INTERVALO DE TEMPO ENTRE UMA LINHA DE CÓDIGO E OUTRA.
def d(): #FUNÇÃO CRIADA PARA CHAMAR UMA DECORAÇÃO DE TEXTO SIMPLES.
   print('-=-'*20)
n_usuário = input('Crie um nome de usuário: ') #input PARA RECEBER UM NOVO NOME DE USUÁRIO
n_senha = input('Crie uma senha de até 4 caracteres: ') #input PARA RECEBER A SENHA
while len(n_senha) != 4: #ENQUANTO A SENHA NÃO TIVER APENAS 4 CARACTERES O while CONTINUA PEDINDO PARA CRIAR SENHA
   n_senha = input('A senha deve ter apenas 4 caracteres: ')
sleep(2)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#A PARTIR DESSE MOMENTO O USUÁRIO PODE FAZER LOGIN DEPOIS DE TER SE CADASTRADO.
d()
print('Entre na sua conta')
d()
user = input('Nome de usuário: ') #input  PARA RECEBER O NOME DE USUÁRIO CRIADO PELO MESMO.
while user != n_usuário: #SE O NOME DE USUÁRIO ESTIVER INCORRETO O  while CONTINUARÁ PEDINDO O MESMO.
   user = input('''Este nome de usuário não existe!
   Tente novamente: ''')
key = input('Senha: ') #input  PARA RECEBER A SENHA CRIADA PELO USUÁRIO.
while key != n_senha: #SE A SENHA ESTIVER INCORRETA O  while CONTINUARÁ PEDINDO O MESMO.
   key = input('''A senha está incorreta!
   Tente novamente: ''')
sleep(2)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#A PARTIR DAQUI O JOGO COMEÇA:
d()
print('''SEJA BEM VINDO AO JOGO DA ADVINHAÇÃO!
LET`S GO!!!''')
d()
sleep(3)
cont = 1 #AQUI TEMOS UM CONTADOR PARA MARCAR QUANTAS TENTATIVAS FORAM NECESSÁRIAS ATÉ ACERTAR
print('A maquina está pensando em um número de 0 a 10...    ','AGUARDE...')
d()
sleep(5)
computador = randint(0,10) #AQUI NÓS USAMOS A FUNÇÃO randint PARA GERAR UM NÚMERO ALEATÓRIO.
print('Pronto!...')
sleep(2)
jogador = int(input('TENTE DESCOBRIR EM QUE NÚMERO EU PENSEI...: ')) #NESSE MOMENTO O USUÁRIO TEM A PRIMEIRA CHANCE DE TENTAR ADIVINHAR O NUMERO GERADO.
while jogador != computador: #ENQUANTO O O JOGADOR NÃO ACERTAR O NÚMERO GERADO O PROGRAMA VAI FICAR REPETINDO AS TENTATIVAS.
   if jogador > computador: #SE O JOGADOR PALPITAR UM NÚMERO MAIOR DO QUE O NUMERO GERADO O PROGRAMA VAI DAR UMA DICA QUE O NÚMERO É MENOR.
    print('....')
    sleep(2)
    print('HUMMM... Não foi dessa vez.')
    d()
    jogador = int(input('''Ta quase, eu pensei em um numero um pouco menor...
    Tente de novo
    --> : '''))
    cont += 1 #AQUI É ADICIONADO MAIS UM VALOR A VARIÁVEL cont PARA CONTAR AS TENTAIVAS DO JOGADOR.
   elif jogador < computador: #SE O JOGADOR PALPITAR UM NÚMERO MENOR DO QUE O NUMERO GERADO O PROGRAMA VAI DAR UMA DICA QUE O NÚMERO É MAIOR.
    print('....')
    sleep(2)
    print('HUMMM... Não foi dessa vez.')
    d()
    jogador = int(input('''Ta quase, eu pensei em um numero um pouco maior...
    Tente de novo
    --> : '''))
    cont += 1 
if jogador == computador:
    d()
    sleep(2)
    print('PARABÉNS!!! VOCÊ ACERTOU!')
    sleep(2)
    print('A máquina pensou no número {}'.format(computador))
    d()
    sleep(1)
    print('Foram necessárias {} tentativas para acertar'.format(cont))
    d()
