from Menu_Functions import *
while True:
    print_menu()
    action = input("Choose an action ")
    valid_act(action)

    if action == "1":
        print("Add a new customer")
        add_customer()

    if action == "2":
        print("Add a new book")
        add_book()

    if action == "3":
        print("Loan a book")
        loan_book()

    if action == "4":
        print("Return a book")
        return_a_book()

    if action == "5":
        print("Display all books")
        display_all_books()

    if action == "6":
        print("Display all customers")
        display_all_customers()

    if action == "7":
        print("Display all loans")
        display_all_loans()

    if action == "8":
        print("Display late loans")
        display_late_loans()

    if action == "9":
        find_book_by_name()

    if action == "10":
        find_customer_by_name()

    if action == "11":
        print("Remove book")
        remove_a_book()

    if action == "12":
        print("Remove customer")
        remove_a_customer()

    if action == "13":
        break
