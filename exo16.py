list = [1,2,3,4,5];
while (True) : 
    index = int(input("Give the index : ")); 
    value = int(input("Give the value : "));
    if (value != -1 ):
     if (index >= 0 and index < len(list) ):
      list[index] = value ;
      print(list);
     else:
       print("out of range")
    else  : 
        break 
