list = [1,2,3,4,5]
print("----Menu----")
print("1).Append an element")
print("2).Insert an element at a specific postition")
print("3).Pop an element")
print("4).Remove an element")
print("5).Quit")

option = int(input("Choose an option: "))

if (option == 1) : 
    value = input("Choose an element:")
    if (type(eval(value))!=int) : 
        print("that's not an integer")
    else :
     list.append(int(value))
     print(list)
else : 
   if (option == 2) : 
      index = int(input("Give the index : ")); 
      value = int(input("Give the value : "));
      if (index >= 0 and index < len(list) ):
        list[index] = value ;
        print(list);
      else:
       print("out of range")  
   else : 
     if (option == 3) : 
       if (len(list)!=0) : 
         list.pop()
         print(list)
       else : 
         print("empty list , cant pop bro") 
     else : 
      if(option == 4) : 
       value = input("Choose an element to remove: ")
       if (type(eval(value))!=int) : 
        print("that's not an integer")
       else : 
         if (list.__contains__(int(value))==False) : 
           print("cant remove the element , doesnt exist")
         else :
          list.remove(int(value))
          print(list)  
      else : 
        print("quitting....")     
            