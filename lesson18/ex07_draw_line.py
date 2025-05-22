import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Малювання ліній")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))

    pygame.draw.line(screen, (255, 0, 0), (100, 100), (700, 100), 5)
    pygame.draw.line(screen, (0, 255, 0), (100, 200), (700, 200), 5)
    pygame.draw.line(screen, (0, 0, 255), (100, 300), (700, 300), 5)

    pygame.display.flip()

pygame.quit()
