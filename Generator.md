# Generators

A generator returns a series of values. Generally, implicity invoked more than once. It is capable of save and restore its state between subsequent invocations.

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

## Iterators

**iterator prorocol** When defining a custom object that we want to be able to iterate through, we can define an object to confrom to the rules imposed by the context of the for and in statements.

**iterator** An object conforming to the iterator protocol.

`__iter__()` returns the object itself, invoked once.

`__next__()` invoked by the `for`/`in` statements. intended to return the next value of the desired series. If there are no more values to provide, the method should rais a **StopIteration** exception.

```python
class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")    
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

for i in Fib(10):
    print(i)
```

## YIELD

The problem mentioned earlier, about making a function which acts like the range function. The problem with implementing it in the fashion that we normally implement functions is that we are not able to save and restore its state between susequent invocations.

Below is an example of a generator.

```python

    def fun(n):
        for i in range(n):
            yield i

    for v in fun(5):
        print(v)

```

The above code looks like a function however it should not be invoked explicitly. Once the yield keyword is used, it is no longer a function; it is a generators object. The invocation will return the objects identifier.

