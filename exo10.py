word = input("Please type in the word ! ")
if(len(word)==0) : 
   print("there is no word ! ")
else : 
   isPalindrome = True 
   i = 0 
   j = len(word) - 1
   while (i<len(word)) : 
     if word[i] != word[j] :
       isPalindrome = False 
       break 
     else : 
       i+=1
       j-=1
   if (isPalindrome == False ) : 
     print("No it's not a palindrome")
   else :      
    print("Yes it's  a palindrome")