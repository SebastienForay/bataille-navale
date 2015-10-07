#!/usr/bin/env python
#-*- coding utf-8 -*-

from tkinter import *

class Interface():
	def __init__(self):
		self.letterLabel = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
		self.root = Tk()
		self.initTab()
		self.root.mainloop()

	def initTab(self):
		#frame qui contient tout les éléments
		cadre = Frame(self.root, width=1050, height=500,  borderwidth=1, bg="white")
		cadre.pack()

		Label(cadre, text="Jeu de la bataille navale !", bg="white").pack(padx=10, pady=10)

		#Frame premier tableau
		tableau1 = Frame(cadre, width=500, height=500,  borderwidth=1, bg="white")
		tableau1.pack(side=LEFT, padx=25, pady=5)

		#canvas du tableau
		canvas = Canvas(tableau1, width=550, height=550, borderwidth=2, bg="white")

		#label chiffre

		txt = 1
		for x in range(75,575,50):
			canvas.create_text(x,30,text=txt,font=30)
			txt += 1

		#label lettre
		txt = 0
		for x in range(75,575,50):
			canvas.create_text(30,x,text=self.letterLabel[txt],font=30)
			txt += 1

		rectangle = canvas.create_rectangle(50, 550, 550, 50)

		#lignes et colonnes
		for line in range(50,550,50):
			canvas.create_line(line, 50, line, 550)

		for line in range(100,550,50):
			canvas.create_line(50, line, 550, line)

		canvas.pack()

		#tableau 2
		tableau2 = Frame(cadre, width=500, height=500,  borderwidth=1, bg="white")
		tableau2.pack(side=LEFT, padx=25, pady=5)

		canvas2 = Canvas(tableau2, width=550, height=550, borderwidth=2, bg="white")
		rectangle2 = canvas2.create_rectangle(50, 550, 550, 50)

		#label chiffre
		letterLabel = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
		txt = 1
		for x in range(75,575,50):
			canvas2.create_text(x,30,text=txt,font=30)
			txt += 1

		#label lettre
		txt = 0
		for x in range(75,575,50):
			canvas2.create_text(30,x,text=self.letterLabel[txt],font=30)
			txt += 1


		#lignes et colonnes
		for line in range(50,550,50):
			canvas2.create_line(line, 50, line, 550)

		for line in range(100,550,50):
			canvas2.create_line(50, line, 550, line)

		canvas2.pack()

	#def placeBateau(self):


Interface()