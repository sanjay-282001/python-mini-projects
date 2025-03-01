



# Student Result Management System


# made by sk

print("student database \n student = s \n admin = a \n exit = e")
l=[]
while True:
    option=input("select your option - ").lower()
    if option=="a":
        nos=int(input("no of students - "))
        for i in range(nos):
            l.append(int(input("reg no - ")))
            l.append(input("enter student name - "))
            l.append(int(input("tam - ")))
            l.append(int(input("eng - ")))
            l.append(int(input("mat - ")))
            l.append(int(input("sci - ")))
            l.append(int(input("soc - ")))
        else:
            print("student details upload sucessfully")
    elif option=="s":
        reg=int(input("enter your reg no - "))
        b= False
        for i in range(0,len(l),7):
            if l[i]==reg:
                b=True
                print(f" reg no = {l[i]} \n name = {l[i+1]} \n tam= {l[i+2]} \n eng= {l[i+3]} \n mat= {l[i+4]} \n sci= {l[i+5]} \n soc= {l[i+6]}")
                s=(l[i+2]+l[i+3]+l[i+4]+l[i+5]+l[i+6])
                if (l[i+2] >=35 and l[i+3] >=35 and l[i+4] >=35 and l[i+5] >=35 and l[i+6] >=35):
                    print(f"total = {s} \n pass")
                    
                else:
                    print(f"total = {s} \n fail")
        if b==False:
            print("student not found")
            
    elif option=="e":
        print("sucessfully logout")
        break
    else:
        print("invalid option choose correct option")

