import pygame

run = True
displayText = ""
responses = []
npcDialog = []

def readText(filename):
	global responses, npcDialog
	with open (filename, 'r') as myfile:
		for line in myfile:
			if "@NPC" in line:
				npcDialog.append(line)
				npcDialog = ([s.strip("@NPC ") for s in npcDialog])
				npcDialog = ([s.strip('\n') for s in npcDialog])

			if "@PLAYER" in line:
				responses.append(line)
				responses = ([s.strip("@PLAYER ") for s in responses])

while(run):
	readText("test.txt")
	print npcDialog
	print responses
	run = False