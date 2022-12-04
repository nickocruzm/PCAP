# Generators

A generator returns a series of values. Generally, implicity invoked more than once.

For example the range() function is a generator.

```python

for i in range(5):
    print(i)

```

How would we implement a range() function which returns multiple value, but doesn't terminate the function? It is not possible using the standard return keyword. Since return will cause the function to terminate.

```python

def fake_range(n):
    return n

```
