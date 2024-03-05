import pygame

screen = pygame.display.set_mode()
SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()
FPS = 60
clock = pygame.time.Clock()
bg = pygame.image.load("assets/bg.png")
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
castle_img_100 = pygame.image.load("assets/castle/castle_100.png")
bullet_img = pygame.image.load("assets/bullet.png")


enemy_animations = []
enemy_types = ("knight", "goblin", "purple_goblin", "red_goblin")
enemy_health = (75, 100, 125, 150)
animation_types = ("walk", "attack", "death")

for enemy in enemy_types:
    for_any_enemy = []
    for animation in animation_types:
        for_any_animation_type = []
        for i in range(20):
            img = pygame.image.load(f"assets/enemies/{enemy}/{animation}/{i}.png")
            w = img.get_width()
            h = img.get_height()
            img = pygame.transform.scale(img, (w * 0.3, h * 0.3))
            for_any_animation_type.append(img)
        for_any_enemy.append(for_any_animation_type)
    enemy_animations.append(for_any_enemy)
        
            
        