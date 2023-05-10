import math

firstNum = int  (input("Enter first number : "))       #Asking the user to enter 2 numbers
secondNum = int  (input("Enter second number: "))

print("1 - (+)")                #let the user choose an action
print("2 - (-)")
print("3 - (*)")
print("4 - (:)")
print("5 - (exponentiation)")
print("6 - (Square root)")

action = int (input("What do you want to do with numbers: " ))

print("===========================================")  

if action == 1 :                                          #The program reads the user's choice, 
    print("result of addition: " + (str(firstNum + secondNum)))          #If the user enters a different number, then we inform him about it.
elif action == 2 :
    print("subtraction result: " + (str(firstNum - secondNum)))
elif action == 3 :
    print("result of multiplication: " + (str(firstNum * secondNum)))
elif action == 4 :
    print("result of division: " + (str(firstNum / secondNum)))
elif action == 5 :
    print("result of exponentiation: " + (str(math.pow(firstNum, secondNum))))
elif action == 6 :
    print("What number do you want to extract the square root of? ")
    print("Enter 1 if you want to take the square root of first number ")
    print("Enter 2 if you want to take the square root of second number ")
    
    choice = int (input("Do you want to take the square root of first number or secons number?: "))

    if choice == 1 :
        print("The result of extracting the root from the number" + (str(firstNum)) + "is: " + (str(math.sqrt(firstNum))))
    if choice == 2 :
        print("The result of extracting the root from the number" + (str(secondNum)) + "is: " + (str(math.sqrt(secondNum))))
        
else :
    print ("Enter numbers from 1 to 6!")