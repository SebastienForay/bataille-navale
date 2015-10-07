#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from class_player import Player

#Clear screen before the game
os.system('cls' if os.name == 'nt' else 'clear')

pseudo = str(input("Entrez le pseudo du premier joueur : "))
player1 = Player(1, pseudo)
os.system('cls' if os.name == 'nt' else 'clear')

pseudo = str(input("Entrez le pseudo du second joueur : "))
player2 = Player(2, pseudo)
os.system('cls' if os.name == 'nt' else 'clear')


playerToPlay = 1
while True:
	if playerToPlay == 1:
		player1.printPlateauShip()
		print("Joueur 1, à toi de jouer !")
		posFire = player1.play()
		posX = 0
		posY = ''
		posYInt = 0

		#print("[DEBUG] posFire : " + str(posFire))

		# Parcours le tableau de bateau du P2
		for x in range(0, 5):
			index = 0
			try:
				index = player2.tableShips[x].tablePositions.index(posFire)
			except ValueError:
				#print("[DEBUG] Non trouvé dans le bateau " + str(x))
				continue
			else:
				#print("[DEBUG] Trouvé dans le bateau " + str(x))
				player2.tableShips[x].size -= 1

				posX = int(posFire[0:len(posFire)-1]) - 1
				posY = player2.tablePosYLetters.index(posFire[len(posFire)-1:])
				player2.plateauPlayerShips[posX][posY] = " Ø "

				break
		playerToPlay += 1
	elif playerToPlay == 2:
		player2.printPlateauShip()
		print("Joueur 2, à toi de jouer !")
		posFire = player2.play()

		#print("[DEBUG] posFire : " + str(posFire))

		# Parcours le tableau de bateau du P2
		for x in range(0, 5):
			try:
				index = player1.tableShips[x].tablePositions.index(posFire)
			except ValueError:
				#print("[DEBUG] Non trouvé dans le bateau " + str(x))
				continue
			else:
				#print("[DEBUG] Trouvé dans le bateau " + str(x))
				player1.tableShips[x].size -= 1

				posX = int(posFire[0:len(posFire)-1]) - 1
				posY = player1.tablePosYLetters.index(posFire[len(posFire)-1:])
				player1.plateauPlayerShips[posX][posY] = " Ø "

				break
		playerToPlay -= 1