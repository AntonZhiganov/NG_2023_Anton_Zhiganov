num_lists = int(input("Enter the number of lists: "))     # User enter the number of lists

lists = [[] for _ in range(num_lists)]                    # Create a list with lists

# For each list, the user enters elements until he enters stop

for number in range(num_lists):
    while True:
        user_input = input(f"Enter elements for list {number+1}, enter 'stop' to exit: ") 
        if user_input.lower() == "stop":
            break
        lists[number].append(user_input)

for lst in lists:
    print(list(set(lst)))     #Show lists