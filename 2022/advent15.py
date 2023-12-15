def manhatDist(pos1, pos2):
    return abs(pos2[0]-pos1[0])+abs(pos2[1]-pos1[1])

def inXRange(x):
    for r in xRanges:
        if x >= r[0] and x <= r[1]:
            return True
    return False

def numNonBeacons(row, pos):
    global xRanges
    sensor = positions[0][pos]
    beacon = positions[1][pos]
    # print(f"Sensor: {sensor}")
    # print(f"Beacon: {beacon}")
    dist = manhatDist(sensor, beacon)
    yDiff = abs(row-sensor[1])
    # print(f"Dist: {dist} Ydiff: {yDiff}")
    intersectionPoints = []
    if(yDiff <= dist):
        xDiff = abs(dist-yDiff)
        # print(f"Xdiff: {xDiff}")
        xi, xf = sensor[0] - xDiff, sensor[0] + xDiff
        # print(f"Range: {xRanges}")
        for x in range(xi, xf+1):
            if not inXRange(x):
                if [x, row] not in positions[1]:
                    intersectionPoints.append([x,row])
                    # print(f"Added {[x, row]}")
        xRanges.append([xi, xf])
    return len(intersectionPoints)

def setRowXRanges(row):
    global xRanges
    for pos in range(0, len(positions[0])):
        sensor = positions[0][pos]
        beacon = positions[1][pos]
        # print(f"Sensor: {sensor}")
        # print(f"Beacon: {beacon}")
        dist = manhatDist(sensor, beacon)
        yDiff = abs(row-sensor[1])
        # print(f"Dist: {dist} Ydiff: {yDiff}")
        if(yDiff <= dist):
            xDiff = abs(dist-yDiff)
            # print(f"Xdiff: {xDiff}")
            xi, xf = sensor[0] - xDiff, sensor[0] + xDiff
            if (xi >= 0 and xi <= targetDimension) or (xf >= 0 and xf <= targetDimension):
                # print(f"Range: {xi, xf}")
                prevRange = [xRanges[0].copy(), xRanges[1].copy()]
                #print(f"Prev Range: {prevRange}")
                if xi < prevRange[0][0]:
                    #print("Xi was less than left range")
                    xRanges[0][0] = xi
                elif xi > prevRange[0][1] and xi <= prevRange[1][0]:
                    #print("Xi was in right range")
                    xRanges[1][0] = xi
                    if xf >= prevRange[1][1]:
                        #print("Xf was bigger than right range")
                        xRanges[1][1] = xf
                    prevRange = [xRanges[0].copy(), xRanges[1].copy()]
                if xf < prevRange[0][0] - 1:
                    #print("Xf was less than left range")
                    xRanges[0][1] = xf
                    xRanges[1] = prevRange[0]
                elif xf <= prevRange[0][1]:
                    xRanges[0][1] = prevRange[0][1]
                elif xf > prevRange[0][1] and xf < prevRange[1][0]:
                    #print("Xf was bigger than left range and less than right range")
                    xRanges[0][1] = xf
                elif xf <= prevRange[1][1] and xi <= prevRange[0][1]:
                    #print("Xf was in right range range")
                    xRanges[0][1] = prevRange[1][1]
                    xRanges[1] = [targetDimension, 0]
                elif xf > prevRange[1][1]:
                    #print("Xf was bigger than right range")
                    xRanges[0][1] = xf
                    xRanges[1] = [targetDimension, 0]

                # if xi < xRanges[0][0]: xRanges[0][0] = xi
                # if xf < xRanges[1][0] and xf > xRanges[0][1]: xRanges[0][1] = xf
                # if xi > xRanges[0][1] and xi < xRanges[1][0]: xRanges[1][0] = xi
                # if xf > xRanges[1][0] and xf < xRanges[1][1]: xRanges[1][0] = xf
                # if xi < xRanges[1][0] and xi > xRanges[0][1]: xRanges[0][1] = xi
                # if xf > xRanges[1][1]: xRanges[1][1] = xf
                # print(f"X Range for row {row}: {xRanges}")

with open("advent15.txt","r") as f:
    lines = f.readlines()
    positions = [[],[]]
    minX =  420
    maxX = -420
    for l in range(0, len(lines)):
        data = []
        for part in lines[l].split(":"):
            x = int(part[part.find("x=")+2:part.find(",")])
            y = int(part[part.find("y=")+2:])
            if x <= minX: minX = x
            if x >= maxX: maxX = x
            data.append([x,y])
        positions[0].append(data[0])
        positions[1].append(data[1])
    print(f"Max: {maxX} Min: {minX}")
    print(f"Target Row Length: {maxX-minX+1}")

    for i in range(0, len(positions[0])-1):
        minIndex = i
        for j in range(i, len(positions[0])):
            if positions[0][j][0] < positions[0][minIndex][0]: 
                minIndex = j
                # print(f"Found a min at {j}")
        positions[0][i], positions[0][minIndex], positions[1][i], positions[1][minIndex] = positions[0][minIndex], positions[0][i], positions[1][minIndex], positions[1][i]
     
    # print(f"Sensors: {positions[0]}")
    # print(f"Beacons: {positions[1]}")
    targetRowNum = 2000000
    posInRange = 0
    #xRanges = [[maxX, minX]]
    # for i in range(0, len(positions[0])):
    #     posInRange += numNonBeacons(targetRowNum, i)
    # print(f"Positions that cannot contain a beacon in row {targetRowNum}: {posInRange}")
    targetDimension = 4000000
    xRanges = [[targetDimension,0],[targetDimension,0]]
    distressSignal = [-1,-1]
    for row in range(0, targetDimension+1):
        setRowXRanges(row)
        print(f"Row: {row}")
        if xRanges[0][0] > 0: distressSignal[0] = 0
        if xRanges[0][1] < targetDimension and xRanges[1][1] == 0: distressSignal[0] = targetDimension
        if xRanges[0][1] + 1 < xRanges[1][0]: distressSignal[0] = xRanges[0][1] + 1
        if distressSignal[0] >= 0:
            distressSignal[1] = row
            print(f"Tuning frequency of possible distress signal: {(distressSignal[0]*4000000)+distressSignal[1]}")
            break
        xRanges = [[targetDimension,0],[targetDimension,0]]
    f.close()