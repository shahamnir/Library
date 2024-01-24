def book_id():
    # set an id for a bok
    with open("books_file.csv") as f:
        last_line = f.readlines()[-1]
        if last_line[0].isdigit():
            return int(last_line[0])+1
        else:
            return int("1")


class Books:
    def __init__(self, name, author, year, book_type):
        self.__name = name
        self.__author = author
        self.__year = year
        self.__book_type = book_type
        self.__id = book_id()

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    @property
    def year(self):
        return self.__year

    @property
    def book_type(self):
        return self.__book_type

    @property
    def id(self):
        return self.__id

    def __str__(self):
        lst = [str(self.__id), self.__name, self.__author, self.__year, self.__book_type]
        st = ",".join(lst)
        return st
