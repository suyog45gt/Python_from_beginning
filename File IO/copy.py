# Write a program that copies all the contents of source.txt into a new file called backup.txt. Handle the case where source.txt does not exist.
with open("source.txt", "r") as f1:
    with open("backup.txt", "w") as f2:
        f2.write(f1.read())
