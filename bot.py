import graphics
import botManager
from person import *

class ScheduleEvent(object):
    def __init__(self, hour, minute, place):
        self.hour = hour
        self.minute = minute
        self.place = place
        self.future = True

class Bot(Person):
    FRAMES = [(x*32,y*32,32,32) for y in xrange(5) for x in xrange(10)]
    def __init__(self, location, x):
        self.sprite_sheet = graphics.load_image("img/characters.png")
        self.frame = 1
        self.walkSpeed = 2
        self.scheduleEvents = []
        item = ScheduleEvent(6, 30, "graveyard")
        self.scheduleEvents.append(item)
        self.action = 0
        self.facingRight = False
        self.destination = None
        self.location = location
        self.y = 10
        self.directions = 0
        self.x = x

    def addToSchedule(self,scheduleEvent):
        self.scheduleItems.append(scheduleEvent);

    def checkSchedule(self):
        for event in self.scheduleEvents:
            if event.future and botManager.hour >= event.hour and botManager.minute >= event.minute:
                self.destination = event.place
                event.future = False

    def update(self):
        self.checkSchedule()
        self.snapToGround()
        tileX = self.x / 16
        if self.destination and self.location != 'outside':
            for roomName, doorX in graphics._mapRenderer.rooms[self.location].doors.iteritems():
                if roomName == 'outside':
                    if tileX > doorX:
                        self.x -= self.walkSpeed
                        self.facingRight = False
                    elif tileX < doorX:
                        self.x += self.walkSpeed
                        self.facingRight = True
                    else:
                        oldRoomName = self.location
                        self.location = 'outside'
                        self.x = graphics._mapRenderer.rooms[self.location].doors[oldRoomName] * 16
        self.visible = map.activeRoomName == self.location
