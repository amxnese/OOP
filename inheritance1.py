class Food():
    def __init__(self,name):
        self.name = name
        print(f"{self.name} is created from base method")
    def eat(self):
        print("eat method from base class")
class Apple(Food):
    def __init__(self,name):
        super().__init__(name)
food1 = Food("pizza")
apple1 = Apple("strawbery")
food1.eat()
apple1.eat()