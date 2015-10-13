#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Player():
	tablePosYLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', ]

	def __init__(self, pNumber_init, pseudo_init):
		# Plateau où sont placés les bateaux du joueur
		self.plateauPlayerShips = [ ["   "]*10 for _i in range(10) ]
		# Plateau où le joueur voit où il a déjà tiré et touché des bateaux
		self.plateauPlayerFiring = [ ["   "]*10 for _i in range(10) ]

		# Tableau contenant les 5 bateaux du joueur
		self.tableShips = []

		self.pNumber = pNumber_init
		self.pseudo = pseudo_init
		self.gameboard = 0

		self.placeShips()

	def placeShips(self):
		

	def insertPlateau(self):
		for shipCount in range(0, 5):
			for x in range(0, len(self.tableShips[shipCount].tableAllPosShipsP1)):
				pos = self.tableShips[shipCount].tableAllPosShipsP1[x]
				lenPos = len(pos)
				pos1 = int(pos[1:lenPos-2]) - 1
				pos2 = self.tableShips[shipCount].tablePosYLetters.index(pos[lenPos-2:lenPos-1])
				if pos[lenPos-2:lenPos-1] == "J":
					print(pos1,pos2)
				self.plateauPlayerShips[pos1][pos2] = " O "

	def printPlateauShip(self):
		#for x in range (0, 10):
		#	for y in range (0, 10):
		#		print(self.plateauPlayerShips[x][y])
		self.gameboard = Gameboard(self.plateauPlayerShips)
		self.gameboard.DrawPlayerBoard()