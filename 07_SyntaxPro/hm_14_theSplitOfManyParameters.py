def demo(*args, **kwargs):

    print(args)
    print(kwargs)


gl_nums = (1, 2, 3)
gl_dict = {"name": "frank", "age": 27}

demo(gl_nums, gl_dict)
demo(*gl_nums, **gl_dict)
demo(1, 2, 3, name ="frank", age = 18)
