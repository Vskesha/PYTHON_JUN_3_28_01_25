"""
Намалюйте спіраль, яка поступово збільшується 
та змінює колір кожні 10 кроків.
"""

import colorsys
import math
import pygame
import random


width, height = 800, 600

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw spiral")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))

    x, y = width // 2, height // 2
    length = 1
    angle = random.uniform(0, 2 * math.pi)
    color = (0, 0, 0)
    
    for i in range(250):
        color = colorsys.hsv_to_rgb(i / 40, 1.0, 1.0)
        color = tuple(c * 255 for c in color)
        end_x = x + length * math.cos(angle)
        end_y = y + length * math.sin(angle)
        pygame.draw.line(screen, 
                         color, 
                         (x, y), 
                         (end_x, end_y))
        angle -= math.pi / 20
        length += 0.3
        x, y = end_x, end_y
    
        pygame.display.flip()
        pygame.time.delay(50)

pygame.quit()
