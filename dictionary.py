d1 ={
    1:"python",
    2:"java",
    3:10293,
    4:"c++",
    5:"adv.java",
    }
    
print(d1)
print(type(d1))
print("Size of Data:", len(d1)) 


for i in d1:
    print(d1[i])

d1[4]=110101
print(d1)
d1 [5]= "hello everyone"
print(d1)

d1["6"]="country:india"
print(d1)

del d1[3]
print(d1)   

popvalue=d1.pop(1)
print(d1)
print("print:",popvalue)


popvalue2=d1.popitem()
print(d1)
print("print:",popvalue2)

d1.clear()
print(d1)









