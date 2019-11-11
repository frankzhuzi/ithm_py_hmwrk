file = open("README")

text = file.read()
print(text)
print("-" * 50)
text2 = file.read()
print(text2)
print(len(text2))
file.close()