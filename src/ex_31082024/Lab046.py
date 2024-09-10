class Dog:
    name = None
    breed = None
    color = None

    def sleep(self):
        print("Sleeping")

    def bark(self):
        print("bark")

    def eat(self,food):
        print("food")


dog1 = Dog()
print(dog1.name)
dog1.name = "Chow"
print(dog1.name)
dog1.sleep()

print("_____________")

dog2 = Dog()
print(dog2.name)
dog2.name = "Mow"
print(dog2.name)
