import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

objects = [
    {"rect": pygame.Rect(100, 100, 80, 80), "color": (255, 0, 0)},
    {"rect": pygame.Rect(300, 200, 80, 80), "color": (0, 255, 0)},
    {"rect": pygame.Rect(500, 150, 80, 80), "color": (0, 0, 255)},
]

dragging_obj = None
offset_x, offset_y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for obj in objects:
                if obj["rect"].collidepoint(event.pos):
                    dragging_obj = obj
                    mouse_x, mouse_y = event.pos
                    offset_x = obj["rect"].x - mouse_x
                    offset_y = obj["rect"].y - mouse_y
                    break

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging_obj = None

        elif event.type == pygame.MOUSEMOTION:
            if dragging_obj:
                mouse_x, mouse_y = event.pos
                dragging_obj["rect"].x = mouse_x + offset_x
                dragging_obj["rect"].y = mouse_y + offset_y

    screen.fill((30, 30, 30))
    for obj in objects:
        pygame.draw.rect(screen, obj["color"], obj["rect"])
    pygame.display.flip()
    clock.tick(60)
