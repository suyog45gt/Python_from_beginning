# to find the gratest of 3 number enter by user
x=int(input("Enter a first number"))
y=int(input("Enter a second number"))
z=int(input("Enter a third number"))
if (x>y and x>z):
    print(f"gratest number is{x}")
elif(y>x and y>z):
    print(f"gratest number is{y}")
else:
    print(f"gartest number is{z}")