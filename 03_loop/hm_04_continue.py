i = 0

while i < 10:

    # continue:when condition satisfied
    # ignore the execute code
    # be care: modify the cal before continue line

    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

print("over")