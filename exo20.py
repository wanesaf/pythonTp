def represents_int(s): #to check if the input is int before transformation the string to int 
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True

currentList = [] 
sortedList= []
while (True) : 
    number = input("Give a number: ") 
    if (represents_int(number)== True) : 
      if (number != '0') : 
        number = int(number)
        currentList.append(number)
        print("Current List is :",currentList)
        sortedList = currentList.copy() # because there is no pointers u must create a copy of the list 
        sortedList.sort(reverse=False)
        print("Sorted List is :",sortedList)
      else : 
         break 
    else : 
       print("That's not an Integer! ")    