class Ship():
	""" Objet représentant un bateau """

	size = 0
	posX = 0
	posY = 0

	def __init__(self, size_init, posX_init, posY_init, dispo_init):
		self.size = int(size_init)
		self.posX = posX_init
		self.posY = posY_init
		self.dispo = dispo_init

		print("Bateau créé : longueur de " + str(self.size) + ", position (" + str(self.posX) + "/" + str(self.posY) + ")")

	def placerBateau(joueur):
	print("Vous devez placer vos bateaux. Vous disposer de 5 bateaux: \n- 1 porte avion (5 cases)\n- 1 croiseur (4 cases)\n- 1 sous marin( 3 cases)\n- 1 contre torpilleur (3 cases) \n- 1 torpilleur (2 cases) ")
	
	for nbrBateau in range(0,5):
		num = int(input("Veuillez entrer le nombre de cases du bateau"))
		posX = str(input("position X"))
		posY= int(input("position X"))
		dispos = str(input ("Veuillez entrer sa dispotion : u (up), d (down), r (right, l (left)"))
		
		Ship(num, pasX, posY, didpos)