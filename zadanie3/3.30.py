a=1
N=int(input("Enter number: "))
while a<N:
    b=0
    c=0
    while c<2 and b<=a:
        b=b+1
        if a%b==0:
            c=c+1
        
    if b==a and c==2:
        print(f"{b} ")
    a=a+1