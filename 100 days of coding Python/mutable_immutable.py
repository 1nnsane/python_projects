#  IMMUTABLE (Неизменчивый)
a = "corey"
print(a)
print(format(id(a)))  # address of a

a = "john"
print(a)
print(format(id(a)))  # address of new copy a
# a[0] = "C" #can't change (doesn't support item assignment) because this is IMMUTABLE

print("==============================================================")

#  MUTABLE (Изменчивый) - LIST
# modifying list, address is same
a = [1, 2, 3, 4, 5]
print(a)
print(format(id(a)))

a[0] = 6  # modified, address of a doesn't changed
print(a)
print(format(id(a)))