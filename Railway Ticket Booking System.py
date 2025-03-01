



# Railway Ticket Booking System



d_ac=10
d_sl=0
d_ur=50
m_ac=12
m_sl=21
m_ur=33
option = input("welcome to IRCTC online booking \n choose your train \n Delhi - D \n Mumbai - M \n exit - E \n ").upper()
while True:
    if option =="D":
        coach = input("\n choose your coach \n ac - AC \n sleeper - SL \n un reserved - UR \n").upper()
        seats = int(input("how many tickets you want - "))
        if coach == "AC":
            if seats>d_ac:
                print(f"{seats} seats not available \n available seats are - {d_ac} \n")
            else:
                d_ac-=seats
                print(f" {seats} seat sucessfully booked \n balance seats available - {d_ac}")
        elif coach == "SL":
            print("seats not available")
        elif coach == "UR":
            if seats>d_ur:
                print(f"{seats} seats not available \n available seats are - {d_ur} \n")
            else:
                d_ur-=seats
                print(f"{seats} seats sucessfully booked \n balance seats avilable - {d_ur}")
    elif option == "M":
        coach = input("\n choose your coach \n ac - AC \n sleeper - SL \n un reserved - UR \n").upper()
        seats = int(input("how many tickets you want - "))
        if coach == "AC":
            if seats>m_ac:
                print(f"{seats} seats not available \n available seats are - {m_ac} \n ")
            else:
                m_ac-=seats
                print(f" {seats} seat sucessfully booked \n balance seats available - {m_ac}")
        elif coach == "SL":
            if seats>m_sl:
                print(f"{seats} seats not available \n available seats are - {m_sl} \n")
            else:
                m_sl-=seats
                print(f" {seats} seat sucessfully booked \n balance seats available - {m_sl}")
           
        elif coach == "UR":
            if seats>m_ur:
                print(f"{seats} seats not available available seats are - {m_ur} \n")
            else:
                d_ur-=seats
                print(f"{seats} seats sucessfully booked \n balance seats avilable - {m_ur}")
    elif option == "E":
        print("logout sucessfully")
        break
    else:
        print("invalid option")
        break
        
