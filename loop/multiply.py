# wap to print thr multiplication table of a giveb number using loop
x=int(input("enter a number"))
for i in range(1,10):
    print(f"{x} * {i} = {x*i}")