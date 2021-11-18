def bubblesort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def minmax(array):
    bubblesort(array)
    return [array[0],array[len(array)-1]]

a=[4,2,8,4,7,9,5]
print(minmax(a))