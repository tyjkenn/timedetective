import pygame
import pytmx
import map
import botManager

images = {}

_width = None
_height = None
_screen = None
_mapRenderer = None
_font = None

_entities = []

def register(entity):
    global _entities
    if entity not in _entities:
        _entities.append(entity)

def set_map(filename):
    global _mapRenderer
    _mapRenderer = map.Renderer(filename)

def init(width, height, title = 'Time Detective'):
    global _width, _height, _screen, _font
    _width = width
    _height = height
    pygame.display.init()
    _screen = pygame.display.set_mode((_width, _height), pygame.DOUBLEBUF)
    pygame.display.set_caption(title)
    _font = pygame.font.SysFont("monospace", 16)

def draw_map():
    global _screen
    _mapRenderer.render(_screen)

def draw_ui():
    global _screen, _font
    label = _font.render(`botManager.hour` + ":" + `botManager.minute`, 1, (255,255,0))
    _screen.blit(label, (0, 0))

def update():
    global _screen, _entities
    _screen.fill((0,0,0))
    draw_map()
    for entity in _entities:
        _screen.blit(pygame.transform.flip(
                            entity.sprite_sheet.subsurface(
                                entity.FRAMES[10 * entity.action + int(entity.frame)]
                            ), entity.facing, False
                        ),
                        (entity.x, entity.y))
    draw_ui()
    pygame.display.flip();

def load_image(path):
    global images
    if path in images:
        return images[path]
    image = pygame.image.load(path)
    image.convert()
    images[path] = image
    return image
