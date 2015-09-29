class Player:

	pseudo = "kikoo"
	plateauPlayer = [[" "]*10 for _i in range(10)]

	def __init__(self, pseudo_init):
		self.pseudo = pseudo_init
		self.placerBateau()

	def placerBateau(self):
		print("Vous devez placer vos bateaux. Vous disposer de 5 bateaux: \n- 1 porte avion (5 cases)\n- 1 croiseur (4 cases)\n- 1 sous marin( 3 cases)\n- 1 contre torpilleur (3 cases) \n- 1 torpilleur (2 cases) ")
	
		for nbrBateau in range(0,5):
			num = int(input("Veuillez entrer le nombre de cases du bateau"))
			posX = str(input("position X"))
			posY= int(input("position X"))
			dispos = str(input ("Veuillez entrer sa dispotion : u (up), d (down), r (right, l (left)"))
			
			#instanciation du bateau
			Ship(num, pasX, posY, didpos)
			#récupérer le tableau des positions pour remplir lr plateauPLayer visuel
