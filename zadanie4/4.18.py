def NumSum(number):
    number=str(number)
    sum=0
    for x in range(0,len(number)):
        sum=sum+int(number[x])
    return sum
print(NumSum(7182)) 
    

    