arr1=[2,2,6,3,6,5,2,3]
arr2=arr1
a=0
b=len(arr1)-1
for x in range(0,len(arr1)):
    if arr1[x]%2==0:
        arr2[a]=arr1[x]
        a=a+1
    else:
        arr2[b]=arr1[x]
        b=b-1
print(arr2)