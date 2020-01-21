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

class kids:
    def __init__(self, name, lname): #Self by default is put into parameters of the newly created objects, name however is not
        self.name = name # instance variable
        self.lname = lname
        #You can print like this too:
        print(f'{self.name} {self.lname}')

Kazim = kids("Kazim", "Shabbir") # << signatures have to match with constructor signature. 
# print(Kazim.name)
# print(Kazim.lname) #Or you can print like this too.
Foorkan = kids("Foorkan", "Shabbir")
# print(Foorkan.name)
# print(Foorkan.lname)
Rayan = kids("Rayan", "Shabbir")
# print(Rayan.name)
# print(Rayan.lname)