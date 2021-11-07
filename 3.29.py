a=int(input("Enter number: "))
Quantity=0
Sum=0
Mean=0
while a!=0:
    Sum=Sum+a
    Quantity=Quantity+1
    a=int(input("Enter number: "))
Mean=Sum/Quantity
print(f"RESULT: Quantity={Quantity}, Sum={Sum}, Mean={Mean}")