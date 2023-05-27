import math

firstNum = int(input("Enter the number 1: "))
secondNum = int(input("Enter the number 2: "))

print("1 - (+)")
print("2 - (-)")
print("3 - (*)")
print("4 - (:)")
print("5 - (exponentiation)")
print("6 - (square root)")

action = int(input("What do you want to do with the numbers: "))

print("===========================================")

if action == 1:
    result = "Addition result: " + str(firstNum + secondNum)
elif action == 2:
    result = "subtraction result: " + str(firstNum - secondNum)
elif action == 3:
    result = "Multiplication result: " + str(firstNum * secondNum)
elif action == 4:
    result = "division result: " + str(firstNum / secondNum)
elif action == 5:
    result = "The result of exponentiation: " + str(math.pow(firstNum, secondNum))
elif action == 6:
    print("What number do you want to take the square root of?")
    print("Enter 1 if you want to take the square root of the first number")
    print("Enter 2 if you want to take the square root of the second number")
    choice = int(input("Choose a number to take the square root: "))

    if choice == 1:
        result = "The result of taking the square root of a number " + str(firstNum) + " equals: " + str(math.sqrt(firstNum))
    elif choice == 2:
        result = "The result of taking the square root of a number " + str(secondNum) + " equals: " + str(math.sqrt(secondNum))
    else:
        result = "Enter a number from 1 to 2!"
else:
    result = "Enter a number from 1 to 6!"

print(result)