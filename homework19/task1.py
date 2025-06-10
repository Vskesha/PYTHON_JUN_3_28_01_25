"""
Напишіть програму, в якій об'єкт змінює свій колір на
випадковий кожного разу, коли ви натискаєте пробіл.
"""

import pygame
from random import randint

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Зміна кольору")

color = (255, 0, 0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color = (randint(0, 255),
                         randint(0, 255),
                         randint(0, 255))
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, 
                     color, 
                     (350, 250, 100, 100))
    pygame.display.flip()

pygame.quit()
