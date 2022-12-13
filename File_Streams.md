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

## Portability

Depending on the operating system being used, there may be unsupported formatting while reading / saving data. For example, Windows uses the '/r/t' character to denote the end of a line while Unix/Linux like systems use '/n' these differences can lead to an error being rasied when programs and data are being transferred between different operating systems.

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

## File Modes

'r': Permitted to read
'w': Permitted to write
'a': Permitted to append
'r+': Permitted to read and update
'r+t': Permitted to read and update text file
'r+b': Permitted to read and update binary file

'w+' : Permitted to write and update
'w+t': Permitted to write and upate text file
'w+b': Permitted to write and update binary file
'x'  : Exlcusively creates file

If file is not in append mode then the pointer on where to read or write will always start at the first byte of the file. In other words it will overwrite
previous work. If append is used, then the pointer starts at the end of file and will add to the previous work.


### Sys

Importing the sys module will pre-open the three streams 

```python
import sys

sys.stdin
sys.stdout
sys.stderr

```

The seperation of these streams gives the possibility of redirecting information to different targets.

### Sys.stdin

This stream is normally associated with the keyboard. pre-opened for reading

The input() function reads data from stdin

### sys.stdout

stream is normally associated with the screen, pre-opened for writing

The print() funciton outputs the data to the stdout stream

### sys.stderr

Standard error output, associated with the screen where the running program should send information on the errors encountered during its work.

### Closing streams

The last operation performed on a stream should be closing
This doesn't inclued (stdin, stdout and stderr), which will all be automatically closed.

Close() method can fail. When attempting to transfer data to a physcial device, there is a possibility that the data sent to the device has not been successfully transfered by the time the file is closed.

### Diagnosis

IOError, equipped with a property named errno

errno.EACCES -> Permission denied

The error occurs when attempting to open a file that only has read only permission.

errno.EBADF -> Bad file number

to operate with an unopened stream

errno.EEXIST -> File exists

to rename a file with its previous name

errno.EFBIG -> File too large

When trying to create a file that is larger than the maximum allowed.

errno.EISDIR -> Is a directory

treat a directory name as the name of an ordinary file.

errno.EMFILE -> Too many open files

when attempting to open more streams than acceptable for operating system.

errno.ENOENT -> No such file or dir

when attempting to access a non-existent file/dir

errno.ENOSPC -> No space left on device

When there is no free space on the media


### Simplify Error handling code

from the os module there is a function which takes in the error number as the argument, which then returns a string describing the meaning of the error number.

```python

from os import strerror

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))


```

