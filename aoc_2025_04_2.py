with open("inputs/input_04.txt") as file:
    grid = [[x for x in a] for a in file.read().strip("\n").split("\n")]

removed_items = []
removed = 0
previously_removed = -1

while removed - previously_removed:
    previously_removed = removed
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            adj = 0
            for x_neigh in [-1, 0, 1]:
                for y_neigh in [-1, 0, 1]:
                    if ((x_neigh or y_neigh)
                            and x + x_neigh <= len(grid[0])-1
                            and y + y_neigh <= len(grid)-1
                            and x + x_neigh >= 0
                            and y + y_neigh >= 0):
                        if grid[y + y_neigh][x + x_neigh] == '@':
                            adj += 1

            if adj < 4 and grid[y][x] == '@':
                removed += 1
                removed_items.append((x,y))

    for item in removed_items:
        grid[item[1]][item[0]] = '.'

print(removed)