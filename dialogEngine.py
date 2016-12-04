import pygame
import graphics
import events
import json
import bot

dialog = {}
label = {}
y = 0
fontHeight = 255
nextRow = 17

def readJson(filename):
	global dialog
	with open(filename) as myfile:
		dialog = json.load(myfile)

def readText(filename):
	global responses, dialog, nextFileName
	with open (filename, 'r') as myfile:
		for line in myfile:
			if "@DIALOG" in line:
				dialog.append(line)
				dialog = ([s.replace("@DIALOG","") for s in dialog])
				dialog = ([s.strip('\n') for s in dialog])

def showDialog(theBot):
	global dialog
	print theBot.name + ": " + dialog["greetings"][theBot.name];
	if theBot.behavior == "Standoffish":
		print "Go away"
	else:
		for clue in theBot.clues:
			print clue

def update():
	global y, dialog, fontHeight, nextRow, label

	if graphics.talking == True & graphics.optionPhase == True:
		label[y] = (graphics._font.render(dialog[y], 1, (255,255,0)))
		y = y + 1
		graphics.optionPhase = False
		print len(dialog)
		print y
		if y > len(dialog) - 1:
			graphics.talking = False
			y = 0
			label = {}
			dialog = []

	for x in label:
		graphics._screen.blit(label[x], (15, fontHeight))
		fontHeight = fontHeight + nextRow

	fontHeight = 255
