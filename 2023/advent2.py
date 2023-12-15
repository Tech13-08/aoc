# Part 1
# sum = 0
# f = open("2023/advent2.txt", "r")
# for f in f:
#     game = [x.split(", ") for x in f.split(":")[1][1:].split(";")]
#     id = int(f.split(":")[0][f.split(":")[0].find(" "):])
#     for items in game:
#         r,g,b = 0,0,0
#         for i in items:
#             if i.find(" b")>0:
#                 b += int(i[0:i.find(" b")])
#             elif i.find(" r")>0:
#                 r += int(i[0:i.find(" r")])
#             elif i.find(" g")>0:
#                 g += int(i[0:i.find(" g")])
#         if (r > 12 or g > 13 or b > 14): 
#             id = 0
#             break
#     sum += id

# print(sum)

# Part 2
sum = 0
f = open("2023/advent2.txt", "r")
for f in f:
    game = [x.split(", ") for x in f.split(":")[1][1:].split(";")]
    r,g,b = 0,0,0
    for items in game:
        for i in items:
            if i.find(" b")>0:
                b = max(b, int(i[0:i.find(" b")]))
            elif i.find(" r")>0:
                r = max(r, int(i[0:i.find(" r")]))
            elif i.find(" g")>0:
                g = max(g, int(i[0:i.find(" g")]))
    sum += (r*b)*g

print(sum)