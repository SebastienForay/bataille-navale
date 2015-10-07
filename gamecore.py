#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from class_player import Player

#Clear screen before the game
os.system('cls' if os.name == 'nt' else 'clear')

pseudo = str(input("Entrez le pseudo du premier joueur : "))
player1 = Player(1, pseudo)
pseudo = str(input("Entrez le pseudo du second joueur : "))
player2 = Player(2, pseudo)
