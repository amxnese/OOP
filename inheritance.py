from abc import ABCMeta, abstractmethod
class Programming(metaclass=ABCMeta):
    @abstractmethod
    def has_oop(self):
        pass
class Python(Programming):
    def has_oop(self):
        return "yes"
class Pascal(Programming):
    def has_oop(self):
        return "no"
class Java(Programming):
    def has_oop(self):
        return "yes"
one = Programming()
two = Python()
three = Pascal()
four = Java()
print(one.has_oop())
print(two.has_oop())
print(three.has_oop())
print(four.has_oop())