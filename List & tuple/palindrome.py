# to check if a list contains a palindrome of element
x=list(input("Enter a group of list"))
y=x.copy() # since x.reverse doesnot return value we have to use copy function
y.reverse()
if x==y:
    print("list is palindrome")
else:
    print("list is not palindrome")