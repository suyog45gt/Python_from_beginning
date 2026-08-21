# wap to find find the greatest of three number enered by user
x=int(input("Enter a first number"))
y=int(input("Enter a second number"))
z=int(input("Enter a third number"))
if(x>y and x>z):
    print(f"greatest = {x}")
elif(y>x and y>z):
    print(f"greatest = {y}")
else:
    print(f"greatest = {z}")