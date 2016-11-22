from pygame.locals import *
import graphics
import pygame
import bot

bots = []
hour = 6
minute = 0
frames = 0
paused = False

def createMockBot():
    global bots
    theBot = bot.Bot()
    graphics.register(theBot)
    bots.append(theBot)

def tickClock():
    global hour, minute, frames
    if paused == False:
        frames += 1
        if frames >= 20:
            frames = 0
            minute += 1
        if minute >= 60:
            minute = 0
            hour += 1

def update():
    global bots
    tickClock()
    for theBot in bots:
        theBot.update()

def init():
    createMockBot()
