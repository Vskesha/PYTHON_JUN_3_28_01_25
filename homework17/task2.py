"""
Додайте текст "Привіт, Pygame!" 
у центрі вашого вікна гри. 
Використовуйте білий колір для тексту.
"""

import pygame

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Моя перша гра")
screen.fill((255, 0, 0))
pygame.display.flip()

font = pygame.font.Font(None, 70)
text = font.render("Привіт, Pygame!",
                   True,
                   (255, 255, 255))
text_rect = text.get_rect(center=(width // 2, height //2))
screen.blit(text, text_rect)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
