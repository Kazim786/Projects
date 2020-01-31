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
        
def unique_characters():
    new_list=[]

    aList1= ["a", "b", "c", "d", "e"]
    aList2= ["a", "b", "c", "d", "f"]
    for letter1 in aList1:
        for letter2 in aList2:
            if(letter1 == letter2):
                new_list.append(letter1)
                print(new_list)
            else:
                print("does not match")
    print(new_list)

unique_characters()
            






















