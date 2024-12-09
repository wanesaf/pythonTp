while (1) : 
    price = float(input("Please type in a price (postif):"))
    if (price > 0) : 
      break  

print("Dinars:",(str(price).split('.'))[0])
print("centimes:",(str(price).split('.'))[1])