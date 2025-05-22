import pygame
from pathlib import Path

pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Викориистання спрайтів")
sprites_folder = Path(__file__).parent.joinpath("images/sprites/bird")
sprite_images = []
for i in range(26):
    image = pygame.image.load(f"{sprites_folder}/frame_{i:0>2}_delay-0.04s.gif")
    sprite_images.append(image)


class AnimatedPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = sprite_images
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)

    def update(self):
        current_time = pygame.time.get_ticks()
        frame_time = 40
        self.current_image = current_time // frame_time % len(self.images)
        self.image = self.images[self.current_image]

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 1
        if keys[pygame.K_RIGHT]:
            self.rect.x += 1
        if keys[pygame.K_UP]:
            self.rect.y -= 1
        if keys[pygame.K_DOWN]:
            self.rect.y += 1


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
    pygame.time.delay(5)

pygame.quit()
