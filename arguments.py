#Possitional arguments 
def sum(a,b):
    print("Addition",a+b)

sum(30,4)

#Default arguments

def mul(a=34,b=9):
    print("Multipy",a*b)

mul(4,3)
mul(2)

#keyword arguments

def display(x=6,y=8):
    print("Display value of x:",x)
    print("Display value of y:",y)

display(3,6)
display(y=5,x=9)

#variable length Arguments

def add(*n):  
    sum=0
    for i in n:
        sum +=i

        print("sum",sum)

sum(1,3)
sum(4,5)

