def HowMany(string,letter):
    sum=0
    
    for x in range(0, len(string)):
        if string[x]==letter:
            sum=sum+1
    return sum
    
print(HowMany("You never get a second chance to make a first impression","e"))