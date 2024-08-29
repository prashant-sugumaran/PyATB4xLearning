def my_decorator(func):
    # wrapper and call

    def wrapper():
        print("something is happening before the function is called")
        print("Add helmet, dashcam, gloves, knee gaurds")
        func()
        print("something is happening after the function is called")
        print("Secure driving")
    return wrapper()


@my_decorator
def driver_bike():
    print("I am driving")
