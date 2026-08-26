# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
marks = {}
x = int(input("Enter a mark of physics: "))
y = int(input("Enter a mark of chem: "))
z = int(input("Enter a mark of math: "))
marks.update({"physics": x, "chem": y, "math": z})
print(marks)
