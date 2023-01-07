with open("input.txt", "r") as file:
    data = file.read().split("\n") #setting input to data

def ContainsThreeVowels(input, vowels): #checking if string contains at least 3 vowels
    vowels = vowels
    i = 0
    for vowel in vowels:
        for char in input:
            if vowel in char:
                i+=1
            if i >= 3:
                return True
    return False

def ContainsAtLeastOneDoubleLetterRow(input): #checking if string contains at least one letter that appears twice in a row
    for i in range(len(input)-1):
        if input[i] == input[i+1]:
            return True
    return False

def ContainsPair(input): #checking if string contains pair like "xjtextxj" 
    for i in range(len(input)-1):
            pair = input[i] + input[i+1]
            if input.count(pair) >= 2:
                return True
    return False

def SameLetterBetweenAnother(input): #checking if string contains 2 same letters with another letter between like "xzx"
    for i in range(len(input)-2):
        if input[i] == input[i+2]:
            return True
    return False


def Part1(): #Solution to Part 1
    niceStringCounter = 0
    notAllowedStrings = ["ab", "cd", "pq", "xy"]
    vowels = ["a", "e", "i", "o", "u"]
    for input in data:
        if not any(bad in input for bad in notAllowedStrings): #Checking if input don't contains not allowed strings
            if ContainsThreeVowels(input, vowels):
                if ContainsAtLeastOneDoubleLetterRow(input):
                    niceStringCounter += 1
    return niceStringCounter

def Part2(): #Solution to Part 2
    niceStringCounter = 0
    for input in data:
        if ContainsPair(input):
            if SameLetterBetweenAnother(input):
                niceStringCounter += 1
    return niceStringCounter
            


#Printing answers
print(f"Part 1 - The result is: {Part1()}")
print(f"Part 2 - The result is: {Part2()}")