import math

x = int  (input("Enter x: "))
y = int  (input("Enter y: "))

print("1 - (+)")
print("2 - (-)")
print("3 - (*)")
print("4 - (:)")
print("5 - (exponentiation)")
print("6 - (Square root)")

z = int (input("What do you want to do with numbers: " ))

print("===========================================")

if z == 1 :
    print("result of addition: " + (str(x + y)))
if z == 2 :
    print("subtraction result: " + (str(x - y)))
if z == 3 :
    print("result of multiplication: " + (str(x * y)))
if z == 4 :
    print("result of division: " + (str(x / y)))
if z == 5 :
    print("result of exponentiation: " + (str(x ** y)))
if z == 6 :
    print("What number do you want to extract the square root of? ")
    print("Enter 1 if you want to take the square root of x ")
    print("Enter 2 if you want to take the square root of y ")
    
d = int (input("Do you want to take the square root of x or y?: "))

if d == 1 :
    print("The result of extracting the root from the number" + (str(x)) + "is: " + (str(x ** (0.5))))
if d == 2 :
    print("The result of extracting the root from the number" + (str(y)) + "is: " + (str(y ** (0.5))))