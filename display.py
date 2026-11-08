import pygame

CELL = 20
BLACK = (0, 0, 0)
GRAY = (40, 40, 40)
WHITE = (255, 255, 255)
BAR_HEIGHT = 40
DARK = (20, 20, 20)
YELLOW = (0, 128, 0)

def draw_bar(screen, font, grid, text):
    top = len(grid) * CELL
    width = len(grid[0]) * CELL
    bar = pygame.Rect(0, top, width, BAR_HEIGHT)
    pygame.draw.rect(screen, DARK, bar)
    image = font.render(text, True, YELLOW)
    screen.blit(image, image.get_rect(center=bar.center))

def draw_map(screen, grid):
    screen.fill(BLACK)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            rect = pygame.Rect(j * CELL, i * CELL, CELL, CELL)
            if grid[i][j] == 1:
                pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)
            