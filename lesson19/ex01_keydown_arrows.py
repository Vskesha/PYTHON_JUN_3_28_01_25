import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Натискання клавіш")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Натиснуто стрілку вліво")
            elif event.key == pygame.K_RIGHT:
                print("Натиснуто стрілку вправо")
            elif event.key == pygame.K_UP:
                print("Натиснуто стрілку вгору")
            elif event.key == pygame.K_DOWN:
                print("Натиснуто стрілку вниз")
            elif event.key == pygame.K_SPACE:
                print("Натиснуто пробіл")

pygame.quit()
