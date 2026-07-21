##========================================================##
##              MINI PROJECT 5
##          MOVIE TICKET BOOKING SYSTEM
##========================================================##

# Display Header
def display_header():
    print("=========================================")
    print("     MOVIE TICKET BOOKING SYSTEM")
    print("=========================================")


# Calculate Total Amount
def calculate_total_amount(price, no_of_tickets):
    total_amount = price * no_of_tickets
    return total_amount


# Calculate Discount
def calculate_discount(total_amount):
    if total_amount >= 2000:
        return total_amount * 0.20
    elif total_amount >= 1000:
        return total_amount * 0.10
    else:
        return 0


# Calculate Final Bill
def calculate_final_bill(total_amount, discount):
    return total_amount - discount


# Booking Status
def booking_status(final_bill):
    if final_bill >= 3000:
        return "VIP Booking"
    elif final_bill >= 1000:
        return "Premium Booking"
    else:
        return "Regular Booking"


# Booking Report (Master Function)
def booking_report(name, movie_name, no_of_tickets, price):

    total_amount = calculate_total_amount(price, no_of_tickets)

    discount = calculate_discount(total_amount)

    final_bill = calculate_final_bill(total_amount, discount)

    status = booking_status(final_bill)

    print("=========================================")
    print("           BOOKING REPORT")
    print("=========================================")
    print("Customer Name     :", name)
    print("Movie Name        :", movie_name)
    print("Number of Tickets :", no_of_tickets)
    print("Ticket Price      : ₹", price)
    print("-----------------------------------------")
    print("Total Amount      : ₹", total_amount)
    print("Discount          : ₹", discount)
    print("Final Bill        : ₹", final_bill)
    print("Booking Status    :", status)
    print("=========================================\n")


# Main Program
display_header()

booking_report(
    name="Suresh",
    movie_name="OG",
    no_of_tickets=5,
    price=1000
)

booking_report(
    name="Raju",
    movie_name="Bro",
    no_of_tickets=4,
    price=250
)

booking_report(
    name="Ramesh",
    movie_name="HHVM",
    no_of_tickets=3,
    price=600
)