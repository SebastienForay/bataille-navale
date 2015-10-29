import sys, threading, time, json
from class_player import Player
from class_ship import Ship

class ThreadReceive(threading.Thread):

	def __init__(self, sock, playerLocal_init, playerOnline_init):
		threading.Thread.__init__(self)
		self.sock = sock
		self.bReceivedReady = False
		self.playerLocal = playerLocal_init
		self.playerOnline = playerOnline_init
		
	def run(self):
		while True:
			message_recu = (self.sock.recv(8192)).decode()
			#print(message_recu)
			if message_recu == "disconnected":
				break
			elif message_recu[0:5] == "said ":
				print("\n" + message_recu[5:] + "\n")
			elif message_recu == "ready":
				self.bReceivedReady = True
				message_recu = ""

			elif message_recu[0:8] == "shipdata":
				data = str(message_recu[9:])
				parsed_json = json.loads(data)
				
				tmpShip = Ship(self.playerOnline, int(parsed_json['size']), int(parsed_json['posX']), str(parsed_json['posY']), str(parsed_json['orientation']))

				if tmpShip.bCreated == True:
					print("[!] Bateau de l'adversaire reçu et créé !")
					# Ajout du bateau au tableau de sauvegarde
					self.playerOnline.tableShips.append(tmpShip)

				message_recu = ""
			
			elif message_recu[0:4] == "fire":
				self.playerLocal.bPlays = False
				self.playerOnline.bPlays = True

				posFire = message_recu[5:]
				self.playerOnline.firedPos = posFire
				
				message_recu = ""

			elif message_recu[0:6] == "winner":
				print("Vous avez gagné !")
				break

			elif message_recu[0:7] == "youplay":
				print("[!] C'est à vous de jouer !")
				self.playerLocal.bPlays = True
				self.playerOnline.bPlays = False
				message_recu = ""
			elif message_recu[0:7] == "youwait":
				print("[!] C'est à votre adversaire de jouer !")
				self.playerLocal.bPlays = False
				self.playerOnline.bPlays = True
				message_recu = ""

		print("Client arrêté. Connexion interrompue.")
		self.sock.close()

class ThreadEmit(threading.Thread):
	def __init__(self, sock):
		threading.Thread.__init__(self)
		self.sock = sock
		self.bpause = False
		
	def run(self):
		while True:
			while self.bpause == False:
				message_emis = str("/" + input())
				if len(message_emis) > 2:
					self.sock.send(str.encode(message_emis))
			time.sleep(0.5)

	def pauseThread(self):
		self.bpause = True

	def resumeThread(self):
		self.bpause = False