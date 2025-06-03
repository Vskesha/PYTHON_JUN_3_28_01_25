"""
Створіть програму, яка малює коло, яке змінює свій 
колір кожного разу, коли ви натискаєте пробіл.
"""

import pygame
import random

width, height = 800, 600
max_speed = 5

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Анімація кольорових кругів")

radius = random.randint(30, 50)
x = random.randint(radius, width - radius)
y = random.randint(radius, height - radius)
speed_x = random.randint(-max_speed, max_speed)
speed_y = random.randint(-max_speed, max_speed)
color = (random.randint(0, 255),
         random.randint(0, 255),
         random.randint(0, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            color = (random.randint(0, 255),
                     random.randint(0, 255),
                     random.randint(0, 255))

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, color, (x, y), radius)
    x += speed_x
    y += speed_y

    if x < radius or x > width - radius:
        speed_x *= -1
    if y < radius or y > height - radius:
        speed_y *= -1
    
    pygame.display.flip()
    pygame.time.delay(20)

pygame.quit()
