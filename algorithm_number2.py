# import math
# a=0
# b=0
# c=0
# for i in range(1,333): #max value for any side of the triangle must be less      than the semiperimeter
    
#     for j in range(i,499):
        
#         for k in range(j,499):
            
#             if(i+j+k==1000 and i**2+j**2==k**2):
#                 a=i
#                 b=j
#                 c=k
#                 break #the solution is unique, so when it finds a solution, it doesnt need to go through any other loops.
# # print(a)
# # print(b)
# # print(c)
# # print(a*b*c)
# print(math.sqrt(a))
# print(math.sqrt(b))
# print(math.sqrt(c))

#3 string differences
# class the_unique:
#     def __init__(self):
#         pass
        

        #Erics Code:
def unique_characters():
    aList1= ["a", "b", "c", "d", "e"]
    aList2= ["a", "b", "c", "d", "f"]
    new_list=[]
    for i in aList1:
        if i in aList2:
            pass
        else:
            new_list.append(i)
    for j in aList2:
        pass
    else:
        new_list.append(j)
    print(new_list)

unique_characters()



#This is my code.
#     aList1= ["a", "b", "c", "d", "e"]
#     aList2= ["a", "b", "c", "d", "f"]
#     for letter1 in range (len(aList1)):
#         print(letter1)
#         for letter2 in range (len(aList2)):
#             print(letter2)
#             if(aList1[letter1] == aList2[letter2]):
#                 del aList1[letter1]
#                 del aList2[letter2]
#                 break
#                 # new_list.append(letter1)
#                 # new_list.append(letter2)
#                 # print(new_list)
            
#     print(aList1)
#     print(aList2)


            






















