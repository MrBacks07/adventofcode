with open("input.txt", "r") as file:
    data = file.read() #setting input to data

def update(pos, char): #updating every new position 
    if char == "^":
        return (pos[0], pos[1]+1)
    elif char == "v":
        return (pos[0], pos[1]-1)
    elif char == ">":
        return (pos[0]+1, pos[1])
    elif char == "<":
        return (pos[0]-1, pos[1])

    return pos

def IsVisited(visited, pos): #Checking if santa or robot was on that position
    if pos in visited:
        return True
    else:
        return False

def Part1():
    visited = []
    visited.append((0, 0)) #appending starting position
    pos = (0, 0)
    for char in data:
        pos = update(pos, char)
        if not IsVisited(visited, pos):
            visited.append(pos)

    return len(visited)



def Part2():
    visited = []
    visited.append((0, 0)) #appending starting position
    santaPos = (0, 0)
    robotPos = (0, 0)
    for i, char in enumerate(data):
        if i%2==0: #if current move is for robot or santa
            robotPos = update(robotPos, char)
            if not IsVisited(visited, robotPos):
                visited.append(robotPos)
        else:
            santaPos = update(santaPos, char)
            if not IsVisited(visited, santaPos):
                visited.append(santaPos)
    return len(visited)
            

#Printing answers
print(f"Part 1 - The result is: {Part1()}")
print(f"Part 2 - The result is: {Part2()}")