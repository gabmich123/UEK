array=[2,3,2,5,8,1,9,8]
for x in range(0,len(array)):
    appear=False
    for y in range(0,len(array)):
        if array[x]==array[y] and x!=y:
            appear=True
    if appear==False:
        print(array[x])