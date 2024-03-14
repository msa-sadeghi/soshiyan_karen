#TODO 
"""
یک تابع بنویسید که شامل پارامترهای زیر باشد
text, font, size, color, x,y
این تابع برای نمایش دادن موارد زیر بکار گرفته شود
score,
castle health,
money,
level number
"""
from constants import *
from castle import Castle
from enemy import Enemy
pygame.init()

bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
castle = Castle(castle_img_100,castle_img_50,castle_img_25, SCREEN_WIDTH- 400, SCREEN_HEIGHT-500, 0.3)


sample_enemy = Enemy(enemy_health[0], enemy_animations[0], 900, SCREEN_HEIGHT - 250, 1)
enemy_group.add(sample_enemy)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.blit(bg, (0,0))  
    castle.draw() 
    castle.shoot(bullet_group)   
    bullet_group.draw(screen)      
    bullet_group.update()
    enemy_group.draw(screen)      
    enemy_group.update(castle, bullet_group)
    pygame.display.update()
    clock.tick(FPS)