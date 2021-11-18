def tostring(array):
    string=""
    for x in range(0,len(array)):
        string=string+str(array[x])
        if x!=len(array)-1:
            string=string+","
    return string
arr=[5,4,3,2,6,5]
print(tostring(arr))