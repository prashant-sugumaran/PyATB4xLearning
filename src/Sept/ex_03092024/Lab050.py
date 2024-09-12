# Encapsulation

class Bank:

    def __init__(self):
        self.__value = 10

    def __ram(self):
        #print("Value:", self.__value)
        print("Name: Ram")
        print("A/C No: 12345")
        print("Amount: 10000")
        print("Address: Salem")
        print("\n")

    def __tim(self):
        print("Name: Tim")
        print("A/C No: 12345")
        print("Amount: 110000")
        print("Address: Chennai")


obj = Bank()
obj._Bank__ram()
obj._Bank__tim()
print("Value:",obj._Bank__value)
