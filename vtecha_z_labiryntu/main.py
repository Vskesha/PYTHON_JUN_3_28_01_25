import pygame
import random


pygame.init()

# Створення вікна гри
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Втеча з лабіринту')

# Фоновий колір
background_color = (0, 0, 0)  # Чорний колір фону
cell_size = 40

wall_img = pygame.image.load("assets/wall.jpg")
wall_img = pygame.transform.scale(wall_img, (cell_size, cell_size))

key_img = pygame.image.load("assets/key.png")
key_img = pygame.transform.scale(key_img, (cell_size, cell_size))

door_img = pygame.image.load("assets/door.png")
door_img = pygame.transform.scale(door_img, (cell_size, cell_size))

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
height = len(maze)
width = len(maze[0])

free_cells = []
for y in range(height):
    for x in range(width):
        if maze[y][x] == 0:
            free_cells.append((x, y))

key_position = random.choice(free_cells[1:-1])
door_position = free_cells[-1]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заповнюємо екран фоном
    screen.fill(background_color)

    for y in range(height):
        for x in range(width):
            if maze[y][x] == 1:
                screen.blit(wall_img, (x * cell_size, y * cell_size))

    screen.blit(key_img, (key_position[0] * cell_size, key_position[1] * cell_size))
    screen.blit(door_img, (door_position[0] * cell_size, door_position[1] * cell_size))

    # Оновлюємо екран
    pygame.display.flip()

pygame.quit()
