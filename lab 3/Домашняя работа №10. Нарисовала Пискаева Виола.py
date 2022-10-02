import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

#сделаем фон

rect(screen, (31, 241, 244), (0, 0, 500, 500))
rect(screen, (27, 248, 31), (0, 200, 500, 300))


# Рисуем солнце с альфа прозрачностью

for i in range(0, 100):
    sun = pygame.Surface((500, 160))
    sun.fill((31, 241, 244))
    sun.set_colorkey((255, 175, 45))
    sun.set_alpha(75 - i / 0.9)
    pygame.draw.circle(sun, (255, 255, 102), (320, 70), i)
    screen.blit(sun, (75, 0))
    


# Рисуем козерога правого

def unicorn_right(screen, x, y, N, color):
    pygame.draw.ellipse(screen, color, (x, y, 150 // N, 60 // N))
    rect(screen, color, (x + 115 // N, y - 40 // N, 30 // N, 60 // N))
    circle(screen, color, (x + 140 // N, y - 40 // N), 15 // N)
    pygame.draw.ellipse(screen, color,
                        (x + 140 // N, y - 45 // N, 30 // N, 15 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x + 110 // N, y - 60 // N, 30 // N, 15 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x + 100 // N, y - 50 // N, 30 // N, 15 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x + 90 // N, y - 40 // N, 40 // N, 15 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x + 100 // N, y - 20 // N, 30 // N, 10 // N))
    pygame.draw.ellipse(screen, (202, 123, 223),
                        (x + 80 // N, y - 20 // N, 40 // N, 10 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x + 85 // N, y - 30 // N, 35 // N, 10 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x + 70 // N, y - 7 // N, 40 // N, 10 // N))
    pygame.draw.ellipse(screen, (157, 141, 207),
                        (x + 92 // N, y - 25 // N, 40 // N, 10 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x + 90 // N, y - 10 // N, 40 // N, 15 // N))
    pygame.draw.ellipse(screen, (157, 141, 207),
                        (x + 80 // N, y - 15 // N, 40 // N, 10 // N))
    pygame.draw.ellipse(screen, (157, 141, 207),
                        (x + 83 // N, y, 40 // N, 10 // N))
    pygame.draw.ellipse(screen, (157, 141, 207),
                        (x + 107 // N, y - 43 // N, 27 // N, 10 // N))
    pygame.draw.ellipse(screen, (202, 123, 223),
                        (x + 95 // N, y - 35 // N, 20 // N, 7 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x + 10 // N, y, 30 // N, 15 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x, y + 10 // N, 30 // N, 15 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x - 10 // N, y + 20 // N, 40 // N, 15 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x, y + 40 // N, 30 // N, 10 // N))
    pygame.draw.ellipse(screen, (202, 123, 223),
                        (x - 20 // N, y + 40 // N, 40 // N, 10 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x - 15 // N, y + 30 // N, 35 // N, 10 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x - 30 // N, y + 53 // N, 40 // N, 10 // N))
    pygame.draw.ellipse(screen, (157, 141, 207),
                        (x - 8 // N, y + 35 // N, 40 // N, 10 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x - 10 // N, y + 50 // N, 40 // N, 15 // N))
    pygame.draw.ellipse(screen, (157, 141, 207),
                        (x - 20 // N, y + 45 // N, 40 // N, 10 // N))
    pygame.draw.ellipse(screen, (157, 141, 207),
                        (x - 17 // N, y + 60 // N, 40 // N, 10 // N))
    pygame.draw.ellipse(screen, (157, 141, 207),
                        (x + 7 // N, y + 17 // N, 27 // N, 10 // N))
    pygame.draw.ellipse(screen, (202, 123, 223),
                        (x - 5 // N, y + 25 // N, 20 // N, 7 // N))
    rect(screen, color, (x + 105 // N, y + 20 // N, 10 // N, 70 // N))
    rect(screen, color, (x + 130 // N, y + 40 // N, 10 // N, 70 // N))
    rect(screen, color, (x + 35 // N, y + 20 // N, 10 // N, 70 // N))
    rect(screen, color, (x + 60 // N, y + 40 // N, 10 // N, 70 // N))
    circle(screen, (244, 148, 205), (x + 142 // N, y - 42 // N), 7 // N)
    pygame.draw.ellipse(screen, (255, 255, 255),
                        (x + 138 // N, y - 42 // N, 9 // N, 2 // N))
    circle(screen, (0, 0, 0), (x + 147 // N, y - 42 // N), 3 // N)
    pygame.draw.polygon(
        screen, (157, 141, 207),
        [[x + 132 // N, y - 55 // N], [x + 140 // N, y - 55 // N],
         [x + 145 // N, y - 90 // N]])


# Рисуем левого козерога

def unicorn_left(screen, x, y, N, color):
    x = x + 150 // N
    pygame.draw.ellipse(screen, color, (x - 150 // N, y, 150 // N, 60 // N))
    rect(screen, color, (x - 145 // N, y - 40 // N, 30 // N, 60 // N))
    circle(screen, color, (x - 140 // N, y - 40 // N), 15 // N)
    pygame.draw.ellipse(screen, color,
                        (x - 170 // N, y - 45 // N, 30 // N, 15 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x - 140 // N, y - 60 // N, 30 // N, 15 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x - 130 // N, y - 50 // N, 30 // N, 15 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x - 130 // N, y - 40 // N, 40 // N, 15 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x - 130 // N, y - 20 // N, 30 // N, 10 // N))
    pygame.draw.ellipse(screen, (202, 123, 223),
                        (x - 120 // N, y - 20 // N, 40 // N, 10 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x - 120 // N, y - 30 // N, 35 // N, 10 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x - 110 // N, y - 7 // N, 40 // N, 10 // N))
    pygame.draw.ellipse(screen, (157, 141, 207),
                        (x - 132 // N, y - 25 // N, 40 // N, 10 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x - 130 // N, y - 10 // N, 40 // N, 15 // N))
    pygame.draw.ellipse(screen, (157, 141, 207),
                        (x - 120 // N, y - 15 // N, 40 // N, 10 // N))
    pygame.draw.ellipse(screen, (157, 141, 207),
                        (x - 123 // N, y, 40 // N, 10 // N))
    pygame.draw.ellipse(screen, (157, 141, 207),
                        (x - 134 // N, y - 43 // N, 27 // N, 10 // N))
    pygame.draw.ellipse(screen, (202, 123, 223),
                        (x - 115 // N, y - 35 // N, 20 // N, 7 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x - 40 // N, y, 30 // N, 15 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x - 30 // N, y + 10 // N, 30 // N, 15 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x - 30 // N, y + 20 // N, 40 // N, 15 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x - 30 // N, y + 40 // N, 30 // N, 10 // N))
    pygame.draw.ellipse(screen, (202, 123, 223),
                        (x - 20 // N, y + 40 // N, 40 // N, 10 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x - 20 // N, y + 30 // N, 35 // N, 10 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x - 10 // N, y + 53 // N, 40 // N, 10 // N))
    pygame.draw.ellipse(screen, (157, 141, 207),
                        (x - 32 // N, y + 35 // N, 40 // N, 10 // N))
    pygame.draw.ellipse(screen, (244, 148, 205),
                        (x - 30 // N, y + 50 // N, 40 // N, 15 // N))
    pygame.draw.ellipse(screen, (157, 141, 207),
                        (x - 20 // N, y + 45 // N, 40 // N, 10 // N))
    pygame.draw.ellipse(screen, (157, 141, 207),
                        (x - 23 // N, y + 60 // N, 40 // N, 10 // N))
    pygame.draw.ellipse(screen, (157, 141, 207),
                        (x - 20 // N, y + 17 // N, 27 // N, 10 // N))
    pygame.draw.ellipse(screen, (202, 123, 223),
                        (x - 15 // N, y + 25 // N, 20 // N, 7 // N))
    rect(screen, color, (x - 115 // N, y + 20 // N, 10 // N, 70 // N))
    rect(screen, color, (x - 140 // N, y + 40 // N, 10 // N, 70 // N))
    rect(screen, color, (x - 45 // N, y + 20 // N, 10 // N, 70 // N))
    rect(screen, color, (x - 70 // N, y + 40 // N, 10 // N, 70 // N))
    circle(screen, (244, 148, 205), (x - 142 // N, y - 42 // N), 7 // N)
    pygame.draw.ellipse(screen, (255, 255, 255),
                        (x - 147 // N, y - 42 // N, 9 // N, 2 // N))
    circle(screen, (0, 0, 0), (x - 147 // N, y - 42 // N), 3 // N)
    pygame.draw.polygon(
        screen, (157, 141, 207),
        [[x - 132 // N, y - 55 // N], [x - 140 // N, y - 55 // N],
         [x - 145 // N, y - 90 // N]])


# Рисуем деревья

def tree(screen, color_leaves, color_apples, color_trunk, x, y, N):
    rect(screen, color_trunk, (x, y, 30 // N, 100 // N))
    pygame.draw.ellipse(screen, color_leaves,
                        (x - 45 // N, y - 230 // N, 120 // N, 150 // N))
    pygame.draw.ellipse(screen, (134,166,89),
                        (x - 45 // N, y - 230 // N, 120 // N, 150 // N), 2)     #верхний овал
    pygame.draw.ellipse(screen, color_leaves,
                        (x - 85 // N, y - 150 // N, 200 // N, 100 // N))
    pygame.draw.ellipse(screen, (134,166,89),
                        (x - 85 // N, y - 150 // N, 200 // N, 100 // N), 2)     #средний овал
    pygame.draw.ellipse(screen, color_leaves,
                        (x - 45 // N, y - 80 // N, 120 // N, 100 // N))
    pygame.draw.ellipse(screen, (134,166,89),
                        (x - 45 // N, y - 80 // N, 120 // N, 100 // N), 2)      #нижний овал
    circle(screen, color_apples, (x + 30 // N, y - 180 // N), 15 // N)
    circle(screen, color_apples, (x + 50 // N, y - 20 // N), 15 // N)
    circle(screen, color_apples, (x + 75 // N, y - 90 // N), 15 // N)
    circle(screen, color_apples, (x - 45 // N, y - 100 // N), 15 // N)


# Вызываем рисунки

unicorn_left(screen, 400, 195, 2.5, (255, 255, 255))    #дальний правый
unicorn_right(screen, 250, 225, 2, (255, 255, 255))     #дальний левый
unicorn_right(screen, 150, 350, 1, (255, 255, 255))     #ближний левый
unicorn_left(screen, 350, 300, 1.2, (255, 255, 255))    #ближний правый

tree(screen, (5, 70, 2), (244, 148, 205), (255, 255, 255), 150, 150, 1.5)   #дальнее дерево
tree(screen, (5, 70, 2), (244, 148, 205), (255, 255, 255), 175, 263, 2)     #центральное левое дерево
tree(screen, (5, 70, 2), (244, 148, 205), (255, 255, 255), 25, 275, 2)      #центральное левое дерево
tree(screen, (5, 70, 2), (244, 148, 205), (255, 255, 255), 115, 330, 1.8)   #второе спереди дерево
tree(screen, (5, 70, 2), (244, 148, 205), (255, 255, 255), 50, 390, 2)      #ближнее дерево

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()