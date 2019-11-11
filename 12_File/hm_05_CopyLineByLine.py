# *-* coding:utf8 *-*

file_read = open("README")
file_write = open("README[cp]", "w")

while True:

    text = file_read.readline()
    if not text:
        break
    file_write.write(text)
    # wOpen Once Rewrite once, not trigged by .write method

file_read.close()
file_write.close()