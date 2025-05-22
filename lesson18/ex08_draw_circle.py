import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Малювання кіл")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (255, 0, 0), (400, 300), 100, 5)
    pygame.draw.circle(screen, (0, 255, 0), (200, 300), 50, 5)
    pygame.draw.circle(screen, (0, 0, 255), (600, 300), 75, 5)

    pygame.display.flip()

pygame.quit()
