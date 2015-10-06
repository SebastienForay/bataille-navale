class Ship():
	""" Objet représentant un bateau """

	size = 0
	posX = 0
	posY = ''
	orientation = ''

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
		position = '' + str(self.posX) + str(self.posY)
		tablePositions.append(position)

		if self.orientation == 'U':
			pass
		elif self.orientation == 'D':
			pass
		elif self.orientation == 'L':
			pass
		elif self.orientation == 'R':
			pass