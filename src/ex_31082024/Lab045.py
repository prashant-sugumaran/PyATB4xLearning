# OOPS


class Person:
    id = None
    ame = None
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

    def walk(self):
        print("I am Walking")

    def walk_return(self):
        return "I am walking"


# Create an object of the class

Obj = Person()
Obj.name = "Prashant"
print(Obj.name)

Obj1 = Person()
Obj1.name = "Bruno"
print(Obj1.name)