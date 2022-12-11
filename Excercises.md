# Excercises

## 1) What is the expected output?

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

## Excercise 2

write a lambda function, setting the least significant bit of its integer argument, and apply it to the map() function to produce the string 1 3 3 5 on the console.

```python

any_list = [1,2,3,4]
even_list = # lambda goes here
print(even_list)

```

## Excercise 3

What is the expected output of the following code?

```python

def replace_spaces(replacement='*'):
    def new_replacement(text):
        return text.replace(' ', replacement)
    return new_replacement


stars = replace_spaces()
print(stars("And Now for Something Completely Different"))

```


## Answers

1) output: a e i o u y

2) map(lambda x: x | 1, any_list)

3) output: "And*Now*for*Something*Completely*Different"
