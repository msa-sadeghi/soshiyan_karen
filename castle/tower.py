from constants import *
from bullet import Bullet
import math
from pygame.sprite import Sprite
class Tower(Sprite):
    def __init__(self, image100,image50, image25, x,y, scale):
        
        super().__init__()
        self.image100 = pygame.transform.scale(image100, (image100.get_width() * scale, image100.get_height() * scale))
        self.image50 = pygame.transform.scale(image50, (image50.get_width() * scale, image50.get_height() * scale))
        self.image25 = pygame.transform.scale(image25, (image25.get_width() * scale, image25.get_height() * scale))
        self.image = self.image100
        self.rect = self.image100.get_rect(topleft= (x,y))
        self.last_shot = pygame.time.get_ticks()
        
        
    def draw(self):
        if self.health <= 250:
            self.image = self.image25
        elif self.health <= 500:
            self.image = self.image50
        else:
            self.image = self.image100
        screen.blit(self.image, self.rect)
        
    def update(self, enemy_group, bullet_group):
        got_target = False
        for e in enemy_group:
            if e.alive:
                target_x, target_y = e.rect.midbottom
                got_target = True
                break
        if got_target:
            x_dist = target_x - self.rect.midleft[0] # (23,345)
            y_dist = -(target_y - self.rect.midleft[1])
            self.angle = math.atan2(y_dist, x_dist)
        
        if pygame.time.get_ticks() - self.last_shot > 1000:
            self.last_shot = pygame.time.get_ticks()
            bullet = Bullet(bullet_img, self.rect.midleft[0], self.rect.midleft[1], self.angle)
            bullet_group.add(bullet)
            
       
            
    
        