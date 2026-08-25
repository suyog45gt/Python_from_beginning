# wap to find the greatest of three  number using function
def got(num1,num2,num3):
    if(num1>num2 and num1 > num3):
        return num1;
    elif(num2>num1 and num2>num3):
        return num2;
    else:
        return num3;
# x=int(input("enter first number"))
# y=int(input("enter second number"))
# z=int(input("enter third number"))
great=got(5,6,9)
print("greatest of three number is",great)