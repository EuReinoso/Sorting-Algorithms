import pygame, sys
from bar import Bar
from random import shuffle
from button import Button

pygame.init()

WINDOW_SIZE = (1024, 768)
#WINDOW_SIZE = (640, 480)

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

def draw_text(text, surface, size, color, pos):
    font = pygame.font.SysFont('calibri', size)
    text_render = font.render(text, 1, color)
    text_rect = text_render.get_rect()
    text_rect.center = pos
    surface.blit(text_render, text_rect)


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

def bar_swap(bar1, bar2):
    aux = bar1.value
    bar1.set_height(bar2.value)
    bar2.set_height(aux)

def buttons_sequence(quant, pos, size, space= 30, texts= []):
    buttons = []
    for i in range(quant):
        rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        button = Button(rect, text= texts[i])
        buttons.append(button)
        pos[0] += size[0] + space
    
    return buttons

def insert_sort(bar_list):
        for i in range(1, len(bar_list)):
            key = bar_list[i].value
            k = i - 1
            while k >= 0 and key < bar_list[k].value:
                value = bar_list[k].value
                bar_list[k + 1].set_height(value)
                k -= 1

                window_updates(bar_list)
                pygame.draw.rect(window, (0, 200, 0), bar_list[k+1]. rect)
                pygame.display.update()

            bar_list[k + 1].set_height(key)

def selection_sort(bar_list):
    for i in range(len(bar_list)):
        value_min = i

        for k in range(i + 1, len(bar_list)):
            if bar_list[k].value < bar_list[value_min].value:
                value_min = k

            window_updates(bar_list)
            pygame.draw.rect(window, (0, 200, 0), bar_list[value_min].rect)
            pygame.draw.rect(window, (200, 0, 0), bar_list[k].rect)
            pygame.draw.rect(window, (0, 0, 200), bar_list[i].rect)
            pygame.display.update()

        bar_swap(bar_list[i], bar_list[value_min])

def bubble_sort(bar_list):
    n = len(bar_list) - 1
    while n > 0:
        for i in range(n):
            if bar_list[i].value > bar_list[i + 1].value:
                bar_swap(bar_list[i], bar_list[i + 1])

                window_updates(bar_list)
                pygame.draw.rect(window, (0, 200, 0), bar_list[i].rect)
                pygame.draw.rect(window, (200, 0, 0), bar_list[i + 1].rect)
                pygame.display.update()
            
        n -= 1

def comb_sort(bar_list):
    gap = round(len(bar_list)// 1.3)
    i = 0
    while gap > 0 & i < len(bar_list) - 1:
        i = 0
        while i + gap < len(bar_list):
            if bar_list[i].value > bar_list[i + gap].value:
                bar_swap(bar_list[i], bar_list[i + gap])

            window_updates(bar_list)
            pygame.draw.rect(window, (200, 0, 0),  bar_list[i].rect)
            pygame.draw.rect(window, (200, 0, 0),  bar_list[i + gap].rect)
            pygame.display.update()

            i += 1
        gap = round(gap // 1.3)


def window_updates(bar_list):
    window.fill((0, 0, 0))
    draw_bars(bar_list)
    draw_background()

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    draw_text('Sorting...', window, round(WINDOW_SIZE[0] * WINDOW_SIZE[1] * 0.000075), (200, 200, 200), (window.get_rect().center[0], WINDOW_SIZE[1] * 0.9))
    
    pygame.time.Clock().tick(300)

def draw_background():
    pygame.draw.rect(window, (100, 100, 100), (0, WINDOW_SIZE[1] * 0.799, WINDOW_SIZE[0], WINDOW_SIZE[1] * 0.02))
    pygame.draw.rect(window, (50, 50, 200), (0, WINDOW_SIZE[1] * 0.81, WINDOW_SIZE[0], WINDOW_SIZE[1] - (WINDOW_SIZE[1] * 0.1)))


def main():

    fps = 60
    time = pygame.time.Clock()

    bar_quant = 90
    bar_width = WINDOW_SIZE[0]/bar_quant
    bar_list = bars_init(0, WINDOW_SIZE[1] * 0.8, bar_width, bar_quant)

    shuffle_button_rect = pygame.Rect(WINDOW_SIZE[0] * 0.75, WINDOW_SIZE[1] * 0.83, WINDOW_SIZE[0] * 0.2, WINDOW_SIZE[1] * 0.07)
    shuffle_button = Button(shuffle_button_rect, text= 'Shuffle')

    sort_button_rect = pygame.Rect(WINDOW_SIZE[0] * 0.75, WINDOW_SIZE[1] * 0.92, WINDOW_SIZE[0] * 0.2, WINDOW_SIZE[1] * 0.07)
    sort_button = Button(sort_button_rect, text= 'Sort')

    algorithms_buttons_pos = [WINDOW_SIZE[0] * 0.05, WINDOW_SIZE[1] * 0.83]
    algorithms_buttons_size = (WINDOW_SIZE[0] * 0.09, WINDOW_SIZE[1] * 0.07)
    algorithms_buttons = buttons_sequence(4, algorithms_buttons_pos, algorithms_buttons_size, texts= ['Insert', 'Selection', 'Bubble', 'Comb'], space= 20)
    algorithms_buttons[0].selected = True

    algorithm_name = 'Insert'
    loop = True
    while loop:

        window.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if shuffle_button.click(event, mx, my):
                bar_shuffle(bar_list)
            if sort_button.click(event, mx, my):
                if algorithm_name == 'Insert':
                    insert_sort(bar_list)
                if algorithm_name == 'Selection':
                    selection_sort(bar_list)
                if algorithm_name == 'Bubble':
                    bubble_sort(bar_list)
                if algorithm_name == 'Comb':
                    comb_sort(bar_list)
                
            for i in range(len(algorithms_buttons)):
                if algorithms_buttons[i].click(event, mx, my):
                    algorithm_name = algorithms_buttons[i].text
                    algorithms_buttons[i].selected = True

                    for b in range(len(algorithms_buttons)):
                        if algorithms_buttons[b] != algorithms_buttons[i]:
                            algorithms_buttons[b].selected = False

        draw_bars(bar_list)
        draw_background()

        for button in algorithms_buttons:
            button.draw(window)

        shuffle_button.draw(window)
        sort_button.draw(window)
        pygame.display.update()
        time.tick(fps)

main()
