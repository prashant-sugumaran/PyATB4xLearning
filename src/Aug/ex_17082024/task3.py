"""
### Task #3
- Explain the difference between the = operator and the == operator in Python.

- What does the ** operator do in Python, and how is it used?

- What does the ^ operator do in Python, and in what context is it commonly used?
"""
# Explain the difference between the = operator and the == operator in Python.
# In Python, the = operator and the == operator serve different purposes and are used in different contexts:
#
# = Operator
# Purpose: The = operator is used for assignment. It assigns the value on its right-hand side to the variable on its left-hand side.
# Context: You use the = operator when you want to give a variable a value or update its value.
# Example:
# x = 5  # Here, `5` is assigned to the variable `x`
# name = "Alice"  # Here, `"Alice"` is assigned to the variable `name`
# == Operator
# Purpose: The == operator is used for comparison. It checks whether the values on both sides are equal.
# Context: You use the == operator when you want to test if two values or expressions are equal, which returns a Boolean result (True or False).

# a = 10
# b = 20
# print(a == b)  # Output: False, because `10` is not equal to `20`
#
# c = 5
# print(a == c)  # Output: True, because `10` is equal to `5`

""" What does the ** operator do in Python, and how is it used?"""
# In Python, the ** operator is used for exponentiation.
# It raises a number to the power of another number.
# Essentially, it computes the result of the base number raised to the exponent.
# base ** exponent
print(2 ** 3)

""" What does the ^ operator do in Python, and in what context is it commonly used?"""
# In Python, the ^ operator is the bitwise XOR (exclusive OR) operator.
#
# The ^ operator compares each bit of two integers. For each bit position:
# The result bit is 1 if the corresponding bits of the operands are different
# (one is 1 and the other is 0).
# The result bit is 0 if the corresponding bits are the same (both 0 or both 1).
a = 12  # binary: 1100
b = 7  # binary: 0111
result = a ^ b  # binary: 1011, which is 11 in decimal
print(result)  # Output: 11
