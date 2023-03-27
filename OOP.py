'''    OBJECT ORIENTED PROGRAMMING    '''

# class member():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def get_name(self):
#         print(f"the name is {}")

# color1 = input("enter a color:  ")
# color2 = input("enter a second color:  ")
# celebrity = input("enter a celebrity name:  ")
# print(f"roses are {color1}\nviolets are {color2}\ni love {celebrity}")

# class Solution(object):
#     def longestValidParentheses(self, s):
#         l1 = []
#         l2 = []
#         for i in s:
#             if i == "(":
#                 l1.append(i)
#             if s[0] == ")":
#                 continue
#         for n in s:
#             if n == ")":
#                 l2.append(n)
#             if s[-1] == "(":
#                 continue
#         return (min(len(l1),len(l2)))*2
# print(Solution.longestValidParentheses(2,")()())"))

# x = 5 if False else 8
# print(x)
# def re(num):
#     return int(num/2)
# print(re(50))

# class Student():
#     def __init__(self,name,age,year,gpa):
#         self.name = name
#         self.age = age
#         self.year = year
#         self.gpa = gpa
#     def student_info(self):
#         print(f"his name is {self.name} ,he's {self.age} years old,he's in {self.year} year, has a gpa of {self.gpa} ")
# std1 = Student("amine",20,"First",4.1)
# std1.student_info()


# class member():
    # def __init__(self):
        # print("a new member has been added")
# member()
# member()
# member()
# print(dir(member))
# member_one = member()
# member_two = member()
# member_three = member()
# print(member_one.__class__)

# import pyfiglet
# import termcolor
# import colorama
# colorama.init()
# print(pyfiglet.figlet_format("amine"))
# print(termcolor.colored(pyfiglet.figlet_format("amine"), "red"))

# class object():
#     def __init__(self):
#         print("hello there i love python")
# object()

# def dec(name):
#     return (f"==({name})==")
# list = ["samy", "danzo", "steve", "coman"]
# x = map(dec,list)
# for line in x:
#     print(line)

# class Member():
#     def __init__(self):
#         self.name = "amine"
#         self.age = 20
#         self.job = "web development"
# member_one = Member()
# member_two = Member()
# member_three = Member()
# print(member_one,member_two,member_three)

# friends = ["amine","samy","kiloa","housam"]
# def dec(name):
#     if name == "amine" or name == "kiloa":
#         return (f"{name} is awesome")
#     else:
#         return (f"{name} is the name")
# precise = map(dec,friends)
# for line in precise:
#     print(line)

# class Car():
#     def __init__(self):
#         self.model = "mustang"
#         self.year = 2022
#         self.color = "red"
# car1 = Car()
# print(car1.__class__)

# class user():
#     @staticmethod
#     def say_hello():
#         return f"welcome to this fucked up class"
#     not_allowed_names = ["hell", "shit", "punk"]
#     users_num = 0 
#     @classmethod
#     def show_users_num(cls):
#         return f"we have {cls.users_num} users in our system"
#     def getName(self):
#         return f"{self.name}"
#     def setName(self, newName):
#         self.name = newName
#     def __init__(self, first_name,age, job, sex):
#         self.name = first_name
#         self.age = age
#         self.job = job
#         self.sex = sex
#         user.users_num += 1
    # def fullInfo(self):
#         if self.name in user.not_allowed_names:
#             raise ValueError("name not allowed")
#         else:
#             return f"{self.name}, {self.age}yo, {self.job}"
#     def say_hi(self):
#         if self.sex == "male":
#             return f"hello mr {self.name}"
#         else:
#             return f"hello mrs {self.name}"
# first_name,age, job, sex
# user1 = user("amine",20,"male")
# user1.show_users_num()
# print(user.say_hello())
# print(user.users_num)
# user1 = user("steve",50,"doctor", "male")
# user2 = user("samy",40,"teacher", "male")
# user3 = user("carl",30,"programmer", "male")
# user4 = user("sarah",22,"model", "female")
# print(user.users_num)
# print(user.show_users_num())
# print(f"{user1.name} is {user1.age} he is a {user1.job}")
# print(f"{user2.name} is {user2.age} he is a {user2.job}")
# print(f"{user3.name} is {user3.age} he is a {user3.job}")

# my_string = "amine"
# print(type(type))
# print(type(my_string))
# print(my_string.__class__)
# # print(dir(my_string))
# print(my_string.upper())
# print(str.upper(my_string))

# class skill():
#     def __init__(self):
#         self.skills = ["html", "python", "css"]
#     def __str__(self):
#         return f"my skills are ==> {self.skills}"
# profile = skill()
# print(profile)

# class Skill:
#     def __init__(self):
#         self.skills = ["css, java, python"]
#     def __str__(self):
#         return f"my skills are {self.skills}"
#     def __len__(self):
#         return len(self.skills)
# print(len(Skill()))
# print(Skill())


# mems = ["amine", 20, True]
# print(f"his name is {mems[0]} he's {mems[1]}, he consider himself as a {mems[2]}")
# for index in mems:
#     print(index)

# name = "amine"
# print("hello {}".format(name))

# class user():
#     def __init__(self, first_name,last_name,age, job):
#         self.__first = first_name
#         self.__last = last_name
#         self.__age = age
#         self.__job = job
#     @property
#     def fullname(self):
#         return f"{self.__first} {self.__last}"
#     @fullname.setter
#     def fullname(self, new):
#         self.__first,self.__last = new.split(" ")
# user1 = user("steve","harvey",50,"doctor")
# user2 = user("samy","zain",40,"teacher")
# user3 = user("carl","jun",30,"programmer")
# user1.fullname = "steve jobs"
# print(user1.fullname)
# print(user1._user__name)
# print(user1.getName())
# user1.setName("taliska")
# print(user1.getName())
# print(user1.describe())
# class person():
#     def __init__(self,name,age,height):
#         self.name = name
#         self.age = age
#         self.height = height
#     def describe(self):
#         return f"his name is {self.name} he's {self.age} he is {self.height}mm tall"
# class man(person):
#     def __init__(self, name, age, height, gender):
#         super().__init__(name,age,height)
#         self.gender = gender
# man1 = man("steve",22,178,"male")
# print(man.describe(man1))
# print(person.describe(man1))
# print(man1.describe())

# class Man():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __add__(self,other):
#         names = f"names combined are {self.name} and {other.name}"
#         ages = f"ages combined are {self.age + other.age}"
#         return f"{names} and {ages}"
# man1 = Man("dre",22)
# man2 = Man("trevor",23)
# print(man1+man2)

# my_string = "sting"
# print(my_string.__class__)
# print(my_string.upper())
# print(str.upper(my_string))

# class Skill:
#     def __init__(self):
#         self.skills = ["css", "java", "python"]
#     def __str__(self):
#         return f"my skills are {self.skills}"
#     def __len__(self):
#         return len(self.skills)
# profile = Skill()
# print(profile)
# print(len(profile))

# class Food():
#     def __init__(self,name):
#         self.name = name
#         print(f"{self.name} is created from base method")
#     def eat(self):
#         print("eat method from base class")
# class Apple(Food):
#     def __init__(self,name):
#         super().__init__(name)
# # food1 = Food("pizza")
# apple1 = Apple("strawbery")
# food1.eat()
# apple1.eat()

# class Animal():
#     # def __init__(self) -> None:
#     def eat(self):
#         print("this animal is eating")
# class Rabbit(Animal):
#     def eat(self):
#         print("this rabbit is eating a corrot")
# rabbit1 = Rabbit()
# rabbit1.eat()

# class A():
#     def do_something():
#         print("From class A")
#         raise NotImplementedError("something went wrong")
# class B(A):
#     def do_something():
#         print("From class B")
# class C(A):
#     pass
# x = B()
# z = C()
# C.do_something()

# class x():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     @property
#     def hello(self):
#         return f"hello {self.name}!!"
# one = x("amine",23)
# print(one.hello)

# from abc import ABCMeta, abstractmethod
# class Programming(metaclass=ABCMeta):
#     @abstractmethod
#     def has_oop(self):
#         pass
# class Python(Programming):
#     def has_oop(self):
#         return "yes"
# class Pascal(Programming):
#     def has_oop(self):
#         return "no"
# class Java(Programming):
#     def has_oop(self):
#         return "yes"
# one = Programming()
# two = Python()
# three = Pascal()
# four = Java()
# print(one.has_oop())
# print(two.has_oop())
# print(three.has_oop())
# print(four.has_oop())

# import pyfiglet
# import termcolor
# import colorama
# colorama.init()
# print(termcolor.colored("amine","red"))
# print(pyfiglet.figlet_format("amine"))
# print(termcolor.colored(pyfiglet.figlet_format("amine"),"yellow"))

# from abc import ABCMeta, abstractmethod
# class name(metaclass=ABCMeta):
#     def get_first(self):
#         return f"first name is amine"
#     def get_middle(self):
#         return f"middle name is mohamed"
#     @abstractmethod
#     def get_last(self):
#         pass
# class full_name(name):
#     def get_last(self):
#         return f"last name is sedrata"
# one = full_name()
# print(one.get_first(),one.get_middle(),one.get_last())


# class Node():
# 	def __init__(self,data):
# 		self.data = data
# 		self.ref = None
# class Linked_list():
#     def __init__(self):
#         self.head = None
#     def length(self):
#         x = 0
#         if self.head == None:
#             return int(0)
#         else:
#             temp = self.head
#             while temp is not None:
#                 temp = temp.ref
#                 x += 1
#             return int(x)
#     def is_empty(self):
#         if self.head == None:
#             return True
#         else:
#             return False
#     def PrintLL(self):
#         if self.head is None:
#             print("linked list is empty")
#         else:
#             while self.head is not None:
#                 print(self.head.data,end="  ==>  ")
#                 self.head = self.head.ref
#         print()
#     def Add_at_Begining(self,data):
#         new_node = Node(data)
#         new_node.ref = self.head
#         self.head = new_node
#     def Add_at_End(self,data):
#         new_node = Node(data)
#         if not Linked_list().is_empty():
#             self.head = new_node
#         else:
#             temp = self.head
#             while temp.ref is not None:
#                 temp = temp.ref
#             temp.ref = new_node
#     def insert(self,data,index):
#         new_node = Node(data)
#         count = 1
#         temp = self.head
#         while temp.ref != None and count < index:
#             temp = temp.ref
#             count += 1
#         else:
#             new_node.ref = temp.ref
#             temp.ref = new_node
#     def Add_to_Empty(self,data):
#         if not Linked_list.is_empty(self):
#             print("linked list is not empty")
#         else:
#             new_node = Node(data)
#             self.head = new_node
#     def Del_at_Begining(self):
#         if Linked_list.is_empty(self):
#             print("linked list is empty")
#         else:
#             temp = self.head
#             self.head = self.head.ref
#             del(temp)
#     def Del_at_End(self):
#         if Linked_list.is_empty(self):
#             print("linked list is empty")
#         elif Linked_list.length(self) == 1:
#             self.head = None
#         else:
#             temp = self.head
#             while temp.ref.ref is not None:
#                 temp = temp.ref
#             temp.ref = None
#     def Del_by_Value(self,value):
#         if Linked_list.is_empty(self):
#             return "linked list is empty"
#         elif self.head.data == value:
#             Linked_list.Del_at_Begining(self)
#         else:
#             temp = self.head
#             while temp.ref is not None:
#                 if temp.ref.data == value:
#                     break
#                 temp = temp.ref
#             if temp.ref is None:
#                 print(f"value {value} not found")
#             else:
#                 temp.ref = temp.ref.ref
    # def Reverse(self):
#         if self.head == None:
#             print("linked list is empty")
#         elif self.head.ref == None:
#             return self.head
#         else:
#             prv,cur,nxt = self.head,self.head.ref,self.head.ref.ref
#             prv.ref = None
#             while nxt is not None:
#                 cur.ref = prv
#                 prv = cur
#                 cur = nxt
#                 nxt = nxt.ref
#             cur.ref = prv
#             self.head = cur

# LL1 = Linked_list()
# LL1.Add_at_Begining(6)
# LL1.PrintLL()
# LL1.Del_by_Value(1)
# LL1.Del_at_End()
# print(LL1.is_empty())
# print(LL1.length())
# LL1.Del_at_Begining()
# LL1.Add_at_End(4)
# LL1.Add_at_Begining(5)
# LL1.insert()
# LL1.Add_to_Empty(7)

# from os import system
# system("cls")

# class aaa:
#     def __init__(self,integer:int):
#         self.integer = integer
#     def __repr__(self):
#         return "__repr__ from aaa"
#     def __str__(self):
#         return "__str__ from aaa"
# class name():
#     def __init__(self,name):
#         self.name = name
#     def __str__(self):
#         return "__str__ from {self.__class__.__name__}".format(self=self)
# x = name("amine")
# print(x)

# import csv
# class Item:
#     pay_rate = 80
#     all = []
#     users_num = 0
#     def __init__(self,name,price,quantity):
#         assert price >= 0, f"{price} should be greater than zero"
#         assert quantity >= 0, f"{quantity} should be greater than zero"
#         self.price = price
#         self.quantity = quantity
#         self.name = name
#         Item.all.append(self)
#         Item.users_num += 1

#     def __repr__(self):
#         return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"
#     @staticmethod
#     def show_num_users():
#         print("number of users is {}".format(Item.users_num))
#     @staticmethod
#     def from_percent(percent):
#         return percent/100
#     def apply_discount(self):
#         self.price *= self.from_percent(self.pay_rate)
#     def calculate_total_price(self):
#         return self.price * self.quantity
#     def instanciate_from_csv():
#         with open("oop.csv","r") as f:
#             reader = csv.DictReader(f)
#             items = list(reader)
#             for item in items:
#                 Item(
#                     name=item.get('name'),
#                     price=float(item.get('price')),
#                     quantity=float(item.get('quantity'))
#                 )
# # Item.instanciate_from_csv()
# item1 = Item('phone',33,1)
# # item1.pay_rate = 50
# # item1.apply_discount()
# class phone(Item):
#     def __init__(self,name,price,quantity,year):
#         super().__init__(name,price,quantity)
#         self.year = year
#     def __add__(self,other):
#         if isinstance(other,phone):
#             return self.price + other.price
#         else:
#             return NotImplemented
# my_phone1 = phone("huawei",350,1,2022)
# my_phone2 = phone("redmi",199,1,2018)

# print(Item.all)
# print(phone.all)

# class laptop(Item):
#     def __init__(self,name,price,quantity,CPU):
#         super().__init__(name,price,quantity)
#         self.CPU = CPU
# my_laptop = laptop("lenovo",499,1,"core i5")

# print(my_phone1.__add__(my_phone2))
# print(str.__len__("string"))
# print(my_phone1+my_phone2)

# class Employee():
#     def __init__(self,first,last):
#         self.first = first
#         self.last = last
#     @property
#     def email(self):
#         return f"{self.first}.{self.last}@gmail.com"
#     @property
#     def fullname(self):
#         return f"{self.first} {self.last}"
#     @fullname.setter
#     def fullname(self, new_name:str):
#         self.first ,self.last = new_name.split(" ")
#     @fullname.deleter
#     def fullname(self):
#         self.first = None
#         self.last = None
#         print("Name deleted")
# employee1 = Employee("john","clinton")

# employee1.fullname = "john wick"
# del employee1.fullname
# print(employee1.fullname)
# print(employee1.email)
# print(employee1.fullname)

# class x():
#     def __init__(self,name):
#         self.namee = name
    # @property
    # def name(self):
    #     return self.__name
# xxx = x("amine")
# print(xxx.namee) 


# from abc import ABCMeta,abstractmethod
# class person(metaclass=ABCMeta):
#     def imp_method(self):
#         return f"exists in {__class__.__name__}"
#     def unimp_method(self):
#         return f"exists in {__class__.__name__}"
# class man(person):
#     def unimp_method(self):
#         return f"exists in class {__class__.__name__}"
# person1 = person()
# man1 = man()
# print(person1.unimp_method())
# print(person1.imp_method())
# print(man1.unimp_method())
# print(man1.imp_method())

# class person():
#     def __init__(self,firstname,lastname):
#         self.__firstname = firstname
#         self.__lastname = lastname
#     @property
#     def firstname(self):
#         return self.__firstname
#     @firstname.setter
#     def firstname(self,new):
#         self.__firstname = new
# person1 = person("amine","sedrata")
# print(person1.firstname)
# person1.firstname = "main"
# print(person1.firstname)

# class Meta(type):
#     def __new__(self,class_name,bases,attrs):
#         print(attrs)
#         a = {}
#         for name,val in attrs.items():
#             if name.startswith("__"):
#                 a[name] = val
#             else:
#                 if isinstance(val,int):
#                     a[name] = val*2
#                 elif isinstance(val,str):
#                     a[name] = val.upper()
#         print(a)
#         return type(class_name,bases,a)
# class dog(metaclass=Meta):
#     num1 = 4
#     num2 = 8
#     name = "amine"
# print(dog.num1,dog.num2,dog.name)