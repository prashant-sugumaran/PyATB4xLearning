my_list = [1, 2, 3]

print(my_list)
print(len(my_list))
print(my_list[0])
# print(my_list[10])

# indexing
print("element at the index", my_list[0])

my_list[0] = "Prashant"
print(my_list)

print(my_list)
for element in my_list:
    print(element)

# append

my_list.append("Bruno")
print(my_list)

my_list.extend(["Priyaa","Audi"])
print(my_list)

my_list.insert(1, "BWM")
print(my_list)
print(len(my_list))

my_list.remove("Priyaa")
print(my_list)

my_copy_list = my_list.copy()
print(my_copy_list)

print("_________________")
my_copy_list.reverse()
print(my_copy_list)
