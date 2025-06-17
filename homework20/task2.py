import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

player = pygame.Rect(100, 100, 50, 50)
player_color = (0, 255, 0)

target = pygame.Rect(400, 300, 50, 50)
target_color = (255, 0, 0)

score = 0
collided = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    if player.colliderect(target):
        if not collided:
            score += 1
            collided = True
            target.x = random.randint(0, WIDTH - target.width)
            target.y = random.randint(0, HEIGHT - target.height)
    else:
        collided = False

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, player_color, player)
    pygame.draw.rect(screen, target_color, target)

    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
