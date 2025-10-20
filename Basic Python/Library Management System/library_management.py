library = []
def show_menu():
    print("\n Library Management System")
    print("1. Add New Book")
    print("2. Delete Book")
    print("3. Update Book")
    print("4. Issue Book to User")
    print("5. Return Book")
    print("6. Search Book by Title or Author")
    print("7. List Available Books")
    print("8. List Issued Books")
    print("9. Exit")

def add_books():
    print("\n add book")
    title=input("enter the title:")
    author=input("enter the author:")
    issue=False
    book={
        "title":title,
        "author":author,
        "issue":False
    }
    library.append(book)

def delete_book():
    print("\n delete boook")
    title=input("enter the title:")
    for book in library:
        if book["title"].lower==title.lower():
            library.remove(book)
            print("\n book deleted")
            return
        else:
            print("book not found")


def update_book():
    print("\nUPDATE BOOK")
    title = input("Enter book title to update: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            new_title = input("Enter new title: ").strip()
            new_author = input("Enter new author: ").strip()
            book["title"] = new_title
            book["author"] = new_author
            print("Book updated.")
            return
    print("Book not found.")



def issue_book():
    print("\n issue book")
    title=input("enter title to issue:").strip()
    for book in library:
        if book["title"].lower==title.lower():
            if not book["issued"]:
               book["issued"]=True
               print("Book Issued")
               return
            else:
                print("book already issued")
                return
    print("book not found")



def return_book():
     print("\n Return Book")
     title = input("Enter title to return: ").strip()
     for book in library:
          if book["title"].lower==title.lower():
              if book["issued"]:
                  book["issued"]=False
                  print("Book returned")
                  return
              else:
                  print("Book was Issued")
                  return
     print("book not found")



def search_book():
    print("\n Search Book")
    keyword = input("Enter title or author: ").strip().lower()
    found = False
    for book in library:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            print(book)
            found = True
    if not found:
        print(" No matching book found.")




def list_available_books():
    print("\n Available Books:")
    found = False
    for book in library:
        if not book["issued"]:
            print(book)
            found = True
    if not found:
        print("No available books.")



def list_issued_books():
    print("\n Issued Books:")
    found = False
    for book in library:
        if book["issued"]:
            print(book)
            found = True
    if not found:
        print("No issued books.")

    

while True:
    show_menu()
    choice = input("Enter your choice (1-9): ").strip()

    if choice == "1":
        add_books()
    elif choice == "2":
        delete_book()
    elif choice == "3":
        update_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        search_book()
    elif choice == "7":
        list_available_books()
    elif choice == "8":
        list_issued_books()
    elif choice == "9":
        print(" Exiting Library System.")
        break
    else:
        print("Invalid choice. Try again.")
    
 
