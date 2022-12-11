# Closures

"A closure is a technique which allows the storing of values in spite of the fact that the context in which they have been created does not exist anymore"

A closure is a technique, that has to do with storing values.

## Problem

```python

def outer(x):
    variable = x

a = 4
outer(a)

print(a)
print(variable)

```

This code above produces an error. It attempts to access a local variable that only has exists with in the function itself. The variable is out of the scope when print is called.

## a solution

```python

    def outer(x):
        varaible = x
        def inner():
            return variable
        return inner

```

inner() may be invoked only from within outer().

"...inner() is outer()'s private tool..."


a function has access to the arguments passed in and also to Global variables. When we declare inner() inside of outer(). Inner has access to the local variable of outer. This concept seems to be refered to as a **frozen environment**

The outer() function returns the inner() function itself; more precisely it returns a copy of the inner function.

At the moment of outer()'s invocation. inner() is frozen.

The function returned during the outer() invocation is a **closure**.

**a closure has to be invoked in exactly the same way in which it has been declared** The inner function is parameterless so we must invoke it without arguments.

a closure makes use of the frozen evironment, but also modifies its behavior by using values taken from the outside.

You can create as many closures as you want using one and the same piece of code. done with a function named make_closure()