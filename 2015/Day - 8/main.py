with open("input.txt", "r") as file:
    data = file.read().splitlines() #getting data

def Part1(): #Solution to Part 1
    return sum(len(s) - len(eval(s)) for s in data)


def Part2(): #Solution to Part 2
    return sum(s.count("\\") + s.count('"') + 2 for s in data)

#Printing answers
print(f"Part 1 - The result is: {Part1()}")
print(f"Part 2 - The result is: {Part2()}")