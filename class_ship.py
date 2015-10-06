class Ship():
	""" Objet représentant un bateau """

	size = 0
	posX = 0
	posY = ''
	orientation = ''

	tablePosYLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', ]

	tablePositions = []

	def __init__(self, size_init, posX_init, posY_init, orientation_init):
		self.Create(size_init, posX_init, posY_init, orientation_init)

	def Create(self, size_init, posX_init, posY_init, orientation_init):
		self.size = int(size_init)
		self.posX = int(posX_init)
		self.posY = str(posY_init)
		self.orientation = str(orientation_init)

		# calcul des coordonnées occupées par le bateau (fonction) pour ajout dans tablePositions
		self.calculatePositions()
		
		print("Bateau créé : longueur de " + str(self.size) + ", position (" + str(self.posX) + "/" + str(self.posY) + "), orientation : " + str(self.orientation))


	def calculatePositions(self):
		print("Calcul des positions")

		tmpPosX = self.posX
		tmpPosY = self.posY
		tmpSize = self.size

		position = '' + str(tmpPosX) + str(tmpPosY)
		self.tablePositions.append(position)

		posYInt = self.tablePosYLetters.index(tmpPosY) + 1

		# suffisemment de place vers le haut
		if (self.orientation == 'U') and (posYInt - tmpSize >= 0):
			for x in range(posYInt, posYInt-tmpSize, -1):
				position = '' + str(tmpPosX) + str(self.tablePosYLetters[x-1])
				self.tablePositions.append(position)
				print('' + str(position))
		else:
			print("Changez de position, il n'y a pas assez de place !")
		# suffisemment de place vers le bas
		if (self.orientation == 'D') and (posYInt + tmpSize < 10):
			pass
		# suffisemment de place vers la gauche
		elif (self.orientation == 'L') and (tmpPosX - size >= 0):
			pass
		# suffisemment de place vers la droite
		elif (self.orientation == 'R') and (tmpPosX + size < 10):
			pass