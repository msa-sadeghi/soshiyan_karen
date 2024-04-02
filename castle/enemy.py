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
        self.last_attack_time = pygame.time.get_ticks()
        
    def update(self, target, bullet_group)    :
        if self.action == 0:
            self.rect.x += self.speed
        if self.rect.right > target.rect.left:
            self.update_action(1)
        if self.action == 1 and pygame.time.get_ticks() - self.last_attack_time > 3000:
            target.health -= 25
            if target.health < 0:
                target.health = 0
            self.last_attack_time = pygame.time.get_ticks()
                
        
        if pygame.sprite.spritecollide(self, bullet_group, True):
            self.health -= 25
            
        if self.health <= 0:
            
            self.alive = False
            target.money += 200
            target.score += 100
            self.update_action(2)
                
        self.update_animation()
        
    def update_animation(self):
        self.image = self.animation_list[self.action][self.frame_index]
        
        if pygame.time.get_ticks() - self.last_update_time > 50:
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 2:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
    def update_action(self, action):
        if self.action != action:
            self.action = action
            self.frame_index = 0
            self.last_update_time = pygame.time.get_ticks()
        
        
        