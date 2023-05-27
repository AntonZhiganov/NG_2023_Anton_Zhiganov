import json
     
def save_library (library) :
    """
    Save book in library
    """
    with open ('library.txt', 'w') as f :
        json.dump(library, f)

def delete_Book (library) :
    """  
    Delete book from library   
    """  
    name = input("Enter the name of the book you want to delete : ")
    name = name 
    if name in library :  
        del library[name]
        print("The book has been delete!")
        save_library(library)  
    else :
        print("The book was not deleted because it was not found!")
    
def add_Book(library) :
    """
    Add book in library
    """
    while True :
        key = input("Enter the name of the book you want to add : ")
        nested_dic = {}
        name = input("Enter book title : ")
        author = input("Enter the author's full name : ")
        pages = input("Enter number of pages : ")
        genre = input("Enter the genre of the book : ")
        cover = input("Enter book cover : ")
        nested_dic ['name'] = name
        nested_dic ['author'] = author
        nested_dic ['pages'] = pages
        nested_dic ['genre'] = genre
        nested_dic ['cover'] = cover
        library[key] = nested_dic
        print("Your book has been added! ")
        while True :
            exit = input("Do you want to add another book? (yes/no)")
            if exit == "no" :
                return library
            elif exit == "yes" :
                break
            else :
                print("Enter yes or no!")
                continue
                
def lookToBook(library) :
    """
    View all books added by the user
    """
    if not library :
        print("Library not found! First add a book!!")
    else :
        print("Looking for a library\n")
        
        for key, book in library.items() :
            print(f"{key} : {book}")
       
def edit_Book(library) :
    """
    Change any Parameter in any workbook
    """
    if not library :
        print("Library not found! First add a book!!")
    else :
        name = input("Enter the title of the book you want to edit : ") 
        if name in library :
            book = library[name]
            print(f"Current details for {name}: {book}")
            field = input("What value do you want to edit? (title, author, pages, genre, cover):")
            if field in book :
                newValue = input(f"Enter new value for {field}: ")
                book[field] = newValue
                library[name] = book
                save_library(library)
                print(f"{field} has been apdated for {name}") 
            else :
                print(f"{field} is not to valid field for {name}") 
        else :
            print(f"{name} is not faund in the library")
                
try:
    with open('library.txt', 'r') as f :
        library = json.load(f)
        
except FileNotFoundError :
    library = {}

while True :
    
    #Menu
    
    menu = input("Enter 1 to add a book, 2 to delete a book, 3 to save and exit, 4 to wiev your books, 5 to edit book information : ")
    if menu == "1" :
        add_Book(library) 
    elif menu == "2" :
        delete_Book(library)
    elif  menu == "3" :
        save_library(library)
        print("Changes saved!")
        break
    elif menu == "4" :
        lookToBook(library)
    elif menu == "5" :
        edit_Book(library)
    else :
        print("Please enter 1, 2, 4 or 5! ")