class Myclass:
    public_var = "I am Public"
    balance = 0

    __private_var = "I am Private"
    __password = "1234"
    _protected_var = "I am Protected"




obj = Myclass
print(obj.public_var)
print(obj.balance)
print(obj._protected_var)
