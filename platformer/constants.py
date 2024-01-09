import pygame

SCREEN = pygame.display.set_mode()
SCREEN_WIDTH = SCREEN.get_width()
SCREEN_HEIGHT = SCREEN.get_height()
TILE_SIZE = 32


print(SCREEN_WIDTH/TILE_SIZE)
print(SCREEN_HEIGHT/TILE_SIZE)
FPS = 60
clock = pygame.time.Clock()

DIRT_IMAGE = pygame.image.load("assets/dirt.png")
GRASS_IMAGE = pygame.image.load("assets/grass.png")
WATER_IMAGE = pygame.image.load("assets/water.png")