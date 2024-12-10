list = [] 
while (1) : 
    list2 = [] 
    city = input("Please type in the name of the city: ")
    if (city == "stop") : 
        break  
    else :
      population = len(city) * 1000000
      list2.append(city)
      list2.append(population)
      list.append(list2)

from operator import itemgetter
sortedList = sorted(list,key=itemgetter(1),reverse=True) # stack overflow hh
print(sortedList)