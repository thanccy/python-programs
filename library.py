
# Library Catalogue Management using Text Files

FILE = "library.txt"


# Function to add a new book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    book_id = input("Enter book ID: ")

    with open(FILE, "a") as f:
        f.write(book_id + "," + title + "," + author + "\n")

    print("Book added successfully!")


# Function to display all books
def display_books():
    try:
        with open(FILE, "r") as f:
            books = f.readlines()

            if not books:
                print("No books available.")
            else:
                print("\n--- Library Catalogue ---")
                for book in books:
                    book_id, title, author = book.strip().split(",")
                    print("ID:", book_id,
                          "| Title:", title,
                          "| Author:", author)

    except FileNotFoundError:
        print("Catalogue file does not exist.")


# Function to search books by title
def search_title():
    title = input("Enter title to search: ").lower()
    found = False

    try:
        with open(FILE, "r") as f:
            for book in f:
                book_id, name, author = book.strip().split(",")

                if title in name.lower():
                    print("Book found:", name, "| Author:", author)
                    found = True

        if not found:
            print("Book not found.")

    except FileNotFoundError:
        print("Catalogue file does not exist.")


# Function to search books by author
def search_author():
    author = input("Enter author name to search: ").lower()
    found = False

    try:
        with open(FILE, "r") as f:
            for book in f:
                book_id, title, name = book.strip().split(",")

                if author in name.lower():
                    print("Book found:", title, "| Author:", name)
                    found = True

        if not found:
            print("No books found by this author.")

    except FileNotFoundError:
        print("Catalogue file does not exist.")


# Function to generate reports
def generate_report():
    try:
        with open(FILE, "r") as f:
            books = f.readlines()

        print("Total number of books:", len(books))

        author = input("Enter author name for report: ").lower()
        count = 0

        for book in books:
            book_id, title, name = book.strip().split(",")

            if author == name.lower():
                count += 1

        print("Books by this author:", count)

    except FileNotFoundError:
        print("Catalogue file does not exist.")


# Main menu
while True:
    print("\n===== Library Catalogue =====")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Search by Title")
    print("4. Search by Author")
    print("5. Generate Report")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        search_title()
    elif choice == "4":
        search_author()
    elif choice == "5":
        generate_report()
    elif choice == "6":
        print("Exiting Library Catalogue.")
        break
    else:
        print("Invalid choice. Try again.")
