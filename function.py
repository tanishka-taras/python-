#absolute funcion
integer =12
print("Absolute vale of int:",abs(integer))

float = -13
print("Absolute vale of int:",abs(float))


#all function
k = [1, 3, 4, 6]    
print(all(k))    
k = [0, False]    
print(all(k))        
k = [1, 3, 7, 0]    
print(all(k))    
k = [0, False, 5]    
print(all(k))    
k = []    
print(all(k))   

#bool function

test1 = []  
print(test1,'is',bool(test1))  
test1 = [0]  
print(test1,'is',bool(test1))  
test1 = 0.0  
print(test1,'is',bool(test1))  
test1 = None  
print(test1,'is',bool(test1))  
test1 = True  
print(test1,'is',bool(test1))  
test1 = 'Easy string'  
print(test1,'is',bool(test1))  


#bytes function

string = "Hello World."  
array = bytes(string, 'utf-8')  
print(array)  

#callable function
x = 8  
print(callable(x))  


#Execute function 
x = 8  
exec('print(x==8)')  
exec('print(x+4)')  


#summ function
s = sum([1, 2,4 ])  
print(s)  
s = sum([1, 2, 4], 10)  
print(s)  


#any function 

l = [4, 3, 2, 0]                              
print(any(l))                                   
l = [0, False]  
print(any(l))  
l = [0, False, 5]  
print(any(l))  
l = []  
print(any(l)) 

#evaluate function 

x = 8  
print(eval('x + 1'))  
t=5
print(eval('t+2'))

  

#length function 

strA = 'Python'  
print(len(strA))  

strt2 ="programming"
print(len(strt2))

#hecxadecimal function

result = hex(1)   
result2 = hex(342)   
print(result)  
print(result2)  

#sorted function 

str = "TpointTech" 
sorted1 = sorted(str) 
print(sorted1) 

#octal function 

val = oct(10) 
val2 =oct(2)  
print("Octal value of 10:",val)  
print("Octal value of 10:",val2)  

#reversed function 

String = 'Java'  
print(list(reversed(String)))  
Tuple = ('J', 'a', 'v', 'a')  
print(list(reversed(Tuple)))  
Range = range(8, 12)  
print(list(reversed(Range)))  
