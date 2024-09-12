# No return type and no parameter/argument
def greet():
    print("Hello World")


print(greet())


# 2 No Return type and with argument

def greet_by_name(name):
    print("Hello,", name)


greet_by_name("Prashant")


# 3 No return type and with default argument
def say_hello_default_arg(name="Prashant"):
    print("Hello", name)


say_hello_default_arg("Bruno")
say_hello_default_arg()
say_hello_default_arg(name="Priyaa")


def multiple_args(name1="Prashant", name2="Priyaa", name3="Bruno"):
    print("Multiple Arguments", name1, name2, name3)


multiple_args(name1="Ram", name2="Tim", name3="Steve")


# 4 Argument + return type
def sum_of_two_number(num1, num2):
    return num1 + num2

def sum_of_two_number_with_default(num1=100, num2=200):
    return num1 + num2


result = sum_of_two_number(10, 34)
result = sum_of_two_number_with_default()
print(result)
