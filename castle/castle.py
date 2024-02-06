from constants import *
class Castle:
    def __init__(self, image100, x,y, scale):
        self.health = 1000
        self.max_health = self.health
        
        self.image100 = pygame.transform.scale(image100, (image100.get_width() * scale, image100.get_height() * scale))
        self.rect = self.image100.get_rect(topleft= (x,y))
        
    def draw(self):
        self.image = self.image100
        screen.blit(self.image, self.rect)