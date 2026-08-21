# 2 Write a program to find out whether a student is pass or fail, if it requires total 40% and at least 35%, in each subject to pass Pesume 3 Subjects and take marks as an input from the user
x=int(input("enter the marks of first subject"))
y=int(input("enter the marks of second subject"))
z=int(input("enter the marks of third subject"))
avg=(x+y+z)/3
if(avg>=40 and x>=35 and y>=35 and x>=35):
    print("pass")
else:
    print("fail")
