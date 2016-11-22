import pygame
import graphics
import events

run = True
displayText = ""
responses = []
npcDialog = []
order = ""
waiting = False

def readText(filename, npcName):
	global responses, npcDialog, nextFileName, order
	with open (filename, 'r') as myfile:
		for line in myfile:
			if "@NPC" in line:
				npcDialog.append(line)
				npcDialog = ([s.replace("@NPC", npcName + ":") for s in npcDialog])
				npcDialog = ([s.strip('\n') for s in npcDialog])
			
			if "@PLAYER" in line:
				responses.append(line)
				responses = ([s.strip("@PLAYER ") for s in responses])
				responses = ([s.strip('\n') for s in responses])
			
			if "@ORDER" in line:
				order = line
				order = ([s.strip("@ORDER ") for s in order])
				order = ([s.strip('\n') for s in order])


def sortText():
	global responses, npcDialog, order, waiting
	i = 0
	e = 0
	fontHeight = 255 
	nextRow = 17
	for letter in order:
		if letter == 'N':
			label = graphics._font.render(npcDialog[i], 1, (255,255,255))
			graphics._screen.blit(label, (10, fontHeight))
			i = i + 1
			fontHeight = fontHeight + nextRow
 		if letter == 'P':
			label = graphics._font.render(responses[e], 1, (255,255,255))
			graphics._screen.blit(label, (10, fontHeight))
			e = e + 1
			fontHeight = fontHeight + nextRow
		if letter == 'W':
			waiting = True
			while waiting:
				wait()

def wait():
	global waiting
	while waiting:
		pygame.time.wait(3000)
		for event in events.event_queue:
			if event.type is pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					waiting = False;
