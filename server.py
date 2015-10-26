#!/usr/bin/env python
# coding: utf-8 

import os, socket, sys, threading, time

os.system('cls' if os.name == 'nt' else 'clear')

bReadyToPlay = [False, False]

class ThreadClient(threading.Thread):

	def __init__(self, sock_init):
		threading.Thread.__init__(self)
		self.sock = sock_init
		self.bReadyToPlay = False
		
	def run(self):
		self.threadName = self.playerPseudo = str(self.getName())

		while True:
			msg = (self.sock.recv(8192)).decode()
			print("%s> %s" % (self.threadName, msg))
			
			if msg[0:1] == "/":
				try:
					indexSpace = msg.index(' ')
					command = str(msg[1:indexSpace])
				except ValueError:
					command = str(msg[1:])

				if command == "quit":
					self.sock.send(str.encode("disconnected"))
					self.sock.close()
					break
				elif command == "setpseudo":
					pseudo = str(msg[indexSpace+1:])
					print("%s> Changement de pseudo validé" % (self.playerPseudo))

					for cle in list_sockPlayers:
						if cle != self.threadName:
							list_sockPlayers[cle].send(str.encode("[!] " + self.playerPseudo + \
								" change de pseudo pour '" + pseudo + "'"))

					self.playerPseudo = pseudo

				elif command == "say":
					sayMsg = str(msg[indexSpace+1:])
					print("%s> %s" % (self.playerPseudo, sayMsg))

					for cle in list_sockPlayers:
						if cle != self.threadName:
							list_sockPlayers[cle].send(str.encode(self.playerPseudo + ": " + sayMsg))

				elif command == "step":
					arg = str(msg[indexSpace+1:])
					if arg == "2":
						while len(list_sockPlayers) != 2:
							time.sleep(1)
						time.sleep(1)
						for cle in list_sockPlayers:
							if str(cle) == "Thread-1":
								list_sockPlayers["Thread-2"].send(str.encode(self.playerPseudo))
							elif str(cle) == "Thread-2":
								list_sockPlayers["Thread-1"].send(str.encode(self.playerPseudo))

					elif arg == "3":
						print("[!] Infos reçues par " + self.playerPseudo)

					elif arg == "4":
						print("[!] " + self.playerPseudo + " place ses bateaux !\n	En attente de réception ...")
					elif arg == "5":
						print("[!] " + self.playerPseudo + " est prêt à jouer !")
						if self.threadName == "Thread-1":
							bReadyToPlay[0] = True
						elif self.threadName == "Thread-2":
							bReadyToPlay[1] = True

						
						for cle in list_sockPlayers:
							if cle != self.threadName:
								while True:
									time.sleep(1)
									if str(cle) == "Thread-1":
										if bReadyToPlay[0] == True:
											list_sockPlayers["Thread-1"].send(str.encode("ready"))
											break
									elif str(cle) == "Thread-2":
										if bReadyToPlay[1] == True:
											list_sockPlayers["Thread-2"].send(str.encode("ready"))
											break
					elif arg == "6":
						print("[!] " + self.playerPseudo + " a commencé la partie !")

				elif command == "createship":
					shipInfos = str(msg[indexSpace+1:])
					if len(shipInfos) == 5:
						shipNumber = str(shipInfos[0:1])
						shipSize = str(shipInfos[1:2])
						shipPosX = str(shipInfos[2:3])
						shipPosY = str(shipInfos[3:4])
						shipOrientation = str(shipInfos[4:5])

						print("[!] Bateau en création par " + self.playerPseudo + \
							" -> " + shipNumber + ":" + shipSize + ":[" + shipPosX + ":" + shipPosY + "]:" + shipOrientation)
						
						self.sock.send(str.encode("ship ok"))

						jsonString = 'shipdata { "number": "' + shipNumber + '", "size": "' + shipSize + '", "posX": "' + shipPosX + '", "posY": "' + shipPosY + '", "orientation": "' + shipOrientation + '" }'

						for cle in list_sockPlayers:
							if cle != self.threadName:
								list_sockPlayers[cle].send(str.encode(jsonString))
					
					elif len(shipInfos) == 6:
						shipNumber = str(shipInfos[0:1])
						shipSize = str(shipInfos[1:2])
						shipPosX = str(shipInfos[2:4])
						shipPosY = str(shipInfos[4:5])
						shipOrientation = str(shipInfos[5:6])

						print("[!] Bateau en création par " + self.playerPseudo + \
							" -> " + shipNumber + ":" + shipSize + ":[" + shipPosX + ":" + shipPosY + "]:" + shipOrientation)
						self.sock.send(str.encode("ship ok"))

				elif command == "fire":
					posFire = str(msg[indexSpace+1:])
					for cle in list_sockPlayers:
						if cle != self.threadName:
							list_sockPlayers[cle].send(str.encode("youwait"))
							time.sleep(0.2)
							list_sockPlayers[cle].send(str.encode("fire " + str(posFire)))

					for cle in list_sockPlayers:
						if cle == self.threadName:
							time.sleep(0.2)
							list_sockPlayers[cle].send(str.encode("youwait"))
						elif cle != self.threadName:
							time.sleep(0.2)
							list_sockPlayers[cle].send(str.encode("youplay"))

				elif command == "dead":
					for cle in list_sockPlayers:
						if cle != self.threadName:
							list_sockPlayers[cle].send(str.encode("winner"))

		self.sock.close()
		del list_sockPlayers[self.threadName]
		print("\n[-] Le joueur %s s'est déconnecté" % self.playerPseudo)

#################################################################################



print("			######################################\n"\
	"			##    Serveur de Bataille Navale    ##\n"\
	"			######################################\n")

print( "[!] Serveur lancé sur le port 25465")
print( "[!] Partie en attente de joueurs")


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	sock.bind(('', 25465))
except socket.error:
	print("La liaison du socket à l'adresse choisie a échoué.")
	sys.exit()

sock.listen(2)

list_sockPlayers = {}

bPlayerToPlaySent = False
while True:
	if len(list_sockPlayers) < 2:
		connection, adress = sock.accept()
		th = ThreadClient(connection)
		th.start()
		idTh = th.getName()
		list_sockPlayers[idTh] = connection
		print("\n[+] Joueur %s connecté depuis %s:%s" %\
			   (idTh, adress[0], adress[1]))
	if bPlayerToPlaySent == False:
		if bReadyToPlay[0] == True:
			print("Player1 ready")
			if bReadyToPlay[1] == True:
				print("Player2 ready")
				list_sockPlayers["Thread-1"].send(str.encode("youplay"))
				list_sockPlayers["Thread-2"].send(str.encode("youwait"))
				print("messages sent")
				bPlayerToPlaySent = True