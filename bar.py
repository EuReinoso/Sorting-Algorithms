import pygame

pygame.init()

class Bar:
    def __init__ (self, rect):
        self.rect = rect
        self.value = self.rect.height
    
    def draw(self, window):
        pygame.draw.rect(window, (200, 200, 200), self.rect)

    def set_height(self, value):
        window_size_y = self.rect.y + self.rect.height
        self.rect.height = value
        self.rect.y =  window_size_y - self.rect.height 
        self.value = value
        