class Dog:
    name = None

    def __init__(self,name,age):
        print("Called, object is created")
        self.name = name
        self.age = age


    def sleep(self):
        print("sleeping")


dog1 = Dog("Chow",10)
print(dog1.name)


dog1 = Dog("Mow",10)
print(dog1.name)

