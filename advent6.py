with open("advent6.txt","r") as f:
    line = f.read()
    foundRepeat = False
    numChar = 14 # Number of distinct characters
    for i in range(0, len(line)-(numChar-1)):
        for m in range(i, i+(numChar-1)):
            if not foundRepeat:
                for n in range(m+1, i+numChar):
                    if line[m] == line[n]:
                        foundRepeat = True
        if not foundRepeat:
            print(i+numChar)
            break
        else:
            foundRepeat = False
    f.close()