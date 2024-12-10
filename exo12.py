width = int(input("Width: "))
height = int(input("height: "))
#######
#######
#######
#######
#######
for i in range (height) :
     for j in range (width): 
       if (j == width-1) :
           print('#')
       else :    
        print('#' ,end='')
