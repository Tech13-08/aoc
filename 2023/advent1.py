sum = 0
spelledNums = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
f = open("2023/advent1.txt", "r")
for f in f:
    nums = []
    for x in range(0, len(f)):
        if f[x].isdigit():
            nums.append(int(f[x]));
        key = [key for key in spelledNums if f[x:].find(key) == 0]
        if len(key) > 0: nums.append(spelledNums[key[0]])
    
    sum += (nums[0]*10) + nums[-1]
print(sum)