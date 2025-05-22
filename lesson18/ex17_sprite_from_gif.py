import pygame
from pathlib import Path
from PIL import Image

pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Викориистання спрайтів")

sprite_path = Path(__file__).parent.joinpath("images/sprites/bird/bird.gif")
img = Image.open(sprite_path)

frames, durations = [], []

for frame_index in range(img.n_frames):
    img.seek(frame_index)
    rgba = img.convert('RGBA')    
    frame = pygame.image.frombytes(rgba.tobytes(), rgba.size, rgba.mode)
    frames.append(frame)
    durations.append(img.info.get('duration', 50))

class AnimatedPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = frames
        self.durations = durations
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        self.time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.time > self.durations[self.current_image]:
            self.current_image = (self.current_image + 1) % len(self.images)
            self.time += self.durations[self.current_image]
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
