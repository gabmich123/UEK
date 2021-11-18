arr=[15, 8, 31, 47, 2, 19]
for x in range(0,int(len(arr)/2)):
    tmp=arr[len(arr)-x-1]
    arr[len(arr)-x-1]=arr[x]
    arr[x]=tmp
print(arr)