import scheduleItem

class Bot(object):

    scheduleItems = []

    def addToSchedule(self,scheduleItem):
        self.scheduleItems.extend(scheduleItem);

    def update(self):
        pass
