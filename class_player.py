from class_ship import Ship

class Player():

	pseudo = ""

	# Plateau où sont placés les bateaux du joueur
	plateauPlayerShips = [ ["   "]*10 for _i in range(10) ]
	# Plateau où le joueur voit où il a déjà tiré et touché des bateaux
	plateauPlayerFiring = [ ["   "]*10 for _i in range(10) ]

	def __init__(self, pseudo_init):
		self.pseudo = pseudo_init
		self.placeShips()

	def placeShips(self):
		print("Vous devez placer vos bateaux. Vous disposer de 5 bateaux: \n- 1 porte avion (5 cases)\n- 1 croiseur (4 cases)\n- 1 sous marin( 3 cases)\n- 1 contre torpilleur (3 cases) \n- 1 torpilleur (2 cases) ")
	
		for nbrBateau in range(0,5):
			num = int(input("Veuillez entrer le nombre de cases du bateau"))
			posX = str(input("position X"))
			posY= int(input("position X"))
			dispos = str(input ("Veuillez entrer sa dispotion : u (up), d (down), r (right, l (left)"))
			
			#instanciation du bateau
			tmpShip = Ship(num, posX, posY, orientation)
			#récupérer le tableau des positions (dans tmpShip.tablePositions) pour remplir le plateauPlayerShips visuel
