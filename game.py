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
        if botManager.hour >= 24:
            gameState = "end"
    elif gameState == "end":
        gameState = graphics.endScreen()
        for event in events.event_queue:
            if event.type is pygame.KEYDOWN and event.key == pygame.K_1:
                graphics.userInput = 1
            if event.type is pygame.KEYDOWN and event.key == pygame.K_2:
                graphics.userInput = 2
            if event.type is pygame.KEYDOWN and event.key == pygame.K_3:
                graphics.userInput = 3
            if event.type is pygame.KEYDOWN and event.key == pygame.K_4:
                graphics.userInput = 4
            if event.type is pygame.KEYDOWN and event.key == pygame.K_5:
                graphics.userInput = 5
            if event.type is pygame.KEYDOWN and event.key == pygame.K_6:
                graphics.userInput = 6
            if event.type is pygame.KEYDOWN and event.key == pygame.K_7:
                graphics.userInput = 7
            if event.type is pygame.KEYDOWN and event.key == pygame.K_8:
                graphics.userInput = 8
            if event.type is pygame.KEYDOWN and event.key == pygame.K_9:
                graphics.userInput = 9

    elif gameState == "win":
        graphics.win()

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
