#sa taille, ses coordonées de début, sa dispotion. Exemple : 4,A-1,r

def placer_bateau(joueur):
	print("Vous devez placer vos bateaux. Vous disposer de 5 bateaux:")
	print("- 1 porte avion (5 cases)")
	print("- 1 croiseur (4 cases)")
	print("- 1 sous marin( 3 cases)")
	print("- 1 contre torpilleur (3 cases)") 
	print("- 1 torpilleur (2 cases)")
	
	for nbrBateau in range(0,5):
		num = int(input("Veuillez entrer le nombre de cases du bateau"))
		posX = str(input("position X"))
		posY= int(input("position X"))
		dispos = str(input ("Veuillez entrer sa dispotion : u (up), d (down), r (right, l (left)"))
		
		Ship(num, posX, posY, dispos)

