def demo(num_list):

    print("Inner Code")

    num_list.append(9)
    # Methods changes a iterable global value directly

    print(num_list)

    print("Done")


gl_list = [1, 2, 3]
demo(gl_list)
print(gl_list)