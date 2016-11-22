import graphics
import botManager

class ScheduleEvent(object):
    def __init__(self, hour, minute, place):
        self.hour = hour
        self.minute = minute
        self.place = place
        self.future = True

class Bot(object):
    FRAMES = [(x*32,y*32,32,32) for y in xrange(5) for x in xrange(10)]
    def __init__(self):
        self.sprite_sheet = graphics.load_image("img/characters.png")
        self.frame = 1
        self.walkSpeed = 2
        self.scheduleEvents = []
        item = ScheduleEvent(6, 30, "graveyard")
        self.scheduleEvents.append(item)
        self.action = 0
        self.facingRight = False
        self.destination = None
        self.location = "plaza"
        self.y = 10

    def addToSchedule(self,scheduleEvent):
        self.scheduleItems.append(scheduleEvent);

    def checkSchedule(self):
        for event in self.scheduleEvents:
            if event.future and botManager.hour >= event.hour and botManager.minute >= event.minute:
                self.destination = event.place
                event.future = False

    def update(self):
        self.checkSchedule()
        if self.destination:
            print "Going to", self.destination
            self.location = self.destination
            self.x += self.walkSpeed
