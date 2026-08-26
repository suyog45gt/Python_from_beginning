# wap to ask the user to enter names of their 4 favorite movies & store them in list
movie=[]
w=input("enter a first movie")
x=input("enter a second movie")
y=input("enter a third movie")
z=input("enter a fourth movie")
movie.append(w)
movie.append(x)
movie.append(y)
movie.append(z)
movie.sort()
print(movie)