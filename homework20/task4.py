import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

circle_x = 100
circle_y = HEIGHT // 2
circle_radius = 30
circle_color = (255, 100, 100)
speed = 5

fps = 30
low_fps = 15
high_fps = 30

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if fps == high_fps:
                    fps = low_fps
                else:
                    fps = high_fps

    circle_x += speed
    if circle_x + circle_radius >= WIDTH or circle_x - circle_radius <= 0:
        speed = -speed

    screen.fill((30, 30, 30))
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)

    fps_text = pygame.font.SysFont(None, 36).render(f"FPS: {fps}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))

    pygame.display.flip()
    clock.tick(fps)
