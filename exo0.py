ride = int(input("How many people need a ride ? \n"))
taxiSize = int(input("How many people fit in one taxi \n"))

if (ride % taxiSize == 0) :
    print("number of taxis nedded :",ride // taxiSize)
else :
    print("number of taxis nedded :",(ride // taxiSize)+1)

