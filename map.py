import pygame as pg
import os
import pytmx
from pytmx import util_pygame

xOffset = 0
yOffset = 0

class Room(object):
    def __init__(self, data, size):
        self.data = data
        self.size = size
        self.groundPoints = []
        self.leftTileCount = 0
        self.rightTileCount = 0
        self.doors = {}

    def findDoors(self):
        layer_index = 0
        for layer in self.data.layers:
            if layer.name != 'doors':
                layer_index += 1
                continue
            for x in xrange(self.data.width):
                for y in xrange(self.data.height):
                    props = self.data.get_tile_properties(x, y, layer_index)
                    if props is not None and 'doorLocation' in props:
                        self.doors[props['doorLocation']] = x

    def findGround(self):
        self.leftTileCount = 0
        self.rightTileCount = 0
        self.groundPoints = []
        foundGround = False
        layer_index = 0
        for layer in self.data.layers:
            if layer.name != 'ground':
                layer_index += 1
                continue
            for x in xrange(self.data.width):
                foundInCol = False
                for y in xrange(self.data.height):
                    props = self.data.get_tile_properties(x, y, layer_index)
                    if props is not None:
                        slope = props['groundSlope']
                        if slope == 'flat' or slope == 'down':
                            if self.groundPoints.count == 0:
                                if slope == 'flat':
                                    self.groundPoints.append(y * self.data.tileheight + 16)
                                else:
                                    self.groundPoints.append(y * self.data.tileheight)
                            self.groundPoints.append(y * self.data.tileheight + 16)
                            foundGround = True
                            foundInCol = True
                            break
                        if slope == 'up':
                            self.groundPoints.append(y * self.data.tileheight)
                            foundGround = True
                            foundInCol = True
                            break
                if not foundInCol:
                    if foundGround:
                        self.rightTileCount += 1
                    else:
                        self.leftTileCount += 1

class Renderer(object):

    """
    This object renders tile maps from Tiled
    """
    def __init__(self, mapName):
        global activeRoom, activeRoomName
        self.rooms = {}
        for filename in os.listdir('maps'):
            if filename.endswith(".tmx"):
                tm = util_pygame.load_pygame('maps/' + filename)
                size = tm.width * tm.tilewidth, tm.height * tm.tileheight
                room = Room(tm, size)
                room.findDoors()
                room.findGround()
                self.rooms[filename.split(".")[0]] = room
        activeRoom = self.rooms[mapName]
        activeRoomName = mapName

    def render(self, surface):
        global activeRoom
        tw = activeRoom.data.tilewidth
        th = activeRoom.data.tileheight

        if activeRoom.data.background_color:
            surface.fill(activeRoom.data.background_color)

        for layer in activeRoom.data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    theTile = activeRoom.data.get_tile_image_by_gid(gid)
                    if theTile:
                        surface.blit(theTile, (x * tw + xOffset, y * th + yOffset))

            elif isinstance(layer, pytmx.TiledObjectGroup):
                pass

            elif isinstance(layer, pytmx.TiledImageLayer):
                image = activeRoom.data.get_tile_image_by_gid(layer.gid)
                if image:
                    surface.blit(image, (xOffset, yOffset))

    def make_map(self):
        temp_surface = pg.Surface(self.size)
        self.render(temp_surface)
        return temp_surface
