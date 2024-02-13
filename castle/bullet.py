from pygame.sprite import Sprite
import math
from constants import *
class Bullet(Sprite):
    def __init__(self, image, x,y, angle):
        super().__init__()
        self.image = pygame.transform.scale(image, (28,28))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.angle = angle
        self.speed = 10
        self.dx = math.cos(self.angle) * self.speed
        self.dy = -math.sin(self.angle) * self.speed
        
        
    def update(self):
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()
        self.rect.x += self.dx
        self.rect.y += self.dy