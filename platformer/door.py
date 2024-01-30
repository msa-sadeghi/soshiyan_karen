from constants import *
from pygame.sprite import Sprite

class Door(Sprite):
    def __init__(self, image, x,y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        