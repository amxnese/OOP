from abc import ABCMeta,abstractmethod
class person(metaclass=ABCMeta):
    def imp_method(self):
        return f"exists in {__class__.__name__}"
    def unimp_method(self):
        return f"exists in {__class__.__name__}"
class man(person):
    def unimp_method(self):
        return f"exists in class {__class__.__name__}"
person1 = person()
man1 = man()
print(person1.unimp_method())
print(person1.imp_method())
print(man1.unimp_method())
print(man1.imp_method())