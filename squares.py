# Squares of Numbers Based on User Input

count = int(input("How many numbers do you want to enter? "))

i = 0
while i < count:
    num = int(input("Enter number " + str(i + 1) + ": "))
    square = num * num
    print("Square of " + str(num) + " = " + str(square))
    i += 1
