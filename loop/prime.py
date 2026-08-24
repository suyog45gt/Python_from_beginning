# wap to check the given number is prime or not
x=int(input("enter a number"))
if x<=1:
    print("not prime")
else:
    for i in range (2,x):
        if x%i==0:
            print("number is not prime")
            break
    else:
            print("number is prime")