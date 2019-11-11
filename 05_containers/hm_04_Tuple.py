# Tuple is not iterable
# Use () to make a tuple
# Tuple usually contains different types of data

info_tuple = ("Frank", 27, 1.83)
print(info_tuple)
print(info_tuple[0])

single_tuple = (5)
print(type(single_tuple))

single_tuple = (5,)  # how to define a one-element tuple
print(type(single_tuple))

print(info_tuple[0])
print(info_tuple.index("Frank"))

print(info_tuple.count("Frank"))
print(len(info_tuple))

for item in info_tuple:
    print(item)