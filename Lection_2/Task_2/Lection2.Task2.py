quantity = input("Enter Quantity elements: ")  #The user enters the length of the list
elements = input("Enter" + " " + str(quantity) + " " + "elements: ") #User enters list items

my_list = elements.split() #With variable elements we make a list

uniqueList = (set(my_list)) #We create a list identical to ours only without repetitions using the function set

print(uniqueList)