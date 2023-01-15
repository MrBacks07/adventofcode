import numpy as np #importing numpy only for being able to set 16 bits integers

with open("input.txt", "r") as file:
    data = file.read().strip().split("\n") #setting input to data

def Part1(): #Solution to Part 1
    values = {}         
    def calculate():
        for line in data:
            instruction = line.split(" ")
            if instruction[1] == "->": #setting "a" value to "b"
                a,b = line.split(" -> ")
                if a.isalpha():
                    if a in values:
                        a = int(values[a])
                    else:
                        continue
                values[b] = a
            if instruction[1] == "AND": #bitwise AND
                a,b,c = instruction[0], instruction[2], instruction[4]
                if a in values and b in values:
                    a = int(values[a])
                    b = int(values[b])
                elif a.isnumeric() and b in values:
                    b = int(values[b])
                    a = int(a)
                else:
                    continue
                values[c] = a & b % 65536
            if instruction[1] == "OR": #bitwise OR
                a,b,c = instruction[0], instruction[2], instruction[4]
                if a in values and b in values:
                    a = int(values[a])
                    b = int(values[b])
                else:
                    continue
                values[c] = a % 65536 | b % 65536
            if instruction[1] == "LSHIFT": #bitwise LSHIFT
                a,b,c = instruction[0], instruction[2], instruction[4]
                if a in values:
                    a = int(values[a])
                else:
                    continue
                values[c] = a << int(b)
            if instruction[1] == "RSHIFT": #bitwise RSHIFT
                a,b,c = instruction[0], instruction[2], instruction[4]
                if a in values:
                    a = int(values[a])
                else:
                    continue
                values[c] = a >> int(b) % 65536
            if instruction[0] == "NOT": #bitwise NOT
                a,b = instruction[1], instruction[3]
                if a in values:
                    a = values[a]
                else:
                    continue
                values[b] = ~np.uint16(a) % 65536

    while "a" not in values:
        calculate() #Recalculating to pending moment that "a" is in dictionary values
    return values["a"]



def Part2(): #Solution to Part 2
    values = {}         
    def calculate(signalA=None):
        for i, line in enumerate(data):
            instruction = line.split(" ")
            if instruction[1] == "->": #setting "a" value to "b"
                a,b = line.split(" -> ")
                if b == "b" and signalA is not None:
                    values[b] = signalA
                    continue
                if a.isalpha():
                    if a in values:
                        a = int(values[a])
                    else:
                        continue
                values[b] = a
            if instruction[1] == "AND": #bitwise AND
                a,b,c = instruction[0], instruction[2], instruction[4]
                if a in values and b in values:
                    a = int(values[a])
                    b = int(values[b])
                elif a.isnumeric() and b in values:
                    b = int(values[b])
                    a = int(a)
                else:
                    continue
                values[c] = a & b % 65536
            if instruction[1] == "OR": #bitwise OR
                a,b,c = instruction[0], instruction[2], instruction[4]
                if a in values and b in values:
                    a = int(values[a])
                    b = int(values[b])
                else:
                    continue
                values[c] = a % 65536 | b % 65536
            if instruction[1] == "LSHIFT": #bitwise LSHIFT
                a,b,c = instruction[0], instruction[2], instruction[4]
                if a in values:
                    a = int(values[a])
                else:
                    continue
                values[c] = a << int(b)
            if instruction[1] == "RSHIFT": #bitwise RSHIFT
                a,b,c = instruction[0], instruction[2], instruction[4]
                if a in values:
                    a = int(values[a])
                else:
                    continue
                values[c] = a >> int(b) % 65536
            if instruction[0] == "NOT": #bitwise NOT
                a,b = instruction[1], instruction[3]
                if a in values:
                    a = values[a]
                else:
                    continue
                values[b] = ~np.uint16(a) % 65536

    while "a" not in values:
        calculate() #Recalculating to pending moment that "a" is in dictionary values
    signalA = values['a']
    values = {}
    while "a" not in values:
        calculate(signalA) #Recalculating to pending moment that "a" is in dictionary values | but now setting "b" wire to "a" signal from last calculatings
    return values['a']

#Printing answers
print(f"Part 1 - The result is: {Part1()}")
print(f"Part 2 - The result is: {Part2()}")