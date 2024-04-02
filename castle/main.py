
from constants import *
from castle import Castle
from enemy import Enemy
from crosshair import CrossHair
from random import randint, randrange
pygame.init()

def show_text(text, font, color, x,y):
    txt = font.render(text, True, color)
    txt_rect = txt.get_rect(topleft = (x,y))
    screen.blit(txt, txt_rect)
    
level = 1
enemies_alive = 0
level_difficulty = 0
target_difficulty = 400
last_enemy_spawn_time = pygame.time.get_ticks()
font28 = pygame.font.SysFont("arial", 28)


bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
castle = Castle(castle_img_100,castle_img_50,castle_img_25, SCREEN_WIDTH- 400, SCREEN_HEIGHT-500, 0.3)
crosshair = CrossHair()




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    if level_difficulty < target_difficulty:
        d_time = pygame.time.get_ticks() - last_enemy_spawn_time
        if  2000<d_time:
            enemy_index = randrange(len(enemy_types))
            sample_enemy = Enemy(enemy_health[enemy_index], enemy_animations[enemy_index], -100, SCREEN_HEIGHT - 250, 1)
            enemy_group.add(sample_enemy)
            last_enemy_spawn_time = pygame.time.get_ticks() 
            d_time = 0
            level_difficulty += enemy_health[enemy_index]
    
    else:
        enemies_alive = 0
        for enemy in enemy_group:
            if enemy.alive:
                enemies_alive += 1
        if enemies_alive == 0:
            level += 1
            target_difficulty *= 1.1
            level_difficulty = 0
            enemy_group.empty()
                       
        
        
    
    screen.blit(bg, (0,0)) 
    crosshair.draw(screen)
    show_text(f"score: {castle.score}", font28, (255,123,90), 10, 10) 
    castle.draw() 
    castle.shoot(bullet_group)   
    bullet_group.draw(screen)      
    bullet_group.update()
    enemy_group.draw(screen)      
    enemy_group.update(castle, bullet_group)
    pygame.display.update()
    clock.tick(FPS)