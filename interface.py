#!/usr/bin/env python
#-*- coding utf-8 -*-

from tkinter import *

root = Tk()

cadre = Frame(root, width=400, height=400, borderwidth=1, bg="red")
cadre.pack(fill=BOTH, expand=True)

mess = Label(cadre, text="Jeu de la bataille navale")
mess.pack()

quit = Button(cadre, text = "quit", command=root.quit)
quit.pack()


root.mainloop()
