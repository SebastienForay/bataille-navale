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


bEndGame = False
playerToPlay = 1

while bEndGame == False:	
	if playerToPlay == 1:
		player1.printGameboard()
		print("Joueur 1, à toi de jouer !")
		posFire = player1.play()
		posX = 0
		posY = ''
		posYInt = 0

		#print("[DEBUG] posFire : " + str(posFire))

		# Parcours le tableau de bateau du P2
		for x in range(0, 5):
			index = 0
			bFound = False
			try:
				index = player2.tableShips[x].tablePositions.index(posFire)
			except ValueError:
				#print("[DEBUG] Non trouvé dans le bateau " + str(x))
				if x == 4 and bFound == False:
					posX = int(posFire[0:len(posFire)-1]) - 1
					posY = player1.tablePosYLetters.index(posFire[len(posFire)-1:])
					player1.plateauPlayerFiring[posX][posY] = " * "
				continue
			else:
				#print("[DEBUG] Trouvé dans le bateau " + str(x))
				bFound = True
				player2.tableShips[x].size -= 1

				posX = int(posFire[0:len(posFire)-1]) - 1
				posY = player2.tablePosYLetters.index(posFire[len(posFire)-1:])
				player2.plateauPlayerShips[posX][posY] = " Ø "
				player1.plateauPlayerFiring[posX][posY] = " Ø "
				break
		playerToPlay += 1
	elif playerToPlay == 2:
		player2.printGameboard()
		print("Joueur 2, à toi de jouer !")
		posFire = player2.play()

		#print("[DEBUG] posFire : " + str(posFire))

		# Parcours le tableau de bateau du P1
		for x in range(0, 5):
			try:
				index = player1.tableShips[x].tablePositions.index(posFire)
			except ValueError:
				#print("[DEBUG] Non trouvé dans le bateau " + str(x))
				if x == 4 and bFound == False:
					posX = int(posFire[0:len(posFire)-1]) - 1
					posY = player2.tablePosYLetters.index(posFire[len(posFire)-1:])
					player2.plateauPlayerFiring[posX][posY] = " * "
				continue
			else:
				#print("[DEBUG] Trouvé dans le bateau " + str(x))
				player1.tableShips[x].size -= 1

				posX = int(posFire[0:len(posFire)-1]) - 1
				posY = player1.tablePosYLetters.index(posFire[len(posFire)-1:])
				player1.plateauPlayerShips[posX][posY] = " Ø "
				player2.plateauPlayerFiring[posX][posY] = " Ø "

				break
		playerToPlay -= 1

	# Check si un joueur n'a plus de bateaux
	for player in range(0, 2):
		if player == 0:
			if player1.tableShips[0].size == 0:
				if player1.tableShips[1].size == 0:
					if player1.tableShips[2].size == 0:
						if player1.tableShips[3].size == 0:
							if player1.tableShips[4].size == 0:
								print("Le joueur " + str(player1.pseudo) + " n'a plus de bateaux, la partie est terminée !")
								bEndGame = True
		elif player == 1:
			if player2.tableShips[0].size == 0:
				if player2.tableShips[1].size == 0:
					if player2.tableShips[2].size == 0:
						if player2.tableShips[3].size == 0:
							if player2.tableShips[4].size == 0:
								print("Le joueur " + str(player2.pseudo) + " n'a plus de bateaux, la partie est terminée !")
								bEndGame = True