"""
Створіть просту анімацію, де синій квадрат 
рухається зліва направо по екрану. Коли 
квадрат досягає правого краю, він повинен 
почати рух зліва знову.
"""

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

running = True
x_position = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (0, 0, 255), (x_position, 300, 50, 50))
    pygame.display.flip()

    x_position += 5
    if x_position > 800:
        x_position = 0

    pygame.time.delay(20)

pygame.quit()
