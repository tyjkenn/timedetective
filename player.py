from pygame.locals import *
import graphics
import pygame
import events
import math
import map

class Action(object):
    IDLE   = 0
    WALK   = 1

class Dir(object):
    UP    = 1
    DOWN  = 2
    LEFT  = 4
    RIGHT = 8

class Player(object):
    FRAMES = [(x*32,y*32,32,32) for y in xrange(5) for x in xrange(10)]

    def __init__(self, x = 0, y = 200):
        self.sprite_sheet = graphics.load_image("img/characters.png")
        self.x = x
        self.y = y
        self.facingRight = False
        self.frame = 0
        self.action = Action.IDLE
        self.speed = 0
        self.walkSpeed = 2
        self.directions = 0
        self.takingAction = False

    def update(self):
        self.handleInput()
        self.move()
        self.checkCollisions()

    def handleInput(self):
        for event in events.event_queue:
            if event.type is pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.directions = self.directions | Dir.UP
                elif event.key == pygame.K_DOWN:
                    self.directions = self.directions | Dir.DOWN
                if event.key == pygame.K_LEFT:
                    self.directions = self.directions | Dir.LEFT
                    self.facingRight = False
                elif event.key == pygame.K_RIGHT:
                    self.directions = self.directions | Dir.RIGHT
                    self.facingRight = True
                elif event.key == pygame.K_SPACE:
                    self.frame = 0
                    self.takingAction = True
            elif event.type is pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.directions = self.directions & ~Dir.UP
                elif event.key == pygame.K_DOWN:
                    self.directions = self.directions & ~Dir.DOWN
                elif event.key == pygame.K_LEFT:
                    self.directions = self.directions & ~Dir.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.directions = self.directions & ~Dir.RIGHT
                elif event.key == pygame.K_SPACE:
                    self.takingAction = False

    def move(self):
        tileX = (self.x) / 16 - map.leftTileCount
        rightOfTile = (self.x - 16) % 16
        percentRight = float(rightOfTile) / 16.0
        if tileX < len(map.groundPoints) - 1:
            tileY1 = map.groundPoints[tileX]
            tileY2 = map.groundPoints[tileX + 1]
            if tileX > map.leftTileCount - 2:
                self.y = tileY1 + (tileY2 - tileY1) * percentRight  - 32
        if (self.directions & Dir.LEFT) and not self.directions & Dir.RIGHT and tileX > -1:
            self.x -= self.walkSpeed
            self.facingRight = False
            if self.x < 130 - map.xOffset:
                map.xOffset += self.walkSpeed
        elif (self.directions & Dir.RIGHT) and not self.directions & Dir.LEFT and tileX < graphics._mapRenderer.tmx_data.width - map.leftTileCount - map.rightTileCount - 1:
            self.x += self.walkSpeed
            self.facingRight = True
            if self.x > graphics._width - 162 - map.xOffset:
                map.xOffset -= self.walkSpeed
        mapX = self.x / graphics._mapRenderer.tmx_data.tilewidth
        mapY = self.y / graphics._mapRenderer.tmx_data.tileheight

    def checkCollisions(self):
        layer_index = 0
        mapX = int(self.x / 16)
        mapY = int(self.y / 16)
        for layer in graphics._mapRenderer.tmx_data.layers:
            props =  graphics._mapRenderer.tmx_data.get_tile_properties(mapX, mapY, layer_index)
            if props is not None:
                if self.takingAction and 'doorLocation' in props:
                    location =  props['doorLocation']
                    if location is not None:
                        print location
                        map.xOffset = 0
                        map.yOffset = 0
                        graphics.set_map(location)
                        break
            layer_index += 1
