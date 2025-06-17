"""
Створіть вікно гри розміром 640x480 
пікселів з червоним фоном та додайте 
заголовок "Моя перша гра".
"""

import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Моя перша гра")
screen.fill((255, 0, 0))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
