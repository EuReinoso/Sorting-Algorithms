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

def get_values(bar_list):
    values = []
    for i in range(len(bar_list)):
        values.append(bar_list[i].value)
    return values

def bar_shuffle(bar_list):
    values = get_values(bar_list)

    shuffle(values)

    for i in range(len(values)):
        bar_list[i].set_height(values[i])

def insert(bar_list):
        for i in range(1, len(bar_list)):
            key = bar_list[i].value
            k = i - 1
            while k >= 0 and key < bar_list[k].value:
                value = bar_list[k].value
                bar_list[k + 1].set_height(value)
                k -= 1

                window_updates(bar_list)

            bar_list[k + 1].set_height(key)

def window_updates(bar_list):
    window.fill((0, 0, 0))
    draw_bars(bar_list)
    pygame.display.update()

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def main():

    fps = 60
    time = pygame.time.Clock()

    bar_quant = 100
    bar_width = WINDOW_SIZE[0]/bar_quant
    bar_list = bars_init(0, WINDOW_SIZE[1], bar_width, bar_quant)

    bar_shuffle(bar_list)

    insert(bar_list)

    loop = True
    while loop:

        window.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        draw_bars(bar_list)
        pygame.display.update()
        time.tick(fps)

main()
