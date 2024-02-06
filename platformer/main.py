import pygame
from pygame.locals import *
from button import Button
from constants import *
from world import World
import os
import pickle
restart_button = Button(RESTART_BUTTON_IMAGE, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
level = 1
if os.path.exists("levels/level1"):
    f = open("levels/level1", "rb")
    world_data = pickle.load(f)
game_world = World(world_data, player_group, enemy_group, lava_group, door_group)
def reset_level():
    enemy_group.empty()
    lava_group.empty()
    door_group.empty()
    player_group.empty()
    if os.path.exists(f"levels/level{level}"):
        f = open(f"levels/level{level}", "rb")
        world_data = pickle.load(f)
    game_world = World(world_data, player_group, enemy_group, lava_group, door_group)
    return game_world
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    game_world.draw()

    player_group.update(game_world.tile_map_list, enemy_group, door_group)
    if not player_group.sprites()[0].alive:
        restart_button.draw()
        if restart_button.clicked:
            player_group.sprites()[0].alive = True
            player_group.sprites()[0].reset(100, 600)
    if player_group.sprites()[0].next_level:
        level += 1
        if level <= 2:
            player_group.sprites()[0].next_level = False
            world_data = []
            game_world = reset_level()
            
            

    player_group.draw(SCREEN)
    enemy_group.update()
    enemy_group.draw(SCREEN)
    lava_group.draw(SCREEN)
    door_group.draw(SCREEN)
    pygame.display.update()
    clock.tick(FPS)


