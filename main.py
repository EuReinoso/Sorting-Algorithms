import pygame, sys

pygame.init()

WINDOW_SIZE = (640,480)

pygame.display.set_caption('Sorting Algorithms')
window = pygame.display.set_mode(WINDOW_SIZE)

def main():
    
    loop = True
    while loop:

        window.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

main()
