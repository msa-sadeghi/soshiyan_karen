import pygame
from pygame.sprite import Sprite
from constants import *
class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.right_images = []
        self.left_images = []

        self.idle_right_images = []
        self.idle_left_images = []

        for i in range(1,9):
            img = pygame.image.load(f"assets/boy/Run ({i}).png")
            img = pygame.transform.scale(img, (img.get_width() * 0.2, img.get_height() * 0.2))
            self.right_images.append(img)
            img = pygame.transform.flip(img, True, False)
            self.left_images.append(img)
        for i in range(1,10):
            img = pygame.image.load(f"assets/boy/Idle ({i}).png")
            img = pygame.transform.scale(img, (img.get_width() * 0.2, img.get_height() * 0.2))
            self.idle_right_images.append(img)
            img = pygame.transform.flip(img, True, False)
            self.idle_left_images.append(img)


        self.ghost_image = pygame.image.load("assets/img/ghost.png")
        self.reset(x,y)
        
    def reset(self, x,y):
        self.image = self.idle_right_images[0]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.vel_y = 0
        self.speed = 5
        self.jumped = False
        self.frame_index = 0
        self.direction = 1
        self.counter = 0
        self.idle = True
        self.alive = True
        self.next_level = False
        

    def update(self, tile_map_list, enemy_group,door_group):
        if pygame.sprite.spritecollideany(self, enemy_group) and self.alive:

            self.image = self.ghost_image
            self.alive = False
        if self.alive:
            self.move(tile_map_list)
            self.animation()
        if not self.alive and self.rect.y >= 200:

                self.rect.y -= 5
                
        if pygame.sprite.spritecollide(self, door_group, False):
            self.next_level = True
            

   
    def move(self, tile_map_list):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.idle = False
            self.direction = -1
            dx -= self.speed
        if keys[pygame.K_RIGHT]:
            self.idle = False
            self.direction = 1
            dx += self.speed

        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.idle = True


        if keys[pygame.K_SPACE] and not self.jumped:
            self.vel_y = -10
            self.jumped = True

        if not keys[pygame.K_SPACE]:
            self.jumped = False

        self.vel_y += 1
        dy += self.vel_y
        if self.direction == 1:
            rect = pygame.Rect(self.rect.x + 50 ,self.rect.y + 10, self.image.get_width()-80, self.image.get_height()-23)
        elif self.direction == -1:
            rect = pygame.Rect(self.rect.x + 30 ,self.rect.y + 10, self.image.get_width()-80, self.image.get_height()-23)

       
        for tile in tile_map_list:
            if tile[1].colliderect(rect.x ,rect.y + dy, self.image.get_width()-80, self.image.get_height()-23):
                if self.vel_y > 0:
                    self.vel_y = 0
                    dy = tile[1].top - rect.bottom
                else:
                    self.vel_y = 0
                    dy = tile[1].bottom - rect.top
            if tile[1].colliderect(rect.x + dx, rect.y, self.image.get_width()-80, self.image.get_height()-23):
                if self.direction == 1 :
                    dx = tile[1].left - rect.right
                elif self.direction == -1:
                    dx = tile[1].right - rect.left
        
        self.rect.x += dx
        self.rect.y += dy

        # if self.rect.bottom > SCREEN_HEIGHT:
        #     self.rect.bottom = SCREEN_HEIGHT

    def animation(self):
        self.counter += 1
        if self.counter >= 2:
            self.frame_index += 1
            self.counter = 0

        if self.frame_index >= len(self.right_images) - 1:
            self.frame_index = 0
        if self.direction == 1:
            if self.idle:

                self.image = self.idle_right_images[self.frame_index]
            else:
                self.image = self.right_images[self.frame_index]

        if self.direction == -1:
            if self.idle:

                self.image = self.idle_left_images[self.frame_index]
            else:
                self.image = self.left_images[self.frame_index]
