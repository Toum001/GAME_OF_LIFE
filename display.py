import pygame

CELL = 20
BLACK = (0, 0, 0)
GRAY = (40, 40, 40)
WHITE = (255, 255, 255)


def draw_map(screen, grid):
    screen.fill(BLACK)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            rect = pygame.Rect(j * CELL, i * CELL, CELL, CELL)
            if grid[i][j] == 1:
                pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)