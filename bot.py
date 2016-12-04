import graphics
import botManager
import random
from person import *

behaviors = [
    "Gossiper",
    "Standoffish",
    "Liar",
    "Friendly",
    "Hospitable",
]

class ScheduleEvent(object):
    def __init__(self, hour, minute, place):
        self.hour = hour
        self.minute = minute
        self.place = place
        self.future = True

class Bot(Person):
    FRAMES = [(x*32,y*32,32,32) for y in xrange(5) for x in xrange(10)]
    def __init__(self, location, x, frame, name):
        self.sprite_sheet = graphics.load_image("img/characters.png")
        self.frame = frame
        self.walkSpeed = 1
        self.scheduleEvents = []
        self.action = 0
        self.facingRight = False
        self.destination = None
        self.location = location
        self.y = 10
        self.directions = 0
        self.x = x
        self.randomRoomPos = 0
        self.clues = []
        self.behavior = None
        self.name = name

    def addToSchedule(self,scheduleEvent):
        self.scheduleEvents.append(scheduleEvent);

    def checkSchedule(self):
        for event in self.scheduleEvents:
            if event.future and botManager.hour >= event.hour and botManager.minute >= event.minute:
                self.destination = event.place
                event.future = False

    def handleBehavior(self):
        if self.behavior == "Gossiper":
            for other in botManager.bots:
                if other.location == self.location and self.location != 'outside':
                    for clue in self.clues:
                        if clue not in other.clues:
                            other.clues.append(clue)

    def update(self):
        self.checkSchedule()
        self.snapToGround()
        tileX = self.x / 16
        if self.destination:
            if self.destination != self.location:
                for roomName, doorX in graphics._mapRenderer.rooms[self.location].doors.iteritems():
                    if roomName == self.destination or roomName == 'outside':
                        if tileX > doorX:
                            self.x -= self.walkSpeed
                            self.facingRight = False
                        elif tileX < doorX:
                            self.x += self.walkSpeed
                            self.facingRight = True
                        else:
                            oldRoomName = self.location
                            self.location = roomName
                            self.x = graphics._mapRenderer.rooms[self.location].doors[oldRoomName] * 16
                            self.randomRoomPos = random.randrange(-100,100)
            else:
                midPoint = graphics._mapRenderer.rooms[self.location].data.width * 16 / 2
                if self.x < midPoint + self.randomRoomPos:
                    self.x += self.walkSpeed
                else:
                    self.destination = None
        self.visible = map.activeRoomName == self.location
        self.handleBehavior()
        if self.visible:
            self.snapToGround()
