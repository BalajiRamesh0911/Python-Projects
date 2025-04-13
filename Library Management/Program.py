# This is a simple console-based Library Management System in Python.
# It uses lists and dictionaries to manage book data.

# The library will store book entries in a list.
# Each book will be represented as a dictionary with keys: title, author, available.

library = []

# Function to display the main menu to the user
def show_menu():
    print("\n--- Library Menu ---")
    print("1. Add Book")       # Option to add a new book
    print("2. View Books")     # Option to display all books
    print("3. Borrow Book")    # Option to borrow a book
    print("4. Return Book")    # Option to return a borrowed book
    print("5. Exit")           # Option to exit the application

# Function to add a new book to the library
def add_book():
    # Ask the user for book details
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    
    # Create a dictionary for the book and mark it as available
    book = {
        "title": title,
        "author": author,
        "available": True  # New books are available by default
    }
    
    # Add the book to the library list
    library.append(book)
    print(f"Book '{title}' by {author} added to the library.")

# Function to display all books in the library
def view_books():
    if not library:
        # If library is empty
        print("No books in the library.")
        return

    print("\nAvailable Books:")
    for index, book in enumerate(library):
        # Show availability status
        status = "✅ Available" if book["available"] else "❌ Borrowed"
        # Print book details with numbering
        print(f"{index + 1}. {book['title']} by {book['author']} [{status}]")

# Function to borrow a book
def borrow_book():
    view_books()  # Show list of books
    if library:
        try:
            # Ask the user to enter the book number to borrow
            choice = int(input("Enter the book number to borrow: "))
            
            # Check if the number is within the valid range
            if 1 <= choice <= len(library):
                book = library[choice - 1]  # Get the selected book
                if book["available"]:
                    book["available"] = False  # Mark as borrowed
                    print(f"You have borrowed '{book['title']}'.")
                else:
                    print("Sorry, this book is already borrowed.")
            else:
                print("Invalid book number.")
        except ValueError:
            print("Please enter a valid number.")  # Handle invalid (non-integer) input

# Function to return a borrowed book
def return_book():
    view_books()  # Show current list of books
    if library:
        try:
            # Ask the user to enter the book number to return
            choice = int(input("Enter the book number to return: "))
            
            # Check if the choice is valid
            if 1 <= choice <= len(library):
                book = library[choice - 1]
                if not book["available"]:
                    book["available"] = True  # Mark the book as available again
                    print(f"You have returned '{book['title']}'.")
                else:
                    print("This book was not borrowed.")
            else:
                print("Invalid book number.")
        except ValueError:
            print("Please enter a valid number.")

# Main loop of the application
# This loop keeps the program running until the user chooses to exit
while True:
    show_menu()  # Display the main menu
    option = input("Choose an option (1-5): ")  # Get user's menu choice

    # Match user input to the correct function
    if option == "1":
        add_book()
    elif option == "2":
        view_books()
    elif option == "3":
        borrow_book()
    elif option == "4":
        return_book()
    elif option == "5":
        print("Exiting Library System. Goodbye!")  # Exit message
        break  # Break the loop to end the program
    else:
        print("Invalid option. Please try again.")  # Handle wrong input
