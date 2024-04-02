import pygame
class CrossHair:
    def __init__(self):
        image = pygame.image.load("assets/crosshair.png")
        w = image.get_width()
        h = image.get_height()
        self.image = pygame.transform.scale(image, (w * 0.03, h * 0.03))
        self.rect = self.image.get_rect()
        pygame.mouse.set_visible(False)
        
    def draw(self, screen):
        self.rect.center = pygame.mouse.get_pos()
        screen.blit(self.image, self.rect)