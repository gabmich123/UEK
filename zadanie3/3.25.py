a=int(input("a: "))
b=int(input("b: "))
for x in range(1, a+1):
    word=""
    for y in range(1,b+1):
        if x==1 or y==1 or x==a or y==b:
            word=word+"*"
        else:
            word=word+" "
    print(word)