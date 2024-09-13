

class Parent:
    gold = "2kg"

    def BHK2(self):
        print("2BHK")

class Child(Parent):
    diamond = "Diamond"
    def BHK3(self):
        print("3BHK")

child_object = Child()
print(child_object.gold)
child_object.BHK3()
child_object.BHK2()

father_obj= Parent()
father_obj.BHK2()

