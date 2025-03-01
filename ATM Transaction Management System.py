






# # ATM Transaction Management System

def atm(un,up):
    if user_name==un and user_pass==up:
        print(f"welcome {un}")
        print(" withdraw : w , deposite : d , balance check : b, exit : e")
        amount=10000
        while True :
            c=input("choose your option : ")
            if c=="w":
                withdraw=int(input("enter your withdraw amount : "))
                if withdraw>amount:
                    print("insuffciant fund")
                else:
                    amount=amount-withdraw
                    print(f"your balance amount is : {amount} : ")
            elif c=="d":
                deposite=int(input("enter your deposite amount : "))
                amount=amount+deposite
                print(f"your balance amount is : {amount} : ")
            elif c=="b":
                print(f"your balance amount is : {amount} : ")
            elif c=="e":
                print("logout succesfully")
                break
            else:
                print("invalid option")        
    else:
        print("invalid username or password")
        
user_name="sk"
user_pass="12"
un=input("enter your user name : ").lower()
up=input("enter your password : ")
atm(un,up)


