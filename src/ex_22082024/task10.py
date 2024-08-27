# Factorial n = 5 5! -> 54321 -> 120 3! -> 321 -> 6 4! -> 432*1 ->24

num = int(input("Enter a Number: "))
fact = 1
if num < 0:
    print("enter positive number")
elif num == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        fact = fact * i
        print(f"The factorial of number {num} is {fact}")
