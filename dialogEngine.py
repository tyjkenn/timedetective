import pygame
import graphics
import events

next = True
responses = []
dialog = []
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
	global y, dialog, responses, order, length, next, fontHeight, nextRow
	if graphics.talking == False:
		y = 0
		dialog = []
		responses = []
		order = ""
		length = 0
		fontHeight = 255
	if graphics.talking == True & next == True:
			print dialog[y]
			label = graphics._font.render(dialog[y], 1, (255,255,255))
			graphics._screen.blit(label, (10, fontHeight))
			fontHeight = fontHeight + nextRow
			y = y + 1
			next = False

