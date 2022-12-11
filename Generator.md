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

We can use the `list()` constructor, where we pass in a generator as an argument, will populate the list with elements that the function yield.

```python
def fibonacci(n):

    f1 = f2 = 1             # f1 = 1 , f2 = 1
    for i in range(n):      # while (0 <= i < n), for i in [0,n)
        if i in [0, 1]:         # if i = 0 or i = 1 yeld 1.
            yield 1
        else:               
            n = f1 + f2     #  assign the sum of f1 + f2 
            f2, f1 = f1, n  # then assign f2 = f1  , f1 = n
            yield n        # yield n

fibs = list(fibonacci(10))
print(fibs)

```

### conditional expression

a way of selecting one of two different values based on the result of a Boolean expression.

'(expression_one) if (condition) else (expression_two)'

**NOT** a conditional instruction, it is actually an operator.

values provided is equal to `expression_one` when the condition is True`expression_two` otherwise.

```python

    the_list = []
    for x in range(10):
        the_list.append(1 if x % 2 == 0 else 0)
    
    print(the_list)

```

The above code can be made into a list comprehension.

``` python

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]

print(the_list)

```

A change from brackets to parantheses, of a list comprehension, will produce a generator.

```python
    for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
        print(v, end=" ")
    print()

    for v in (1 if x % 2 == 0 else 0 for x in range(10)):
        print(v, end=" ")
    print()
```

## Lambdas

```python
    doSomething = lambda parameter1,parameter2: parameter1 + parameter2
```

We can use lambas as arguments passed into function, that will map the values according to the function

```python

    def print_function(args,fun):
        for x in args:
            print('f( ', x, ') =', fun(x), sep='')

    print_function([x for x in range(-2,3)], lambda x: 2 * x**2 - 4 * x + 2)

```

In the snippet above we passed in a list comprehension and a lambda expression. The elements in the list will be passed into and evaluated by the lambda.

From a design perspective
    Notice how the `print_function()` has an independent purpose/action. That no matter what the arguments are, the print function will do its best to print whatever it is given. Its nice and simple. Each function having a strict role, does greatly simplify reading code.
