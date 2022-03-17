def reverse(sentence,reverse_word):
    long_one=sentence.split()
    for i in long_one    :
        if  i == reverse_word:
            reverse=reverse_word[::-1]
            new_sentence = sentence.replace(reverse_word, reverse,1)
            return(new_sentence)
    if type(sentence)!=str or type(reverse_word)!=str:
        return "INVALID INPUT"  
       
    else :
        return"NO MATCH WORD FOUND"
                

print(reverse("I like apples and I also like bananas", "like") )   
print(reverse("I like apples and I also like bananas", "oranges") )   
print(reverse("I like apples and I also like bananas", "Bananas") )   
print(reverse("I like apples and I also like bananas", 3) )   

    
        
        
