def bubblesort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr=[5,1,9,6,1]
bubblesort(arr)
largest=arr[0]
largest2=largest
for x in arr:
    if largest<x:
        largest2=largest
        largest=x
print(largest2)