with open("advent1.txt","r") as f:
    lines = f.readlines()
    arr = [0]
    i = 0
    for l in lines:
        if(l != "\n"):
            arr[i] += int(l)
        else:
            arr.append(0)
            i += 1
        
    maxArr = [0,0,0,0,0]
    for x in arr:
        for i in range(0,3):
            if x > maxArr[i]:
                maxArr[i+2] = maxArr[i+1]
                maxArr[i+1] = maxArr[i]
                maxArr[i] = x
                break
    print(maxArr[0] + maxArr[1] + maxArr[2])
    f.close()