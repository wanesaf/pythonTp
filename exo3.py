amount = float(input("Total amount : "))
items = int(input("Number of items: "))
day = input("Day of the week: ")
if (day != "Saturday" and day!="Sunday") : 
     amount = amount - amount*0.1
else : 
     amount = amount -amount*0.2     
if (items > 5 ) : 
      print ("Total price after discount :\t",amount - amount * 0.05 )     
else :
   print ("Total price after discount :\t",amount)      