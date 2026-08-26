# Write a Python program that asks the user to enter their name and age, saves the information to students.txt, and then allows new student information to be appended without deleting existing data.
with open("info.txt","a") as f:
    x=input("enter a name")
    y=input("enter a age")
    list=[x,y]
    f.write(str(list)+"\n")