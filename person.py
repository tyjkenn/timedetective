import map
import graphics

class Action(object):
    IDLE   = 0
    WALK   = 1

class Dir(object):
    UP    = 1
    DOWN  = 2
    LEFT  = 4
    RIGHT = 8

'''Abstract class. Should have an x and a y defined in order to work'''
class Person(object):
    def snapToGround(self):
        tileX = (self.x) / 16 - map.activeRoom.leftTileCount
        rightOfTile = (self.x - 16) % 16
        percentRight = float(rightOfTile) / 16.0
        if tileX < len(map.activeRoom.groundPoints) - 1:
            tileY1 = map.activeRoom.groundPoints[tileX]
            tileY2 = map.activeRoom.groundPoints[tileX + 1]
            self.y = tileY1 + (tileY2 - tileY1) * percentRight  - 32
        if (self.directions & Dir.LEFT) and not self.directions & Dir.RIGHT and tileX > -1:
            self.x -= self.walkSpeed
            self.facingRight = False
            if self.x < 130 - map.xOffset:
                map.xOffset += self.walkSpeed
        elif (self.directions & Dir.RIGHT) and not self.directions & Dir.LEFT and tileX < map.activeRoom.data.width - map.activeRoom.leftTileCount - map.activeRoom.rightTileCount - 1:
            self.x += self.walkSpeed
            self.facingRight = True
            if self.x > graphics._width - 162 - map.xOffset:
                map.xOffset -= self.walkSpeed
