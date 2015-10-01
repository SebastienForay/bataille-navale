from class_gameboard import Gameboard
from class_ship import Ship

class Player():

	pseudo = ""

	# Plateau où sont placés les bateaux du joueur
	plateauPlayerShips = [ ["   "]*10 for _i in range(10) ]
	# Plateau où le joueur voit où il a déjà tiré et touché des bateaux
	plateauPlayerFiring = [ ["   "]*10 for _i in range(10) ]

	#~Tableau contenant les 5 bateaux du joueur
	tableShips = []
	gameboard = 0

	def __init__(self, pseudo_init):
		self.pseudo = pseudo_init
		self.gameboard = Gameboard()

		self.placeShips()

	def placeShips(self):
		print("Vous devez placer vos bateaux. Vous en disposer de 5 : \n	- 1 porte-avions (5 cases)\n	- 1 croiseur (4 cases)\n	- 1 sous-marin( 3 cases)\n	- 1 contre-torpilleur (3 cases) \n	- 1 torpilleur (2 cases) ")
		print("Le placement des bateaux s'effectue dans l'ordre ci-dessus.")

		shipSize = 0
		posX = 0
		posY = ''
		orientation = ''

		# Boucle de 0 à 4 pour créer 5 bateaux
		for shipCount in range(0, 5):
			# Défini la taille du bateau en fonction du nombre de boucles faites
			# L'utilisateur ne le saisi pas
			shipSize = 5 if shipCount == 0 else 4 if shipCount == 1 else 2 if shipCount == 4 else 3

			######
			## Boucles de saisie et de validation des informations
			##

			# Saisie de l'entier entre 1 et 10 de la position X du bateau (colonne)
			while True:
				try:
					posX = int(input("Position X (1 - 10) : "))
				except ValueError:
					print("ERREUR : Veuillez saisir un nombre entre 1 et 10")
					continue
				else:
					if int(posX) < 1 or int(posX) > 10:
						print("ERREUR : Veuillez saisir un nombre entre 1 et 10")
						continue
					else:
						break

			# Saisie du caractère entre A et J de la position Y du bateau (ligne)
			while True:
				try:
					posY = str(input("Position Y (A - J) : "))
				except ValueError:
					print("ERREUR : Veuillez saisir une lettre entre A et J")
					continue
				else:
					bTestResult = False
					tableAuthorizedLetters = ['A','B','C','D','E','F','G','H','I','J']
					for x in range(0, len(tableAuthorizedLetters)):
						if str(tableAuthorizedLetters[x]) != str(posY):
							bTestResult = False
						else:
							bTestResult = True
							break

					if bTestResult == True:
						break
					else:
						print("ERREUR : Veuillez saisir une lettre entre A et J")
						continue

			# Saisie du caractère entre U,D,L et R de l'orientation du bateau
			while True:
				try:
					orientation = str(input("Orientation : U (up), D (down), L (left) ou R (right) : "))
				except ValueError:
					print("ERREUR : Veuillez saisir une lettre entre A et J")
					continue
				else:
					bTestResult = False
					tableAuthorizedLetters = ['U','D','L','R']
					for x in range(0, len(tableAuthorizedLetters)):
						if str(tableAuthorizedLetters[x]) != str(orientation):
							bTestResult = False
						else:
							bTestResult = True
							break

					if bTestResult == True:
						break
					else:
						print("ERREUR : Veuillez saisir une lettre entre U, D, L et R")
						continue

			# Instanciation du bateau avec les paramètres précédemment saisis
			tmpShip = Ship(int(shipSize), int(posX), str(posY), str(orientation))
			# Ajout du bateau au tableau de sauvegarde
			self.tableShips.append(tmpShip)

			### TODO
			#récupérer le tableau des positions (dans tmpShip.tablePositions) pour remplir le plateauPlayerShips visuel