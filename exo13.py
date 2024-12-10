while (1) : 
    string = input("Please type in a string: ")
    if (string == '') : 
        break 
    else :
      print("\033[4m" + string + "\033[0m")