from Books import Books
from Customers import Customers
from Loans import Loans
from datetime import date, timedelta


def valid_book_id(book_id_book):
    # check if the book id is in the books file
    with open("books_file.csv") as book_file_book:
        book_file_book.readline()
        for book_line_book in book_file_book:
            book_file_book_arr = book_line_book.split(",")
            if book_file_book_arr[0] == str(book_id_book):
                return True
    return False


def in_loan(id_book_id):
    # check if the book is in loan(in the loan file)
    with open("loans_file.csv") as a_loan_file:
        a_loan_file.readline()
        for loan_line_loan in a_loan_file:
            a_loan_file_arr = loan_line_loan.split(",")
            if a_loan_file_arr[1] == str(id_book_id):
                return True
    return False


def valid_cust_id(cust_id_cust):
    # check if the customer id is in the customers file
    with open("customers_file.csv") as cust_file_cust:
        cust_file_cust.readline()
        for cust_line_cust in cust_file_cust:
            cust_file_cust_arr = cust_line_cust.split(",")
            if cust_file_cust_arr[0] == str(cust_id_cust):
                return True
    return False


def valid_year(year: str):
    if year.isdigit():
        return True
    else:
        return False


def valid_book_type(type1):
    # check the book type is one of the three types
    if type1 == "1" or type1 == "2" or type1 == "3":
        return True
    else:
        return False


def valid_act(act: str):
    # check that user had a valid action from the menu
    if act.isdigit():
        if 0 < int(act) < 14:
            return True
        else:
            print("please choose a number from 1 to 13")
    else:
        print("please choose a number from 1 to 13")


def display_book(a_books_line):
    # create a dictionary to display a book
    books_dict = {}
    books_arr = a_books_line.split(',')
    books_dict["id"] = books_arr[0]
    books_dict["name"] = books_arr[1]
    books_dict["author"] = books_arr[2]
    books_dict["year"] = books_arr[3]
    return books_dict


def add_book():
    # add a book to the books file
    name_book = input("Book name: ")
    book_author = input("Book author: ")
    book_year = input("Book year published: ")
    while not valid_year(book_year):
        book_year = input("year published has to be a number, please type a year number ")
    book_type = input("Book type: ")
    while not valid_book_type(book_type):
        book_type = input("Book type has to be 1, 2, or 3. try again please ")
    if valid_year(book_year) and valid_book_type(book_type):
        book = Books(name=name_book, author=book_author, year=book_year, book_type=book_type)
        with open("books_file.csv", "a") as books_file:
            books_file.write(book.__str__() + "\n")


def add_customer():
    # add a customer to the customers file
    cust_name = input("Customer name: ")
    cust_city = input("Customer city: ")
    cust_age = input("Customer age: ")
    while not cust_age.isdigit():
        print("customer age must be a number")
        cust_age = input("Customer age: ")
    if cust_age.isdigit():
        customer = (Customers(name=cust_name, city=cust_city, age=cust_age))
        with open("customers_file.csv", "a") as cust_file_cust:
            cust_file_cust.write(customer.__str__() + "\n")


def loan_book():
    # add a book to the loans file
    loan_book_id = input("What is the id of the book you wish to loan? ")
    while in_loan(loan_book_id):
        print("the book is already at loan")
        loan_book_id = input("What is the id of the book you wish to loan? ")
    while not valid_book_id(loan_book_id):
        print("book id does not exist")
        loan_book_id = input("What is the id of the book you wish to loan? ")
    loan_cust_id = input("What is the id of the customer who wish to loan the book? ")
    while not valid_cust_id(loan_cust_id):
        print("customer id does not exist")
        loan_cust_id = input("What is the id of the customer who wish to loan the book? ")
    with open("books_file.csv") as books_file_books:
        books_file_books.readline()
        for books_line_books in books_file_books:
            books_arr1 = books_line_books.split(',')
            books_arr1[4] = books_arr1[4].rstrip()
            if books_arr1[4] == "1":
                return_date_set = date.today() + timedelta(10)
            elif books_arr1[4] == "2":
                return_date_set = date.today() + timedelta(5)
            elif books_arr1[4] == "3":
                return_date_set = date.today() + timedelta(2)
        loan_date_set = str(date.today())
        loan = Loans(customer_id=loan_cust_id, book_id=loan_book_id, loan_date=loan_date_set,
                     return_date=return_date_set)
        with open("loans_file.csv", "a") as loan_file:
            loan_file.write(loan.__str__() + "\n")


def return_a_book():
    # remove a book from the loans file, the book is no longer in loan
    return_book = input("What is the id of the book you wish to return?")
    while not in_loan(return_book):
        print("This book id is not in loan")
        return_book = input("What is the id of the book you wish to return?")
    if in_loan(return_book):
        with open("loans_file.csv") as loans_file:
            loans_lines = loans_file.readlines()
        with open("loans_file.csv", "w") as file_loans:
            for loan_line in loans_lines:
                loans_lines_arr = loan_line.split(",")
                if loans_lines_arr[1] != return_book:
                    file_loans.write(loan_line)


def display_all_books():
    with open("books_file.csv") as f_books:
        f_books.readline()
        for f_books_line in f_books:
            print(display_book(f_books_line))


def display_all_customers():
    with open("customers_file.csv") as f_cust:
        f_cust.readline()
        for f_cust_line in f_cust:
            print(display_cust(f_cust_line))


def display_all_loans():
    with open("loans_file.csv") as f_loans:
        f_loans.readline()
        for line_loan in f_loans:
            print(display_loan(line_loan))


def display_late_loans():
    # check if the loan date is today or if it is already passed
    with open("loans_file.csv") as loan_file_loan:
        late_loans_list = []
        loan_file_loan.readline()
        for a_loan in loan_file_loan:
            loan_arr = a_loan.split(",")
            if loan_arr[3].rstrip() <= str(date.today()):
                late_loans_list.append(f'book id: {loan_arr[0]}')
    if len(late_loans_list) > 0:
        print(late_loans_list)
    else:
        print("no late loans currently")


def find_book_by_name():
    search_ans_book = input("Find a book by name: ")
    with open("books_file.csv") as book_file:
        book_search_lst = []
        for book_file_line in book_file:
            book_file_arr = book_file_line.split(",")
            if book_file_arr[1] == search_ans_book:
                book_search_lst.append(display_book(book_file_line))
        if len(book_search_lst) == 0:
            print("book was not found")
        else:
            print("these are the books were found:")
            for book_name in book_search_lst:
                print(book_name)


def find_customer_by_name():
    search_ans = input("Find a customer by name: ")
    with open("customers_file.csv") as cust_file:
        cust_search_lst = []
        for cust_file_line in cust_file:
            cust_file_arr = cust_file_line.split(",")
            if cust_file_arr[1] == search_ans:
                cust_search_lst.append(display_cust(cust_file_line))
        if len(cust_search_lst) == 0:
            print("customer was not found")
        else:
            print("these are the customers were found:")
            for cust in cust_search_lst:
                print(cust)


def remove_a_book():
    # remove a book from the books file
    remove_book = input("What is the id of the book you wish to remove?")
    with open("books_file.csv") as file_books:
        a_book_lines = file_books.readlines()
    with open("books_file.csv", "w") as f_books_f:
        for a_book_line in a_book_lines:
            lines_arr = a_book_line.split(",")
            if lines_arr[0] != remove_book:
                f_books_f.write(a_book_line)


def remove_a_customer():
    # remove a customer from the customers file
    remove_cust = input("What is the id of the customer you wish to remove?")
    with open("customers_file.csv") as customer_file:
        a_cust_lines = customer_file.readlines()
    with open("customers_file.csv", "w") as f_customers:
        for a_cust_line in a_cust_lines:
            a_cust_lines_arr = a_cust_line.split(",")
            if a_cust_lines_arr[0] != remove_cust:
                f_customers.write(a_cust_line)


def display_cust(a_line):
    # create a dictionary to display a customer
    cust_dict = {}
    cust_arr = a_line.split(',')
    cust_dict["id"] = cust_arr[0]
    cust_dict["name"] = cust_arr[1]
    cust_dict["city"] = cust_arr[2]
    cust_dict["age"] = cust_arr[3].rstrip()
    return cust_dict


def display_loan(l_line_loan):
    # create a dictionary to display a loan
    loan_dict = {}
    loan_arr_loan = l_line_loan.split(',')
    loan_dict["customer_id"] = loan_arr_loan[0]
    loan_dict["book_id"] = loan_arr_loan[1]
    loan_dict["loan_date"] = loan_arr_loan[2]
    loan_dict["return_date"] = loan_arr_loan[3].rstrip()
    return loan_dict


def print_menu():
    print("1. Add a new customer\n"
          "2. Add a new book\n"
          "3. Loan a book\n"
          "4. Return a book\n"
          "5. Display all books\n"
          "6. Display all customers\n"
          "7. Display all loans\n"
          "8. Display late loans\n"
          "9. Find book by name\n"
          "10. Find customer by name\n"
          "11. Remove book\n"
          "12. Remove customer\n"
          "13. Exit\n")

