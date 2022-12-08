# File Streams

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
