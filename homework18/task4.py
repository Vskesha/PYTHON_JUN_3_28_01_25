"""
Створіть програму, яка малює синю лінію, яка змінює 
свою товщину при натисканні клавіші '+' та '-'.
"""

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Малювання лінії")

w = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                w += 1
            elif event.key == pygame.K_MINUS:
                if w > 1:
                    w -= 1

    screen.fill((255, 255, 255))
    
    pygame.draw.line(screen, (0, 0, 0), (100, 100), (700, 500), w)
    pygame.display.flip()

pygame.quit()
