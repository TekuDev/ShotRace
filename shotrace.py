#!/usr/bin/python3

import random

class As():
	"""docstring for As"""
	def __init__(self, stick):
		self.position = 0
		self.stick = stick

	def push(self):
		self.position += 1
	def back(self):
		if self.position > 0:
			self.position -= 1
		
class Step():
	"""docstring for Step"""
	def __init__(self, stick=""):
		self.isShown = False
		self.stick = stick

	def setStick(self,stick):
		self.stick = stick

	def show(self):
		self.isShown = True
		return self.stick

class Deck():
	"""docstring for Deck"""
	def __init__(self):
		self.nCor = 13
		self.nTreb = 13
		self.nPicas = 13
		self.nDiam = 13

	def reset(self):
		self.nCor = 13
		self.nTreb = 13
		self.nPicas = 13
		self.nDiam = 13

	def nextCard(self):
		if self.nCor == 0 and self.nTreb == 0 and self.nPicas == 0 and self.nDiam == 0:
			self.reset()
		nextStick = ""
		while nextStick == "":
			rand = random.randrange(4)
			if rand == 0 and self.nCor > 0:
				self.nCor -= 1
				nextStick = "Cor"
			elif rand == 1 and self.nTreb > 0:
				self.nTreb -= 1
				nextStick = "Treb"
			elif rand == 2 and self.nPicas > 0:
				self.nPicas -= 1
				nextStick = "Picas"
			elif rand == 3 and self.nDiam > 0:
				self.nDiam -= 1
				nextStick = "Diam"

		return nextStick

class Player():
	"""docstring for Player"""
	def __init__(self):
		self.nbet = 0
		self.stick = ""

	def printResult(self,stick):
		pass
	def setBet(self,bet,stick):
		self.nbet = bet
		self.stick = stick



class Table():
	"""docstring for Table"""
	def __init__(self,nplayers,maxSteps):
		self.asCor = As("Cor")
		self.asTreb = As("Treb")
		self.asPicas = As("Picas")
		self.asDiam = As("Diam")
		self.deck = Deck()
		self.lastCard = "NoCard"
		self.winner = False
		self.maxPosition = (maxSteps+1)
		self.currentMaxPosition = 0

		self.players = []
		for x in range(0,nplayers):
			self.players.append(Player())
		self.steps = []
		for x in range(0,maxSteps):
			self.steps.append(Step())

	def reset(self):
		pass

	def play(self):
		#nextCard
		self.nextCard()	

		#printTheNewTable
		self.printTable()

		#check steps
		self.checkSteps()

		#Check the win condition
		self.checkWinCondition()
		
	def nextCard(self):
		self.lastCard = self.deck.nextCard()
		if self.lastCard == "Cor":
			self.asCor.push()
		elif self.lastCard == "Treb":
			self.asTreb.push()
		elif self.lastCard == "Picas":
			self.asPicas.push()
		elif self.lastCard == "Diam":
			self.asDiam.push()
		else:
			print("ERROR in next card")
			exit(0)

		if self.asCor.position > self.currentMaxPosition:
				self.currentMaxPosition = self.asCor.position
		elif self.asTreb.position > self.currentMaxPosition:
				self.currentMaxPosition = self.asTreb.position
		elif self.asPicas.position > self.currentMaxPosition:
				self.currentMaxPosition = self.asPicas.position
		elif self.asDiam.position > self.currentMaxPosition:
				self.currentMaxPosition = self.asDiam.position

	def checkSteps(self):
		if self.currentMaxPosition > 0 and self.currentMaxPosition < self.maxPosition and not self.steps[(self.currentMaxPosition-1)].isShown:
			stick = self.steps[(self.currentMaxPosition-1)].show()
			if stick == "Cor":
				self.asCor.back()
			elif stick == "Treb":
				self.asTreb.back()
			elif stick == "Picas":
				self.asPicas.back()
			elif stick == "Diam":
				self.asDiam.back()
			else:
				print("ERROR in check steps")
				exit(0)
			self.printTable()

	def checkWinCondition(self):
		if self.asCor.position == self.maxPosition:
			print("Cor WIN!!")
			for player in self.players:
				player.printResult("Cor")
			exit(0)
		elif self.asTreb.position == self.maxPosition:
			print("Treb WIN!!")
			for player in self.players:
				player.printResult("Treb")		
			exit(0)
		elif self.asPicas.position == self.maxPosition:
			print("Picas WIN!!")
			for player in self.players:
				player.printResult("Picas")
			exit(0)
		elif self.asDiam.position == self.maxPosition:
			print("Diam WIN!!")
			for player in self.players:
				player.printResult("Diam")
			exit(0)

	def printTable(self):
		print("--------------------------------")
		#printAses
		for i in range(0,self.asCor.position):
			print("\t", end="")
		print("AsCor")
		for i in range(0,self.asTreb.position):
			print("\t", end="")
		print("asTreb")
		for i in range(0,self.asPicas.position):
			print("\t", end="")
		print("asPicas")
		for i in range(0,self.asDiam.position):
			print("\t", end="")
		print("asDiam")

		#printSteps
		i = 0
		for step in self.steps:
			print("\t", end="")
			if step.isShown == False:
				print("Step"+str(i), end="")
			else:
				print(step.stick, end="")
			i += 1

		#printLastCard
		print("")
		print(self.lastCard)
		print("--------------------------------")




#main

##define table
nplayers = int(input("How many players? "))
nsteps = int(input("How many steps? "))

table = Table(nplayers,nsteps)

##define steps
for s in table.steps:
	stick4step = table.deck.nextCard()
	if stick4step == "ERROR":
		print("Error generating the steps")
	else:
		s.setStick(stick4step)

#for s in table.steps:
#	print(s.stick)

##define bets
i = 0
for p in table.players:
	bet4player = int(input("How many bets does the player "+str(i)+"? "))
	stick4player = input("From which stick? (Cor, Treb, Picas, Diam) ")
	while stick4player != "Cor" and stick4player != "Treb" and stick4player != "Picas" and stick4player != "Diam":
		print("The player has to choice between 'Cor' or 'Treb' or 'Picas' or 'Diam'")
		stick4player = input("From which stick? (Cor, Treb, Picas, Diam) ")

	p.setBet(bet4player,stick4player)
	i += 1

#for p in table.players:
#	print(p.nbet, " ", p.stick)


##Let PLAY!
print("You have 3 options to play:")
print("Write '1' or press enter to play")
print("Write '2' to reset")
print("Write '3' to end")

table.printTable()

option = input("Select your option (1,2 or 3) ")
if option != '':
	option = int(option)
while(option != 3):
	if option == 2:
		#reset shit
		table.reset()
	else: #PLAY
		table.play()

	
	option = input("Select your option (1,2 or 3) ")
	if option != '':
		option = int(option)