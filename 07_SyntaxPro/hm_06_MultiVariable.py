def measure():


    print("Start...")
    temp = 39
    wetness = 50
    print("End...")

    # if a def returns a tuple, the "()" can be ignored

    return temp, wetness


result = measure()

print(result)

print(result[0])
print(result[1])


gl_temp, gl_wetness = measure()

print(gl_temp)
print(gl_wetness)




