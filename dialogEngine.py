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
page = 0

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
			currentText += clue + " "
	if len(theBot.gossip) > 0:
		currentText += "Here are some things I've been hearing from others: "
		for clue in theBot.gossip:
			currentText += clue + " "
	visible = True

def update():
	global y, dialog, fontHeight, nextRow, label, currentText, page, visible
	if visible:
		lines = textwrap.wrap(currentText, 37)
		if page > (len(lines) - 1) / 5:
			visible = False
			return
		if len(lines) > page * 5 + 5:
			maxLine = 5
		else:
			maxLine = len(lines) - page * 5
		label = {}
		for i in xrange(maxLine):
			label[i] = (graphics._font.render(lines[i + page * 5], 1, (255,255,0)))
	fontHeight = 255
