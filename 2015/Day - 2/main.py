with open('input.txt', 'r') as file:
    data = file.read().split("\n") #setting input to data

# setting an auxiliary variable
totalSqFeet = 0 
totalFeetRb = 0

for i in data:
    l, w, h = i.split("x")
    l, w, h = int(l), int(w), int(h)
    dimensionsList = [l, w, h]
    #PART 1
    tempResult = 2*l*w + 2*w*h + 2*h*l + sorted(dimensionsList)[0]*sorted(dimensionsList)[1]
    totalSqFeet = totalSqFeet + tempResult #summing all square of feet
    #PART 2
    ribbon = l*w*h + sorted(dimensionsList)[0]*2 + sorted(dimensionsList)[1]*2
    totalFeetRb = totalFeetRb + ribbon #summing all feet of ribbon

#Printing answers
print(f"Part 1 - The result is: {totalSqFeet}")
print(f"Part 2 - The result is: {totalFeetRb}")