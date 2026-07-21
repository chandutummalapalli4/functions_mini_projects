##----------- Mini Project 4 -----------##
##------ Library Book Management System ------##

# Function to display header
def display_header():
    print("===================================")
    print("   LIBRARY BOOK MANAGEMENT SYSTEM")
    print("===================================")


# Function to calculate discount
def calculate_discount(price):
    if price >= 1000:
        return price * 0.20
    elif price >= 500:
        return price * 0.10
    else:
        return 0
def book_category(final_price):
    if final_price>=1000:
        return "Premium"
    elif final_price>=500:
        return "Standard"
    else:
        return "Budget"


# Function to display book details
def library_mangement(book_name, author, book_id, price):
    discount = calculate_discount(price)
    final_price = price - discount
    bookcategory=book_category(final_price)

    print("-----------------------------------")
    print("BOOK DETAILS")
    print("-----------------------------------")
    print("Book Name      :", book_name)
    print("Author         :", author)
    print("Book ID        :", book_id)
    print("Original Price : ₹", price)
    print("Discount       : ₹", discount)
    print("Final Price    : ₹", final_price)
    print("Book category  :",bookcategory)
    print()


# Main Program
display_header()

library_mangement(
    book_name="Physics",
    author="Max Planck",
    book_id="21896-1",
    price=3500
)

library_mangement(
    book_name="Chemistry",
    author="Vector K.",
    book_id="216-1/3",
    price=2500
)

library_mangement(
    book_name="Python",
    author="M. K. George",
    book_id="223-6",
    price=4500
)