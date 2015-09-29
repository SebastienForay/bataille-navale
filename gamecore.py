from class_gameboard import Gameboard
from class_ship import Ship

gameboard = Gameboard()


for x in range(0, 6):
	size = int(input("Taille bateau "))
	posX = str(input("posX "))
	posY = int(input("posY "))

	Ship(size, posX, posY)


gameboard.DrawOpponentBoard()
gameboard.DrawPlayerBoard()
