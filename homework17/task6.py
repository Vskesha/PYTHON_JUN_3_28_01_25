"""
Створіть анімований спрайт, який змінює 
свої зображення для створення ефекту бігу, 
коли ви натискаєте стрілку вгору.
"""

import pygame
from pathlib import Path

width, height = 1024, 768
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Анімований сонік")
sprites_folder = Path(__file__).parent.joinpath("sprites")
sprite_images_right = []
sprite_images_left = []
for i in range(8):
    image = pygame.image.load(sprites_folder.joinpath(f"sonic{i}.png"))
    sprite_images_right.append(image)
    mirrored = pygame.transform.flip(image, True, False)
    sprite_images_left.append(mirrored)


class AnimatedPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.right_images = sprite_images_right
        self.left_images = sprite_images_left
        self.image_idx = 0
        self.image = self.right_images[self.image_idx]
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 20
            if self.rect.x < 0:
                self.rect.x = width - self.rect.width
            self.image_idx = (self.image_idx + 1) % len(self.left_images)
            self.image = self.left_images[self.image_idx]
        if keys[pygame.K_RIGHT]:
            self.rect.x += 20
            if self.rect.x > width - self.rect.width:
                self.rect.x = 0
            self.image_idx = (self.image_idx + 1) % len(self.right_images)
            self.image = self.right_images[self.image_idx]
    

all_sprites = pygame.sprite.Group()
player = AnimatedPlayer()
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
    pygame.time.delay(50)

pygame.quit()
