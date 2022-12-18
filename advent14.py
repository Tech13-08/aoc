def movedSandTillRest(pos):
    global minX, maxX
    x, y = pos[0], pos[1]
    gridX, gridY = x-minX,y # Avoid the border and map the x to the grid length
    grid[gridY][gridX] = "o"
    if gridX+1>len(grid[0])-1:
        maxX += 1
        for row in grid:
            row.append(".") # Expand the grid to the right
        grid[len(grid)-1][-1] = "#" # Keep the last row as a row of rock
    if gridX-1 < 0:
        gridX+=1
        minX -= 1
        for row in grid:
            row.insert(0, ".") # Expand the grid to the left
        grid[len(grid)-1][0] = "#" # Keep the last row as a row of rock
    options = [grid[gridY+1][gridX-1], grid[gridY+1][gridX], grid[gridY+1][gridX+1]]
    #print(f"Grid Y: {gridY} Grid X: {gridX} Options: {options}")
    if options[1] == ".":
        #print("Going Down")
        grid[gridY][gridX] = "."
        return movedSandTillRest([x,y+1])
    elif options[0] == ".":
        #print("Going Left")
        grid[gridY][gridX] = "."
        return movedSandTillRest([x-1,y+1])
    elif options[2] == ".":
        #print("Going Right")
        grid[gridY][gridX] = "."
        return movedSandTillRest([x+1,y+1])
    # elif "B" in options:
    #     grid[gridY][gridX] = "."
    #     return False
    else:
        return True

with open("advent14.txt","r") as f:
    lines = f.readlines()
    rocks = []
    minX = 500
    maxX = maxY = 0
    for l in lines:
        if "\n" in l: l = l[:-1]
        positions = l.split(" -> ")
        for i in range(0, len(positions)):
            pos = positions[i]
            pos = [int(pos.split(",")[0]),int(pos.split(",")[1])]
            if i > 0:
                prevPos = rocks[-1]
                xDiff = pos[0]-prevPos[0]
                yDiff = pos[1]-prevPos[1]
                while xDiff != 0:
                    prevPos = [prevPos[0] + ((xDiff)/abs(xDiff)), prevPos[1]]
                    rocks.append(prevPos)
                    xDiff = pos[0]-prevPos[0]
                while yDiff != 0:
                    prevPos = [prevPos[0], prevPos[1] + ((yDiff)/abs(yDiff))]
                    rocks.append(prevPos)
                    yDiff = pos[1]-prevPos[1]
            rocks.append(pos)
            #print(f"Pos: {pos}")
            if pos[0] < minX: minX = pos[0]
            if pos[0] > maxX: maxX = pos[0]
            if pos[1] > maxY: maxY = pos[1]
    grid = []
    for i in range(0, maxY+1):
        grid.append([])
        #grid[i].append("B")
        for j in range(0, maxX-minX+1):
            if [minX+j,i] in rocks:
                grid[i].append("#")
            else:
                grid[i].append(".")
        #grid[i].append("B")
    grid.append(["." for _ in range(0, maxX-minX+1)])
    grid.append(["#" for _ in range(0, maxX-minX+1)])
    #grid[0][500-minX] = "+"
    # for row in grid:
    #     print("".join(row))
    totalSandAtRest = 1 # The source of the sand will eventually become a sand at rest too
    while movedSandTillRest([500,0]) and grid[0][500-minX] == ".":
        totalSandAtRest += 1
    # for row in grid:
    #     print("".join(row))
    print(f"Total sand at rest: {totalSandAtRest}")
    f.close()