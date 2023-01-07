import numpy as np

with open("input.txt", "r") as file:
    data = file.read().split("\n") #setting input to data


def Part1(): #Solution to Part 1
    grid = np.full((1000, 1000), 0)
    for instruction in data:
        words = instruction.split()
        x1,y1 = map(int, words[-3].split(","))
        x2,y2 = map(int, words[-1].split(","))

        if instruction.startswith("turn on"):
            grid[x1:x2+1, y1:y2+1] = 1
        elif instruction.startswith("turn off"):
            grid[x1:x2+1, y1:y2+1] = 0
        elif instruction.startswith("toggle"):
            grid[x1:x2+1, y1:y2+1] = 1 - grid[x1:x2+1, y1:y2+1]
    return grid.sum()

def Part2(): #Solution to part 2
    gridBrightness = np.full((1000, 1000), 0)
    for instruction in data:
        words = instruction.split()
        x1,y1 = map(int, words[-3].split(","))
        x2,y2 = map(int, words[-1].split(","))
        if instruction.startswith("turn on"):
            gridBrightness[x1:x2+1, y1:y2+1] += 1
        elif instruction.startswith("turn off"):
            gridBrightness[x1:x2+1, y1:y2+1] -= 1
            gridBrightness[x1:x2+1, y1:y2+1] = gridBrightness[x1:x2+1, y1:y2+1].clip(min=0)
        elif instruction.startswith("toggle"):
            gridBrightness[x1:x2+1, y1:y2+1] += 2
    return gridBrightness.sum()



#Printing answers
print(f"Part 1 - The result is: {Part1()}")
print(f"Part 2 - The result is: {Part2()}")