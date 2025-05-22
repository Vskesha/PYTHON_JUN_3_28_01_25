"""
Створіть програму, яка малює веселку з кількох 
кіл різних кольорів, розташованих одна над іншою.
"""

import colorsys
import pygame

pygame.init()

width, height = 1200, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rainbow")

BLUE = (26, 209, 255)
radius = height
step = 1
center = (width // 2, height + 150)

i = 0
running = True
screen.fill(BLUE)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if i == 200:
        screen.fill(BLUE)
        radius = height
        pygame.time.delay(2000)
        i = 0

    color = colorsys.hsv_to_rgb(i / 250, 1.0, 1.0)
    color = tuple(c * 255 for c in color)
    pygame.draw.circle(screen, color, center, radius, 30)
    radius -= step
    pygame.display.flip()
    pygame.time.delay(20)
    i += 1

pygame.quit()
