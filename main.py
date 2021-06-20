import pygame, sys
from bar import Bar
from random import shuffle
from button import Button

pygame.init()

WINDOW_SIZE = (960, 720)
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

def draw_bars():
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

def buttons_sequence(quant, pos, size, space_x= 30,space_y= 10, texts= [], break_point= None):
    buttons = []
    pos_x_init = pos[0]
    count = 0
    for i in range(quant):
        rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        button = Button(rect, text= texts[i])
        buttons.append(button)
        pos[0] = pos[0] + size[0] + space_x

        if break_point != None:
            count += 1
            if count > break_point:
                pos[0] = pos_x_init
                pos[1] = pos[1] + size[1] + space_y
                count = 0
        
    return buttons

def insert_sort(values):
        for i in range(1, len(values)):
            key = values[i]
            k = i - 1
            while k >= 0 and values[k] > key:
                values[k + 1] = values[k]
                bar_list[k + 1].set_height(values[k])
                k -= 1

                window_updates()
                pygame.draw.rect(window, (0, 200, 0), bar_list[k+1]. rect)
                pygame.display.update()

            values[k + 1] = key
            bar_list[k + 1].set_height(values[k + 1])
        
        return values


def selection_sort():
    for i in range(len(bar_list)):
        value_min = i

        for k in range(i + 1, len(bar_list)):
            if bar_list[k].value < bar_list[value_min].value:
                value_min = k

            window_updates()
            pygame.draw.rect(window, (0, 200, 0), bar_list[value_min].rect)
            pygame.draw.rect(window, (200, 0, 0), bar_list[k].rect)
            pygame.draw.rect(window, (0, 0, 200), bar_list[i].rect)
            pygame.display.update()

        bar_swap(bar_list[i], bar_list[value_min])

def bubble_sort():
    n = len(bar_list) - 1
    while n > 0:
        for i in range(n):
            if bar_list[i].value > bar_list[i + 1].value:
                bar_swap(bar_list[i], bar_list[i + 1])

                window_updates()
                pygame.draw.rect(window, (0, 200, 0), bar_list[i].rect)
                pygame.draw.rect(window, (200, 0, 0), bar_list[i + 1].rect)
                pygame.display.update()
            
        n -= 1

def comb_sort():
    gap = len(bar_list)
    while gap > 1:
        gap = max(1, int(gap/ 1.25))
        for i in range(len(bar_list) - gap):
            if bar_list[i].value > bar_list[i + gap].value:
                bar_swap(bar_list[i], bar_list[i + gap])

            window_updates()
            pygame.draw.rect(window, (200, 0, 0),  bar_list[i].rect)
            pygame.draw.rect(window, (200, 0, 0),  bar_list[i + gap].rect)
            pygame.display.update()

def merge_sort(start, values):
    if len(values) > 1:

        cut = len(values)//2

        left = values[:cut]
        right = values[cut:]

        merge_sort(start, left)
        merge_sort(start + cut, right)


        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                values[k] = left[i]
                bar_list[k + start].set_height(values[k])
                i += 1
            else:
                values[k] = right[j]
                bar_list[k + start].set_height(values[k])
                j += 1
            k += 1

            window_updates()
            pygame.draw.rect(window, (200, 0, 0), bar_list[k + start])
            pygame.display.update()

        while i < len(left):
            values[k] = left[i]
            bar_list[k + start].set_height(values[k])
            i += 1
            k += 1

            window_updates()
            pygame.display.update()

        while j < len(right):
            values[k] = right[j]
            bar_list[k + start].set_height(values[k])
            j += 1
            k += 1

            window_updates()
            pygame.display.update()

def  heapify(values, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and values[largest] < values[l]:
        largest = l
    
    if r < n and values[largest] < values[r]:
        largest = r
    
    if largest != i:
        values[i], values[largest] = values[largest], values[i]
        bar_list[i].set_height(values[i])
        bar_list[largest].set_height(values[largest])

        window_updates()
        pygame.draw.rect(window, (200, 0, 0), bar_list[i].rect)
        pygame.draw.rect(window, (200, 0, 0), bar_list[largest].rect)
        pygame.display.update()

        heapify(values, n, largest)

def heap_sort(values):
    n = len(values)

    for i in range(n//2 - 1, -1, -1):
        heapify(values, n, i)
    
    for i in range(n - 1, 0, -1):
        values[i], values[0] = values[0], values[i]
        bar_list[i].set_height(values[i])
        bar_list[0].set_height(values[0])

        window_updates()
        pygame.display.update()

        heapify(values, i, 0)

def shell_sort(values):
    n = len(values)
    gap = n//2

    while gap > 0:
        for i in range(gap, n):
            temp = values[i]
            j = i
            while j >= gap and values[j - gap] > temp:
                values[j] = values[j - gap]
                bar_list[j].set_height(values[j])

                window_updates()
                pygame.draw.rect(window, (200, 0, 0), bar_list[j].rect)
                pygame.draw.rect(window, (0, 200, 0), bar_list[i].rect)
                pygame.display.update()

                j -= gap
            values[j] = temp
            bar_list[j].set_height(values[j])

        gap = gap//2

def counting_sort(values, exp1):
    n = len(values)

    output = [0] * n
    count = [0] * (10)

    for i in range(0, n):
        index = (values[i] / exp1)
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (values[i] / exp1)
        output[count[int(index % 10)] - 1] = values[i]
        count[int(index % 10)] -= 1
        i -= 1
       
    for i in range(0, len(values)):
        values[i] = output[i]
        bar_list[i].set_height(values[i])

        window_updates()
        pygame.draw.rect(window, (200, 0, 0), bar_list[i].rect)
        pygame.display.update()

def radix_sort(values):
    max1 = max(values)
    exp = 1

    while max1 / exp > 1:
        counting_sort(values, exp)
        exp *= 10

def gnome_sort(values, n):
    index = 0
    while index < n:
        if index == 0:
            index += 1
        if values[index] >= values[index- 1]:
            index += 1
        else:
            values[index], values[index - 1] = values[index - 1], values[index]
            bar_list[index].set_height(values[index])
            bar_list[index - 1].set_height(values[index - 1])
            
            window_updates()
            pygame.draw.rect(window, (200, 0, 0), bar_list[index].rect)
            pygame.display.update()
            
            index -= 1

def count_sort(values, vmax):
    m = vmax + 1
    count = [0] * m                
    
    for a in values:
        count[a] += 1      

    i = 0
    for a in range(m):            
        for _ in range(count[a]):  
            values[i] = a
            bar_list[i].set_height(values[i])

            window_updates()
            pygame.draw.rect(window, (200, 0, 0), bar_list[i].rect)
            pygame.display.update()
            
            i += 1

def bucket_sort(values):
    max_value = max(values)
    size = max_value/len(values)

    buckets_list= []
    for x in range(len(values)):
        buckets_list.append([]) 

    for i in range(len(values)):
        j = int (values[i] / size)
        if j != len (values):
            buckets_list[j].append(values[i])
        else:
            buckets_list[len(values) - 1].append(values[i])

    k = 0
    for i in range(len(values)):
        for j in range(len(buckets_list[i])):
            values[k] = buckets_list[i][j]
            bar_list[k].set_height(values[k])

            window_updates()
            pygame.draw.rect(window, (200, 0, 0), bar_list[k].rect)
            pygame.display.update()

            k += 1

def cocktail_sort(values):
    n = len(values)
    swapped = True
    start = 0
    end = n-1
    while (swapped==True):
  
        swapped = False
  
        for i in range (start, end):
            if (values[i] > values[i+1]) :
                values[i], values[i+1]= values[i+1], values[i]
                
                bar_list[i].set_height(values[i])
                bar_list[i + 1].set_height(values[i + 1])

                window_updates()
                pygame.draw.rect(window, (200, 0, 0), bar_list[i].rect)
                pygame.draw.rect(window, (200, 0, 0), bar_list[i + 1].rect)
                pygame.display.update()

                swapped=True
  
        if (swapped==False):
            break
  
        swapped = False
  
        end = end-1
  
        for i in range(end-1, start-1,-1):
            if (values[i] > values[i+1]):
                values[i], values[i+1] = values[i+1], values[i]

                bar_list[i].set_height(values[i])
                bar_list[i + 1].set_height(values[i + 1])

                window_updates()
                pygame.draw.rect(window, (200, 0, 0), bar_list[i].rect)
                pygame.draw.rect(window, (200, 0, 0), bar_list[i + 1].rect)
                pygame.display.update()


                swapped = True
  
        start = start+1

MIN_MERGE = 32
def calc_min_run(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

def insert_sort2(values, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and values[j] < values[j - 1]:
            values[j], values[j - 1] = values[j - 1], values[j]
            bar_list[j].set_height(values[j])
            bar_list[j - 1].set_height(values[j - 1])

            window_updates()
            pygame.draw.rect(window, (200, 0, 0), bar_list[j].rect)
            pygame.display.update()

            j -= 1

def merge(values, l, m, r):
     
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(values[l + i])
    for i in range(0, len2):
        right.append(values[m + 1 + i])
 
    i, j, k = 0, 0, l
     
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            values[k] = left[i]
            bar_list[k].set_height(values[k])

            window_updates()
            pygame.draw.rect(window, (200, 0, 0), bar_list[k].rect)
            pygame.display.update()


            i += 1
 
        else:
            values[k] = right[j]
            bar_list[k].set_height(values[k])

            window_updates()
            pygame.draw.rect(window, (200, 0, 0), bar_list[k].rect)
            pygame.display.update()

            j += 1
 
        k += 1
 
    while i < len1:
        values[k] = left[i]
        bar_list[k].set_height(values[k])

        window_updates()
        pygame.draw.rect(window, (200, 0, 0), bar_list[k].rect)
        pygame.display.update()

        k += 1
        i += 1
 
    while j < len2:
        values[k] = right[j]
        bar_list[k].set_height(values[k])

        window_updates()
        pygame.draw.rect(window, (200, 0, 0), bar_list[k].rect)
        pygame.display.update()

        k += 1
        j += 1

def tim_sort(values):
    n = len(values)
    minRun = calc_min_run(n)
     
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insert_sort2(values, start, end)
 
    size = minRun
    while size < n:
         
        for left in range(0, n, 2 * size):
 
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            if mid < right:
                merge(values, left, mid, right)
 
        size = 2 * size

def window_updates():
    window.fill((0, 0, 0))
    draw_bars()
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


bar_quant = int(WINDOW_SIZE[0] * 0.2)
bar_width = WINDOW_SIZE[0]/bar_quant
bar_list = bars_init(0, WINDOW_SIZE[1] * 0.8, bar_width, bar_quant)


def main():
    global bar_list, bar_width, bar_quant

    fps = 60
    time = pygame.time.Clock()

    shuffle_button_rect = pygame.Rect(WINDOW_SIZE[0] * 0.75, WINDOW_SIZE[1] * 0.82, WINDOW_SIZE[0] * 0.2, WINDOW_SIZE[1] * 0.07)
    shuffle_button = Button(shuffle_button_rect, text= 'Shuffle')

    sort_button_rect = pygame.Rect(WINDOW_SIZE[0] * 0.75, WINDOW_SIZE[1] * 0.92, WINDOW_SIZE[0] * 0.2, WINDOW_SIZE[1] * 0.07)
    sort_button = Button(sort_button_rect, text= 'Sort')

    algorithms_buttons_pos = [WINDOW_SIZE[0] * 0.05, WINDOW_SIZE[1] * 0.82]
    algorithms_buttons_size = (WINDOW_SIZE[0] * 0.1, WINDOW_SIZE[1] * 0.05)
    algorithms_buttons = buttons_sequence(12, algorithms_buttons_pos, algorithms_buttons_size, 
                                        texts= ['Insert', 'Selection', 'Bubble', 'Comb', 'Merge', 'Heap', 'Shell', 'Radix', 'Gnome', 'Counting','Cocktail','Tim'],
                                        space_x= WINDOW_SIZE[0] * 0.003, space_y= WINDOW_SIZE[1] * 0.003, break_point= 4)
    algorithms_buttons[0].selected = True

    bar_buttons_pos = [WINDOW_SIZE[0] * 0.61, WINDOW_SIZE[1] * 0.82]
    bar_buttons_size = (WINDOW_SIZE[0] * 0.1, WINDOW_SIZE[1] * 0.04)
    bar_buttons = buttons_sequence(4, bar_buttons_pos, bar_buttons_size,
                                texts= ['Small', 'Medium', 'Large', 'Very Large'],
                                space_x= WINDOW_SIZE[0] * 0.003, space_y= WINDOW_SIZE[1] * 0.003, break_point= 0)
    bar_buttons[1].selected = True

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
                    values = get_values(bar_list)
                    insert_sort(values)
                if algorithm_name == 'Selection':
                    selection_sort()
                if algorithm_name == 'Bubble':
                    bubble_sort()
                if algorithm_name == 'Comb':
                    comb_sort()
                if algorithm_name == 'Merge':
                    values = get_values(bar_list)
                    merge_sort(0, values)
                if algorithm_name == 'Heap':
                    values = get_values(bar_list)
                    heap_sort(values)
                if algorithm_name == 'Shell':
                    values = get_values(bar_list)
                    shell_sort(values)
                if algorithm_name == 'Radix':
                    values = get_values(bar_list)
                    radix_sort(values)
                if algorithm_name == 'Gnome':
                    values = get_values(bar_list)
                    gnome_sort(values, len(values))
                if algorithm_name == 'Counting':
                    values = get_values(bar_list)
                    count_sort(values, max(values))
                if algorithm_name == 'Cocktail':
                    values = get_values(bar_list)
                    cocktail_sort(values)
                if algorithm_name == 'Tim':
                    values = get_values(bar_list)
                    tim_sort(values)
                
            for i in range(len(algorithms_buttons)):
                if algorithms_buttons[i].click(event, mx, my):
                    algorithm_name = algorithms_buttons[i].text
                    algorithms_buttons[i].selected = True

                    for b in range(len(algorithms_buttons)):
                        if algorithms_buttons[b] != algorithms_buttons[i]:
                            algorithms_buttons[b].selected = False
            
            for i in range(len(bar_buttons)):
                if bar_buttons[i].click(event, mx, my):
                    bar_buttons[i].selected = True

                    for b in range(len(bar_buttons)):
                        if bar_buttons[b] != bar_buttons[i]:
                            bar_buttons[b].selected = False
                    
                    if bar_buttons[i].text == 'Small':
                        bar_quant = int(WINDOW_SIZE[0] * 0.05)
                        bar_width = WINDOW_SIZE[0]/bar_quant
                        bar_list = bars_init(0, WINDOW_SIZE[1] * 0.8, bar_width, bar_quant)
                    if bar_buttons[i].text == 'Medium':
                        bar_quant = int(WINDOW_SIZE[0] * 0.2)
                        bar_width = WINDOW_SIZE[0]/bar_quant
                        bar_list = bars_init(0, WINDOW_SIZE[1] * 0.8, bar_width, bar_quant)
                    if bar_buttons[i].text == 'Large':
                        bar_quant = int(WINDOW_SIZE[0] * 0.5)
                        bar_width = WINDOW_SIZE[0]/bar_quant
                        bar_list = bars_init(0, WINDOW_SIZE[1] * 0.8, bar_width, bar_quant)
                    if bar_buttons[i].text == 'Very Large':
                        bar_quant = int(WINDOW_SIZE[0] * 0.8)
                        bar_width = WINDOW_SIZE[0]/bar_quant
                        bar_list = bars_init(0, WINDOW_SIZE[1] * 0.8, bar_width, bar_quant)


        draw_bars()
        draw_background()

        for button in algorithms_buttons:
            button.draw(window)
        
        for button in bar_buttons:
            button.draw(window)

        shuffle_button.draw(window)
        sort_button.draw(window)
        pygame.display.update()
        time.tick(fps)

main()
