import pygame, sys
import graphics
import events
import pytmx
import botManager
import player
import bot
import dialogEngine

pygame.init()
graphics.init(400, 400)
graphics.set_map('outside')
thePlayer = player.Player(200, 100)
graphics.register(thePlayer)
botManager.init()

paused = False

def update():
    events.update()
    thePlayer.update()
    graphics.update()
    if not paused:
        botManager.update()

run = True
clock = pygame.time.Clock()
while True:
    update()
    for e in events.event_queue:
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_F4 and e.mod == pygame.KMOD_ALT:
                run = False
    clock.tick(120)
    if not run:
        pygame.quit()
        break
