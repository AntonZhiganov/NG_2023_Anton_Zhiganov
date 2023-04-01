my_Flo = []
my_Int = []
my_Str = []

while True :
    myFloList = input("Enter float elements, enter 'stop' to exit :")
    if myFloList.lower() == "stop" :
        break
    my_Flo.append(float(myFloList))
    
while True :
    myIntList = input("Enter int elements, enter 'stop' to exit :")
    if myIntList.lower() == "stop" :
        break
    my_Int.append(int(myIntList))
            
while True :
    myStrList = input("Enter str elements, enter 'stop' to exit :")
    if myStrList.lower() == "stop" :
        break
    my_Str.append(str(myStrList))
    
    print(list(set(my_Flo)))
    print(list(set(my_Int)))
    print(list(set(my_Str)))