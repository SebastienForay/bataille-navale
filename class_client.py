#!/usr/bin/env python
# coding : utf-8

import socket, threading

class ThreadClient(threading.Thread):

	def __init__(self, ip_init, port_init):
		threading.Thread.__init__(self)
		self.port = port_init
		self.ip = ip_init
		self.bConnectionDone = False

		self.sockServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def run(self):
		if self.bConnectionDone == False:
			print("[?] Tentative de connexion ...")
			self.sockServer.connect((self.ip, self.port))

			# Effectué seulement quand la connexion est établie
			self.bConnectionDone = True

	def receive(self, bufferSize):
		message = (self.sockServer.recv(bufferSize)).decode()
		return message

	def send(self, msg):
		bytes = str.encode(str(msg))
		self.sockServer.send(bytes)

