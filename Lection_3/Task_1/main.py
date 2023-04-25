import math

def addition() :
    """
    Adding two numbers entered by the user
    """ 
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print(float(x + y))

def subtraction() :
    """
    Subtraction of two numbers entered by the user
    """
    print("The second is subtracted from the first!")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print(float(x - y))
    
def multiplication() :
    """
    Multiplication of two numbers entered by the user
    """
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print(float(x * y))

def division() :
    """
    Division of two numbers entered by the user
    """
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    if y == 0 :
        print("Can't divide by 0!")
    else :
        print("The first number is divisible by the second!")
        print(float(x / y))

def exponentiation() :
    """
    Raising a number to a power
    """
    print("The first value is raised to the power of the second value!")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print(float(x ** y))

def squareNumber () :
    """
    Squaring a number
    """
    x = float(input("Enter the number you want to square: "))
    print(float(x ** 2)) 

def squareRoot() :
    """
    The square root of the number entered by the user
    """
    x = float(input("Enter the number you want to take the square root of: "))
    if x < 0 :
        print("The number must not be negative!")  
    else :
        print(float(x ** 0.5))

while True :
    print("1 - (+)")
    print("2 - (-)")
    print("3 - (*)")
    print("4 - (:)")
    print("5 - (exponentiation)")
    print("6 - (square number)")
    print("7 - (Square root)")
    menu = input("What do you want to do with numbers: ")
    if menu == "1" :
        addition()
    elif menu == "2" :
        subtraction()
    elif menu == "3" :
        multiplication()
    elif menu == "4" :
        division()
    elif menu == "5" :
        exponentiation()
    elif menu == "6" :
        squareNumber()
    elif menu == "7" :
        squareRoot()
    else :
        print("You entered an invalid number, please enter 1, 2, 3, 4, 5, 6 or 7! ")
        
        
