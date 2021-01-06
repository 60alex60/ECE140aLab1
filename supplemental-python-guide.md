## Introduction
This will be a quick guide to some important concepts in python, you should have seen most of these in other programming laguages as well.

Before continuing, be sure to have finished a python tutorial as stated in the lab writeup.

# Contents:
1. [Variable Assignment and Python basics syntax](##1.-variable-assignment-and-syntax)
2. [Execution control (loops, logic)](##2.-execution-control)
3. [Try/except clauses (error catching)](##3.-error-handling)
4. [Functions (also known as methods)](##4.-functions)
5. [Objects](##5.-objects)
6. [Libraries](##6.-libraries)



## 1. Variable Assignment and Syntax

### 1.0 Variable Types

Python is a dynamically typed language. This means you do not need to declare variable types when assigning, however there most certainly are variable types in Python (it is strongly but implicitly typed)!
For example:

```python
a = 's'
b = 1
c = 1.0
d = [1,2,3]
e = "string"
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
```

Will print:

```bash
<class 'str'>
<class 'int'>
<class 'float'>
<class 'list'>
<class 'str'>
```

A couple things of note here:

1. There are no 'chars' vs. "strings". A 'char' is simply a "string" of length 1. Strings are always arrays.

    ```python
    for char in "hello":
        print(char)
    char = 'a'
    print(char[0])  # even a single character is still a string array!
    ```

2. When we typed `1.0`, Python "inferred" that we wanted a float (it could not be an int), but when we typed `1` Python verified that this could be an int so it chose that. If you want to force a type, you can do it as follows:

```python
b = float(1)
c = int(1.0)  # note that this will truncate, NOT round!
```

### 1.1 List Syntax

Lists are the basic "iterable" (array) in Python. Lists are an ordered collection of other objects. These objects need not be of the same type and can even be other lists! There are other types of arrays, including strings, tuples, and sets. We will probably only ever use lists, strings, and tuples in this course, but you are encouraged to try and understand all of the data types available to you since the optimal choice depends on your specific use case.

```python
a = [1, 2.5, "string"]
b = [0, None]
c = a + b
d = [a, b]
for sublist in d:
    print("Working on sublist: " + str(sublist))
    for element in sublist:
          print(type(element))
```

Again, do not worry about the nested loops yet!

To acess elements in a list or part of a list, we use slices. Slices with postive numbers denote "from the start of the list" and negative numbers denote "from the end of the list".

Slicing syntax is: `list[start:stop:step]`. For example:

```python
a = [1, 2, 3, 4, ["firstelemlist2", "secondelemlist2"]]
print(a[0])
print(a[0::2])
print(a[-2])
print(a[-1][0])
```

### 1.2 Mutability

You may have heard about mutable vs. immutable objects in Python. What this means is: can we make changes to this object in memory, or do we have to re-assign it?

This may be easier to understand in practice.

```python
# Example of an unmutable object
a = 1
b = a
a = 2
print(b) # prints 1

# Example of a mutable object
a = [1,2]
b = a[:]
a[0] = "new_item"
print(b) # prints [1,2]
```

Floats and ints are *immutable* while lists are *mutable*. In most situations, lists will usually be the only mutable objects you will encounter.

The other commonly used "iterators" that you may confuse with lists at first are tuples. Tuples are commonly used in variable assignments, while lists are generally used in iterations:

```python
# Example use of a tuple
tup = ("a", "b", "c")
tup[1] = "d"
# An error should be raised, but if not:
print(tup)
# Youl see no changes to the items in 'tup'

# A common use is to assign multiple return values with tuples:
def my_function():
    a = 1
    b = 2
    tup = (a,b)
    return tup
x, y = my_function()
print(x)
print(y)

# Note that this is a trivial function and is equivalent to:
def my_function():
    return 1, 2
```

So **why** are there mutable and inmutable objects in Python? Here is the breakdown:

Mutable:

  1. Modify: fast
  2. Read: slow

Immutable:

  1. Modify: slow (need to make a copy to edit)
  2. Read: very fast

### 1.3 Python Programs (Modules)

Programs in Python are called modules and end with the .py file extension. Unlike C/C++, you will discover that there is no compiler in Python. This is because Python is an _interpreted_ language, meaning that the code that you write automagically gets interpreted into a lower-level subroutine that has already been precompiled down to machine-readable code. This means that in order to run a Python module, you simply have to invoke the Python interpreter. For example, if you wrote a module named "foobar.py" and wanted to run it, you would simply open a terminal window and run the command:

```bash
python foobar.py
```

NOTE: make _**SURE**_ that you are using Python 3. As of 2020, Python 2 has official been deprecated and there will be no more support for it. To check what version of Python you are using, you can issue the command:

```bash
python -V
```

This should print out "Python 3.x.x" where the x's will be the specific version of Python 3 you have installed. If it shows you are still on Python 2, please install Python 3 before procedding any further.


## 2. Execution Control

Like most other languages you have probably used, Python has while loops, for loops, and execution control (such as if/else) statements. Let's start with for loops.

### 2.0 For Loops

We assume that most are familiar with the logical operation of a for loop. The main difference Python has with other languages is the syntax of the for loops. In C you might write:

```c
char data[] = {'a','b','c'};
for (int i=0; i<3; i++) {
    printf("%c\n", data[i]);
}
```

If you write C-style Python, you might get something like below. It works, but it's not "Pythonic":

```python
data = ['a','b','c']
for i in [0,1,2]:
    print(data[i])
```

The "Pythonic" way to do this is to focus on simplicity and elegance, like you see below:

```python
data = ['a','b','c']
for char in data:
    print(char)
```

### 2.1 While Loops

While loops in Python are relativley "unremarkable" compared to other Python constructs.

```python
i = 0
while i < 10:
    i += 1
```

Using more complex logic:

```python
import numpy as np

data=[]
while len(data) < 10:
    data.append(np.random.rand())
```

Note that we need to define `data` and `i` before the loop starts. Python does not offer the ability to create the counter variable in the loop syntax. In fact, the general use of counter variables is highly discouraged.

### 2.2 If Statements & Logic Control

We have used some boolean logic in the examples above. The only clarifications to make are:

  1. In Python (as in most languages) int(0) and int(1) have boolean values (0 == False and 1 == True).
  2. True/False *must be capitalized* to be detected as booleans (to constrast with variable names).
  3. Boolean operators are:
     1. "not": `if not (2<1):`
     2. "or"   `if (a<10) or (a>20):`
     3. "and"  `if not (2<1) or (a==10 and True):`

Boolean logic can also be used to test existence of objects:

```python
a = None
b = []
if not a:
  print("a is boolean false, Nonetype evaluates to False")
if not b:
  print("b is boolean false, like all empty lists")
```

As far full **if conditional statements**, the syntax is:

```python
if <condition>:
  pass
elif <condition>:
  break
else:
  pass
```

Now let's look at those `pass` and `break` keywords!

### 2.3 Execution Control Keywords

There are special keywords that allow you to break out of a logic block (loop, while, if, etc.), continue onto the next iteration of a loop, skip it, etc.

```python
for number in range(10):
    if number == 2:
        pass
        print("this will get executed")
    elif number == 5:
        continue
        print("this will not get executed")
    elif number == 9:
        print("this will not get executed because of the break statement below")
    elif number == 8:
        break
    else:
        print(number)
```


## 3. Error Handling

### 3.0 Try-except Blocks

Often times (like with external libraries!) you may encounter errors. Python gives us the functionality to catch these errors and deal with them accordingly. Try running this example *without* any error catching:

```python
items = [1.1,2.2,3.3,"upsie"]
for item in items:
    print(int(item))
```

Now try it *with* error catching:

```python
items = [1.1,2.2,3.3,"upsie"]
for item in items:
    try:
        print(int(item))
    except ValueError:
        print(item)
```

Note that while it is not *required* to specity which type of error to catch, it is good practice to do so to avoid catching unexpected errors. For example, see what happens if we had a typo and did not specify the type of error to catch. Here the undefined variable is caught, but then our exception fails because the error did not come from the typecasting as expected but rather from the typo in the variable name ("iem" instead of "item"):

```python
items = [1.1,2.2,3.3,"upsie"]
for item in items:
    try:
        print(int(iem))
    except:
        print(item)
```

### 3.1 Assertions

Assertions are an easy way to verify function arguments are what we expect (great for test-driven design!):

```python
def add_ints(int1, int2):
  try:
      assert (isinstance(int1, int) and isinstance(int2, int)), "Inputs must be integers!"
      print("Inputs are confirmed to be ints")
      return int1+int2
  except AssertionError:
      print("Attempting to cast to int")
      try:
          int1 = int(int1)
          int2 = int(int2)
          return int1 + int2
      except ValueError:
          print("Could not cast to int, inputs are not a number")
          return None
```

Test:

```python
add_ints(1,2)
add_ints(1,2.0)
add_ints(1,"nope")
```


## 4. Functions

In Python programming, functions accept intputs, perform actions, and give outputs, but none of these are mandatory! The most basic function is:

```python
def function():
    pass

# this function call does nothing
function()
```

Notice that there is a `pass` statement in the function. Python is very demanding with indentation. If you do not put *any* statement in the function, Python does not know where your function starts/ends. This also applies to if/else statements or any other statements with indentation.

Also, note that there are no inputs or outputs in this function. Python does not require for you to assign any output value. However, you can put a `return` statement anywhere in your function to force it to return from the function with or without output values.

### 4.0 Function Syntax

Function inputs come in four basic types:

1. Required
2. Default (optional)
3. Keyword
4. Variable length

```python
def my_function(required_argument, optional_argument="default value", *extra_args):
    print(required_argument)
    print(optional_argument)
    if extra_args:
        print(extra_args)
    for extra_arg in extra_args:
        print(extra_arg)
        if extra_arg == 5:
            return "got the number "+str(extra_arg)    # this is just to demo return statements
```

Notice that required arguments must always come before optional arguments.

You can call functions using the keyword arguments or without them. Using keyword arguments allows you to switch the order of input parameters without affecting the result (i.e. you don't need to remember the order of arguments for each function).

```python
my_function("test", "okay", "extra 1", "extra 2")
my_function(optional_argument="okay", required_argument="test")
```

Note that the follwing ordering does not work.

```python
my_function(required_argument="test", "okay")
SyntaxError: positional argument follows keyword argument
```

### 4.1 Variable Scope

Unless you use the keyword global, variables are by default local. You can access global variables from inside an enclosing scope but not modify them, unless you explicitly use the `global` keyword before it.

```python
global_var1 = 123
global_var2 = 321

def function():
    local_var = 567

    # only accessing global_var1
    print(global_var1)

    # accessing and modifying global_var2
    global global_var2
    global_var2 = 42
    print(global_var2)
    return

function()

try:
    print(local_var)
except NameError:
    print("Variable does not exist!")
```


## 5. Objects

In traditional programming languages, the notion of Object-Oriented Programming has been a paradigm shift in how software is constructed. This is one of the largest differences between the C and C++ languages. However, Python has been built from the ground up with the notion of objects implicitly included, so almost every data type is really an object of one kind or another. We do not have the bandwidth to cover the basics of OOP in ECE 140, but if you have taken ECE 16, you would have worked with them extensively. If you have never seen classes and objects in Python, here is the basic signature of a Python class with a simple counter:

```python
class MyFancyCounter:
    # attributes of the class
    __my_count__ = 0

    # class constructor
    def __init__(self, starting_count=0):
        self.__my_count__ = starting_count

    # a method of the class
    def count(self):
        self.__my_count__ += 1
        return self.__my_count__
```

Then usage of the class is simple:

```python
counter = MyFancyCounter()
for i in range(10):
    print(counter.count())

# this will print out the numbers 0, 1, 2, 3... 10
```

There you have it! Your very own object!


## 6. Libraries

Libraries (aka packages) in Python are simply an organizational construct. It's a simple way to package up a bunch of modules together under a common namespace, but the reality is that all you have to do is put an empty file named __init__.py inside the folder and you Python will identify it as a library. You won't have to know much more than that for this class, but you will use many existing libraries extensively. In order to import a library, you can do it in one of the following ways:

```python
import time            # import the entire time library as a single huge object
now = time.time()
print(now)

from time import time  # import just the sleep module from the time library
now = time()
print(now)

```

So we just saw that modules can be both imported into other modules and that they can be run as executables. In order to allow Python to differentiate which is happening, a common convention is to place this snippet of code at the end of the module:

```python
if __name__ == '__main__':
    # run code as if it is being executed from the command line
```

If the module is being run as a program, then that condition will be true and the program will run. Otherwise, your module will behave as part of a package that will be included in some other program (like we just did with the time example above).


