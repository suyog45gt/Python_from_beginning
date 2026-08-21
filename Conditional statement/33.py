# Wap to find whether a given username contains less than 10 characters or not
x=input("Enter the user name")
count=len(x)
if(count<10):
    print("username is valid")
else:
    print("username is invalid")
    