class user():
    @staticmethod
    def say_hello():
        return f"welcome to this fucked up class"
    not_allowed_names = ["hell", "shit", "punk"]
    users_num = 0 
    @classmethod
    def show_users_num(cls):
        return f"we have {cls.users_num} users in our system"
    def getName(self):
        return f"{self.name}"
    def setName(self, newName):
        self.name = newName
    def __init__(self, first_name,age, job, sex):
        self.name = first_name
        self.age = age
        self.job = job
        self.sex = sex
        user.users_num += 1
    def fullInfo(self):
        if self.name in user.not_allowed_names:
            raise ValueError("name not allowed")
        else:
            return f"{self.name}, {self.age}yo, {self.job}"
    def say_hi(self):
        if self.sex == "male":
            return f"hello mr {self.name}"
        else:
            return f"hello mrs {self.name}"
user1 = user("amine",20,"male")
user1.show_users_num()
print(user.say_hello())
print(user.users_num)
user1 = user("steve",50,"doctor", "male")
user2 = user("samy",40,"teacher", "male")
user3 = user("carl",30,"programmer", "male")
user4 = user("sarah",22,"model", "female")
print(user.users_num)
print(user.show_users_num())
print(f"{user1.name} is {user1.age} he is a {user1.job}")
print(f"{user2.name} is {user2.age} he is a {user2.job}")
print(f"{user3.name} is {user3.age} he is a {user3.job}")

