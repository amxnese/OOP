class person():
    def __init__(self,firstname,lastname):
        self.__firstname = firstname
        self.__lastname = lastname
    @property
    def firstname(self):
        return self.__firstname
    @firstname.setter
    def firstname(self,new):
        self.__firstname = new
person1 = person("amine","sedrata")
print(person1.firstname)
person1.firstname = "main"
print(person1.firstname)