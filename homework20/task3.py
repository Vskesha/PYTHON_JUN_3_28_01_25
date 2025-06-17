import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

ball = pygame.Rect(100, 100, 50, 50)
ball_color = (0, 200, 255)

speed_x = 4
speed_y = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball.x += speed_x
    ball.y += speed_y

    if ball.left <= 0 or ball.right >= WIDTH:
        speed_x = -speed_x
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        speed_y = -speed_y

    screen.fill((20, 20, 20))
    pygame.draw.ellipse(screen, ball_color, ball)
    pygame.display.flip()
    clock.tick(60)
