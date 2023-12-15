def move(num):
    initialIndex = copyArray.index(num)
    intNum = 0
    if num[-1] == "_": intNum = int(num.split("_")[0])
    else: intNum = int(num)
    finalIndex = (abs(initialIndex + (intNum*descryptionKey)) % (len(copyArray)-1)) * (1 if intNum>=0 else -1)
    #print(f"{intNum*descryptionKey} | {initialIndex + (intNum*descryptionKey)} | {len(copyArray)-1} | {finalIndex}")
    copyArray.pop(initialIndex)
    copyArray.insert(finalIndex, num)
    #print(f"Num: {intNum} IndexI: {initialIndex} IndexF: {finalIndex}")
    #print(f"Current array: {copyArray}")
    
def findNdigit(n):
    finalIndex = (copyArray.index("0") + n) % len(copyArray)
    #print(f"{n} index: {finalIndex}")
    return 811589153*(int(copyArray[finalIndex].split("_")[0]) if "_" in copyArray[finalIndex] else int(copyArray[finalIndex]))
with open("advent20.txt","r") as f:
    lines = f.readlines()
    orignalArray = []
    for l in lines:
        l = l[:-1] if "\n" in l else l
        while l in orignalArray: l += "_"
        orignalArray.append(l)
    copyArray = orignalArray.copy()
    descryptionKey = int(811589153%((len(copyArray)-1)))
    print(descryptionKey)
    for i in range(0, 10):
        for num in orignalArray:
            move(num)
        print(f"Round {i+1} done")
    groveSum = findNdigit(1000) + findNdigit(2000) + findNdigit(3000)
    print(f"Sum of grove coordinates: {groveSum}")
