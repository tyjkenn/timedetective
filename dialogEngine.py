import pygame
import graphics
import events
import json
import bot

dialog = []
label = {}
fontHeight = 255
nextRow = 17

def readJson(filename):
	global dialog
	with open(filename) as myfile:
		dialog = json.load(myfile)

def showDialog(theBot):
	global dialog

	y = 0
	graphics.talking = True
	label[y] = (graphics._font.render(theBot.name + ": " + dialog["greetings"][theBot.name], 1, (255,255,0)))
	y += 1
	print theBot.name + ": " + dialog["greetings"][theBot.name];
	if theBot.behavior == "Standoffish":
		label[y] = (graphics._font.render("Go away", 1, (255,255,0)))
		print "Go away"
	else:
		for clue in theBot.clues:
			if len(clue) > 37:
				label[y] = (graphics._font.render(clue[:37], 1, (255,255,0)))
				y += 1
				label[y] = (graphics._font.render(clue[37:], 1, (255,255,0)))
				y += 1
			else:
				label[y] = (graphics._font.render(clue, 1, (255,255,0)))
				print clue
			y += 1

def update():
		global fontHeight, nextRow, label
		if graphics.talking == True:
			for x in label:
				graphics._screen.blit(label[x], (15, fontHeight))
				fontHeight = fontHeight + nextRow	

			if graphics.talking == False:
				label = {}
		fontHeight = 255
