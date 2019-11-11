space_str = "   \t\n\r"
print(space_str.isspace())

num_str = "\u00b2"  # NumbersInChinese

print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())


hello_str = "hello world"
print(hello_str.find("llo"))
print(hello_str.find("abc"))
print(hello_str.index("llo"))
print(hello_str.startswith("hell"))
print(hello_str.endswith("rld"))

hello_str1 = hello_str.replace("world", "python")
hello_str.replace("world", "python")
# replace function return a new string
# dont modify the orginal string
print(hello_str)
print(hello_str1)


poem = [
    "Frank",
    "    Cindy",
    "FFFFFFFFFFword    ",
    "littleboy"]

for poem_str in poem:

    print(poem_str.strip().center(20, "="))
    # print(poem_str.rjust(20, "="))

trush = "aaa\t bbb\n ccc\t\t ddd"
print(trush)
trush_list = trush.split()
print(trush_list)
sentence = "~".join(trush_list)
# use ~ to combine the following list into a string
print(sentence)


num_str = "0123456789"
print(num_str[2:6])
print(num_str[2:])
print(num_str[:6])
print(num_str[:])
print(num_str[::2])
print(num_str[2:-1])
print(num_str[-2:])
print(num_str[-1::-1])
print(num_str[::-1])





