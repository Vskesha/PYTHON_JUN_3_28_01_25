"""
Завантажте зображення спрайта та зробіть так, 
щоб спрайт рухався ліворуч при натисканні клавіші 'A', 
праворуч при натисканні 'D', вгору при натисканні 'W' 
та вниз при натисканні 'S'.
"""

import pygame
from pathlib import Path

width, height = 1024, 768

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Викориистання спрайтів")
sprites_folder = Path(__file__).parent.joinpath("sprites")
sprite_image_path = sprites_folder.joinpath("sonic.png")
sprite_image = pygame.image.load(sprite_image_path)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = sprite_image
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 1
        if keys[pygame.K_d]:
            self.rect.x += 1
        if keys[pygame.K_w]:
            self.rect.y -= 1
        if keys[pygame.K_s]:
            self.rect.y += 1


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    all_sprites.update()

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
