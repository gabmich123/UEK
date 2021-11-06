x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
if x>0 and y>0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
elif x>0 and y<0:
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")
elif x<0 and y<0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
elif x<0 and y>0:
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")
elif x==0 and y!=0:
    print(f"Point P({x},{y}) is on the y axis of the coordinate system")
elif x!=0 and y==0:
    print(f"Point P({x},{y}) is on the x axis of the coordinate system")
elif x==0 and y==0:
    print(f"Point P({x},{y}) is on the middle of the coordinate system")