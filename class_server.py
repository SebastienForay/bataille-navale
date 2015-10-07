#!/usr/bin/env python
# coding : utf-8

import socket, threading

class ThreadServer(threading.Thread):

	def __init__(self, listeningPort_init):
		threading.Thread.__init__(self)
		self.listeningPort = listeningPort_init

		self.bServerStarted = False
		self.bConnectionDone = False
		self.bServerFull = False

		self.connexClient = 0

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind(('', self.listeningPort))
		self.sock.listen(1)

	def run(self):
		if self.bServerStarted == False:
			print("[!] Server lancé, prêt à héberger une partie !")
			self.bServerStarted = True

		if self.bConnectionDone == False:
			print("[?] En attente d'une connexion ...")
			self.connexClient, infos = self.sock.accept()

			# Effectué seulement quand une connexion entre
			self.bConnectionDone = True

		if self.bConnectionDone == True and self.bServerFull == False:
			pseudoRemotePlayer = self.receive(8192)
			print("[+] Le joueur %s vient de rejoindre la partie !\n" % (pseudoRemotePlayer))
			self.bServerFull = True

	def receive(self, bufferSize):
		message = (self.connexClient.recv(bufferSize)).decode()
		return message

	def send(self, msg):
		self.connexClient.send(str.encode(msg))

