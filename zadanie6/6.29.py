def appear(arr1,arr2):
    appears1=True
    for x in arr1:
        appears2=False
        for y in arr2:
            if x==y:
                appears2=True
                break
        if appears2==False:
            appears1=False
            break
    return appears1
arr1=[1,2,3]
arr2=[1,2,3,4,5,6]
print(appear(arr1,arr2))