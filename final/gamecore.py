#!/usr/bin/env python
# coding: utf-8

import os, socket, time, sys, json, uuid
from class_player import Player
from class_threads import ThreadReceive, ThreadEmit


os.system("mode con: cols=80 lines=50")

#Clear screen before the game
os.system('cls' if os.name == 'nt' else 'clear')

pseudoPlayer = ""
ip_server = "localhost"
port_server = 25465

pseudoClient = ""

print("			###########################\n"\
	"			##    Bataille Navale    ##\n"\
	"			###########################\n")

pseudoPlayer = str(input("Entrez votre pseudo : ")).replace(" ","")
ip_serverNew = input("IP du serveur [localhost]: ")
port_serverNew = input("Port du serveur [25465]: ")

if ip_serverNew != "":
	ip_server = ip_serverNew
if port_serverNew != "":
	port_server = port_serverNew

connectionServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[?] Tentative de connexion ...")
try:
	connectionServer.connect((ip_server, int(port_server)))
except socket.error:
	print("[/!\] La connexion a échoué !")
	sys.exit()

print("[!] Connexion établie !")


playerLocal = Player("WAIT", 1, pseudoPlayer, connectionServer)
playerOnline = Player("ONLINE", 2, pseudoClient, connectionServer)

thEmit = ThreadEmit(connectionServer)
thReceive = ThreadReceive(connectionServer, playerLocal, playerOnline)
thEmit.start()
thReceive.start()

print("[!] Envoi des informations client !")
connectionServer.send(str.encode("/setpseudo " + pseudoPlayer))

print("[?] Attente des informations de la partie ...")
connectionServer.send(str.encode("/step 2"))

pseudoClient = (connectionServer.recv(80)).decode()
print("Vous jouez contre " + str(pseudoClient) + " !\n")

connectionServer.send(str.encode("/step 3"))

print("[!] Préparez-vous à placer vos bateaux")
connectionServer.send(str.encode("/step 4"))

thEmit.pauseThread()

playerLocal.type = "LOCAL"
playerLocal.init_interface(thEmit, thReceive, playerLocal, playerOnline)
"""playerLocal.placeShips()
playerLocal.insertPlateau()"""

os.system('cls' if os.name == 'nt' else 'clear')

print("[!] En attente de votre adversaire ...")
connectionServer.send(str.encode("/step 5"))
thEmit.resumeThread()

while thReceive.bReceivedReady == False:
	sys.stdout.write(".")
	sys.stdout.flush()
	time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')
print("[!] La partie commence !")
connectionServer.send(str.encode("/step 6"))
time.sleep(1)

nbrCoup = 0

while True:
	nbrCoup += 1
	if playerLocal.bPlays == True and playerOnline.bPlays == False:
		os.system('cls' if os.name == 'nt' else 'clear')
		playerLocal.printGameboard()
		posFire = playerLocal.play()
		posX = 0
		posY = ''
		posYInt = 0

		connectionServer.send(str.encode("/fire " + posFire))

		playerLocal.playerFiring.append(posFire)
		#print("[DEBUG] posFire : " + str(posFire))

		# Parcours le tableau de bateau du P2
		for x in range(0, 5):
			index = 0
			bFound = False

			try:
				index = playerOnline.tableShips[x].tableAllPosShipsP1.index("'"+posFire+"'")
			except ValueError:
				#print("[DEBUG] Non trouvé dans le bateau " + str(x))
				if x == 4 and bFound == False:
					posX = int(posFire[0:len(posFire)-1]) - 1
					posYInt = playerLocal.tablePosYLetters.index(posFire[len(posFire)-1:])
					playerLocal.plateauPlayerFiring[posX][posYInt] = " * "
				continue
			else:
				#print("[DEBUG] Trouvé dans le bateau " + str(x))
				bFound = True
				playerOnline.tableShips[x].size -= 1

				posX = int(posFire[0:len(posFire)-1]) - 1
				posYInt = playerLocal.tablePosYLetters.index(posFire[len(posFire)-1:len(posFire)])
				playerLocal.plateauPlayerFiring[posX][posYInt] = " Ø "
				break
		playerLocal.bPlays = False

	elif playerLocal.bPlays == False and playerOnline.bPlays == True:
		os.system('cls' if os.name == 'nt' else 'clear')
		time.sleep(0.1)
		print("Veuillez attendre que votre opposant ai finit de jouer ...")
		posFire = playerOnline.firedPos
		while posFire == "":
			posFire = playerOnline.firedPos
		posX = 0
		posY = ''
		posYInt = 0

		for x in range(0, 5):
			index = 0
			bFound = False
			try:
				index = playerLocal.tableShips[x].tableAllPosShipsP1.index("'"+posFire+"'")
			except ValueError:
				#print("[DEBUG] Non trouvé dans le bateau " + str(x))
				if x == 4 and bFound == False:
					posX = int(posFire[0:len(posFire)-1]) - 1
					posYInt = playerLocal.tablePosYLetters.index(posFire[len(posFire)-1:len(posFire)])
					playerLocal.plateauPlayerShips[posX][posYInt] = " * "
				continue
			else:
				#print("[DEBUG] Trouvé dans le bateau " + str(x))
				bFound = True
				playerLocal.tableShips[x].size -= 1

				posX = int(posFire[0:len(posFire)-1]) - 1
				posYInt = playerLocal.tablePosYLetters.index(posFire[len(posFire)-1:len(posFire)])
				playerLocal.plateauPlayerShips[posX][posYInt] = " Ø "
				break

	# Check si le joueur local n'a plus de bateaux
	if playerLocal.tableShips[0].size == 0:
		if playerLocal.tableShips[1].size == 0:
			if playerLocal.tableShips[2].size == 0:
				if playerLocal.tableShips[3].size == 0:
					if playerLocal.tableShips[4].size == 0:
						print("Vous n'avez plus de bateaux, la partie est terminée !")
						connectionServer.send(str.encode("/dead"))
						playerLocal.winner = False
						break

#save score JSON
if hasattr(playerLocal, 'winner'):
	TitleH = ""
	if playerLocal.winner == True:
		TitleH = "Vous avez gagné la partie !"
		#winner
	if playerLocal.winner == False:
		TitleH = "Vous avez perdu la partie."
		#looser

	gameNbr = str(uuid.uuid4()) #radom uuid
	playerFire = ""
	for val in playerLocal.plateauPlayerFiring:
		for val2 in val:
			playerFire += val2 + ","

	playerPlateau = ""
	for val in playerLocal.plateauPlayerShips:
		for val2 in val:
			playerPlateau += val2 + ","

	data = {
		'gameNbr' : gameNbr,
		'myName' : playerLocal.pseudo,
		'hisName' : playerOnline.pseudo,
		'TitleH' : TitleH,
		'winner' : playerLocal.winner,
		'playerFire' : playerFire,
		'playerPlateau' : playerPlateau
		}

	fileName = "Demo\\blog\\templates\\blog\\games\\game_" + str(gameNbr)

	with open(fileName, 'w') as outfile:
		json.dump(data, outfile, ensure_ascii=False).encode('utf8')

cleanup_stop_thread();
connectionServer.close()
sys.exit()