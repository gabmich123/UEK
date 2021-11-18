array=[4,36,12,28,9,44,5]
array2=[5,1,36]
for x in array:
    appear=False
    for y in array2:
        if x==y:
            appear=True
    if appear==False:
        print(x)