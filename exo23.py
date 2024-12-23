def represents_int(s): #to check if the input is int before transformation the string to int 
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True
    
integer = input("Type in an integer: ")
if (represents_int(integer))  :
        integer = int(integer)
        if(integer > 0) : 
            i = -(integer) 
            while (i<=integer) : 
                print(i)
                i+=1
        else : 
            print("This is not a positive integer")

else : 
     print("This is not an integer")


