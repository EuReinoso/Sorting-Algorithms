import pygame

pygame.init()

class Button:
    def __init__(self, rect, color= (100, 100, 100), selected_color= (0, 100, 0), text= '', text_color= (200, 200, 200), text_size= None):
        self.rect = rect
        self.color = color
        self.selected_color = selected_color
        self.text = text

        if text_size == None:
            self.text_size = round(rect.height * rect.width * 0.005)
        else:
            self.text_size = text_size

        self.text_color = text_color
        self.on_down = False
        self.on_up = False
        self.selected = False

    def draw(self, window):
        if not self.selected:
            pygame.draw.rect(window, self.color, self.rect)
        else:
            pygame.draw.rect(window, self.selected_color, self.rect)
        if self.text != '':
            self.draw_text(window)

    def draw_text(self, surface):
        font = pygame.font.SysFont('calibri', self.text_size)
        text_render = font.render(self.text, 1, self.text_color)
        text_rect = text_render.get_rect()
        text_rect.center = self.rect.center
        surface.blit(text_render, text_rect)
    
    def turn_select(self):
        if self.selected:
            self.selected = False
        else:
            self.selected = True

    def click(self, event, mx, my, color_change = True, color_down = (100, 100, 200), color_up= (100, 100, 100)):
        if self.rect.collidepoint((mx, my)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if color_change:
                        self.color = color_down
                    
                    self.on_down = True
                    self.on_up = False
                    return False

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if color_change:
                        self.color = color_up
                    
                    self.on_down = False
                    self.on_up = True

                    return True