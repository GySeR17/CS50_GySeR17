#Ask user for their name
name = input("What's your name? ").strip().title()

#Split user's name into first name and last name
first, last = name.split(" ") #Como hacer para que una vez separados el nombre y el apellido solo tengan un espacio entre si

#Say hello to user
print(f"Hello {first,last}, love you!")

