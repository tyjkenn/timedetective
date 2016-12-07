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
dialogEngine.readJson("dialog.json");
botManager.init()

paused = False

def update():
    events.update()
    thePlayer.update()
    if not dialogEngine.visible:
        botManager.update()
    graphics.update()

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
    clock.tick(60)
    if not run:
        pygame.quit()
        break
