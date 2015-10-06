class Gameboard():
	""" Plateau du jeu
			Gestion du plateau de jeu (Affichage et traitements du contenu des cases)
			Contient le plateau de tir et le plateau des bateaux du joueur
	"""

	
	def __init__(self):
		tableMatchesLinePosY = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

	def DrawFiringBoard(self):
		print("			   1   2   3   4   5   6   7   8   9   10")
		print("			 ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐")
		for line in range(0, 9):
			lineToFill = "			" + str(self.tableMatchesLinePosY[line]) + "│"
			lineSeparator = "			 ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤"
			for col in range(0, 10):
				lineToFill += "   │"
			print(lineToFill)
			print(lineSeparator)
		print("			J│   │   │   │   │   │   │   │   │   │   │")
		print("			 └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘\n")
		
	def DrawPlayerBoard(self):
		print("			   1   2   3   4   5   6   7   8   9   10")
		print("			 ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗")
		for line in range(0, 9):
			lineToFill = "			" + str(self.tableMatchesLinePosY[line]) + "║"
			lineSeparator = "			 ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣"
			for col in range(0, 10):
				lineToFill += "   ║"
			print(lineToFill)
			print(lineSeparator)
		print("			J║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║")
		print("			 ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝\n")

		