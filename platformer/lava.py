from constants import *
from pygame.sprite import Sprite

class Lava(Sprite):
    def __init__(self, image, x,y):
        super().__init__()
        image = pygame.transform.scale(image, (image.get_width() * 2, image.get_height()* 2))
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))