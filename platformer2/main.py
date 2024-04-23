import pygame
from solider import Soldier
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FPS = 60
clock = pygame.time.Clock()

player = Soldier('player', 200, 300, 3, 3)
enemy = Soldier('enemy', 400, 300, 3, 3)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))        
    player.draw(screen)
    enemy.draw(screen)
    pygame.display.update()
    clock.tick(FPS)