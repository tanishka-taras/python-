tup1 =(12,34.6,(45,678,9),[1123],"python")

print(tup1)
print(type(tup1))
print(len(tup1))


for i in tup1:
   print(i)

i=0
while i<len(tup1):
   print(tup1[i])
   i+=1


num1 =(34.6,899,("welcome"),"tpointtech",34,4564,456)

print(num1[1])
print(num1[3])

print(num1[0:3])
print(num1[1:4])
print(num1[::-1])
print(num1[::2])

products = ("TV","Printer","Computer")

(p1,p2,p3) = products

print(p1)
print(p2)
print(p3)


a = (1,2,4)
b =("a","b","c")

print(a+b)
print(a*3)
print(4 in a)
print(4 in a)
print(5 not in a)
print(4  not in a)

nums= (1,2,12,24,67,5,3,22,89,32,54,17,1,2,6,73,73)

print(nums.count(24))
print(nums.index(24))
print(nums.index(73))
print(nums.index(73,16))
