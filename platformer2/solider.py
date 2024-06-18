from pygame.sprite import Sprite
import pygame
import os
from bullet import Bullet
class Soldier(Sprite):
    def __init__(self, char_type, x,y , scale, speed):
        super().__init__()
        self.char_type = char_type
        self.animation_list = []
        self.speed = speed
        self.image_number = 0
        self.action = 0
        self.flip = False
        self.animation_types = ("Idle", "Run", "Jump", "Death")
        for animation in self.animation_types:
            list1 = []
            n = len(os.listdir(f"assets/images/{self.char_type}/{animation}"))
            for i in range(n):
                img = pygame.image.load(f"assets/images/{self.char_type}/{animation}/{i}.png")
                w = img.get_width()
                h = img.get_height()
                img = pygame.transform.scale(img, (w * scale, h * scale))
                list1.append(img)
            self.animation_list.append(list1)
        self.image = self.animation_list[self.action][self.image_number]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.last_update_time = pygame.time.get_ticks()
        self.direction = 1
        self.shoot_cooldown = 20
        self.jump = False
        self.vel_y = 0
        self.in_air = False
        
    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
    def update(self)    :
        self.shoot_cooldown -= 1
        if self.shoot_cooldown <= 0:
            self.shoot_cooldown = 0
        self.animation()
    def animation(self):
        self.image = self.animation_list[self.action][self.image_number]
        if pygame.time.get_ticks() - self.last_update_time > 100:
            self.last_update_time = pygame.time.get_ticks()
            self.image_number += 1
            if self.image_number >= len(self.animation_list[self.action]):
                self.image_number = 0
            
    def move(self, moving_left, moving_right)    :
        dx = 0
        dy = 0
        if moving_left:
            self.flip = True
            dx -= self.speed
            self.direction = -1
        if moving_right:
            self.flip = False
            dx += self.speed
            self.direction = 1
        if self.jump and not self.in_air:
            self.vel_y = -12
            self.jump = False
            self.in_air = True
            
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.in_air = False
                   
        self.rect.x += dx
        self.rect.y += dy
        
    def update_action(self, action)   :
        if action != self.action:
            self.action = action
            self.image_number = 0
        
    def shoot(self, bullet_group):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 20
            bullet = Bullet(self.rect.centerx + (0.6 * self.rect.size[0]*self.direction),\
                self.rect.centery, self.direction)
            bullet_group.add(bullet)
      