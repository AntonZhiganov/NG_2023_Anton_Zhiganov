
quantity = int(input("Enter Quantity elements: "))  # The user enters the length of the list
elements = input(f"Enter {quantity} elements: ")  # User enters list items

my_list = elements.split()  # Convert input to list

dictionary = {}  # Initialize dictionary

# Count repetitions
for element in my_list:
    if element not in dictionary:
        dictionary[element] = 1
    else:
        dictionary[element] += 1

# Output the number of repetitions for each element that is repeated
for key, value in dictionary.items():
    if value > 1:
        print(f"{key} repeats {value} time(s)")
