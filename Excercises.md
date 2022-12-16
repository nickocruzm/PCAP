# Excercises


## 4.1
### Excercises 1

What is the expected output?

```python
class Vowels:
    def __init__(self):
        self.vow = "aeiouy "  
        self.pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos - 1]


vowels = Vowels()

for v in vowels:
    print(v, end=' ')

```

### Excercise 2

write a lambda function, setting the least significant bit of its integer argument, and apply it to the map() function to produce the string 1 3 3 5 on the console.

```python

any_list = [1,2,3,4]
even_list = # lambda goes here
print(even_list)

```

### Excercise 3

What is the expected output of the following code?

```python

def replace_spaces(replacement='*'):
    def new_replacement(text):
        return text.replace(' ', replacement)
    return new_replacement


stars = replace_spaces()
print(stars("And Now for Something Completely Different"))

```

## 4.1 Answers

1) output: a e i o u y

2) map(lambda x: x | 1, any_list)

3) output: "And*Now*for*Something*Completely*Different"

## 4.2

### Excercise 1)

How do you encode an open() function's mode argument value if you're going to create a new text file to only fill it with an article?

### Excercise 2)

what is the meaning of the value represented by errno.EACESS ?

### Excercise 3)

Expected output of the following code?

```python

import errno

try:
    stream = open("file", "rb")
    print("exists")
    stream.close()
except IOError as error:
    if error.errno == errno.ENOENT:
        print("absent")
    else:
        print("unknown")


```

## 4.2 Answers

1) "wt" or "w"
2) Permission denied
3) absent



## 4.3

### Excercise 1

what do we expect fromt the readlines() method when the stream is associated with an empty file?

### Excersice 2

What is the following intended to do?

```python
for line in open("file", "rt"):
    for char in line:
        if char.lower() not in "aeiouy ":
            print(char, end='')
```



## Exercise 3

You're going to process a bitmap stored in a file named image.png, and you want to read its contents as a whole into a bytearray variable named image. Add a line to the following code to achieve this goal.

```python
try:
    stream = open("image.png", "rb")
    # Insert a line here.
    stream.close()
except IOError:
    print("failed")
else:
    print("success")
```

## 4.3 Answers

1) an empty string (zero-length list)
2) Copies file's contents to the console ignoring all vowels.
3) image = bytearray(stream.read())