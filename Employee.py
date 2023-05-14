class Employee():
    def __init__(self,first,last):
        self.first = first
        self.last = last
    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    @fullname.setter
    def fullname(self, new_name:str):
        self.first ,self.last = new_name.split(" ")
    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        print("Name deleted")
employee1 = Employee("john","clinton")

employee1.fullname = "john wick"
del employee1.fullname
print(employee1.fullname)
print(employee1.email)
print(employee1.fullname)