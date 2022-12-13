with open("advent4.txt","r") as f:
    lines = f.readlines()
    total = 0
    for l in lines:
        ranges = list(l.split(","))
        range1 = list(ranges[0].split("-"))
        range2 = list(ranges[1].split("-"))
        range1[0] , range1[1] = int(range1[0]), int(range1[1])
        range2[0] , range2[1] = int(range2[0]), int(range2[1])
        if((range1[0] <= range2[0] and range1[1] >= range2[0]) or (range1[0] >= range2[0] and range1[0] <= range2[1])):
            total += 1
        
    print(total)
    f.close()