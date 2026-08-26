# Write a Python program that creates a file named students.txt and writes the names of 5 students into it.
with open("student.txt","w") as f:
    print("enter the name of five student")
    for i in range(5):
        x=input("")
        f.write(x+"\n")
        