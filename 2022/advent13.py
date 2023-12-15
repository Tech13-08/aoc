import math

def inOrder(p1, p2):
    for i in range(0, min(len(p1),len(p2))):
        left = p1[i]
        right = p2[i]
        #print(f"Left: {left} Right: {right}")
        if type(left) == type(right) == int:
            #print("Both ints")
            if left < right: return 1
            elif left > right: return 0
            else: continue
        elif type(right) == int:
            #print("Right is int")
            right = [int(right)]
        elif type(left) == int:
            #print("Left is int")
            left = [int(left)]

        order = inOrder(left, right)
        if order != -1:
            return order
        
    if len(p1) < len(p2): return 1
    elif len(p1) > len(p2): return 0
    return -1


def parsePacket(packet):
    #print(f"Before: {packet} Length: {len(packet)}")
    i = 0
    while i < len(packet):
        if len(packet[i]) > 0:
            #print(f"First Char: {packet[i][0]}")
            if(packet[i][0] == "["):
                tempString = ",".join(packet[i:])
                openBrackets = 0
                closedBracketIndex = 0
                for j in range(1, len(tempString)):
                    if tempString[j] == "[":
                        openBrackets+=1
                    elif tempString[j] == "]":
                        if openBrackets == 0:
                            closedBracketIndex = j
                            break
                        else:
                            openBrackets -= 1
                packet[i] = (tempString[1:closedBracketIndex]).split(",")
                if len(packet[i]) > 1:
                    del packet[i+1:len(packet[i])+i]
                    #print(f"Deleted from index {i+1} to {len(packet[i])+i-1}")
                parsePacket(packet[i])
            else:
                packet[i] = int(packet[i])
        else:
            del packet[i]
        i+=1

with open("advent13.txt","r") as f:
    lines = f.readlines()
    sumIndices = 0
    packets = [[[2]],[[6]]]
    for l in range(0, len(lines)-1, 3):
        packet1 = (lines[l][1:-2].split(","))
        parsePacket(packet1)
        #print(f"Packet1: {packet1} Length: {len(packet1)}")
        packet2 = (lines[l+1][1:(lambda : -2 if (l+2 != len(lines)) else -1)()].split(","))
        parsePacket(packet2)
        #print(f"Packet2: {packet2} Length: {len(packet2)}")
        #print(f"In order: {inOrder(packet1, packet2)}")
        packets.append(packet1)
        packets.append(packet2)
        # if inOrder(packet1, packet2): # Part 1
        #     sumIndices += math.ceil((l+1)/3.0)
        #     #print(f"Line: {l} Index: {math.ceil((l+1)/3.0)} True")
        # else:
        #     pass
        #     #print(f"Line: {l} Index: {math.ceil((l+1)/3.0)} False")

    for i in range(0, len(packets)-1):
        for j in range(i+1, len(packets)):
            if inOrder(packets[j], packets[i]):
                packets[i], packets[j] = packets[j], packets[i]
    print(f"The decoder key is {(packets.index([[2]])+1) * (packets.index([[6]])+1)}")
    #print(f"Sum of indices that are in order: {sumIndices}")
    f.close()