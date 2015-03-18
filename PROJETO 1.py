# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:44:59 2015

@author: PedroSambi
"""
#importando random e craindo as variaveis
from random import randint
jogador=0
computador=0 
#escolhendo opcao do computador em x e do jogador em y
while jogador<3 and computador <3:
	x=randint(1,5)
	y=int(input("Vamos jogar!, escolha uma opção: 1=tesoura, 2=spock, 3=papel, 4=lagarto, 5=pedra, ganha quem fizer 3 pontos primeiro"))
		


	if x == y:
		print("voces empataram")

#computador sendo tesoura
	elif x==1 and y==2:
		print("o computador jogou tesoura,voce venceu")
		jogador+=1
	elif x==1 and y==3:
		print("o computador jogou tesoura,Voce perdeu")
		computador+=1
	elif x==1 and y==4:
		print("o computador jogou tesoura, voce perdeu")
		computador+=1
	elif x==1 and y==5:
		print("o computador jogou tesoura, voce venceu")
		jogador+=1

#computador sendo spock
	elif x==2 and y==1:
		print("o computador jogou spock, voce perdeu")
		computador+=1
	elif x==2 and y==3:
		print("o computador jogou spock, voce venceu")
		jogador+=1
	elif x==2 and y==4:
		print("o computador jogou spock, voce venceu")
		jogador+=1
	elif x==2 and y==5:
		print("o computador jogou spock, voce perdeu")
		computador+=1

#computador sendo papel
	elif x==3 and y==1:
		print("o computador jogou papel, voce venceu")
		jogador+=1
	elif x==3 and y==2:
		print("o computador jogou papel, voce perdeu")
		computador+=1
	elif x==3 and y==4:
		print("o computador jogou papel, voce venceu")
		jogador+=1
	elif x==3 and y==5:
		print("o computador jogou papel, voce perdeu")
		computador+=1
		
#computador sendo lagarto
	elif x==4 and y==1:
		print("o computador jogou lagarto, voce venceu")
		jogador+=1
	elif x==4 and y==2:
		print("o computador jogou lagarto, voce perdeu")
		computador+=1
	elif x==4 and y==3:
		print("o computador jogou lagarto, voce perdeu")
		computador+=1
	elif x==4 and y==5:
		print("o computador jogou lagarto, voce venceu")
		jogador+=1
		
#computador sendo pedra
	elif x==5 and y==1:
		print("o computador escolheu pedra, voce perdeu")
		computador+=1
	elif x==5 and y==2:
		print("o computador escolheu pedra, voce venceu")
		jogador+=1	
	elif x==5 and y==3:
		print("o computador escolheu pedra, voce venceu")
		jogador+=1
	elif x==5 and y==4:
		print("o computador escolheu pedra, voce perdeu")
		computador+=1


if jogador==3:
  print("voce venceu o jogo, prabens")
if computador == 3:
  print("voce perdeu, jogue novamente")	
	

		
		


