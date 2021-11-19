x=int(input("Enter the dog's age in human years: "))
z=0
for y in range(1,x+1):
    if y <=2:
        z=z+10.5
    else:
        z=z+4
print(f"The dog's age in dog’s years is {z} years.")