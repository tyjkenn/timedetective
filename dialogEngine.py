import pygame
import graphics
import events
import json
import bot
import textwrap

dialog = []
label = {}
fontHeight = 255
nextRow = 17
currentText = ""
visible = False

def readJson(filename):
	global dialog
	with open(filename) as myfile:
		dialog = json.load(myfile)

def showDialog(theBot):
	global dialog, currentText, visible, label
	label = {}
	currentText = theBot.name + ": " + dialog["greetings"][theBot.name] + " "
	if theBot.behavior == "Standoffish":
		currentText += "Go away"
	else:
		for clue in theBot.clues:
			currentText += clue
	visible = True

def update():
	global y, dialog, fontHeight, nextRow, label, currentText

	if visible:
		lines = textwrap.wrap(currentText, 38)
		for i in xrange(len(lines)):
			label[i] = (graphics._font.render(lines[i], 1, (255,255,0)))
	fontHeight = 255
