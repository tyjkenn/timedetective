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

gameState = "start"
paused = False

def update():
    global gameState
    events.update()
    if gameState == "start":
        graphics.intro()
        for event in events.event_queue:
            if event.type is pygame.KEYDOWN and event.key == pygame.K_SPACE:
                gameState = "interact"
    elif gameState == "interact":
        thePlayer.update()
        if not dialogEngine.visible:
            botManager.update()
        graphics.update()
    elif gameState == "end":
        pass
    elif gameState == "win":
        pass

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
