quantity = input("Enter Quantity elements: ")  #The user enters the length of the list
elements = input("Enter" + " " + str(quantity) + " " + "elements: ") #User enters list items

my_list = elements.split() #With variable elements we make a list

dictionary = {} #Announce dictionary

#Checking the number of repetitions

for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i] == my_list[j]:
             if my_list[i] not in dictionary:
                 dictionary[my_list[i]] = 2
             else:
                  dictionary[my_list[i]] += 1
                  
#output the number of repetitions for each element that is repeated
                  
for key, value in dictionary.items():
    print(f"{key} repeats {value} time(s)")