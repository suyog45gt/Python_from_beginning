# wap which finds out whether a given name is present in the list or not
name =["ram","hari","sita","gita"]
x=input("Enter a name you want to check")
if x in name:
    print(f"{x} is present")
else:
    print(f"{x} is not present")