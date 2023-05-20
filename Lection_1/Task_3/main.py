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

result = match action : 
case 1 :                                          #The program reads the user's choice, 
    "result of addition: " + (str(firstNum + secondNum))          #If the user enters a different number, then we inform him about it.
case 2 :
    "subtraction result: " + (str(firstNum - secondNum))
case 3 :
    "result of multiplication: " + (str(firstNum * secondNum))
case 4 :
    "result of division: " + (str(firstNum / secondNum))
case 5 :
    "result of exponentiation: " + (str(math.pow(firstNum, secondNum)))
case 6 :
    "What number do you want to extract the square root of? "
    "Enter 1 if you want to take the square root of first number "
    "Enter 2 if you want to take the square root of second number "
    
    choice = int (input("Do you want to take the square root of first number or secons number?: "))

root = match choice :
    case 1 :
        "The result of extracting the root from the number" + (str(firstNum)) + "is: " + (str(math.sqrt(firstNum)))
    case 2 :
        "The result of extracting the root from the number" + (str(secondNum)) + "is: " + (str(math.sqrt(secondNum)))
        
case _ :
    "Enter numbers from 1 to 6!"