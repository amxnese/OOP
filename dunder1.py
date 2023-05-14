class Man():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __add__(self,other):
        length1 = len(self.name)//2
        length2 = len(other.name)//2
        names = f"names combined are {self.name[:length1]+other.name[length2:]}"
        ages = f"ages combined are {self.age + other.age}"
        return f"{names} and {ages}"
man1 = Man("micheal",22)
man2 = Man("trevor",23)
print(man1+man2)