class Gameboard():
	""" Gestion du plateau de jeu (Affichage et traitements du contenu des cases) """

	def __init__(self):
		return None

	def DrawOpponentBoard(self):
		print("			┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐")
		for line in range(0, 9):
			print("			│   │   │   │   │   │   │   │   │   │   │")
			print("			├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
		print("			│   │   │   │   │   │   │   │   │   │   │")
		print("			└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘")

	def DrawPlayerBoard(self):
		print("			╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗")
		for line in range(0, 9):
			print("			║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║")
			print("			╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
		print("			║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║")
		print("			╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝")

		