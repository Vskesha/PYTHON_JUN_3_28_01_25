import pygame
import random

# Створити налаштування гри
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

score = 0
speed = 1
number_of_obstacles = 10
start_x = 0
start_y = 0
size = 50

# Ініціалізація і створення вікна
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Уникати і збирати")

# Створення гравця, цілі та перешкод
player = pygame.Rect(start_x, start_y, size, size)
goal = pygame.Rect(random.randint(0, WIDTH - size),
                   random.randint(0, HEIGHT - size),
                   size,
                   size)
obstacles = []
for _ in range(number_of_obstacles):
    x = random.randint(size, WIDTH - size * 2)
    y = random.randint(size, HEIGHT - size * 2)
    obstacle = pygame.Rect(x, y, size, size)
    obstacles.append(obstacle)

# Головний цикл гри
game_over = False
running = True
while running:
    # Перевірка закриття вікна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Перевірка натискання клавіш і зміна позиції гравця
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    # Перевірка зіткнення з перешкодами
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            player.x = start_x
            player.y = start_y
            score = 0
            break
    
    # Перевірка зіткнення з ціллю
    if player.colliderect(goal):
        game_over = True

    # Малювання об'єктів на екрані
    screen.fill(WHITE)
    
    if game_over:
        font = pygame.font.Font(None, 74)
        text = font.render("YOU WIN!", True, RED)
        text_rect = text.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT // 2)
        screen.blit(text, text_rect)
    else:
        for obstacle in obstacles:
            pygame.draw.rect(screen, RED, obstacle)
        pygame.draw.rect(screen, YELLOW, goal)
        pygame.draw.rect(screen, GREEN, player)

    # Оновлення екрану
    pygame.display.flip()
    pygame.time.delay(2)

# Завершення гри
pygame.quit()
