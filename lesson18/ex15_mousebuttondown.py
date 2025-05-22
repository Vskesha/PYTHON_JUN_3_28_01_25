import pygame
from random import randint

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Обробка натискання клавіш")

circles = []        

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:            
            if event.button == 1:
                circle = {
                    "pos": event.pos, 
                    "radius": 5,
                    "max_radius": randint(50, 150),
                    "color": (randint(0, 255), randint(0, 255), randint(0, 255)),
                }
                circles.append(circle)
            elif event.button == 3:
                circles.clear()

    screen.fill((0, 0, 0))

    for circle in circles:
        if circle["radius"] < circle["max_radius"]:
            circle["radius"] += 1
        pygame.draw.circle(screen, circle["color"], circle["pos"], circle["radius"], 3)

    pygame.display.flip()
    pygame.time.delay(15)

pygame.quit()
