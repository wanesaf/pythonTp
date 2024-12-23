def anagram (string1,string2) : 
    if (len(string1)!=len(string2)) : 
        return False 
    else : 
        i = 0 
        while (i<len(string1)) : 
            if (string2.__contains__(string1[i])!=True) :
                return False
            else : 
                i+=1 

        return True         

string1 = "tame" 
string2 = "meta"
print(anagram(string1,string2))     

      