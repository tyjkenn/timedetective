import pygame as pg

import pytmx
from pytmx import util_pygame

xOffset = 0
yOffset = 0

class Renderer(object):
    """
    This object renders tile maps from Tiled
    """
    def __init__(self, filename):
        tm = util_pygame.load_pygame(filename)
        self.size = tm.width * tm.tilewidth, tm.height * tm.tileheight
        self.tmx_data = tm

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
