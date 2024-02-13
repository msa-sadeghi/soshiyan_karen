from constants import *
from castle import Castle
pygame.init()

bullet_group = pygame.sprite.Group()
castle = Castle(castle_img_100, SCREEN_WIDTH- 400, SCREEN_HEIGHT-500, 0.3)

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
    pygame.display.update()
    clock.tick(FPS)