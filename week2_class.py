#Tuesday 

# class student:
#     def __init__ (self): #Self is reference to the objects memory location
#         print("constructor called") #Everytime object is created, Constructor is called. 
#         # it prints "constructor called 3 times b/c you have made 3 objects"
        
#     def good_morning(self):
#         print("Good morning ")
# Alina = student()
# Sean = student()
# Alex = student()

# Alex.good_morning()

# This is creating a class and the objects of that class. In this example I also called the object with its method.

# class kids:
#     def __init__(self, name, lname): #Self by default is put into parameters of the newly created objects, name however is not
#         self.name = name # instance variable
#         self.lname = lname
#         #You can print like this too:
#         print(f'{self.name} {self.lname}')

# Kazim = kids("Kazim", "Shabbir") # << signatures have to match with constructor signature. 
# # print(Kazim.name)
# # print(Kazim.lname) #Or you can print like this too.
# Foorkan = kids("Foorkan", "Shabbir")
# # print(Foorkan.name)
# # print(Foorkan.lname)
# Rayan = kids("Rayan", "Shabbir")
# # print(Rayan.name)
# print(Rayan.lname)

# import datetime

# class Person:
#     def __init__(self, Fname, Lname, Birthdate, address, email):
#         self.Fname = Fname
#         self.Lname = Lname
#         self.Birthdate = Birthdate
#         self.address = address
#         self.email = email

#     def age(self):
#         today = datetime.date.today()
#         age = today.year - self.Birthdate.year

#         if today < datetime.date(today.year, self.Birthdate.month, self.Birthdate.day):
#             age -= 1
#         return age
# sammy = Person("Sammy", "Kry", datetime.date(1998, 8, 21), "123 sesame st", "samy@gmail.com")
# print(f'{sammy.Fname}, {sammy.Lname}, {sammy.Birthdate}, {sammy.address}, {sammy.email}')

# age = sammy.age()
# print(age)
# #Age is a variable that is storing the info from the object sammy and its method called age. When age variable prints 
# #it shows the results of the calculations from the age method in the object of Sammy. 

# Why class's are better than objects.
# def Greeting(name):
#     count = 0
#     print(f'Hello {name}')
#     count += 1
#     print(count)

# Greeting("Kazim")
# Greeting("Ali")
# Greeting("Muhammad")
# Count doesnt store how many times its ran. It resets each time. 
# Objects RETAIN STATE, hence its better to have classes.

# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.count = 0
#     def greeting(self):
#             print(f'hello {self.name}')
#             self.count += 1
#     def printCount(self):
#             print(self.count)

# alina = Person("alina")

# alina.greeting("alina")
# alina.greeting("alina")
# alina.printCount()

# In class assignment:
# Write code to
# Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
# Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
# Have sonny greet jordan using the greet method.
# Have jordan greet sonny using the greet method.
# Write a print statement to print the contact info (email and phone) of Sonny.
# Write another print statement to print the contact info of Jordan.

# class friends:
#     def __init__ (self, fname, phone_number, email):
#         self.fname = fname
#         self.phone_number = phone_number
#         self.email = email
#     def greet(self, other_guy):
#         print("Hello {other_guy.fname}, I am {self.fname}!") #dont forget that self refers to the first person object


# sonny = friends("sonny", "832-220-9999", "sonny@hotmail.com")
# jordan = friends("jordan", "281-209-1333", "jordan@hotmail.com")
# sonny.greet(jordan)
# jordan.greet(sonny)
# print(f'Contact info of Sonny, {sonny.fname}, {sonny.phone_number}, {sonny.email}')
# print(f'Contact info of Jordan, {jordan.fname}, {jordan.phone_number}, {jordan.email}')

# Has some errors that need to be fixed ^^^^^^^^^

# class Person:
#     def __init__ (self, name):
#         self.name = name
#         self.count = 0
#     def greet (self):
#         self._greet()
#     def _greet (self):
#         self.count += 1
#     if self.count > 1:
#         print("Stop being so nice")
#         self.__reset_count()
#     else:
#         print("Hello", self.name)
#     def __reset_count(self):
#         self.count = 0

# alex = Person("alex")
# alex.greet()
# alex.greet()
#HAS ERRORS THAT NEED TO BE FIXED ^^^^^^^^^^

#Inheritance
# class VString(str):
#     def reverse(self, name):
#         rstring = ""

#         for char in name:
#             rstring = char + rstring
#         return rstring

# myString = VString('Hello') #myString is an object of the VString class
# print(myString.capitalize())
# backwards = myString.reverse("hello")
# print(backwards)

#Implicit inheritance #GET CLARITY
# class Parent(object):
#         def implicit(self):
#             print("PARENT implicit()")
# class Child(Parent):
#     pass
# dad = Parent()
# son = Child()
# dad.implicit()
# son.implicit()

# Another example. Constructors being called with super()

# class Character:
#     def __init_(self, name, power, health):
#         self.name = name 
#         self.power = power
#         self.health = health
# class Hero(Character):
#     def __init__(self, weapon, name, power, health):
#         self.weapon = weapon
#         super(Hero, self).__init__(name, power, health)
    

# Ali = Hero("Sword","Ali", "Lion", "Good health")
# print(Ali.weapon)
# Find out why its not working 

# INDEPENDENT ASSIGNMENT:

# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def printInfo(self):
#         print(f'{self.year}, {self.make}, {self.model}')  



# car = Vehicle("Ford", "F150", "2015")
# car.printInfo()

class friends:
    def __init__ (self, fname, phone_number, email,):
        self.fname = fname
        self.phone_number = phone_number
        self.email = email
        self.my_friends = []
        # self.greeting_count = 0
        self.number_of_friends = len(self.my_friends)
        # self.greet_count += 1
        
    def greet(self, other_guy):
        print(f'Hello {other_guy.fname}, I am {self.fname}!') #dont forget that self refers to the first person object
        # self.greet_count += 1
    def print_contact_info(self):
        print(f'{self.phone_number}')
    def add_friend(self, name): # The friend which is passed into this method is added into friends list.
        self.my_friends.append(name)
        for O in self.my_friends:
            print(O.fname, O.email) 
            # Add a add_friend method
    # def num_friends(self):
    #     self.number_of_friends = print(len(self.my_friends))
    

    


sonny = friends("sonny", "832-220-9999", "sonny@hotmail.com")
jordan = friends("jordan", "281-209-1333", "jordan@hotmail.com")

sonny.greet(jordan)
# sonny.greeting_count
jordan.greet(sonny)
jordan.greet(sonny)
# jordan.greeting_count
# sonny.print_contact_info()
# jordan.print_contact_info()
# sonny.my_friends.append(jordan)
# jordan.my_friends.append(sonny)
# print(len(jordan.my_friends))
# print(jordan.my_friends)
jordan.add_friend(sonny)
jordan.add_friend(sonny)
jordan.add_friend(sonny)
print(jordan.my_friends[0].fname) #will go to the list in the add_friends method in jordan object and give name.
# jordan.num_friends() #since currently you added sonny as your friend 3 times. It counts 3 friends in your list.
#^Need help with num_friends stuff