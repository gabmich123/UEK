a=0
for x in range(1,10):
    a=a+1
    if x>5:
        a=a-2
    word=""
    for y in range(1,a+1):
        word=word+"* "
    print(word)