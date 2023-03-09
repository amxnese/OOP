import csv
class Item:
    pay_rate = 80
    all = []
    users_num = 0
    def __init__(self,name,price,quantity):
        assert price >= 0, f"{price} should be greater than zero"
        assert quantity >= 0, f"{quantity} should be greater than zero"
        self.__price = price
        self.quantity = quantity
        self.name = name
        Item.all.append(self)
        Item.users_num += 1

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,value):
        self.__price = value

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"
    @classmethod
    def show_num_users(cls):
        print("number of users is {}".format(cls.users_num))
    @staticmethod
    def from_percent(percent):
        return percent/100
    def apply_discount(self):
        self.price *= self.from_percent(self.pay_rate)
    def calculate_total_price(self):
        return self.price * self.quantity
    def instanciate_from_csv():
        with open("oop.csv","r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
            for item in items:
                Item(
                    name=item.get('name'),
                    price=float(item.get('price')),
                    quantity=float(item.get('quantity'))
                )
class phone(Item):
    def __init__(self,name,price,quantity,year):
        super().__init__(name,price,quantity)
        self.year = year
    def __add__(self,other):
        if isinstance(other,phone):
            return self.price + other.price
        else:
            return NotImplemented