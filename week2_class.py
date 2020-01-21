class student:
    def __init__ (self):
        print("constructor called") #Everytime object is created, Constructor is called. 
        # it prints "constructor called 3 times b/c you have made 3 objects"
    def good_morning(self):
        print("Good morning ")
Alina = student()
Sean = student()
Alex = student()

# Alex.good_morning()

# This is creating a class and the objects of that class. In this example I also called the object with its method.