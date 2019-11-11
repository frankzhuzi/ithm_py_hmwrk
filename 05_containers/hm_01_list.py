name_list = ["1", "2", "3"]

print(name_list.index("2"))

# add sth into list
name_list.append("4")
name_list.insert(1,"x")
name_list.extend(["i", "o", "u"])

# modify sth in list
name_list[0] = "q"

# delete sth from the list
name_list.remove("o") # delete the exact element. Default:delete the 1st element
name_list.pop(3) # delete the element that ordered, the last one default
del name_list[2] # del: delete the data from memory
# name_list.clear()

# calculate the list
print(len(name_list))  # cal the length
print(name_list.count("i"))  # count the times of the element

# sort the list
name_list.sort()
name_list.sort(reverse=True)
name_list.reverse()

print(name_list)