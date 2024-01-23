import pygame
from pygame.locals import *
from button import Button
from constants import *
from world import World
from levels.level1 import world_data

restart_button = Button(RESTART_BUTTON_IMAGE, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()

game_world = World(world_data, player_group, enemy_group, lava_group)


running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    game_world.draw()

    player_group.update(game_world.tile_map_list, enemy_group)
    if not player_group.sprites()[0].alive:
        restart_button.draw()
        if restart_button.clicked:
            player_group.sprites()[0].alive = True


    player_group.draw(SCREEN)
    enemy_group.update()
    enemy_group.draw(SCREEN)
    lava_group.draw(SCREEN)
    pygame.display.update()
    clock.tick(FPS)


# TODO reset player