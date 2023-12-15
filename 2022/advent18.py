with open("advent18.txt","r") as f:
    lines = f.readlines()
    allX = []
    allY = []
    allZ = []
    surfaceArea = 6
    for l in lines:
        pos = l.split(",")
        pos = [int(pos[0]), int(pos[1]), int(pos[2])]
        index = 0
        #print(f"Number of cubes checked: {len(allX)}")
        while index < len(allX):
            if pos[0] in allX[index:]: 
                index += allX[index:].index(pos[0])
                #print(f"{pos[0]} is in X values")
                if (allY[index] == pos[1] and abs(allZ[index] - pos[2]) == 1) or (allZ[index] == pos[2] and abs(allY[index] - pos[1]) == 1):
                    #print(f"Found match at index {index}, subtracting surfaces...")
                    surfaceArea -= 2
            elif pos[1] in allY[index:]: 
                index += allY[index:].index(pos[1])
                #print(f"{pos[1]} is in Y values")
                if (allX[index] == pos[0] and abs(allZ[index] - pos[2]) == 1) or (allZ[index] == pos[2] and abs(allX[index] - pos[0]) == 1):
                    #print(f"Found match at index {index}, subtracting surfaces...")
                    surfaceArea -= 2
            elif pos[2] in allZ[index:]: 
                index += allZ[index:].index(pos[2])
                #print(f"{pos[2]} is in Z values")
                if (allY[index] == pos[1] and abs(allX[index] - pos[0]) == 1) or (allX[index] == pos[0] and abs(allY[index] - pos[1]) == 1):
                    #print(f"Found match at index {index}, subtracting surfaces...")
                    surfaceArea -= 2
            index += 1
            #print(f"New index: {index}")

        allX.append(pos[0])
        allY.append(pos[1])
        allZ.append(pos[2])
    # for i in range(0, len(allX)):
    #     print(f"X: {allX[i]} Y: {allY[i]} Z: {allZ[i]}")
    print(f"Surface Area: {surfaceArea}")
