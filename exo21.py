def length(lst): #using exceptions
    count = 0
    while True:
        try:
            lst[count]
            count += 1
        except IndexError:
            return count
def mean (lst) : 
    sum = 0 
    for i in range(length(lst)):
        sum += lst[i]
    return sum / length(lst)

def range_of_list (lst) : 
    return max(lst) - min(lst)


print(length([1,2,3,4,5]))
print(mean([1,2,3,4,5]))
print(range_of_list([1,2,3,4,5]))
