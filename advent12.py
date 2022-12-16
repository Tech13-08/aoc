import dijkstra as djk

def nodes(i, j):
    nodes = []
    if i > 0 and ord(grid[i-1][j]) <= ord(grid[i][j])+1:
        nodes.append(str(i-1)+" "+str(j)+":"+"1")
    if i < len(grid)-1 and ord(grid[i+1][j]) <= ord(grid[i][j])+1:
        nodes.append(str(i+1)+" "+str(j)+":"+"1")
    if j > 0 and ord(grid[i][j-1]) <= ord(grid[i][j])+1 and [i,j-1]:
        nodes.append(str(i)+" "+str(j-1)+":"+"1")
    if j < len(grid[i])-1 and ord(grid[i][j+1]) <= ord(grid[i][j])+1:
        nodes.append(str(i)+" "+str(j+1)+":"+"1")
    return nodes
    
def findMin():
    global start
    data = nodes(start[0], start[1])
    djk.initialNode = djk.createNewDict(0, "PASSING_ARGS", len(data), data)
    minimumSteps = 0
    while(djk.recentMinNum < djk.stopNum):
        djk.findMinNode(djk.initialNode)
        #print(f"Lowest Node: {djk.lowestNode}")
        x = int(djk.lowestNode[0].split()[0])
        y = int(djk.lowestNode[0].split()[1])
        if djk.lowestNode[0] == str(end[0])+" "+str(end[1]):
            break
        if djk.lowestNode[0] != "":
            djk.path = []
            minimumSteps = int(djk.lowestNode[1])
            data = nodes(x, y)
            djk.updateMinNode(djk.initialNode, ["PASSING_ARGS", len(data), data])
        else:
            minimumSteps = djk.stopNum
            break

    largestCharDist = 0
    for node in djk.path:
        x = int(node.split()[0])
        y = int(node.split()[1])
        if grid[x][y] == "a": # Elevation to start from in addition to the S
            #print(f"X: {x} Y: {y} Dist: {dist}")
            if djk.spt[node] > largestCharDist:
                largestCharDist = djk.spt[node]
                start = [x, y]
    return minimumSteps - largestCharDist

with open("advent12.txt","r") as f:
    lines = f.readlines()
    grid = []
    start = [[0,0]]
    end = []
    for i in range(0, len(lines)):
        row = list(lines[i].replace("\n",""))
        start = (lambda : [i, row.index("S")] if ("S" in row) else start)()
        end = (lambda : [i, row.index("E")] if ("E" in row) else end)()
        grid.append(row)
        #print(grid[i])
    djk.stopNum = len(grid) * len(grid) * len(grid)
    djk.splitString = ":"
    past = [start]
    grid[start[0]][start[1]] = 'a'
    grid[end[0]][end[1]] = 'z'
    dist = findMin()
    print(f"Start: {start} End: {end} Dist: {dist}")
    print(f"Minimum steps: {dist}")