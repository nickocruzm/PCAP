from os import strerror

# List comprehension
pos_neg = ['+' if x%2 == 0 else '-' for x in range(10)]


# file write()
try:
    with open('scratch.txt','w') as f:
        for i in range(1,11):
            f.write("line #" + str(i) + '\n')
except IOError as e:
    print(strerror(e.errno))



