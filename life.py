def create_map(height, width):
    map = []
    for i in range(height):
        line = [0] * width
        map.append(line)
    return map

def count_around(map, height, width, x, y):
    nb = 0
    for i in range (-1, 2):
        if (x + i < 0 or x + i >= height):
            continue
        for j in range (-1, 2):
            if (y + j < 0 or y + j >= width):
                continue
            if (i == 0 and j == 0):
                continue
            if (map[x + i][y + j] == 1):
                nb += 1
    return (nb)

def next_generation(map):
    height = len(map)
    width = len(map[0])
    new = create_map(height, width)
    for i in range(height):
        for j in range(width):
            nb = count_around(map, height, width, i, j)
            if (map[i][j] == 1):
                if (nb == 2 or nb == 3):
                    new[i][j] = 1
                else:
                    new[i][j] = 0
            else:
                if (nb == 3):
                    new[i][j] = 1
                else:
                    new[i][j] = 0
    return (new)
