# Triangle classifier

side1 = int(input("Enter length of side 1: "))
side2 = int(input("Enter length of side 2: "))
side3 = int(input("Enter length of side 3: "))
if side1 == side2 == side3:
    print("Equilateral Triangle")
elif (side1 == side2) or (side1 == side3) or (side2 == side3):
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")