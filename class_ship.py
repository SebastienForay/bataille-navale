class Ship():
	""" Gestion des bateaux """

	size = 0
	posX = 0
	posY = 0

	tablePositions = []

	def __init__(self, size_init, posX_init, posY_init):
		self.size = int(size_init)
		self.posX = posX_init
		self.posY = posY_init

		# calcul des coordonnées occupées par le bateau (fonction) pour ajout dans tablePositions

		print("Bateau créé : longueur de " + str(self.size) + ", position (" + str(self.posX) + "/" + str(self.posY) + ")")