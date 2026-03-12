str1 ="this is Python language"

print(str1.upper())
print(str1.lower())
print(str1.capitalize())
print(str1.title())
print(str1.swapcase())


str2 = "IlovemyIndia"

print(str2.find("e"))
print(str2.index("a"))
print(str2.rfind("I"))
print(str2.rindex("o"))
print(str2.count("I"))
print(str2.startswith("I"))
print(str2.endswith("o"))

str3="learning -pyhon is -fun with tpointtech"

print(str3.split("n"))
print(str3.rsplit("t"))
print(str3.partition("is"))
print(str3.join("-"))

str4 ="nice123"

print("1",str4.isalnum())
print("2",str4.isalpha())
print("3",str4.isdigit())
print("4",str4.istitle())
print("5",str4.isspace())
print("6",str4.islower())
print("7",str4.islower())

str5 ="Good Evening"

print(str5.center (100))
print(str5.ljust (100))
print(str5.rjust (100))
print(str5.zfill(100))
