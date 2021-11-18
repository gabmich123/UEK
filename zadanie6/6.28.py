arr=[1,23,5,382,1,17,4,906]
for x in range(0,len(arr)):
    if x!=0:
        print("-",end="")
    print("---",end="")
print("--")
print("|",end="")
for x in range(0,len(arr)):
    a=2
    b=arr[x]
    while b>10:
        a=a-1
        b=b/10
    for y in range(0,a):
        print(" ",end="")
    print(arr[x],end="")
    print("|",end="")
print()
for x in range(0,len(arr)):
    if x!=0:
        print("-",end="")
    print("---",end="")
print("--")