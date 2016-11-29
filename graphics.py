import pygame
import pytmx
import map
import botManager
import dialogEngine

images = {}

_width = None
_height = None
_screen = None
_mapRenderer = None
_font = None

_entities = []

#Dialog Variables
talking = False
optionPhase = False
firstRun = True

def register(entity):
    global _entities
    if entity not in _entities:
        _entities.append(entity)

def set_map(mapName):
    global _mapRenderer
    if _mapRenderer is None:
        _mapRenderer = map.Renderer(mapName)
    else:
        map.activeRoomName = mapName
        map.activeRoom = _mapRenderer.rooms[mapName]

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
    global _screen, _font, firstRun
    label = _font.render(`botManager.hour` + ":" + `botManager.minute`, 1, (255,255,0))
    _screen.blit(label, (0, 0))
    if talking == True:
        botManager.paused = True
        pygame.draw.rect(_screen, (0, 0, 0), (0, 250, 400, 150))
        if firstRun == True:
            dialogEngine.readText("test.txt")
            firstRun = False
        dialogEngine.update()
    if talking == False:
        botManager.paused = False
        firstRun = True

def update():
    global _screen, _entities
    _screen.fill((100,100,255))
    draw_map()
    for entity in _entities:
        if not hasattr(entity, 'visible') or entity.visible:
            _screen.blit(pygame.transform.flip(
                                entity.sprite_sheet.subsurface(
                                    entity.FRAMES[10 * entity.action + int(entity.frame)]
                                ), entity.facingRight, False
                            ),
                            (entity.x + map.xOffset, entity.y + map.yOffset))
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
