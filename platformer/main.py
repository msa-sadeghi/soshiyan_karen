import pygame
from pygame.locals import *

from constants import *
from world import World
from levels.level1 import world_data

player_group = pygame.sprite.Group()

game_world = World(world_data, player_group)


running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    game_world.draw()
    player_group.update(game_world.tile_map_list)
    player_group.draw(SCREEN)
    pygame.display.update()
    clock.tick(FPS)