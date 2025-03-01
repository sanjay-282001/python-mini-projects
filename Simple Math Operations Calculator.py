




# Simple Math Operations Calculator

def cal(f):
    while True:
        pros=input(" +\n -\n *\n /\n  \n ")
        if (pros=="+"):
            s=int(input("enter second number - "))
            add=f+s
            print(add)
            r=input("you want to use this number press y or new press n exit back")
            if r=="y":
                cal(add)
            elif r=="n":
                new=int(input("enter first number - "))
                cal(new)
        elif pros=="-":
             s=int(input("enter second number - "))
             sub=f-s
             print(sub)
             r=input("you want to use this number press y or new press n exit back")
             if r=="y":
                 cal(sub)
             elif r=="n":
                 new=int(input("enter first number - "))
                 cal(new)
        elif pros=="*":
             s=int(input("enter second number - "))
             mul=f*s
             print(mul)
             r=input("you want to use this number press y or new press n exit back")
             if r=="y":
                 cal(mul)
             elif r=="n":
                 new=int(input("enter first number - "))
                 cal(new)
        elif pros=="/":
             s=int(input("enter second number - "))
             div=f/s
             print(div)
             r=input("you want to use this number press y or new press n exit back")
             if r=="y":
                 cal(div)
             elif r=="n":
                 new=int(input("enter first number - "))
                 cal(new)
        else:
            print("invalid operation")
            break

a=int(input("enter first number - "))
re=cal(a)







# or







def cal(f):
    while True:
        pros=input(" +\n -\n *\n /\n  \n ")
        if (pros=="+"):
            s=int(input("enter second number - "))
            res=f+s
        elif pros=="-":
             s=int(input("enter second number - "))
             res=f-s
        elif pros=="*":
             s=int(input("enter second number - "))
             res=f*s
        elif pros=="/":
             s=int(input("enter second number - "))
             res=f/s
        else:
            print("invalid operation")
            break
        print(f"result - {res}\n")
        new=input(" use this number enter - y \n new calculation enter - n \n exit - e \n")
        if new=="y":
            cal(res)
        elif new=="n":
            ni=int(input("enter first number - "))
            cal(ni)
        elif new=="e":
            print("exit")
            break

a=int(input("enter first number - "))
cal(a)



