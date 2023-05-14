class user():
    def __init__(self, first_name,last_name,age, job):
        self.__first = first_name
        self.__last = last_name
        self.__age = age
        self.__job = job
    @property
    def fullname(self):
        return f"{self.__first} {self.__last}"
    @fullname.setter
    def fullname(self, new):
        self.__first,self.__last = new.split(" ")
user1 = user("steve","harvey",50,"doctor")
user2 = user("samy","zain",40,"teacher")
user3 = user("carl","jun",30,"programmer")
user1.fullname = "steve jobs"
print(user1.fullname)
print(user1._user__name)
print(user1.getName())
user1.setName("taliska")
print(user1.getName())
print(user1.describe())