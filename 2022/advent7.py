def setDir(curr, prevDirs = []):
    #print(f"Curr: {curr} Prev: {prevDirs}")
    for l in lines:
        contents = l.split()
        if(contents[0] == "$"):
            if (contents[1] == "cd"):
                if(contents[2] == ".."):
                    #print("CD to Prev")
                    curr = prevDirs.pop()
                if(contents[2] in curr):
                    #print(f"CD to {contents[2]}")
                    #print(f"Curr: {curr}")
                    if curr not in prevDirs:
                        prevDirs.append(curr)
                    curr = curr[contents[2]]
            else:
                continue
        elif (contents[0] == "dir"):
            curr.update([(contents[1], {})])
            dirs.append(curr[contents[1]])
            #print(f"Added dir {contents[1]}")
        else:
            curr.update([(contents[1], int(contents[0]))])
            #print(f"Added file {contents[1]} with size {contents[0]}")

def dirSize(dir):
    size = 0
    for key in dir:
        if (type(dir[key]) is int):
            size += dir[key]
        else:
            size += dirSize(dir[key])
    return size

with open("advent7.txt","r") as f:
    lines = f.readlines()
    dirs = [{"/":{}}]
    setDir(dirs[0])
    #print(dirs)
    listSizes = []
    for dir in dirs:
        listSizes.append(dirSize(dir))
    minSizeNeeded = listSizes[0] - 40000000
    minSizeAvailable = listSizes[0]
    for size in listSizes:
        if size >= minSizeNeeded and size <= minSizeAvailable:
            minSizeAvailable = size
    print(f"Smallest directory available to delete: {minSizeAvailable}")
    f.close()