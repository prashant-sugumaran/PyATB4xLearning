# Leap year checker

year = int(input("Enter the year :"))

if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
    print("Yes, this is a leap year")
else:
    print("This year is not a leap year")
