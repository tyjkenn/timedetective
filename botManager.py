import bot

class BotManager(object):

    bots = []
    hour = 6
    minutes = 0
    frames = 0

    def tickClock(self):
        self.frames += 1
        if self.frames >= 20:
            self.frames = 0
            self.minutes += 1
        if self.minutes >= 60:
            self.minutes = 0
            self.hours += 1

    def update(self):
        self.tickClock()
        for bot in self.bots:
            bot.update()
