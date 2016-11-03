import pygame, sys
import graphics
import events

graphics.init(400, 400)

def update():
    events.update()

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
    clock.tick(20)
    if not run:
        pygame.quit()
        break
