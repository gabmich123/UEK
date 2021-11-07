a=str(input("Enter the PIN code: "))
pin="0805"
tries=0
while a!=pin and tries<2:
    tries=tries+1
    print("Incorrect...")
    a=str(input("Enter the PIN code: "))
if a==pin:
    print("Correct")
else:
    print("Inorrect...")
    print("Sorry, your payment card has been blocked.")