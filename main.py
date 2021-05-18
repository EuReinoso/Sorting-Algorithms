import pygame, sys
from bar import Bar
from random import shuffle

pygame.init()

WINDOW_SIZE = (640, 480)

pygame.display.set_caption('Sorting Algorithms')
window = pygame.display.set_mode(WINDOW_SIZE)

def bars_init(x, y, width, size):
    bar_list = []
    height = 1
    height_increment = y/size
    for i in range(size):
        rect = pygame.Rect(x, y - height, width, height)
        bar_list.append(Bar(rect))
        x += width
        height += height_increment
    return bar_list

def draw_bars(bar_list):
    for i in range(len(bar_list)):
        bar_list[i].draw(window)

def bar_shuffle(bar_list):
    pos_list = []
    for i in range(len(bar_list)):
        pos = bar_list[i].rect.x
        pos_list.append(pos)

    shuffle(pos_list)

    for i in range(len(pos_list)):
        bar_list[i].rect.x = pos_list[i]

def main():

    bar_quant = 100
    bar_width = WINDOW_SIZE[0]/bar_quant
    bar_list = bars_init(0, WINDOW_SIZE[1], bar_width, bar_quant)

    bar_shuffle(bar_list)

    loop = True
    while loop:

        window.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        draw_bars(bar_list)
        pygame.display.update()

main()
