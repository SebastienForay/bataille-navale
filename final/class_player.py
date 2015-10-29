#!/usr/bin/env python
# -*- coding: utf-8 -*-

from class_gameboard import Gameboard
from interface import Interface

import os, sys

class Player():
	tablePosYLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', ]

	def __init__(self, type_init, pNumber_init, pseudo_init, connectionServer_init):
		# Plateau où sont placés les bateaux du joueur
		self.plateauPlayerShips = [ ["   "]*10 for _i in range(10) ]
		# Plateau où le joueur voit où il a déjà tiré et touché des bateaux
		self.plateauPlayerFiring = [ ["   "]*10 for _i in range(10) ]

		# Tableau contenant les 5 bateaux du joueur
		self.tableShips = []
		self.playerFiring = []

		self.type = type_init
		self.pNumber = pNumber_init
		self.pseudo = pseudo_init
		self.gameboard = Gameboard(self.plateauPlayerShips, self.plateauPlayerFiring)

		self.connectionServer = connectionServer_init

		self.firedPos = ""
		self.bPlays = False

		"""if self.type == "LOCAL":
			self.placeShips()
			self.insertPlateau()"""

	def insertPlateau(self):
		for shipCount in range(0, 5):
			if self.pNumber == 1:
				for x in range(0, len(self.tableAllPosShipsP1)):
					pos = self.tableAllPosShipsP1[x]
					pos = pos.replace("'", "")
					lenPos = len(pos)
					pos1 = int(pos[0:lenPos-1]) - 1
					pos2 = self.tablePosYLetters.index(pos[lenPos-1:])
					self.plateauPlayerShips[pos1][pos2] = " O "
			elif self.pNumber == 2:
				for x in range(0, len(self.tableShips[shipCount].tableAllPosShipsP2)):
					pos = self.tableShips[shipCount].tableAllPosShipsP2[x]
					lenPos = len(pos)
					pos1 = int(pos[0:lenPos-1]) - 1
					pos2 = self.tableShips[shipCount].tablePosYLetters.index(pos[lenPos-1:])
					self.plateauPlayerShips[pos1][pos2] = " O "

	def printGameboard(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		self.gameboard.DrawFiringBoard()
		self.gameboard.DrawPlayerBoard()

	def play(self):
		posXFire = 0
		posYFire = ''

		while True:
			try:
				posXFire = int(input("Position de tir (1 - 10) : "))
			except ValueError:
				print("ERREUR : Veuillez saisir un nombre entre 1 et 10")
				continue
			else:
				if int(posXFire) < 1 or int(posXFire) > 10:
					print("ERREUR : Veuillez saisir un nombre entre 1 et 10")
					continue
				else:
					break

		# Saisie du caractère entre A et J de la position Y du bateau (ligne)
		while True:
			try:
				posYFire = str(input("Position de tir (A - J) : ").upper())
			except ValueError:
				print("ERREUR : Veuillez saisir une lettre entre A et J")
				continue
			else:
				bTestResult = False
				tableAuthorizedLetters = ['A','B','C','D','E','F','G','H','I','J']
				for x in range(0, len(tableAuthorizedLetters)):
					if str(tableAuthorizedLetters[x]) != str(posYFire):
						bTestResult = False
					else:
						bTestResult = True
						break

				if bTestResult == True:
					break
				else:
					print("ERREUR : Veuillez saisir une lettre entre A et J")
					continue

		return '' + str(posXFire) + str(posYFire)

	def init_interface(self, threadeit, threadrec, pLocal, pOnline):
		iPLayer = Interface(self.pNumber, self.pseudo, self.connectionServer, threadeit, threadrec, pLocal, pOnline)
		self.tableAllPosShipsP1 = iPLayer.tmpShip.tableAllPosShipsP1
		self.insertPlateau()