import match
print("a - First element, b - second element, c - third element")  # Information for user

a = float(input("enter a (a can't be 0): "))
b = float(input("enter b: "))
c = float(input("enter c: "))

result = match(a)
with result as m:
    m.case(a == 0)
    print("Error - a can't be 0")
    m.case()
    d = float(b * b) - (4 * a * c)

if result:
    with result as m:
        m.case(d < 0)
        print("There are no roots in this equation because d < 0!")
        m.case()
        x1 = (-b + (d ** 0.5)) / (2 * a)
        x2 = (-b - (d ** 0.5)) / (2 * a)

        with match(x1, x2) as m2:
            m2.case((x1 != 0 and d >= 0), lambda: print(f"The first root of your equation: {x1}"))
            m2.case()
            print("There is no first root of your equation!")
            m2.case((x2 != 0 and d >= 0), lambda: print(f"The second root of your equation: {x2}"))
            m2.case()
            print("There is no second root of your equation!")