# OOPS


class Person:
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None

    # Behaviour
    def talk(self):
        print("I can talk")

    def sleep(self, name):
        print("I am a method")
        print("sleep", name)

    def sleep2(self, name):
        print("I am a method")
        return None

    def walk_return(self):
        return "I am walking"

    # Create an object
obj = Person()
obj.name = "Prashant"
obj.talk()
print(obj.name)


obj1 = Person()
obj1.name = "Bruno"
print(obj1.name)
obj1.talk()
