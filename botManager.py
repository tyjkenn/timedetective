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

def randomizeClues():
    global bots
    clues = ["clue 1", "clue 2", "clue 3", "clue 4", "clue 5"]
    for bot in bots:
        clue = clues.pop(random.randint(0,len(clues) - 1))
        bot.clues.append(clue)

def randomizeBehaviors():
    global bots
    behaviors = [bot.Behavior.Gossiper, bot.Behavior.Standoffish, bot.Behavior.Liar, bot.Behavior.Friendly, bot.Behavior.Gossiper]
    for theBot in bots:
        if len(behaviors) > 0:
            theBot.behavior = behaviors.pop(random.randint(0, len(behaviors) - 1))

def createMockBot():
    global bots
    hobo = bot.Bot('shack', 200, 1, "Hobo")
    artist = bot.Bot('studio', 200, 2, "Artist")
    chef = bot.Bot('bakery', 200, 3, "Chef")
    innkeeper = bot.Bot('inn', 200, 4, "Innkeeper")
    huntress = bot.Bot('house', 200, 7, "Huntress")
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
    randomizeClues()
    randomizeBehaviors()
