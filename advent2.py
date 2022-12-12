with open("advent2.txt","r") as f:
    lines = f.readlines()
    total = 0
    for l in lines:
        moves = list(l.strip())
        outcome = ord(moves[2]) - 87
        oppMove = ord(moves[0]) - 64
        total += ((outcome-1) *3)
        if(outcome == 3):
            myMove = oppMove+1
            if(myMove>3): myMove=1
            total+=myMove
        elif(outcome == 2):
            total += oppMove
        else:
            myMove = oppMove-1
            if(myMove <1): myMove = 3
            total+=myMove
        
    print(total)
    f.close()