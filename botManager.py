from pygame.locals import *
import graphics
import pygame
import bot
import random
import dialogEngine
import re

bots = []
hour = 6
minute = 0
frames = 0
paused = False

roomNames = ['shack','studio','inn','bakery','house']

def randomizeSchedule(theBot):
    for i in xrange(9):
        hour = random.randrange(6, 12)
        room = roomNames[random.randrange(0,len(roomNames))]
        theBot.addToSchedule(bot.ScheduleEvent(i*2 + 6, 0, room))

def randomizeRoles():
    global bots
    roles = bot.roles[:]
    for theBot in bots:
        if len(roles) > 0:
            theBot.role = roles.pop(random.randint(0, len(roles) - 1))

def randomizeClues():
    global bots
    clues = dialogEngine.dialog["clues"]
    for bot1 in bots:
        clue = clues.pop(random.randint(0,len(clues) - 1))
        behaviorToken = re.search(r"\[([A-Za-z0-9_]+)\]", clue)
        roleToken = re.search(r"\{([A-Za-z0-9_]+)\}", clue)
        if behaviorToken != None:
            if bot1.behavior == "Liar":
                randBot = None
                while randBot == None or randBot.behavior == behaviorToken:
                    randBot = random.choice(bots)
                clue = re.sub(r"\[([A-Za-z0-9_]+)\]", randBot.name, clue)
            else:
                for bot2 in bots:
                    if bot2.behavior == behaviorToken.group(1):
                        clue = re.sub(r"\[([A-Za-z0-9_]+)\]", bot2.name, clue)
                        break
        if roleToken != None:
            if bot1.behavior == "Liar":
                randBot = None
                while randBot == None or randBot.role == roleToken:
                    randBot = random.choice(bots)
                clue = re.sub(r"\{([A-Za-z0-9_]+)\}", randBot.name, clue)
            else:
                for bot2 in bots:
                    if bot2.role == roleToken.group(1):
                        clue = re.sub(r"\{([A-Za-z0-9_]+)\}", bot2.name, clue)
                        break
        bot1.clues.append(clue)

def randomizeBehaviors():
    global bots
    behaviors = bot.behaviors[:]
    for theBot in bots:
        if len(behaviors) > 0:
            theBot.behavior = behaviors.pop(random.randint(0, len(behaviors) - 1))

def randomizeAbilities():
    global bots
    abilities = bot.abilities[:] + bot.abilities[:] + bot.abilities
    for theBot in bots:
        if len(abilities) > 0:
            theBot.ability = abilities.pop(random.randint(0, len(abilities) - 1))

def createMockBot():
    global bots
    hobo = bot.Bot('shack', 200, 1, "Hobo")
    artist = bot.Bot('studio', 200, 2, "Artist")
    chef = bot.Bot('bakery', 200, 3, "Chef")
    innkeeper = bot.Bot('inn', 200, 4, "Innkeeper")
    huntress = bot.Bot('house', 200, 7, "Huntress")
    oldMan = bot.Bot('house2', 200, 0, "Old Man")
    scientist = bot.Bot('lab', 200, 5, "Scientist")
    gardener = bot.Bot('garden', 200, 6, "Gardener")
    merchant = bot.Bot('house3', 200, 8, "Merchant")
    bots.append(hobo)
    bots.append(artist)
    bots.append(chef)
    bots.append(innkeeper)
    bots.append(huntress)
    bots.append(oldMan)
    bots.append(scientist)
    bots.append(gardener)
    bots.append(merchant)
    for theBot in bots:
        graphics.register(theBot)
        randomizeSchedule(theBot)

def tickClock():
    global hour, minute, frames
    frames += 1
    if frames >= 10:
        frames = 0
        minute += 1
    if minute >= 60:
        minute = 0
        hour += 1

def update():
    global bots
    if paused == False:
        tickClock()
        for theBot in bots:
            theBot.update()

def init():
    createMockBot()
    randomizeRoles()
    randomizeBehaviors()
    randomizeClues()
