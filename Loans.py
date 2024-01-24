class Loans:
    def __init__(self, customer_id, book_id, loan_date, return_date):
        self.__customer_id = customer_id
        self.__book_id = book_id
        self.__loan_date = loan_date
        self.__return_date = return_date

    def __str__(self):
        lst = [str(self.__customer_id), str(self.__book_id),
               str(self.__loan_date), str(self.__return_date)]
        st = ",".join(lst)
        return st
