def save_library(library):
    with open('library.txt', 'w') as f:
        for key, book in library.items():
            f.write(f"{key}: {book}\n")

def delete_book(library):
    name = input("Enter the name of the book you want to delete: ")
    if name in library:
        del library[name]
        print("The book has been deleted!")
        save_library(library)
    else:
        print("The book was not deleted because it was not found!")

def add_book(library):
    while True:
        key = input("Enter the name of the book you want to add: ")
        nested_dict = {}
        name = input("Enter book title: ")
        author = input("Enter the author's full name: ")
        pages = input("Enter number of pages: ")
        genre = input("Enter the genre of the book: ")
        cover = input("Enter book cover: ")
        nested_dict['name'] = name
        nested_dict['author'] = author
        nested_dict['pages'] = pages
        nested_dict['genre'] = genre
        nested_dict['cover'] = cover
        library[key] = nested_dict
        print("Your book has been added!")
        while True:
            exit_choice = input("Do you want to add another book? (yes/no)")
            if exit_choice == "no":
                return
            elif exit_choice == "yes":
                break
            else:
                print("Enter yes or no!")
                continue

def look_up_book(library):
    if not library:
        print("Library not found! First add a book!!")
    else:
        print("Looking up the library\n")
        for key, book in library.items():
            print(f"{key}: {book}")

def edit_book(library):
    if not library:
        print("Library not found! First add a book!!")
    else:
        name = input("Enter the title of the book you want to edit: ")
        if name in library:
            book = library[name]
            print(f"Current details for {name}: {book}")
            field = input("What value do you want to edit? (title, author, pages, genre, cover): ")
            if field in book:
                new_value = input(f"Enter new value for {field}: ")
                book[field] = new_value
                save_library(library)
                print(f"{field} has been updated for {name}")
            else:
                print(f"{field} is not a valid field for {name}")
        else:
            print(f"{name} is not found in the library")

library = {}

while True:
    menu = input("Enter 1 to add a book, 2 to delete a book, 3 to save and exit, 4 to view your books, 5 to edit book information: ")
    if menu == "1":
        add_book(library)
    elif menu == "2":
        delete_book(library)
    elif menu == "3":
        save_library(library)
        print("Changes saved!")
        break
    elif menu == "4":
        look_up_book(library)
    elif menu == "5":
        edit_book(library)
    else:
        print("Please enter 1, 2, 4, or 5!")