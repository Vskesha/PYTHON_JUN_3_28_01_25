import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

width, height = 800, 600
size = 50
radius = 40
interval_ms = 500
speed = 5

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Збір кружечків")

player = pygame.Rect(0, 0, size, size)
player.center = (width // 2, height // 2)

circles = []
for _ in range(10):
    x = random.randint(0, width - size)
    y = random.randint(0, height - size)
    circles.append(pygame.Rect(x, y, radius, radius))

score = 0
font = pygame.font.Font(None, 36)

CREATE_CIRCLE = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_CIRCLE, interval_ms)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CREATE_CIRCLE:
            x = random.randint(0, width - size)
            y = random.randint(0, height - size)
            circles.append(pygame.Rect(x, y, radius, radius))
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= speed
        if player.y < 0:
            player.y = 0
    if keys[pygame.K_DOWN]:
        player.y += speed
        if player.y > height - size:
            player.y = height - size
    if keys[pygame.K_LEFT]:
        player.x -= speed
        if player.x < 0:
            player.x = 0
    if keys[pygame.K_RIGHT]:
        player.x += speed
        if player.x > width - size:
            player.x = width - size

    for circle in circles.copy():
        if player.colliderect(circle):
            circles.remove(circle)
            score += 1

    screen.fill(WHITE)
    
    for circle in circles:
        pygame.draw.ellipse(screen, BLUE, circle)

    pygame.draw.rect(screen, RED, player)

    score_text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    pygame.time.delay(25)    

pygame.quit()
