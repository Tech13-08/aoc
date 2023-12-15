with open("advent3.txt","r") as f:
    lines = f.readlines()
    total = 0
    for i in range(0,len(lines)-2,3):
        #print(i)
        first = lines[i]
        second = lines[i+1]
        third = lines[i+2]
        found = False
        for i in list(first.strip()):
            if(not found):
                for j in list(second.strip()):
                    if i == j and not found:
                        for n in list(third.strip()):
                            if i == n:
                                score = ord(i) - 96
                                if score < 0:
                                    score += 58
                                #print(f'{i}: {score}')
                                total += score
                                found = True
                                break
        
    print(total)
    f.close()