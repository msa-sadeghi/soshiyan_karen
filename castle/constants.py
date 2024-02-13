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