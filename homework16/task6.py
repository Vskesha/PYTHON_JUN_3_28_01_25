"""
Додайте фонове зображення до вашого вікна гри та 
розмістіть на ньому кілька об'єктів, які рухаються.
"""

import os
import pygame
import random
from pathlib import Path

os.environ['SDL_VIDEO_WINDOW_POS'] = "100,40"
pygame.init()

width, height = 1024, 768

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving cat")

icon_path = Path(__file__).parent.joinpath("images/icon_cat.png")
icon_image = pygame.image.load(icon_path)
pygame.display.set_icon(icon_image)

bg_path = Path(__file__).parent.joinpath("images/bg_cat.png")
bg_image = pygame.image.load(bg_path)
bg_width = bg_image.get_width()
bg_height = bg_image.get_height()

speed_x = speed_y = 5
x = random.randint(0, width - bg_width)
y = random.randint(0, height - bg_height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((150, 200, 0))

    screen.blit(bg_image, (x, y))
    x += speed_x
    y += speed_y

    if x < 0 or x + bg_width > width:
        speed_x = -speed_x
    if y < 0 or y + bg_height > height:
        speed_y = -speed_y
    
    pygame.time.delay(20)
    pygame.display.flip()

pygame.quit()
