from pygame.locals import *
import graphics
import pygame
import events
import math
import map
from person import *

class Player(Person):
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
        self.snapToGround()

    def update(self):
        self.handleInput()
        self.move()
        self.checkCollisions()

    def handleInput(self):
        self.takingAction = False
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

    def move(self):
        self.snapToGround()

    def checkCollisions(self):
        layer_index = 0
        mapX = int(self.x / 16)
        mapY = int(self.y / 16)
        for layer in map.activeRoom.data.layers:
            props =  map.activeRoom.data.get_tile_properties(mapX, mapY, layer_index)
            if props is not None:
                if self.takingAction and 'doorLocation' in props:
                    location =  props['doorLocation']
                    if location is not None:
                        map.xOffset = 0
                        map.yOffset = 0
                        graphics.set_map(location)
                        self.x = map.activeRoom.outX
                        self.snapToGround()
                        break
            layer_index += 1
