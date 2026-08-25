# write a recursive function to calculte the sum of first n natural number
x=int(input("Enter a number"))
def naturalNumber(x):
    if x==1:
        return 1
    else:
        return x + naturalNumber(x-1)
print("sum of first n natural number is",naturalNumber(x))