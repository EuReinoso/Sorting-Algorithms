import pygame

pygame.init()

class Bar:
    def __init__ (self, rect):
        self.rect = rect
        self.value = self.rect.height
    
    def draw(self, window):
        pygame.draw.rect(window, (200, 200, 200), self.rect)