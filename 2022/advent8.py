def isVisible(i, j):
    visibleDirections = 4
    for x in range(0, j):
        if grid[i][x] >= grid[i][j]:
            visibleDirections -= 1
            break
    for y in range(0, i):
        if grid[y][j] >= grid[i][j]:
            visibleDirections -= 1
            break
    for x in range(j+1, len(grid[i])):
        if grid[i][x] >= grid[i][j]:
            visibleDirections -= 1
            break
    for y in range(i+1, len(grid)):
        if grid[y][j] >= grid[i][j]:
            visibleDirections -= 1
            break
    return visibleDirections > 0

def scenicScore(i, j):
    leftScore = rightScore = topScore = downScore = 0
    for x in range(j-1, -1,-1):
        leftScore += 1
        if grid[i][x] >= grid[i][j]:
            break
    for y in range(i-1, -1, -1):
        topScore += 1
        if grid[y][j] >= grid[i][j]:
            break
    for x in range(j+1, len(grid[i])):
        rightScore += 1
        if grid[i][x] >= grid[i][j]:
            break
    for y in range(i+1, len(grid)):
        downScore += 1
        if grid[y][j] >= grid[i][j]:
            break
    return leftScore * rightScore * topScore * downScore

with open("advent8.txt","r") as f:
    lines = f.readlines()
    grid = []
    for i in range(0, len(lines)):
        grid.append([])
        for j in range(0, len(lines[i])):
            if lines[i][j] != "\n": grid[i].append(lines[i][j])
    
    # Gets the number of edges first
    # visible = (2*(len(grid)-1)) + (2*(len(grid[0])-1))
    maxScore = 0
    for x in range(1, len(grid)-1):
        for y in range(1, len(grid[x])-1):
            score = scenicScore(x, y)
            if score >= maxScore: maxScore = score

    #print(f"Total visible trees: {visible}")
    print(f"Highest possible scenic score: {maxScore}")
    f.close()