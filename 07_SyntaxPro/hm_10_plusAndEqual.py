def demo(num, num_list):

    print("Start...")

    num += num
    num_list += num_list
    num_list.extend(num_list)
    # To a list "+=" equals method "extend"

    print(num)
    print(num_list)

    print("Done...")

gl_num = 9
gl_num_list = [1, 2, 5]
demo(gl_num, gl_num_list)
print(gl_num)
print(gl_num_list)