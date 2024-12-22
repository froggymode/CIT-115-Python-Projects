# objective: create a program that computes the avg of 4 test scores and
# determines a letter grade. Also, add option to drop the lowest grade and
# average the remaining 3 test grades. Include a name prompt, store as variable.
# prompt user for 4 test scores, only whole numbers accepted- int

# 1. prompt the person's name
name = input("Hi there! Please enter your name: ")
print(f"Great! Thank you for choosing my grade analyzer, {name}. Now, let us begin!")
# 2. prompt the user for their 4 test scores. only whole numbers accepted, so use int instead of float
nFirst = int(input("Please enter your first test score: "))
nSecond = int(input("Please enter your second test score: "))
nThird = int(input("Please enter your third test score: "))
nFourth = int (input("Please enter your fourth test score: "))
if nFirst <0:
    print("Test scores must be greater than 0.")
    exit()
if nSecond <0:
    print("Test scores must be greater than 0.")
    exit()
if nThird <0:
    print("Test scores must be greater than 0.")
    exit()
if nFourth <0:
    print("Test scores must be greater than 0.")
    exit()
nAverage = float(f"{(nFirst + nSecond + nThird + nFourth) / 4}")
# 3. ask the user if they'd like the lowest grade to be dropped, only Y or N are valid answers. then calculate.
sDropLowest = input("Would you like to drop the lowest grade before calculating your average? ")
if sDropLowest == 'Y':
    if nFirst < nSecond and nFirst < nThird and nFirst < nFourth:
        nLowest = nFirst
        nAverage = float(f"{(nSecond + nThird + nFourth) / 3}")
    elif nSecond < nFirst and nSecond < nThird and nSecond < nFourth:
        nLowest = nSecond
        nAverage = float(f"{(nFirst + nThird + nFourth) / 3}")
    elif nThird < nFirst and nThird < nSecond and nThird < nFourth:
        nLowest = nThird
        nAverage = float(f"{(nFirst + nSecond + nFourth) / 3}")
    elif nFourth < nFirst and nFourth < nSecond and nFourth < nThird:
        nLowest = nFourth
        nAverage = float(f"{(nFirst + nSecond + nThird) / 3}")

#4. outputs
print(f"Student Name: {name}")
print(f"Test 1: {nFirst}")
print(f"Test 2: {nSecond}")
print(f"Test 3: {nThird}")
print(f"Test 4: {nFourth}")
print(f"Lowest grade dropped Y or N? {sDropLowest}")
# 5. ensure the user has entered a valid input for grade drop
if sDropLowest != 'Y' and sDropLowest != 'N':
    print("Please enter Y or N to drop the lowest grade.")
    exit()
# 6. determine lowest grade in case the user decides they want it to be dropped
print(f"{name}, your test average is: " +format(nAverage, '.1f'))
# 7. determine letter grade equivalents
sLetter = ''
if nAverage >= 97.0:
    sLetter = 'A+'
elif nAverage >= 94.0 and nAverage <= 96.9:
    sLetter = 'A'
elif nAverage >= 90.0 and nAverage <= 93.9:
    sLetter = 'A-'
elif nAverage >= 87.0 and nAverage <= 89.9:
    sLetter = 'B+'
elif nAverage >= 84.0 and nAverage <= 86.9:
    sLetter = 'B'
elif nAverage >= 80.0 and nAverage <= 83.9:
    sLetter = 'B-'
elif nAverage >= 77.0 and nAverage <= 79.9:
    sLetter = 'C+'
elif nAverage >= 74.0 and nAverage <= 76.9:
    sLetter = 'C'
elif nAverage >= 70.0 and nAverage <= 73.9:
    sLetter = 'C-'
elif nAverage >= 67.0 and nAverage <= 69.9:
    sLetter = 'D+'
elif nAverage >= 64.0 and nAverage <= 66.9:
    sLetter = 'D'
elif nAverage >= 60.0 and nAverage <= 63.9:
    sLetter = 'D-'
elif nAverage <= 59.9:
    sLetter = 'F'
# 8. more outputs now that letter grade is determined
print(f"{name}, the letter grade equivalent is: {sLetter}")



