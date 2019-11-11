# Dictionary is orderless
# Use : to split keys and values
# 1 key should be only 1
# We use dictionary to store the data that describe an object
# 1 pair of key-value takes 1 row

frank = {"name": "Frank",
         "age": 18,
         "gender": True,
         "height": 1.83}

# take value from a dict
print(frank["name"])

# add / modify key & value
frank["weight"] = 75
frank["age"] = 27

# delete
frank.pop("gender")

print(frank)
print(len(frank))

# combine & update a dict
temp_dict = {"gender": "Male",
             "weight": 74}
frank.update(temp_dict)

print(frank)

for key in frank:

    print("%s - %s" % (key, frank[key]))

