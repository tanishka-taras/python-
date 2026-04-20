import math    
functions = dir(math)    
print( functions )  

num=5
print(math.sqrt(num)) 

num=8
print(math.cbrt(num))

n1=12.42
n2=90.1
print(math.ceil(n1))
print(math.floor(n2))
print(math.factorial(num))

x=4
y=-5

print("exponenial value",math.exp(x))
print("exponenial value",math.exp(y))
print("power",math.pow(5,2))
print("GCD",math.gcd(12,6,4))

#Constant values in math module

print("constant value of pi",math.pi)
print("constant value of e",math.e)
print("constant value of tau",math.tau)
print("constant value of inf",math.inf)