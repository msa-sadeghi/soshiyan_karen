from constants import *
from player import Player
from enemy import Enemy
from lava import Lava

class World:
    def __init__(self, data, player_group, enemy_group, lava_group):
        self.tile_map_list = []
        self.player_group = player_group
        self.enemy_group = enemy_group
        self.lava_group = lava_group
        bg_img = pygame.image.load("assets/background.png")
        self.image = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect(topleft=(0,0))

        for row in range(len(data)):
            for col in range(len(data[row])):
                if data[row][col] == 1:
                    img = DIRT_IMAGE
                    rect = img.get_rect(topleft=(col * TILE_SIZE, row * TILE_SIZE))
                    self.tile_map_list.append((img, rect))
                if data[row][col] == 2:
                    img = GRASS_IMAGE
                    rect = img.get_rect(topleft= (col * TILE_SIZE, row * TILE_SIZE))
                    self.tile_map_list.append((img, rect))
                if data[row][col] == 3:
                    img = WATER_IMAGE
                    rect = img.get_rect(topleft= (col * TILE_SIZE, row * TILE_SIZE))
                    self.tile_map_list.append((img, rect))
                
                if data[row][col] == 4:
                    player = Player(col * TILE_SIZE, row * TILE_SIZE)
                    self.player_group.add(player)
                
                if data[row][col] == 5:
                    enemy = Enemy(BLOB_IMAGE, col * TILE_SIZE, row * TILE_SIZE)
                    self.enemy_group.add(enemy)
                if data[row][col] == 6:
                    lava = Lava(LAVA_IMAGE, col * TILE_SIZE, row * TILE_SIZE + 8)
                    self.lava_group.add(lava)



                # TODO   اضافه کردن تصویر آب به زمین بازی
                # اضافه کردن سکوهای مختلف به زمین بازی

    def draw(self):
        SCREEN.blit(self.image, self.rect)
        for tile in self.tile_map_list:
            SCREEN.blit(tile[0], tile[1])