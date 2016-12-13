import pygame
import pytmx
import map
import botManager
import dialogEngine
import textwrap

images = {}

_width = None
_height = None
_screen = None
_mapRenderer = None
_font = None

_entities = []

userInput = 0
murdererGuess = 0
weaponGuess = 0

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
    if dialogEngine.visible:
        botManager.paused = True
        pygame.draw.rect(_screen, (0, 0, 0), (0, 250, 400, 150))
        dialogEngine.update()
        for x in dialogEngine.label:
    		_screen.blit(dialogEngine.label[x], (15, dialogEngine.fontHeight))
    		dialogEngine.fontHeight = dialogEngine.fontHeight + dialogEngine.nextRow
    else:
        botManager.paused = False

def intro():
    global _screen, _font
    _screen.fill((0,0,0))
    text = "You intercept a note hinting of a planned murder. You journey to a small town to investigate..."
    lines = textwrap.wrap(text, 35)
    for i in xrange(len(lines)):
        label = (_font.render(lines[i], 1, (255,255,255)))
        _screen.blit(label, (30, 100 + (i*20)))
    pygame.display.flip();

def endScreen():
    global _screen, _font, userInput, murdererGuess, weaponGuess
    _screen.fill((0,0,0))
    if userInput != 0:
        if murdererGuess == 0:
            murdererGuess = userInput
        elif weaponGuess == 0:
            weaponGuess = userInput
        userInput = 0

    i = 0
    for theBot in botManager.bots:
        i += 1
        if theBot.role == "Murderer":
            Correct = i
            if "Magic" in theBot.ability:
                correctWeapon = 1
            elif "Gun" in theBot.ability:
                correctWeapon = 2
            elif "Sword" in theBot.ability:
                correctWeapon = 3
            print Correct, correctWeapon
    if murdererGuess == 0:
        text = "Who do you think is the murderer?"
        lines = textwrap.wrap(text, 35)
        lines.append("1. Hobo")
        lines.append("2. Artist")
        lines.append("3. Chef")
        lines.append("4. Innkeeper")
        lines.append("5. Huntress")
        lines.append("6. Old Man")
        lines.append("7. Scientist")
        lines.append("8. Gardener")
        lines.append("9. Merchant")
    elif weaponGuess == 0:
        text = "What will the murder use?"
        lines = textwrap.wrap(text, 35)
        lines.append("1. Magic")
        lines.append("2. Gun")
        lines.append("3. Sword")
    else:
        if murdererGuess == Correct and weaponGuess == correctWeapon:
            return "win"
        else:
            return "lose"
    for i in xrange(len(lines)):
        label = (_font.render(lines[i], 1, (255,255,255)))
        _screen.blit(label, (30, 50 + (i*20)))
    pygame.display.flip();
    userInput = 0
    return "end"

def win():
    global _screen, _font
    _screen.fill((0,0,0))
    for bot in botManager.bots:
        if bot.role == "Murderer":
            murdererName = bot.name
        if bot.role == "Victim":
            victimName = bot.name
    text = murdererName + " sneaks in to attack " + victimName
    text += ", only to find the authorities ready for him. They cuff the villian and take him to jail. The day is saved!"
    lines = textwrap.wrap(text, 35)
    for i in xrange(len(lines)):
        label = (_font.render(lines[i], 1, (255,255,255)))
        _screen.blit(label, (30, 100 + (i*20)))
    pygame.display.flip();

def lose():
    global _screen, _font
    murdererGuess = 0
    weaponGuess = 0
    _screen.fill((0,0,0))
    text = "You hear screaming in the distance. Your rescue failed. Fortunately, this is just a game, and games can be reset. You travel back in time to the start of the day to try again."
    lines = textwrap.wrap(text, 35)
    for i in xrange(len(lines)):
        label = (_font.render(lines[i], 1, (255,255,255)))
        _screen.blit(label, (30, 100 + (i*20)))
    pygame.display.flip();

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
