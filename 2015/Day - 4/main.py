from hashlib import md5

with open("input.txt", "r") as file:
    input = file.read() #getting input


def Part1(): #Solution to Part 1
    i = 0
    result = md5(input.encode()).hexdigest()
    while not result.startswith("00000"):
        i+=1
        key = input + str(i)
        result = md5(key.encode("ascii")).hexdigest()
    return i

def Part2(): #Solution to Part 2
    i = 0
    result = md5(input.encode()).hexdigest()
    while not result.startswith("000000"):
        i+=1
        key = input + str(i)
        result = md5(key.encode("ascii")).hexdigest()
    return i

#Printing answers
print(f"Part 1 - The result is: {Part1()}")
print(f"Part 2 - The result is: {Part2()}")