#!/usr/bin/env python
#-*- coding utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from class_shipInterface import Ship

class Interface():
	def __init__(self, pNumber_init, pseudo_init):
		self.letterLabel = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
		self.allPos = ['D', 'R', 'U', 'L']
		self.nbShip = 6
		self.lastPos = 0
		self.saveX = -1
		self.pNumber = pNumber_init
		self.pPseudo = pseudo_init
		self.root = Tk()
		self.bigFrame()
		#self.allTab = self.initTab()
		self.beginBateau()
		self.root.mainloop()

	def bigFrame(self):
		#frame qui contient tout les éléments
		cadre = Frame(self.root, width=1050, height=500, bg="white", borderwidth=1)
		cadre.pack()

		Label(cadre, text="Jeu de la bataille navale !", bg="white").pack(padx=10, pady=10)

		notebook = ttk.Notebook(cadre)
		f1 = Frame(notebook)   # first page, which would get widgets gridded into it
		f2 = Frame(notebook)   # second page
		notebook.bind("<ButtonRelease-1>", self.changeTab)
		notebook.add(f1, text='PLayer1')
		notebook.add(f2, text='Player2')

		self.F1 = f1
		self.F2 = f2

		notebook.pack()
		self.initTab(f1)
		self.initTab(f2)

		return cadre

	def changeTab(self, event):
		if self.nbShip > 1:
			messagebox.showerror("Bateau", "Veuillez finir de placer vos bateaux !")
			return False
		else:
			if self.pNumber == 1:
				self.pNumber = 2
			else:
				self.pNumber = 1
			self.nbShip = 6
			print (self.pNumber)

			self.beginBateau()


	def initTab(self, root):
		cadre = Frame(root, width=1050, height=500,  borderwidth=1, bg="white")
		cadre.pack()

		reset = Button(cadre, text = "reset", command=self.resetShip)
		reset.pack()

		#Frame premier tableau
		tableau1 = Frame(cadre, width=500, height=500,  borderwidth=1, bg="white")
		tableau1.pack(side=LEFT, padx=25, pady=5)

		#canvas du tableau
		canvas = Canvas(tableau1, width=550, height=550, borderwidth=2, bg="white")
		canvas.focus_set()
		canvas.bind("<Button-1>", self.placeBateau)
		canvas.bind("<Button-3>", self.tournerBateau)
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
		canvas2.focus_set()
		canvas2.bind("<Button-1>", self.lancer)

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
		return cadre

	def placeBateau(self,event):
		x = event.x
		y = event.y
		caller = event.widget
		#plus de bateau
		if self.nbShip == 1:
			messagebox.showinfo("Bateaux", "Vous avez posé tous vos bateaux !")
		else:
			if x > 50 and x < 550 and y > 50 and y < 550:
				lengShip = self.nbShip
				if lengShip > 3:
					lengShip -= 1

				calShip = lengShip * 50
				#calcul du petit entier divisible par 50 le plus proche
				entX = x // 50 * 50
				entY = y // 50 * 50
				pos = ""
				#bateau bas
				if (entY + calShip) <= 550:
					pos = "D"
					idPos = 0
					rect = caller.create_rectangle(entX, entY, entX+50, entY+calShip, fill="red", tags="rect")
				#bateau droite
				elif (entX + calShip) <= 550:
					pos = "R"
					idPos = 1
					rect = caller.create_rectangle(entX, entY, entX+calShip, entY+50, fill="red", tags="rect")
				#bateau haut
				elif (entY - calShip) >=0:
					pos = "U"
					idPos = 2
					rect = caller.create_rectangle(entX, entY+50, entX+50, entY-calShip+50, fill="red", tags="rect")
				elif (entX - calShip) >=0:
					pos = "L"
					idPos = 3
					rect = caller.create_rectangle(entX+50, entY, entX-calShip+50, entY+50, fill="red", tags="rect")
				else:
					messagebox.showError("Placement", "Impossible à placer !")
				
				if self.nbShip < 6:
					self.tmpShip.insertShip()
				tmpShip = Ship(self.pNumber, lengShip, int(x//50) , int(y//50), pos)

				inc = -1
				if tmpShip.bCreated == False:
					caller.delete(rect)
					self.lastPos = 5
					self.saveX = -1
					#try other position
					inc = idPos + 1
					while inc != idPos:
						print(self.allPos[inc])
						tmpShip = Ship(self.pNumber, lengShip, int(x//50) , int(y//50), self.allPos[inc])
						if tmpShip.bCreated == True:
							pos = self.allPos[inc]
							if inc == 0:
								rect = caller.create_rectangle(entX, entY, entX+50, entY+calShip, fill="red", tags="rect")
								self.lastPos = 0
							elif inc == 1:
								rect = caller.create_rectangle(entX, entY, entX+calShip, entY+50, fill="red", tags="rect")
								self.lastPos = 1
							elif inc == 2:
								rect = caller.create_rectangle(entX, entY+50, entX+50, entY-calShip+50, fill="red", tags="rect")
								self.lastPos = 2
							else:
								rect = caller.create_rectangle(entX+50, entY, entX-calShip+50, entY+50, fill="red", tags="rect")
								self.lastPos = 3
							break
						inc += 1
						if inc > 3:
							inc = 0
				
				if tmpShip.bCreated == True:
					#save for rotate
					self.saveX = x
					self.saveY = y
					self.pos = pos
					self.tmpShip = tmpShip
					self.rect = rect
					self.nbShip -= 1
					if inc == -1:
						self.lastPos = 0

				#stop rotate
				#if self.nbShip == 1:
				#	self.saveX = -1

	def tournerBateau(self,event):
		if self.saveX != -1:
			caller = event.widget
			x = self.saveX
			y = self.saveY

			entX = x // 50 * 50
			entY = y // 50 * 50
			pos = self.pos
			lengShip = self.nbShip
			if lengShip < 3:
				lengShip += 1
			calShip = lengShip * 50
			#bateau bas
			if ((entY + calShip) <= 550) and pos != "D" and self.lastPos < 1:
				pos = "D"
				self.lastPos = 1
				rect = caller.create_rectangle(entX, entY, entX+50, entY+calShip, fill="red", tags="rect")
			#bateau droite
			elif ((entX + calShip) <= 550) and pos != "R" and self.lastPos < 2:
				pos = "R"
				self.lastPos = 2
				rect = caller.create_rectangle(entX, entY, entX+calShip, entY+50, fill="red", tags="rect")
			#bateau haut
			elif ((entY - calShip) >= 0) and pos != "U" and self.lastPos < 3:
				pos = "U"
				self.lastPos = 3
				rect = caller.create_rectangle(entX, entY+50, entX+50, entY-calShip+50, fill="red", tags="rect")
			elif ((entX - calShip) >=0) and pos != "L" and self.lastPos < 4:
				pos = "L"
				self.lastPos = 0
				rect = caller.create_rectangle(entX+50, entY, entX-calShip+50, entY+50, fill="red", tags="rect")
			else:
				messagebox.showinfo("déplacer", "Impossible à déplacer !")
				self.lastPos = 0
				self.tournerBateau(event)
				return

			tmpShip = Ship(self.pNumber, lengShip, int(x//50) , int(y//50), pos)
			if tmpShip.bCreated == False:
				caller.delete(rect)
				messagebox.showinfo("déplacer", "Impossible à déplacer !")
			else:
				caller.delete(self.rect)
				self.pos = pos
				self.tmpShip = tmpShip
				self.rect = rect

	def lancer(self, event):
		x = event.x
		y = event.y
		caller = event.widget
		entX = x // 50 * 50
		entY = y // 50 * 50

		if x > 50 and x < 550 and y > 50 and y < 550:
			#rect = caller.create_rectangle(entX, entY, entX+50, entY+50, fill="red")
			ovl = caller.create_oval(entX+5, entY+5, entX+45, entY+45, fill="blue")

	def beginBateau(self):
		text = "player" + str(self.pNumber) + "veuillez placer vos bateaux"
		messagebox.showinfo("Bienvenue", text)

	def resetShip(self):
		if hasattr(self,'tmpShip'):
			self.tmpShip.deleteAllShip()
			self.nbShip = 6
			if self.pNumber == 1:
				for widget in self.F1.winfo_children():
					widget.destroy()
				self.initTab(self.F1)

Player1 = Interface(1, "ed")