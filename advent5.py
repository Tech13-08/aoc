from itertools import islice

with open("advent5.txt","r") as f:
    lines = f.readlines()
    stacks = []
    count = 0
    for l in lines:
        if(l[1] != "1"):
            for i in range(0, len(l)-3,4):
                if(len(stacks) < (i//4)+1):
                    stacks.append([])
                stacks[i//4].append(l[i+1])
            count += 1
        else:
            count += 2
            for stack in stacks:
                stack.reverse()
                while(" " in stack): stack.remove(" ")
            break

    for l in islice(lines, count, None):
        content = l.split()
        amount = int(content[1])
        prevStack = int(content[3])
        newStack = int(content[5])
        while(amount > 0):
            crate = stacks[prevStack-1].pop(-amount)
            stacks[newStack-1].append(crate)
            amount -= 1

    topCrates = ""
    for stack in stacks:
        if(stack):
            topCrates += stack.pop()    
        else:
            topCrates += " " 
    print(topCrates)
    f.close()