
x = True
y = False

print(x,type(x))
print(y,type(y))

print("0",bool(0))
print("0.2",bool(0.2))
print("",bool())
print("-4",bool(-4))
print("10",bool(10))

print("tpointtech",bool('tpointtech'))

print("[] ", bool([]))   
print("[11, 12, 13] ", bool([11, 12, 13]))  

print("() ", bool(()))   
print("(11, 12, 13) ", bool((10, 8, 5)) ) 
  
print("{}", bool({}))   
print("{11, 12, 13} ", bool({1, 1,3}))  



print("(8 == 8) ", 8 == 8)  
print("(True == 1) ", True == 1)  
print("(False == 0) ", False == 0)
print("(6 == -4) ", 6 == -4)  
  
  
a = [13, 26, 39]  
b = a  
c = [13, 26, 39]  
   
print("a is b ", a is b )  
print("a is c =>", a is c)  

  
 