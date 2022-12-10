# File Streams

## Working with text files

we are only working with plain text files. The encoding of text files depend on the O.S, for the examples below we assume the encoding to be 'UTF-8'.

A simple implementation

```python

    stream = open('fileName.txt','rt',encoding='utf-8')

    print(stream.read())

```

### Routine 1

```python
from os import strerror

try:
    count = 0
    s = open('file.txt','rt')
    ch = s.read(1) # reads one character

    while(ch != ''):
        print(ch, end='')
        count += 1
        ch = s.read(1)
    
    s.close()

    print('character count: ', count)

except IOError as e:

    print("I/O ERROR occured: ", strerror(e.errno))

```

### readline

readline will return a string of the line of input
else it will return an empty string


## idk the name yet

Portability issues are still presently a problem

When the stream is open, its contents are taken as-is, without any conversion, no bytes are added or omitted.

We must open the stream

if openning is successful then the funciton returns a stream object
else and exception is raised
    'FileNotFoundError' if the file you're going to read doesn't exist;

first argument: file name.

second argument: mode
    a string filled with a sequence of characters. Each of the characters have their own special meaning.

third argument: encoding
    specifies the encoding type
        (UTF-8 working with text files)

mode and encoding args may be omitted. Each have assumed default arguments, assumes to be reading in text mode. Encoding depends on the platform used.

```python
    stream = open(file,mode = 'r', encoding = None)
```
