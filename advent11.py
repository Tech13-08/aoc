class Monkey:
    def __init__(self):
        self.items = self.operation = []
        self.test = self.trueMonkey = self.falseMonkey = self.numInspections = 0

    def __str__(self):
        return f"{self.items}"
    
    def inspect(self):
        for i in range(0, len(self.items)):
            self.numInspections += 1
            self.items[i] = int(self.items[i]) % allTestProd
            #print(f"Monkey inspects an item with a worry level of {self.items[i]}.")
            newWorry = 0
            operationNum = 0
            if self.operation[1] == "old":
                operationNum = int(self.items[i])
            else:
                operationNum = int(self.operation[1])
            
            if self.operation[0] == "*":
                newWorry = int(self.items[i])*operationNum
            elif self.operation[0] == "+":
                newWorry = int(self.items[i])+operationNum
            self.items[i] = (newWorry)//relief
            #print(f"Worry level is now {self.items[i]}")

            if self.items[i] % self.test == 0:
                #print(f"Current worry level is divisible by {self.test}.")
                #print(f"Item is thrown to Monkey {self.trueMonkey}")
                monkeys[self.trueMonkey].items.append(self.items[i])
            else:
                #print(f"Current worry level is not divisible by {self.test}.")
                #print(f"Item is thrown to Monkey {self.falseMonkey}")
                monkeys[self.falseMonkey].items.append(self.items[i])
        self.items.clear()

with open("advent11.txt","r") as f:
    lines = f.readlines()
    monkeys = []
    rounds = 10000
    relief = 1
    for i in range(1, len(lines)-4, 7):
        monkeys.append(Monkey())
        monkeys[(i-1)//7].items = lines[i].split(":")[1][:-1].split(",")
        monkeys[(i-1)//7].operation = (lines[i+1].split(":")[1][11:-1]).split()
        monkeys[(i-1)//7].test = int(lines[i+2].split(":")[1].split()[2])
        monkeys[(i-1)//7].trueMonkey = int(lines[i+3].split(":")[1].split()[3])
        monkeys[(i-1)//7].falseMonkey = int(lines[i+4].split(":")[1].split()[3])
    
    allTestProd = 1
    for m in range(0, len(monkeys)):
        allTestProd *= monkeys[m].test

    for x in range(0, rounds):
        #print(f"Round {x+1}:\n")
        for m in range(0, len(monkeys)):
            monkeys[m].inspect()
        # for n in range(0, len(monkeys)):
        #     print(f"\tMonkey {n}: {monkeys[n]}")
    topMonkeys = [0,0,0]
    for n in range(0, len(monkeys)):
        #print(f"\tMonkey {n}: Inspected {monkeys[n].numInspections} times")
        for t in range(0, len(topMonkeys)-1):
            if monkeys[n].numInspections >= topMonkeys[t]:
                topMonkeys[t+1] = topMonkeys[t]
                topMonkeys[t] = monkeys[n].numInspections
                break
    print(f"Monkey Business: {topMonkeys[0]*topMonkeys[1]}")
    

    