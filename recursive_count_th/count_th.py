'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word, count=0):
    
    if word != "":
       
        if word[0:2] == 'th':
            #print(word[0:2])
            count +=1
            
            return count_th(word[1:], count)

            #print(count)
        else:
            return count_th(word[1:], count)
        

    return count

    
    




    

print(count_th("thetheth"))
print(count_th("thetheth"))

