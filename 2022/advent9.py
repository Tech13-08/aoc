def updateRopeKnot(knot):
    xDiff = rope[knot-1][0] - rope[knot][0]
    yDiff = rope[knot-1][1] - rope[knot][1]
    # print("Before:")
    # print(f"Prev Knot {knot-1}: {rope[knot-1]} Knot {knot}: {rope[knot]}")
    # print(f"xDiff: {xDiff} yDiff: {yDiff}")
    if abs(xDiff) > 1 or abs(yDiff) > 1:
        if abs(xDiff) > abs(yDiff):
            rope[knot][0] += xDiff - int((xDiff/abs(xDiff)))
            rope[knot][1] = rope[knot-1][1]
        elif abs(xDiff) < abs(yDiff):
            rope[knot][1] += yDiff - int((yDiff/abs(yDiff)))
            rope[knot][0] = rope[knot-1][0]
        else:
            rope[knot][0] += xDiff - int((xDiff/abs(xDiff)))
            rope[knot][1] += yDiff - int((yDiff/abs(yDiff)))
    # print("\nAfter:")
    # print(f"Prev Knot {knot-1}: {rope[knot-1]} Knot {knot}: {rope[knot]}\n")
    if rope[len(rope)-1] not in positions:
        positions.append(rope[len(rope)-1].copy())

with open("advent9.txt","r") as f:
    lines = f.readlines()
    rope = []
    ropeLength = 10
    for i in range(0,ropeLength):
        rope.append([0,0])
    positions = [[0,0]]
    for l in lines:
        direction = l.split()[0]
        iterations = l.split()[1]
        for i in range(0, int(iterations)):
            if direction == "R":
                rope[0][0] += 1
            if direction == "U":
                rope[0][1] += 1
            if direction == "L":
                rope[0][0] -= 1
            if direction == "D":
                rope[0][1] -= 1
            for knot in range(1,len(rope)):
                updateRopeKnot(knot)
        #print(rope)
    print(f"Number of unique positions: {len(positions)}")
    f.close()