students = [
    {"name": "Frank"},
    {"name": "Rose"}
]

find_name = "Issac"

for stu_dict in students:

    print(stu_dict)

    if stu_dict["name"] == find_name:
        print("We find %s" % find_name)
        break

else:
    print("Sry We Didn't Find %s" % find_name)

print("ExitLoop")

