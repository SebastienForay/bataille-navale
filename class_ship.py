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
		self.bCreated = False
		self.player = player_init

		self.tablePositions = []

		self.Create(player, size_init, posX_init, posY_init, orientation_init)

	def Create(self, size_init, posX_init, posY_init, orientation_init):
		self.size = int(size_init)
		self.posX = int(posX_init)
		self.posY = str(posY_init)
		self.orientation = str(orientation_init)

		# calcul des coordonnées occupées par le bateau (fonction) pour ajout dans tablePositions
		if self.calculatePositions(player) == True:
			print("Bateau créé : longueur de " + str(self.size) + ", position (" + str(self.posX) + "/" + str(self.posY) + "), orientation : " + str(self.orientation))
			self.bCreated = True
		else:
			print("Erreur à la création du bateau ! Veuillez le refaire !")
			self.bCreated = False

	def calculatePositions(self):
		bResultat = True

		tmpPosX = self.posX
		tmpPosY = self.posY
		tmpSize = self.size

		position = '' + str(tmpPosX) + str(tmpPosY)
		self.tablePositions.append(position)

		posYInt = self.tablePosYLetters.index(tmpPosY) + 1

		# Calcul vers le haut
		if self.orientation == 'U':
			if posYInt - tmpSize >= 0:
				for x in range(posYInt-1, posYInt-tmpSize, -1):
					position = '' + str(tmpPosX) + str(self.tablePosYLetters[x-1])
					self.tablePositions.append(position)
			else:
				bResultat = False
		# Calcul vers le bas
		elif self.orientation == 'D':
			if posYInt + (tmpSize-1) <= 10:
				for x in range(posYInt+1, posYInt+tmpSize):
					position = '' + str(tmpPosX) + str(self.tablePosYLetters[x-1])
					self.tablePositions.append(position)
			else:
				bResultat = False
		# Calcul vers la gauche
		elif self.orientation == 'L':
			if tmpPosX - tmpSize >= 0:
				for x in range(tmpPosX-1, tmpPosX-tmpSize, -1):
					position = '' + str(x) + str(self.tablePosYLetters[posYInt-1])
					self.tablePositions.append(position)
			else:
				bResultat = False
		# Calcul vers la droite
		elif self.orientation == 'R':
			if tmpPosX + (tmpSize-1) <= 10:
				for x in range(tmpPosX+1, tmpPosX+tmpSize):
					position = '' + str(x) + str(self.tablePosYLetters[posYInt-1])
					self.tablePositions.append(position)
			else:
				bResultat = False

		# Print les positions calculées pour le debug
		if bResultat == True:
			print("[DEBUG] Positions du bateau :")
			for x in range(0, len(self.tablePositions)):
				print(self.tablePositions[x])
				if self.player == 1:
					self.tableAllPosShipsP1.append(self.tablePositions[x])
				elif self.player == 2:
					self.tableAllPosShipsP2.append(self.tablePositions[x])

		return bResultat