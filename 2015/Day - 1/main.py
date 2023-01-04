with open('input.txt', 'r') as file:
    data = file.read() #setting input to data

floor = 0 #counting floor on which santa is 
firstTime = None #checking if this is the first time at the basement - "-1"
i = 0

for char in data:
    i += 1
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
    if floor == -1 and firstTime == None: #simple logic to avoid repeting the "firstTime"
        firstTime = i 

#Printing answers
print(f"Part 1 - The result is: {floor}")
print(f"Part 2 - The result is: {firstTime}")
