from pygame.sprite import Sprite
import pygame
class Enemy(Sprite):
    def __init__(self, health, animation_list, x,y,speed):
        super().__init__()
        self.alive = True
        self.speed = speed
        self.health = health
        self.animation_list = animation_list
        self.action = 0
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect(center = (x,y))
        self.last_update_time = pygame.time.get_ticks()
        
    def update(self)    :
        self.rect.x += self.speed
        self.update_animation()
        
    def update_animation(self):
        self.image = self.animation_list[self.action][self.frame_index]
        
        if pygame.time.get_ticks() - self.last_update_time > 50:
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
        
        