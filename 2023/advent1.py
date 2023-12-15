sum = 0
f = open("2023/advent1.txt", "r")
for f in f:
    nums = [int(x) for x in f if x.isdigit()]
    sum += (nums[0]*10) + nums[-1]
print(sum)