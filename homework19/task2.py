"""
Створіть програму, де об'єкт слідує за курсором миші.
"""

import pygame

pygame.init()

width, height = 800, 600
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
speed = 5
radius = 50

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Переслідування курсору")

x, y = width // 2, height // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mx, my = pygame.mouse.get_pos()
    distance = ((mx - x) ** 2 + (my - y) ** 2) ** 0.5
    if distance > speed:
        x += (mx - x) / distance * speed
        y += (my - y) / distance * speed
        if x < radius:
            x = radius
        elif x > width - radius:
            x = width - radius
        if y < radius:
            y = radius
        elif y > height - radius:
            y = height - radius

    screen.fill(BLACK)
    pygame.draw.circle(screen, GREEN, (x, y), radius)
    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()
