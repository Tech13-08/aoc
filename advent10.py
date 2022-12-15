def updateSignalStrengths():
    if(len(cycles) == start or (len(cycles) - start) % increment == 0):
        #print(f"Cycle {len(cycles)} * X: {cycles[len(cycles)-1]}")
        signalStrengths.append(len(cycles)*cycles[len(cycles)-1])

with open("advent10.txt","r") as f:
    # Part 1 ------------
    lines = f.readlines()
    start = 20
    increment = 40
    cycles = []
    x = 1
    signalStrengths = []
    for l in lines:
        content = l.split()
        if content[0] == "addx":
            cycles.append(x)
            updateSignalStrengths()
            cycles.append(x)
            updateSignalStrengths()
            x += int(content[1])
        else:
            cycles.append(x)
            updateSignalStrengths()
    print(f"The signal strength sum starting from cycle {start} and then every {increment} cycles is {sum(signalStrengths)}")

    # Part 2 ----------
    crt = []
    dimensions = [6, 40]
    sprite = [0,0,0]
    pos = 0
    for i in range(0, dimensions[0]):
        crt.append([])
        pos = 0
        for j in range(0, dimensions[1]):
            sprite = [cycles[(i*40)+j]-1, cycles[(i*40)+j], cycles[(i*40)+j]+1]
            #print(f"Pos: {pos} Sprite: {sprite}")
            if pos in sprite:
                crt[i].append("#")
            else:
                crt[i].append(".")
            pos += 1
        print("".join(crt[i]))
    
    
        