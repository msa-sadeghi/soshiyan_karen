from pygame.sprite import Sprite
import pygame
import os
class Soldier(Sprite):
    def __init__(self, char_type, x,y , scale, speed):
        super().__init__()
        self.char_type = char_type
        self.animation_list = []
        self.speed = speed
        self.image_number = 0
        self.action = 0
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
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
            
        
        
        
        