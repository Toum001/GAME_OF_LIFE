import pygame
from display import draw_map
from life import create_map, count_around, next_generation

ROWS = 30
COLS = 40
CELL = 20

pygame.init()
screen = pygame.display.set_mode((COLS * CELL, ROWS * CELL))
clock = pygame.time.Clock()

map = create_map(ROWS, COLS)
running = True
paused = True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            elif event.key == pygame.K_c:
                map = create_map(ROWS, COLS)
            elif event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            map[y // CELL][x // CELL] = 1 - map[y // CELL][x // CELL]
    
    if not paused:
        map = next_generation(map)
        
    draw_map(screen, map)
    pygame.display.flip()
    clock.tick(10)

pygame.quit()