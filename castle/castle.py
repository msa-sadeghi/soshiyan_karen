from constants import *
from bullet import Bullet
import math
class Castle:
    def __init__(self, image100, x,y, scale):
        self.health = 1000
        self.max_health = self.health
        
        self.image100 = pygame.transform.scale(image100, (image100.get_width() * scale, image100.get_height() * scale))
        self.rect = self.image100.get_rect(topleft= (x,y))
        self.fired = False
        
    def draw(self):
        self.image = self.image100
        screen.blit(self.image, self.rect)
        
    def shoot(self, bullet_group):
        pos = pygame.mouse.get_pos() # (100,100)
        x_dist = pos[0] - self.rect.midleft[0] # (23,345)
        y_dist = -(pos[1] - self.rect.midleft[1])
        self.angle = math.atan2(y_dist, x_dist)
        
        if pygame.mouse.get_pressed()[0] and not self.fired:
            bullet = Bullet(bullet_img, self.rect.midleft[0], self.rect.midleft[1], self.angle)
            bullet_group.add(bullet)
            self.fired = True
        if not pygame.mouse.get_pressed()[0]:
            self.fired = False
            
        