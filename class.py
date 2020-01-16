# print("I'm a String")
# # Use hashtag for comments. To comment out entire block of code you use command and forward slash. Command Z undos any errors or anything you do.
#Concactenation
#print("hello " + "world")
#print("hello \nworld")
#a = 20
#b = 15
#c = 3
#print (a + b + c)

#name = "Kazim"
#lname = "Shabbir"

#output = "good morning {0} {1} {1}".format(name,lname)
#print(output)
#output = f' hello world {student1} {student2}' #ask about the F thing
# consolelog = input("Enter your name")
# print(consolelog)
# output = f'Hello {consolelog}'
# print(output)
# dt = type(consolelog)
# print(dt)
# input_number_from_user = input("Insert a number ")
# print(type(input_number_from_user))
# casted_output = int(input_number_from_user)
# print(type(casted_output))
# some_math = casted_output * 7
# print(some_math)
# age = 26
# if True:
#     print(age)
# name = input("Enter your name")
# if (name == "Kazim" ) :
#     print(name) #Get clarity on this
# greeting = "Hello {}, it is very nice to meet you and your friend {}!"
# name_of_user = input("What is your name? ")
# length_of_name = len(name_of_user)
# if length_of_name > 0:
#     name_of_friend = input("What is your friend's name? ")
#     print(greeting.format(name_of_user, name_of_friend))
# else:
#     print("OK, I'll ask again some other time.")
# F string

# name_of_user = input("What is your name? ")
# length_of_name = len(name_of_user)
# if length_of_name > 0:
#     name_of_friend = input("What is your friend's name? ")
#     greeting = f"Hello {name_of_user}, it is very nice to meet you and your friend {name_of_friend}!"
#     print(greeting)
# else:
#     print("OK, I'll ask again some other time.")
# userInput = input("Is your name Hussain?") 
# if(userInput == "Hussain"):
#     print("Hurray!")
# elif(userInput == "Bob"):
#     print("No!")
# else:
#     print("No comment")

#WEDNESDAY WEEK1
# numbers = [1, 2, 3, 4, 5]
# print(numbers[1])
# numbers[0] = "Monday"
# print(numbers)
# numbers.append("4") #adding something to the end of the list.
# print(numbers)
# todos = ["pet the cat", "go to work", "shop for groceries", 
# "go home", "feed the cat"]
# todos.append("binge watch a show")
# todos.append("go to sleep")
# print(todos)
# index = 0
# while index < len(todos):
#     print(f'{index} : {todos[index]}' )
#     index += 1
# a = [1, 4, 7, 9, 10]
# b = [4, 6, 8, 9]
# print(a)
# print(b)
# print(a+b) #combining strings
# todos.extend(["binge watch a show", "go to sleep"])
# list_a = [1, 4, 7, 9]
# list_b = [5, 7, 9]
# print(list_a + list_b)
#concactenation doesnt change the current lists that you have.
# list_1 = []
# to_add = input("Add items to the list ")
# while len(to_add) > 0:
#     list_1.extend(to_add)
#     print(list_1)
#     to_add = input("Want more? ")
#     print(list_1)
   
# numbers = [1, 2, 3, 4, 5]
# numbers [2:4]
# new_list = numbers[2:4]
# print(new_list)
# numbers.insert(3, 6)
# print(numbers)
# numbers = [1, 2, 3, 4, 5]
# while(len(numbers) > 0):
#     print(numbers.pop())
#     print(numbers)
# print("finished")
# numbers = [1, 2, 3, 4, 5]
# result = numbers.index(3)
# print(result)
# a = [1, 2]
# example = a * 3
# print(example)
# x = [[2,6],[6,2],[8,2],[5,12]]
# print(x[2])
# print(x[2][1])
# myTuple = (1, 4, 6, "word")
# myTuple[1] = 34
# print(myTuple[1]) << CLARITY
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for character in alphabet:
#     print(character)
# In class assignment, create a loop that prints out every other numbers, 1, 3, 5, 7....1000
# for number in range(1, 1001, 2):
#   print(number)
#   # 1 + 2 =3 (and 1 is where youre starting from, and 2 is what you are adding it by because its every other number)
# for o_index in range (1, 11):
#     for i_index in range (1, 10):
#         total = o_index * i_index
#         print(str(o_index) + "X" + str(i_index) + "=" + str(total))


# Thursday 
# count = 0
# while count < 3:
#     print("Hello")
#     count += 1

#Week - Days nested loop
# Week = [1, 2, 3, 4, 5, 6]
# Days = ["Mon", "Tues", "Wednesday", "Thursday", "Friday"]
# subjects = ["Math", "sci", "english"]

# for outter_variable in Week:
#     print("Week", outter_variable)
#     for inner_var in Days:
#         print("\t", inner_var)
#         for inner_inner_var in subjects:
#             print('\t\t', inner_inner_var)


# myVar = 1
# myVar2 = 2 
# def greeting():
#     print("Hello world")
# if (myVar == 1):
#     print('Hello')

# greeting()

# def print_students():
#     print("Day 1: Students in SRE class")
#     print("lecture: git 101")
#     print("Shu")
#     print("Thomas")
#     print("Gustavo")
#     print("Alim")
# print("Day 2: Students in SRE class")
# print("lecture: git 102")
# print_students()

    
# print("Day 3: Students in SRE class")
# print("lecture: python 101")
# print_students()

# def greeting(person):
#     print('hello', person)
# greeting('Kazim')

# def add(num1, num2):
#     print(num1 + num2)
    
# add(2, 3)

# def cal_avg(param1, param2, param3, param4):

#     sum = param1 + param2 + param3 + param4
#     average = sum/4
#     return average
# result = cal_avg(4, 6, 9, 0)
# print(result)

# Class Exercise, Find the average of any given list with your function: 

# def the_average(numberList):
#     total = 0
#     for i in numberList:
#         equals = sum(numberList)/len(numberList) #DONT FORGET WHEN DOING AVERAGE THE SUM AND LEN STATEMENTS
#         return equals
# my_list = [3, 5, 19, 0, 18]
# print(the_average(my_list))
# my_list2 = [2, 5, 8, 10]
# print(the_average(my_list2)) 

# End of exercise :)

# Tuple practice:
# def myFunction(num1, num2, num3):
#     return num1*2, num2*3, num3*4
# # result = myFunction(3, 6, 9)
# # print(type(result))
# # print(result)


# More function practice

# def greeting(name):
#     print(f'Hello {name}')
# #*************************** scope of this function
# students = ['Kazim', 'John', 'Karim']
# for i in students:
#     greeting(i) # Functions called in this loop to perform its function.
# print('bye')

TAX_RATE = .09  # 9 percent tax
COST_PER_SMALL_WIDGET = 5.00
COST_PER_LARGE_WIDGET = 8.00
def calculateCost(nSmallWidgets, nLargeWidgets):
    subTotal = (nSmallWidgets * COST_PER_SMALL_WIDGET) + (nLargeWidgets * COST_PER_LARGE_WIDGET)
    taxAmount = subTotal * TAX_RATE
    totalCost = subTotal + taxAmount
    return totalCost
total1 = calculateCost(4, 8)  #  4 small and 8 large widgets
print('Total for first order is', total1)
total2 = calculateCost(12, 15)



    