import os
from class_gameboard import Gameboard
from class_ship import Ship

#Clear screen before the game
os.system('cls' if os.name == 'nt' else 'clear')



gameboard = Gameboard()

gameboard.DrawFiringBoard()
gameboard.DrawPlayerBoard()
