import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Оновлення дисплея: update")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 255, 0), (100, 100, 200, 150))

    pygame.display.update(pygame.Rect(100, 100, 400, 350))
    # pygame.display.update(pygame.Rect(50, 50, 400, 350))

pygame.quit()
