from pygame.locals import *
import graphics
import pygame
import bot
import random

bots = []
hour = 6
minute = 0
frames = 0
paused = False

roomNames = ['shack','studio','inn','bakery','house']

def randomizeSchedule(theBot):
    for i in xrange(40):
        minute = random.randrange(0, 60)
        hour = random.randrange(6, 12)
        room = roomNames[random.randrange(0,len(roomNames))]
        theBot.addToSchedule(bot.ScheduleEvent(hour, minute, room))

def createMockBot():
    global bots
    hobo = bot.Bot('shack', 200, 1)
    artist = bot.Bot('studio', 200, 2)
    chef = bot.Bot('bakery', 200, 3)
    innkeeper = bot.Bot('inn', 200, 4)
    huntress = bot.Bot('house', 200, 7)
    graphics.register(hobo)
    graphics.register(artist)
    graphics.register(chef)
    graphics.register(innkeeper)
    graphics.register(huntress)
    bots.append(hobo)
    bots.append(artist)
    bots.append(chef)
    bots.append(innkeeper)
    bots.append(huntress)
    randomizeSchedule(hobo)
    randomizeSchedule(artist)
    randomizeSchedule(chef)
    randomizeSchedule(innkeeper)
    randomizeSchedule(huntress)

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
