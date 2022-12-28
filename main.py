from os import strerror
from datetime import date,datetime
import calendar
# List comprehension
pos_neg = ['+' if x%2 == 0 else '-' for x in range(10)]


# file write()
try:
    with open('scratch.txt','w') as f:
        for i in range(1,11):
            f.write("line #" + str(i) + '\n')
except IOError as e:
    print(strerror(e.errno))
    


# Byte array

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i
    for bit in data:
        print(hex(bit))
        

class A:
    def __init__(self):
        pass
    

a = A()


numbers = (1,2,5,9,15)

def filter_numbers(num):
    nums = (1,5,17)
    if num in nums:
        return True
    else:
        return False

filtered_numbers = filter(filter_numbers,numbers)

for n in filtered_numbers:
    print(n)
    
def I():
    s = 'abcdef'
    for c in s[::2]:
        yield c
        

for x in I():
    print(x, end='')
print()
datetime = datetime(2019,11,27,11,27,22)
print(datetime.strftime('%y/%B/%d %H:%M:%S'))


print(calendar.weekheader(2))
print(calendar.weekheader(3))
print()

b = bytearray(3)
print(b)

def fun(n):
    s = '+'
    
    for i in range(n):
        s += s
        yield s
        

for x in fun(2):
    print(x,end='')


c = calendar.Calendar()

for weekday in c.iterweekdays():
    print(weekday, end=" ")
    

print()

d = date(1992,1,16)
d2 = date(1991,2,5)

print(d - d2)