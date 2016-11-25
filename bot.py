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
        if self.destination:
            if self.location != 'outside':
                if self.x > map.activeRoom.outX + 2:
                    self.x -= self.walkSpeed
                    self.facingRight = False
                elif self.x < map.activeRoom.outX - 2:
                    self.x += self.walkSpeed
                    self.facingRight = True
                else:
                    self.location = 'outside'
        self.visible = map.activeRoomName == self.location
