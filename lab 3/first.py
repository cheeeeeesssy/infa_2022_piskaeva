import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

#сделаем фон

rect(screen, (31, 241, 244), (0, 0, 500, 500))
rect(screen, (27, 248, 31), (0, 200, 500, 300))

# Рисуем солне с альфа прозрачностью
for i in range(0, 100):
    sun = pygame.Surface((500, 100))
    sun.fill((31, 241, 244))
    sun.set_colorkey((255, 175, 45))
    sun.set_alpha(100 - i / 0.9)
    pygame.draw.circle(sun, (255, 255, 102), (350, 10), i)
    screen.blit(sun, (100, 0))


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

    #  Вызываем рисунки


unicorn_right(screen, 330, 250, 2, (170, 250, 250))
unicorn_right(screen, 260, 200, 3, (255, 255, 255))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
