# wap to find the sum of first n natural number using while loop
x=int(input("enter nth natural number"))
count = 1
sum=0
while count <=x:
    sum=sum+count
    count=count+1
print(f"sum={sum}")