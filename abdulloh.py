import datetime

class Supermarket:
    __branchs_count = 0
    __products = list()
    def __init__(self, name, address) -> None:
        Supermarket.__branchs_count += 1
        self.__name = name
        self.__address = address

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    @classmethod
    def get_branchs_count(cls):
        return cls.__branchs_count

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def is_open():
        now = datetime.datetime.now()
        now = datetime.datetime.strftime(now, "%H:%M:%S")
        if int(now[0:2]) >= 8 and int(now[0:2]) <= 22:
            return "Supermarket is open!"
        else:
            return "Supermarket is close!"

    @classmethod
    def enter_products(cls):
        count = int(input("Nechta mahsulot kiritmoqchisiz: "))
        for i in range(count):
            cls.__products.append(input(f"{i + 1}-mahsulotni kiriting: "))

    @classmethod
    def search_product(cls):
        product = input("Qaysi mahsulot kerak: ")
        for i in cls.__products:
            if i == product:
                return f"{product} supermarketimizda mavjud"
        return f"{product} supermarketimizda mavjud emas"

    def __str__(self) -> str:
        return f"{self.__name} supermarketi {self.__address} da joylashgan."