import math
a=0
b=0
c=0
for i in range(1,1000): #max value for any side of the triangle must be less      than the semiperimeter
    
    for j in range(i,499):
        
        for k in range(j,499):
            
            if(i+j+k==1000 and i**2+j**2==k**2):
                a=i
                b=j
                c=k
                break #the solution is unique, so when it finds a solution, it doesnt need to go through any other loops.
print(a)
print(b)
print(c)
print(a*b*c)
print(math.sqrt(a))
print(math.sqrt(b))
print(math.sqrt(c))





















