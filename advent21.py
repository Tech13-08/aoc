def findMonkey(monkey):
    for l in lines:
        if l.split(":")[0] == monkey:
            if len(l.split(":")[1]) > 4:
                value1 = l.split(":")[1][1:5]
                value2 = (l.split(":")[1][8:-1] if "\n" in l.split(":")[1] else l.split(":")[1][8:])
                #print(f"V1: {value1} V2: {value2}")
                if " + " in l.split(":")[1]:
                    return int(findMonkey(value1)) + int(findMonkey(value2))
                elif " - " in l.split(":")[1]:
                    return int(findMonkey(value1))- int(findMonkey(value2))
                elif " * " in l.split(":")[1]:
                    return int(findMonkey(value1)) * int(findMonkey(value2))
                elif " / " in l.split(":")[1]:
                    return int(findMonkey(value1)) / int(findMonkey(value2))
            return int(l.split(":")[1])
    return 0

def isHumn(monkey):
    if monkey == "humn": return True
    for l in lines:
        if l.split(":")[0] == monkey:
            if len(l.split(":")[1]) > 4:
                value1 = l.split(":")[1][1:5]
                value2 = (l.split(":")[1][8:-1] if "\n" in l.split(":")[1] else l.split(":")[1][8:])
                #print(f"V1: {value1} V2: {value2}")
                if value1 == "humn" or value2 == "humn":
                    return True
                else:
                    return isHumn(value1) != isHumn(value2)
            else:
                return False
    return False

def findHumn(monkey, val = 0):
    for l in lines:
        if l.split(":")[0] == monkey:
            if len(l.split(":")[1]) > 4:
                value1 = l.split(":")[1][1:5]
                value2 = (l.split(":")[1][8:-1] if "\n" in l.split(":")[1] else l.split(":")[1][8:])
                #print(f"V1: {value1} V2: {value2}")
                numMonkey = 0
                humnMonkey = ""
                if isHumn(value1):
                    numMonkey = findMonkey(value2)
                    humnMonkey = value1
                else:
                    numMonkey = findMonkey(value1)
                    humnMonkey = value2
                if monkey == "root":
                    return int(findHumn(humnMonkey, numMonkey))
                if " + " in l.split(":")[1]:
                    numMonkey = val - numMonkey
                elif " - " in l.split(":")[1]:
                    numMonkey = val + numMonkey if humnMonkey == value1 else numMonkey - val
                elif " * " in l.split(":")[1]:
                    numMonkey = val / numMonkey
                elif " / " in l.split(":")[1]:
                    numMonkey = val * numMonkey if humnMonkey == value1 else numMonkey / val
                return int(findHumn(humnMonkey, numMonkey)) if humnMonkey != "humn" else numMonkey
    return 0

with open("advent21.txt","r") as f:
    lines = f.readlines()
    # Part 1 ----
    # print(findMonkey("root"))
    # Part 2 ----
    print(f"Humn Value: {findHumn('root')}")
    f.close()