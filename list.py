L1 = [20, 'TpointTech', 35.75, [20, 40, 60]]  
  
print(L1)  
print(type(L1))
L1[2] ='Welcome'
print(L1)
print(L1[1])
print(L1[-1])
L1.append("good job")
print(L1)

L1.insert(3,1234567)
print(L1)
L1.extend("python")
print(L1)
L1[0]= 23.450
print(L1)
L1.remove(20)
print(L1)

L1.pop(-1)
print(L1)

del L1[0]
print(L1)
for list in L1:
   print(list)
   
i =0
while i<len(L1):
    print(L1[i])
    i+=1
      
cop = len(L1)
print(cop)  
L2 =[23,1,3,546,78,909,34]

L2.sort()
L2.reverse()
print("Largest Number:", max(L2))  
print("Smallest Number:", min(L2))
print("sum of elements:", sum(L2))  

print(L2)     