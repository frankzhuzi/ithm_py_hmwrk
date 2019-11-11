row = 1
while row <= 5:
    col = 1    # define col in the loop,so col will be reset everytime
    while col <= row:
        print("*", end="")     # make no new row
        col += 1
    print("")    # make a new row
    row += 1
