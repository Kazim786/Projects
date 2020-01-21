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



