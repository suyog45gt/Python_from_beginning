x=int(input("Enter the number"))
def fact(x):
    if (x==0):
        return 1
    elif(x==1):
        return 1
    else:
        return x*fact(x-1)
print(f"factorial of {x} = {fact(x)}")