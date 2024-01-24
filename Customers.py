def cust_id():
    # set an id for the customer
    with open("customers_file.csv") as f:
        last_line = f.readlines()[-1]
        if last_line[0].isdigit():
            return int(last_line[0])+1
        else:
            return int("1")


class Customers:
    def __init__(self,  name, city, age):
        self.__name = name
        self.__city = city
        self.__age = age
        self.__id = cust_id()

    @property
    def name(self):
        return self.__name

    @property
    def city(self):
        return self.__city

    @property
    def age(self):
        return self.__age

    @property
    def id(self):
        return self.__id

    def __str__(self):
        lst = [str(self.__id), self.__name, self.__city, self.__age]
        st = ",".join(lst)
        return st
