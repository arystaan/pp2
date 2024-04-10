import pygame
from pygame.locals import *
pygame.init()

#Создание окна
screen = pygame.display.set_mode((1080, 800))
clock = pygame.time.Clock()

#Создание переменных
radius = 10
x = 0
y = 0
done = False
radius_for_eraser = 0

#Создание цветов заранее для удобства
RED = (230, 0, 0)
GREEN = (0, 230, 0)
BLUE = (0, 0, 230)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colors = [RED, GREEN, BLUE]
color = WHITE
rect = [(120, 0, 40, 60), (200, 0, 40, 40)]
polygon = [((250, 0), (250 + 40, 0), (250, 0 + 60)), ((300+23, 0), (300, 0+40), (300 + 46, 0 + 40)), 
           ((350, 0 + 30), (350 + 20, 0), (350 + 40, 0 + 30), (350 + 20, 0 + 60))]

#Загрука ластика
eraser = pygame.image.load("eraser.png")
eraser = pygame.transform.scale(eraser, (70,70))

#Создание квадратов
def draw_rect(index):
    pygame.draw.rect(screen, colors[index], (index*40, 0, 40, 40))

def draw_rect45(index):
    pygame.draw.rect(screen, WHITE, index, 4)
    
def draw_polygon(index):
    pygame.draw.polygon(screen, WHITE, index, 4)

#Выбор цвета и раположение их на окне
def color_pick():
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if 0<x<40 and 0<y<40:
            return RED
        elif 40<x<80 and 0<y<40:
            return GREEN
        elif 80<x<120 and 0<y<40:
            return BLUE
        elif 120<x<160 and 0<y<60:
            return "rect"
        elif 160<x<200 and 0<y<40:
            return "circle"
        elif 1010<=x<=1080 and 0<=y<=40:
            return BLACK 
        elif 200<x<240 and 0<y<40:
            return "square"
        elif 250<x<290 and 0<y<40:
            return "right triangle"
        elif 300<x<340 and 0<y<40:
            return "equilateral triangle"
        elif 350<x<390 and 0<y<40:
            return "rhombus"
    return color 

#Сам процесс рисования
def painting(color):
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if color not in ["circle", "square", "rect", BLACK, 
                        "right triangle", "equilateral triangle", "rhombus"]:
            pygame.draw.circle(screen, color, (x,y), radius)
        elif color == "rect":
            pygame.draw.rect(screen, WHITE, (x,y, 40, 60), 4) 
        elif color == "circle":
            pygame.draw.circle(screen, WHITE, (x,y), 20, 4)
        elif color == "square":
            pygame.draw.rect(screen, WHITE, (x,y, 40,40), 4)
        elif color == BLACK:
            pygame.draw.circle(screen ,color, (x,y), 20, 27)
        elif color == "right triangle":
            pygame.draw.polygon(screen, WHITE, [(x, y), (x + 40, y), (x, y + 60)], 4)
        elif color == "equilateral triangle":
            pygame.draw.polygon(screen, WHITE, [(x+23, y), (x, y+40), (x + 46, y + 40)], 4)
        elif color == "rhombus":
            pygame.draw.polygon(screen, WHITE, [(x, y + 30), (x + 20, y), (x + 40, y + 30), 
                                                (x + 20, y + 60)], 4)
while not done:
    for event in pygame.event.get():
        
        #Условия выхода
        if event.type == QUIT:
            done = True
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        
        #Отрисковка квадратов на экране
        for i in range(len(colors)):
            draw_rect(i)
        pygame.draw.circle(screen, WHITE, (180,20), 20, 4)
        screen.blit(eraser, (1010, 0))
        for i  in rect:
            draw_rect45(i)
        for i in polygon:
            draw_polygon(i)
            
        #выбор цвета рисование
        color = color_pick()
        painting(color)
        
        clock.tick(370)
        pygame.display.update()