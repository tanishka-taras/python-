students=[]

while True:
    print("students",students)
    ch = int(input("1)add students\n 2)view students\n 3)display students\n 4)update students\n 5)delete students\n 6)exit\n Enter your choice:"))

    if ch==1:
        id = int(input("Enter your ID:"))
        name = (input("Enter your name:"))
        age =int(input("Enter your Age:"))

        std={"name":name,"age":age,"id":id}
        students.append(std)

    elif ch==2:
        id =int(input("Enter your ID:"))

        for i in students:
            for j in i:
                if i['id'] == id:
                    print("Student Found")
                    print("ID :",id)
                    print("Name: ",name)
                    print("Age :",age)
                    break
           
    elif ch==3:
        if len(students)>0:
            print("Displaying All Student: ")
            for i in students:
                    print("ID :",i["id"])
                    print("Name: ",i["name"])
                    print("Age :",i["age"])
        else:    
            print("No Students Found")


    elif ch==4:
         id = int(input("Enter ID of Student :"))
         for j in i:
            if i['id'] == id:
                ch = int(input("1)Update Name\n2)Update Age\n3)Update Id\n4)Cancle Update\nEnter Choice :"))

                if ch==1:
                    name = (input("Enter Name :"))
                    i['name'] = name

                    print("Student Updated Successfully")
                elif ch==2:
                    age = int(input("Enter Age :"))
                    i['age'] = age

                    print("Student Updated Successfully")
                elif ch==3:
                    age = int(input("Enter ID :"))
                    i['id'] = id

                    print("Student Updated Successfully")
                elif ch == 4:
                    break
                else:
                    print("Invalid Choice")   
    
    elif ch==5:
        id = int(input("Enter ID of Student :"))
        counter = 0
        for i in students:
            for j in i:
                if i['id'] == id:
                    students.pop(counter)
                    print("Student deleted successfully")
                    break
            counter+=1
        print("Student Not Found")
    
    elif ch==6:
         print("Thnak you")
         break
    else:
        print("invalid choice")