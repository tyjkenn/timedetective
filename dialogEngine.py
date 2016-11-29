import pygame
import graphics
import events

next = True
responses = []
dialog = []
label = {}
order = ""
length = 0
y = 0
fontHeight = 255 
nextRow = 17

def readText(filename, npcName):
	global responses, dialog, nextFileName, order, length
	with open (filename, 'r') as myfile:
		for line in myfile:
			if "@DIALOG" in line:
				dialog.append(line)
				dialog = ([s.replace("@DIALOG","") for s in dialog])
				dialog = ([s.strip('\n') for s in dialog])
				length = length + 1
			if "@CHOICE" in line:
				responses.append(line)
				responses = ([s.strip("@PLAYER ") for s in responses])
				responses = ([s.strip('\n') for s in responses])
			
			if "@ORDER" in line:
				order = line
				order = ([s.strip("@ORDER ") for s in order])
				order = ([s.strip('\n') for s in order])

def update():
	global y, dialog, responses, order, length, next, fontHeight, nextRow, label
	if graphics.talking == False:
		y = 0
		dialog = []
		respxonses = []
		order = ""
		length = 0

	if graphics.talking == True & graphics.optionPhase == True:
			print dialog[y]
			label[y] = (graphics._font.render(dialog[y], 1, (255,255,0)))
			y = y + 1
			graphics.optionPhase = False

	for x in label:
		graphics._screen.blit(label[x], (15, fontHeight))
		fontHeight = fontHeight + nextRow
		
	fontHeight = 255