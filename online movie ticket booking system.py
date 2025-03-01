



# online ticket booking

unup, pu_10ss, pu_1s, ka_11s, ka_4s, ka_9s, vi_3s = ([] for i in range(7))
tts, pu10, pu1, ka11, ka4, ka9, vi3 = (0 for i in range(7))

for i in range(1, 101):
    for j in [pu_10ss, pu_1s, ka_11s, ka_4s, ka_9s, vi_3s]:
        j.append(i)
        
def p(fun):
     for k in range(0,len(fun),10):
         print(*fun[k:k+10])
         
def df(a,c):
    nos=int(input("how many tickets you want - "))
    
    for i in range(nos):
        p(a)
        s=int(input("choose your seat \n "))
        
        if a[s-1]=="x": print("seat already booked")
        else:
            print(f"seat no {s} is booked sucessfully ")
            a[s-1]="x"
            c+=1
    return c


while True:
    option = input(" Admin - A \n Sign in - S \n Login - L \n exit - E \n ").upper()
    
    if option =="S":
        
        unup.append(input("enter you name - "))
        unup.append(int(input("enter you password in numbers - ")))
        print("sucessfully registered")
        
    elif option == "L":
        
        while True:
            un=input("enter you username - ")
            up=int(input("enter you password - "))
            
            for i in range (0,len(unup),2):
                
                if unup[i]==un and unup [i+1]== up:
                    mn=input(" pushpa - pu \n kanguva - ka \n viduthalai - vi \n ").lower()
                    
                    if mn=="pu":
                        time=int(input(" 10.00 am - 10  \n 1.00 pm - 1 \n"))
                        
                        if time==10:
                            ts=df(pu_10ss,0)
                            tts+=ts
                            pu10+=ts
                            
                        elif time == 1:
                            ts=df(pu_1s,0)
                            tts+=ts
                            pu1+=ts
                            
                        else: print("invalid time")
                        
                    elif mn=="ka":
                        time=int(input(" 11.00 am - 11 \n 4.00 pm - 4 \n 9.00 pm - 9 \n "))
                        
                        if time==11:
                            ts=df(ka_11s,0)
                            tts+=ts
                            ka11+=ts
                            
                        elif time == 4:
                            ts=df(ka_4s,0)
                            tts+=ts
                            ka4+=ts
                            
                        elif time == 9:
                            ts+df(ka_9s,0)
                            tts+=ts
                            ka9+=ts
                            
                        else: print("invalid time ")
                        
                    elif mn =="vi":
                        time=int(input(" 3.00pm - 3 \n"))
                        
                        if time==3:
                            ts=df(vi_3s,0)
                            tts+=ts
                            vi3+=ts
                            
                        else: print("invalid movie time")
                        
                    else: print("invalid movie name ")
                    
                else: print("incorrect username or password")
                
            else: break
            
    elif option == "A":
        o=input(" History - HI \n Total tickets sold - TTS \n ").upper()
        
        if o == "TTS": print(f" total ticket sold - {tts} tickets")
        
        elif o == "HI":
            w=input(" which movie history you want \n pushpa - pu \n kanguva - ka \n viduthalai - vi \n")
            
            if w == "pu": print(f" pushpa \n 10.00 am sold tickets are {pu10} \n 1.00 pm sold tickets are {pu1}")
            
            elif w == "ka": print(f" kanguva \n 11.00 am sold tickets are {ka11} \n 4.00 pm sold ticktes are {ka4} \n 9.00 pm sold ticktes are {ka9} ")
            
            elif w == "vi": print(f" viduthalai \n 3.00 pm sold tickets are {vi3}")
            
            else: print("invalid input")
            
        else: print("invalid input")
        
    elif option == "E": break
    
    else: print("invalid input")

