# Constructor

class Dog:
    name = None

    def __init__(self,name):
        print("Called, object is created")
        self.name = name

    def sleep(self):
        print("Sleeping")


dog1 = Dog("Chow")
print(dog1.name)


dog1 = Dog("Mow")
print(dog1.name)