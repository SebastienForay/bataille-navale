#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Ship():
	""" Objet représentant un bateau """


	tablePosYLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', ]

	tableAllPosShipsP1 = []
	tableAllPosShipsP2 = []
	

	def __init__(self, player_init, size_init, posX_init, posY_init, orientation_init):
		self.size = 0
		self.posX = 0
		self.posY = ''
		self.orientation = ''
		#insert prev
		self.bCreated = False
		self.player = player_init
		self.tablePositionsP1 = []
		self.tablePositionsP2 = []
		self.tablePositions = []

		print(self.player)

		self.Create(size_init, posX_init, posY_init, orientation_init)

	def Create(self, size_init, posX_init, posY_init, orientation_init):
		self.size = int(size_init)
		self.posX = int(posX_init)
		self.posY = self.tablePosYLetters[posY_init-1]
		self.orientation = str(orientation_init)

		# calcul des coordonnées occupées par le bateau (fonction) pour ajout dans tablePositions
		if self.calculatePositions() == True:
			print("Bateau créé : longueur de " + str(self.size) + ", position (" + str(self.posX) + "/" + str(self.posY) + "), orientation : " + str(self.orientation))
			self.bCreated = True
		else:
			print("Erreur à la création du bateau ! Veuillez le refaire !")
			self.bCreated = False

		if self.player == 1:
			self.tablePositionsP1 = self.tablePositions
		else:
			self.tablePositionsP2 = self.tablePositions

	def calculatePositions(self):
		bResultat = True

		if self.player == 1:
			self.tablePositions = self.tablePositionsP1
		else:
			self.tablePositions = self.tablePositionsP2

		tmpPosX = self.posX
		tmpPosY = self.posY
		tmpSize = self.size

		position = "'" + str(tmpPosX) + str(tmpPosY) + "'"
		self.tablePositions.append(position)

		posYInt = self.tablePosYLetters.index(tmpPosY) + 1
						
		# Calcul vers le haut
		if self.orientation == 'U':
			print (posYInt - tmpSize)
			if posYInt - tmpSize >= 0:
				for x in range(posYInt-1, posYInt-tmpSize, -1):
					position = "'" + str(tmpPosX) + str(self.tablePosYLetters[x-1]) + "'"
					self.tablePositions.append(position)
			else:
				return False
		# Calcul vers le bas
		elif self.orientation == 'D':
			if posYInt + (tmpSize-1) <= 10:
				for x in range(posYInt+1, posYInt+tmpSize):
					position = "'" + str(tmpPosX) + str(self.tablePosYLetters[x-1]) + "'"
					self.tablePositions.append(position)
			else:
				return False
		# Calcul vers la gauche
		elif self.orientation == 'L' :
			if tmpPosX - tmpSize >= 0:
				for x in range(tmpPosX-1, tmpPosX-tmpSize, -1):
					position = "'" + str(x) + str(self.tablePosYLetters[posYInt-1]) + "'"
					self.tablePositions.append(position)
			else:
				return False
		# Calcul vers la droite
		elif self.orientation == 'R':
			if tmpPosX + (tmpSize-1) <= 10:
				for x in range(tmpPosX+1, tmpPosX+tmpSize):
					position = "'" + str(x) + str(self.tablePosYLetters[posYInt-1]) + "'"
					self.tablePositions.append(position)
			else:
				return False
			print("[DEBUG] tablePositions : ")
		for x in range(0, len(self.tablePositions)):
			print(self.tablePositions[x])
			# Vérification de la disponibilité de toutes les positions
		if (self.player == 1) and (len(self.tableAllPosShipsP1) > 0):
			print("[DEBUG] Test All Pos Player1")
			for x in range(0, len(self.tablePositions)):
				try:
					a = self.tableAllPosShipsP1.index(self.tablePositions[x])
				except ValueError:
					print("ValueError Player1")
					bResultat = True
					continue
				else:
					bResultat = False
					break
		elif (self.player == 2) and (len(self.tableAllPosShipsP2) > 0):
			print("[DEBUG] Test All Pos Player2")
			for x in range(0, len(self.tablePositions)):
				try:
					a = self.tableAllPosShipsP2.index(self.tablePositions[x])
				except ValueError:
					bResultat = True
					continue
				else:
					bResultat = False
					break

		# Print les positions calculées pour le debug
	#if bResultat == True:
	#	print("[DEBUG] Positions du bateau :")
	#	for x in range(0, len(self.tablePositions)):
	#		print(self.tablePositions[x])
	#		if self.player == 1:
	#			self.tableAllPosShipsP1.append(self.tablePositions[x])
	#		elif self.player == 2:
	#			self.tableAllPosShipsP2.append(self.tablePositions[x])
		return bResultat

	def insertShip(self):
		for x in range(0, len(self.tablePositions)):
			print(self.tablePositions[x])
			if self.player == 1:
				self.tableAllPosShipsP1.append(self.tablePositions[x])
			elif self.player == 2:
				self.tableAllPosShipsP2.append(self.tablePositions[x])

		self.tablePositions.clear()