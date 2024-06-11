from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    def __init__(self, x,y, direction):
        super().__init__()
        self.speed = 3
        self.image = pygame.image.load("assets/images/icons/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction
    def update(self):
        self.rect.x += self.direction * self.speed
        if self.rect.right < 0 or self.rect.left > 800:
            self.kill()
            