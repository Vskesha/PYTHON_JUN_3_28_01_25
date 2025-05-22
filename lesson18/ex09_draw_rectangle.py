import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Малювання прямокутників")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 150), 5)
    pygame.draw.rect(screen, (0, 255, 0), (400, 100, 200, 150), 5)
    pygame.draw.rect(screen, (0, 0, 255), (250, 300, 200, 150), 5)

    pygame.display.flip()

pygame.quit()
