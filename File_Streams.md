# File Streams

## Modes

read mode: allows read operations only
write mode: write operations only
update mode: both reads and writes

exceptions raised if these are not used properly
*UnsupportedOperation*, *OSError*, *ValueError*. Each of these exceptions are from the **io** module


## File Handles

an object of an adequate class is created when you open the file and annihilate it at the time of closing.

The operations we are allowed to use are determined by the way we open them.

a handler object is created when a file is opened and when its life cycle comes to an end when we decide to close that file.

The object created, at the time of openning, comes from 
**IOBase** and is of the three **RawIOBase**,**BufferedIOBase** , **TextIOBase**

We will only focus on the streams represented by **BufferIOBase** and **TextIOBase**

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

### readline and readlines

**readline** will read one line and return it as a string. If it is currently at the end of file, else it will return an empty string

**readlines** tries to read all the file contnets, and returns a list of strings, one element per file line (A[0] = line1,
A[i] = line(i+1) ). We are also able to pass in an **maximum accepted input buffer** integer(n) argurment into the readlines method. Doing so will only read (n) lines of a file. When the EOF is reached, readlines returns and empty list.

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
