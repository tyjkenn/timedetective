import pygame, sys
import graphics
import events
import pytmx

graphics.init(400, 400)
graphics.set_map("maps/outside.tmx");

def update():
    events.update()
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
    clock.tick(20)
    if not run:
        pygame.quit()
        break
