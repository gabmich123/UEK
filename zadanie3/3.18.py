x=int(input("Enter the amount in PLN: "))
five=0
two=0
one=0
while x>0:
    if x>=5:
        five=five+1
        x=x-5
    elif x>=2:
        two=two+1
        x=x-2
    elif x>=1:
        one=one+1
        x=x-1
print(f"Amount of PLN {x} in coins")
print(f"5zł - {five}")
print(f"2zł - {two}")
print(f"1zł - {one}")