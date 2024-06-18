import pygame
from solider import Soldier
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
bullet_group = pygame.sprite.Group()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

moving_left = False
moving_right = False
shoot = False
FPS = 60
clock = pygame.time.Clock()

player = Soldier('player', 200, 300, 3, 3)
enemy = Soldier('enemy', 400, 300, 3, 3)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_SPACE:
                shoot = True
            if event.key == pygame.K_UP:
                player.jump = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_SPACE:
                shoot = False
            if event.key == pygame.K_UP:
                player.jump = False
    if player.in_air:
        player.update_action(2)
    elif moving_left or moving_right:
        player.update_action(1)
    else:
        player.update_action(0)   
    if shoot:
        player.shoot(bullet_group)         
    screen.fill((0,0,0))        
    player.draw(screen)
    player.update()
    player.move(moving_left, moving_right)
    bullet_group.update()
    bullet_group.draw(screen)
    enemy.draw(screen)
    pygame.display.update()
    clock.tick(FPS)