from abc import ABCMeta, abstractmethod
class name(metaclass=ABCMeta):
    def get_first(self):
        return f"first name is amine"
    def get_middle(self):
        return f"middle name is mohamed"
    @abstractmethod
    def get_last(self):
        pass
class full_name(name):
    def get_last(self):
        return f"last name is sedrata"
one = full_name()
print(one.get_first(),one.get_middle(),one.get_last())