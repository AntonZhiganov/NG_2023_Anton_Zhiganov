print("a - First element, b - second element, c - third element")

a = float (input("enter a (a can't be 0): "))
b = float (input("enter b : "))
c = float (input("enter c : "))

if a == 0 :
    print(" Error - a can't be 0")
else :
    d = float (b * b) - (4 * a * c)
    
if d < 0 : 
    print("There are no roots in this equation because d < 0!")
else :
    x1 = float (-b + (d ** (0.5))) / (2 * a)
    x2 = float (-b - (d ** (0.5))) / (2 * a)


if (x1 != 0 and d >= 0) :
    print("The first root of your equation : " + str(x1))
else :
    print("There is no first root of your equation!")
if (x2 != 0 and d >= 0) :
    print("The second root of your equation : " + str(x2))
else :
    print("There is no second root of your equation!")
  
    
