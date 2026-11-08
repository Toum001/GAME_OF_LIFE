import pygame
from display import draw_map, CELL, draw_bar, BLACK, WHITE, GRAY, BAR_HEIGHT, DARK, YELLOW
from life import create_map, count_around, next_generation

ROWS = 30
COLS = 40

pygame.init()
screen = pygame.display.set_mode((COLS * CELL, ROWS * CELL + BAR_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)
generation = 0

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
                generation = 0
            elif event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if y < ROWS * CELL:
                row = y // CELL
                col = x // CELL
                map[row][col] = 1 - map[row][col]    
    if not paused:
        map = next_generation(map)
        generation += 1

    state = "PAUSE" if paused else "EN COURS"
    draw_map(screen, map)
    draw_bar(screen, font, map, f"Generation : {generation}  |  {state}  |  Espace: pause   C: effacer")
    pygame.display.flip()
    clock.tick(5) 

pygame.quit()