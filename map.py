import pygame as pg

import pytmx
from pytmx import util_pygame

xOffset = 0
yOffset = 0
groundPoints = []
leftTileCount = 0
rightTileCount = 0

class Renderer(object):
    def findGround(self):
        global groundPoints, leftTileCount, rightTileCount
        foundGround = False
        layer_index = 0
        for layer in self.tmx_data.layers:
            if layer.name != 'ground':
                layer_index += 1
                continue
            for x in xrange(self.tmx_data.width):
                foundInCol = False
                for y in xrange(self.tmx_data.height):
                    props = self.tmx_data.get_tile_properties(x, y, layer_index)
                    if props is not None:
                        slope = props['groundSlope']
                        if slope == 'flat' or slope == 'down':
                            if groundPoints.count == 0:
                                if slope == 'flat':
                                    groundPoints.append(y * self.tmx_data.tileheight + 16)
                                else:
                                    groundPoints.append(y * self.tmx_data.tileheight)
                            groundPoints.append(y * self.tmx_data.tileheight + 16)
                            foundGround = True
                            foundInCol = True
                            break
                        if slope == 'up':
                            groundPoints.append(y * self.tmx_data.tileheight)
                            foundGround = True
                            foundInCol = True
                            break
                if not foundInCol:
                    if foundGround:
                        rightTileCount += 1
                    else:
                        leftTileCount += 1

    """
    This object renders tile maps from Tiled
    """
    def __init__(self, filename):
        tm = util_pygame.load_pygame(filename)
        self.size = tm.width * tm.tilewidth, tm.height * tm.tileheight
        self.tmx_data = tm
        self.findGround()


    def render(self, surface):

        tw = self.tmx_data.tilewidth
        th = self.tmx_data.tileheight

        if self.tmx_data.background_color:
            surface.fill(self.tmx_data.background_color)

        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    theTile = self.tmx_data.get_tile_image_by_gid(gid)
                    if theTile:
                        surface.blit(theTile, (x * tw + xOffset, y * th + yOffset))

            elif isinstance(layer, pytmx.TiledObjectGroup):
                pass

            elif isinstance(layer, pytmx.TiledImageLayer):
                image = self.tmx_data.get_tile_image_by_gid(layer.gid)
                if image:
                    surface.blit(image, (xOffset, yOffset))

    def make_map(self):
        temp_surface = pg.Surface(self.size)
        self.render(temp_surface)
        return temp_surface
