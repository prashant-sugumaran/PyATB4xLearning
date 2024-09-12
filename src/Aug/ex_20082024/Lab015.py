# Write a program to take a user age and let him know if he can go to the club.


age = input("enter your age\n")
age = int(age)

if age > 21:
    print(f"Can go to club{age}")
else:
    print(f"Can't go with this age{age}")
