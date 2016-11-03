import pygame

event_queue = []
event_buffer = []

def new_event(event):
    global event_buffer
    event_queue.extend(event)

def update():
    global event_queue, event_buffer
    event_queue = pygame.event.get()
    event_queue.extend(event_buffer)
    event_buffer = []
