    


unique_words = [] 
while (True) : 
    word = input("Give the word (stop to exit) :")
    word.lower()
    if (word  != "stop") : 
        unique_words.append(word)
    else : 
        break 


for i in range (len(unique_words)-2) :   
    j = i + 1 
    for j in range (len(unique_words)-1) : 
        if (unique_words[j]==unique_words[i]) : 
            unique_words.remove(unique_words[j])

print("You typed in ",len(unique_words),"unique words")