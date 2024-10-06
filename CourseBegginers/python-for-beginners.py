# # Python, Installation, Jupyter, NumPy, & Matplotlib
#
# A refresher for getting started with Python
#
# Matt Harrison - metasnake.com @\_\_mharrison\_\_


# # Overview
#
# -   Why Python?
# -   Jupyter
# -   Python
# -   NumPy
# -   Matplotlib

# # Why?
#
#
# -   People who aren\'t CS can pick it up quickly. (Engineers, admins,
#     scientists)
# -   300,000+ packages!
# -   Easy to get started
# -   Taught at Schools (MIT, Stanford, etc)

# ## For What?
#
# -   Cloud/Admin
# -   Embedded Logic
# -   Micro-controllers
# -   Web development
# -   Data Science
#

# # Installation
#
# Two options:
#
# -   Anaconda
# -   Python.org

# ## Anaconda
#
# -   Pre-compiled meta-distribution
# -   Includes many scientific libraries
# -   Can create \"environments\"

# ## Basic Setup Steps
#
# -   Install Anaconda (for Python 3) from anaconda.org
# -   Launch Ananconda Prompt (or terminal) and create an environment:
#
#         conda create --name condaenv python=3.9
#
# -   Activate the environment:
#
#         conda activate condaenv
#
# -   Install libraries:
#
#         conda install notebook numpy matplotlib
#
# -   Launch Jupyter:
#
#         jupyter notebook

# ## Python from python.org
#
# -   Just \"Python\" (including standard library)
# -   Need to install libraries into virtual environments

# ## Basic Setup Steps
#
# -   Install Python 3
# -   Launch a terminal or command prompt and create a virtual
#     environment:
#
#         python3 -m venv pyenv
#
# -   Activate virtual environment
#     -   Windows:
#
#             pyenv\Scripts\activate
#
#     -   Unix (Mac/Linux):
#
#             source pyenv/bin/activate
#
# -   Install libraries:
#
#         pip install notebook numpy matplotlib
#
# -   Launch Jupyter:
#
#         jupyter notebook

# ## Pros/Cons
#
# -   Traditionally setting up system to build libraries as painful
#     (especially on Windows)
# -   For \"basic\" libraries doesn\'t really matter
# -   For some libraries (GPU) might be easier with Conda

# # Jupyter
#
# A REPL with two modes:
#
# -   Command
# -   Edit

# ## Command Mode
#
# -   `a` - Above
# -   `b` - Below
# -   `CTL-Enter` - Run
#     -   `c`, `x`, `v` - Copy, cut, paste
# -   `ii` - Interrupt Kernel
# -   `00` - Restart Kernel (zero two times)

# ## Edit Mode
#
# -   `TAB` - Completion
# -   `Shift-TAB` - Documentation (hit 4x to popup)
# -   `ESC` - Back to command mode w/o running
# -   `CTL-Enter` - Run

# ## Hints
#
# -   Add `?` to functions and methods to see docs
# -   Add `??` to functions and methods to see source
# -   Add cell magic to make matplotlib plots show up:
#
#         # %matplotlib inline
#
# -   See cell magics:
#
#         # %lsmagic

# %lsmagic

# %%timeit?

# ## Not really an editor
#
# When I\'m writing code to deploy I use an editor. When I\'m exploring
# data, I use Jupyter.

# ## Other Options
#
# -   Jupyterlab
# -   VSCode
# -   Pycharm
# -   Emacs















# # Python

print('hello world') 


import this

status = 'off'


# Variables don't have a type (note `a` is a horrible variable name)

a = 400

a = '400'

# Everything in *Python* is an object that has:
#
# * an *identity* (``id``)
# * a *type* (``type``).  Determines what operations object can perform.
# * a *value* (mutable or immutable)
# * a *reference count*


id(a)

type(a)

import sys
sys.getrefcount(a)













# ## Literals

name = 'matt \N{GRINNING FACE}'  # literal
age_string = str(40)  # using str constructor
name


# Constructor in parens
age = 40   # integer literal (int)
cost = 5.5   # float literal (float)
loc = 1+0j   # complex literal (complex)


# List literal
names = [name, 'suzy', 'fred']
characters = list('aeiou')  # constructor


# Constructor is different than literal
characters = list('aeiou')  # constructor
characters


['aeiou']


# Tuple literal
person = ('fred', 42, '123-432-0943', '123 North Street')
person2 = tuple(['susan', 43, '213-123-0987', '789 West Ave'])


person2


# Dictionary
types = {'name': 'string', 'age': 'int'}
ages = dict(zip(['fred', 'suzy'], [20, 21]))
types2 = dict(name='string', age='int')


# +
# dict?
# -

ages


types2


# Set
digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
unique_chars = set('lorem ipsum dolor')
unique_chars


# Where are the built-in constructors?
print(dir(__builtins__))


# ### Lookup hierarchy
#
# * Local - function/method
# * Enclosed - nested function/method
# * Global 
# * Builtin
# * Name error!

# NameError
missing

# ### Naming
#
# See PEP 8  http://legacy.python.org/dev/peps/pep-0008/
#
# * lowercase
# * underscore_between_words
# * don't start with numbers











# ## Math

# Addition, subtraction, multiplication, division, modulus
42 + 10


42 ** 100


57 % 2  # modulus (remainder)


# Number Tower Hierarchy: int, float, complex
3 + 4.5


1 - (2+4j)


# Integers are Objects!
print(dir(42))


help((42).bit_length)


42.bit_length()


(42).bit_length()


# ### "Dunders"
#
# Double underscore, magic, or special methods. We don't usually call the "dunder" method, but Python does for us.



42 + 10


(42).__add__(10)

















# # Getting Help

# ### Basics
#
# * Internet search
# * IDE/Tool popup
# * REPL
# * Jupyter specific

# ### Internet Search
#
# Use as a last resort. This will distract you and make you less productive.

# ### IDE/Tool Popup
#
# Many Editors/IDEs have the ability to show documentation and parameters.

help(len)


def adder(x, y):
    "Adds two values"
    return x + y


help(adder)


# Help mode (hit ENTER to exit)
help()


# Use ``dir`` to inspect an object
dir('a string')


# +
# adder?

# +
# adder??
# -












# ## Conditionals

grade = 82
if grade > 90:
    print("A")
elif grade > 80:
    print("B")
elif grade > 70:
    print("C")
else:
    print("D")


5 > 9


'matt' != 'fred'


isinstance('matt', str)


# ``and``, ``or``, ``not`` (for logical), ``&``, ``|``, and ``^`` (for bitwise
x = 5
x < -4 or x > 4















# # Iteration

for number in [1,2,3,4,5,6]:
    print(number)


number

for number in range(1, 7):
    print(number)

# Returns an iterable containing numbers from start up to but not including end
range(6)


list(range(6))


list(range(2, 6))


# ### ``range`` 
#
# Python tends to follow *half-open interval* (``[start,end)``) with ``range`` and *slices*:
#
# * end - start = length
# * easy to concat ranges w/o overlap (ie ``list(range(3)) + list(range(3,9))``)


# Java/C-esque style of object in array access (BAD):
animals = ["cat", "dog", "bird"]
for index in range(len(animals)):
    print(index, animals[index])

#If you need indices, use ``enumerate`` (to replace ``range(len(a_list))``):
animals = ["cat", "dog", "bird"]
for index, value in enumerate(animals):
    print(index, value)

index

value

animals = ["cat", "dog", "bird"]
for index, value in enumerate(animals):
    if value == 'dog':
        break
    print(index, value)

animals = ["cat", "dog", "bird"]
for index, value in enumerate(animals):
    if value == 'dog':
        continue
    print(index, value)

# Can loop over lists, strings, iterators, dictionaries... sequence-like things
my_dict = { "name": "matt", "cash": 5.45}
for key in my_dict:  # loop over keys
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)











# ## Strings & Unicode

name = 'paul'


print(dir(name))


help(name.upper)


name.upper()


name.title()


name.find('au')


name[0]


name[-1]


name[len(name) - 1]


greeting = 'Hello \N{GRINNING FACE} \U0001f600 😀'
greeting


# Encoding to binary
greeting.encode('utf8')


greeting.encode('utf8').decode('utf8')


paragraph = """Greetings,
Thank you for attending tonight.
Long-winded talk.
Goodbye!"""


# f-strings
minutes = 36
paragraph = f"""Greetings {name.title()},
Thank you for attending tonight.
We will be here for {minutes/60:.2f} hours
Long-winded talk.
Goodbye {name}!"""
print(paragraph)


# formatting following a ":"
name = 'Ringo'
f"Name: {name:*^12}"


per = -44/100
f"Percent: {per:=10.1%}"


f"Binary: {12:b}"


f"Hex: {12:x}"















# ## Files

fout = open('names.csv', mode='w', encoding='utf8')
fout.write('name,age\n')


fout.write('jeff,30\n')


fout.write('linda,29\n')


fout.close()


# The  ``with`` statement will automatically close your files. (Also used in plotting and setting pandas parameters)
with open('names.csv', mode='w', encoding='utf8') as fout:
    fout.write('name,age\n')
    fout.write('jeff,30\n')
    fout.write('linda,29\n')


# file is automatically closed when we dedent    
fout.write('bad,42\n')


print(dir(fout))


help(fout.write)


# +
# fout.write?
# -


with open('names.csv', encoding='utf8') as fin:
    data = fin.read()
data


with open('names.csv', mode='rb') as fin:
    one_byte = fin.read(1)
    ten_bytes = fin.read(10)
one_byte


ten_bytes.decode('utf8')


# Careful with Encoding
with open('unigreeting.txt', 'w', encoding='utf8') as fout:
    fout.write('Hello \N{GRINNING FACE}')


greeting = open('unigreeting.txt', 'r', encoding='utf8').read()
greeting


greeting = open('unigreeting.txt', 'r', encoding='windows_1252').read()
greeting


greeting = open('unigreeting.txt', 'r', encoding='ascii').read()


greeting = open('unigreeting.txt', 'r', encoding='windows_1252').read()
greeting


greeting.encode('windows_1252')


greeting.encode('windows_1252').decode('utf8')


import encodings
print(sorted(encodings.aliases.aliases))
















# ## Lists

# Literal vs constructor
names = ['john', 'paul', 'george']


vals = list(range(4))
vals


print(dir(names))


# +
# names.append?
# -


help(names.append)


# Mutation!
names


names.append('ringo')


names


names.index('paul')


names[1]


names.__getitem__(1)


names


names[1] = 'Paul'
names


'paul' in names


# These operations dispatch to "dunders"
names.__contains__('paul')















# ## Slicing

names = ['john', 'paul', 'george', 'ringo']


# When you need the index as well as item of enumeration
enumerate(names)


# Defeat Laziness - With constructor, not literal!
list(enumerate(names))


[enumerate(names)]


list((i - len(names), n)
    for i, n in enumerate(names))


names[0]


names[-1]


# ### Half-open Interval
#
# Two properties:
#
# * Includes start index but not end
# * length = end - start


names[0:3]


names[:3]


names[3]


names


names[3:]


names[-2:]


# Shallow Copies
names2 = names[:]
id(names2)


id(names)


names[0] is names2[0]


names == names2


names is names2


# Stride
names[::-1]


list(range(10))


list(range(10))[::3]


# Slicing a string
filename = 'resume.pdf'
filename[:4]


filename[4]


filename[-3:]


filename[::-1]















# ## Dictionaries
# Map keys to values. Called associative arrays or hashmaps in other languages.

hash('name')


hash('name') % 30


hash([])


# Literals and constructors
types = {'name': str, 'age': int, 'address': str}
types2 = dict(name=str, age=int, address=str)


# The "key" (``'name'``) must be hashable:
types['name']


# "Index assignment". Note that this mutates
types['language'] = str
types


types['food']


types.get('food', 'missing')


'food' in types


dir(types)

# ### Python 3.6+ Note
# Remember key insertion order.














# ## Comprehensions
# Common pattern, looping, mapping (optional), filtering (optional), and accumulating.


# pattern for list comprehension
names2 = []
for name in names:
    if len(name) == 4:  # filter
        names2.append(name.title())  # title is mapping
names2


names2 = [name.title() for name in names if len(name) == 4]

names2 = [name.title() for name in names if len(name) == 4]
names2


# Dict Comprehensions
types = {'name': str, 'age': int, 'address': str}


new_names = {}
for t in types:
    new_names[t] = t.title()
new_names


new_names = {t: t.title() for t in types}

new_names = {t:t.title() for t in types}


# Set Comprehensions
uniq_names = {name for name in names if len(name) == 4}


# Generator Expression
lazy_names = (name for name in names if len(name) == 4)

list(lazy_names)












# ## Functions and Lambdas


def add(x, y):
    """This adds two values
    >>> add(2, 4)
    6
    """
    return x + y


add(2, 4)


add


# +
# add?


# +
# add??
# -

help(add)


def median(values):
    '''
    Return the middle value (if odd) 
    or the average of the two middle values (if even)
    >>> median([1, 4, 5])
    4
    >>> median([0, 2, 6, 100])
    4.0
    '''
    values = sorted(values)
    size = len(values)
    if size % 2 == 0:
        left = values[int(size/2 -1)]
        right = values[int(size/2)]
        return (left + right)/2
    else:
        return values[int(size/2)]


median


median(range(100))


median([100,1, 200])


# Tuple aside - Record-type data
person = ('Paul', 'McCartney', 'Bass')


type(person)

# Tuple - Return multiple items from a function
def roots(val):
    return (val**.5, -(val**.5))


roots(4)

# Lambda - One-line anonymous function
def adder(x, y):
    """This adds two values
    >>> add(2, 4)
    6
    """
    return x + y


adder2 = lambda x, y: x + y
adder(42, 10) == adder2(42, 10)


def roots(val):
    return (val**.5, -(val**.5))


roots2 = lambda val: (val**.5, -(val**.5))


roots2(64)


# Lambdas in sorting
names = ['john', 'paul', 'george', 'ringo']


sorted(names)


sorted(names, key=lambda name: len(name))


# ### Lambda Uses
#
# * Useful for "key" functions when sorting
# * Pandas creating columns with ``.assign``














# # Modules & Packages
# * Module - Python file
# * Package - Directory with ``__init__.py`` file (and other packages or modules)

import math
import pandas as pd


math


pd


dir(math)


math.sin(0)


df = pd.read_csv('names.csv')


# %%writefile sample.py
def median(values):
    '''
    Return the middle value (if odd) 
    or the average of the two middle values (if even)
    >>> median([1, 4, 5])
    4
    >>> median([0, 2, 6, 100])
    4.0
    '''
    values = sorted(values)
    size = len(values)
    if size % 2 == 0:
        left = values[int(size/2 -1)]
        right = values[int(size/2)]
        return (left + right)/2
    else:
        return values[int(size/2)]
roots2 = lambda val: (val**.5, -(val**.5))


import sample
sample


dir(sample)


sample.median


sample.median(range(20))











# # Classes
# Everything is an object. You can define your own class to group common actions with data.

class MyInt:
    '''Docstring for MyInt'''
    def __init__(self, val):
        self.value = val


    def __add__(self, other):
        return MyInt(self.value + other)


    def __repr__(self):
        return f'MyInt({self.value})'


    def __str__(self):
        return f'{self.value}'


    def square(self):
        "Return the square of the value"
        return MyInt(self.value**2)


MyInt


num = MyInt(42)
num + 5  # calls .__add__ the .__repr__ methods


num.__add__(5)


num - 5


print(num)  # calls .__str__


num

# +
# In Jupyter use ``??`` to see source code
# MyInt.square??
# -




















# # Exceptions

# NameError - Generally means you typoed the name or forgot to import something
missing


names = ['john', 'paul', 'george', 'ringo']
names.find('fred')


types = {'name': str, 'age': int, 'address': str}
types['missing']


try:
    types['missing']
except KeyError:
    print("missing is not a key")


# Can also subclass and raise errors
raise KeyError('Key was missing')


dir(__builtins__)















# # NumPy

# * N-Dimensional arrays
# * Overcome slowness of Python

# ## Secret of NumPy
#
# There are not 10 Python integers under the covers:


import numpy as np
digits = np.array(range(10))
digits


slow_digits = list(range(10))


digits.dtype


# Operations
digits.shape


digits + 10


digits + digits


np.sin(digits)


# Creation
np.arange(3)


np.ones(3)


np.zeros(3)


np.eye(3, 5)


# +
# np.eye?
# -

np.diag(range(3))


np.linspace(0, 10, num=15)


# Random Creation
np.random.random(3)  # between [0,1)


rng = np.random.default_rng()
rng.integers(low=11, high=15, size=5)  # 5 between [11,15)


np.random.bytes(5)  # 5 bytes


np.random.randn(3)  # normal distribution















# ## More NumPy


# Array Features
dir(digits) 


len(dir(digits))


digits.mean()


# NumPy Features
dir(np)  


len(dir(np))


np.log(digits)


np.log(digits+1)















# # NumPy Dimensions

nums = np.arange(100).reshape(20, 5)
nums 


nums.transpose() 


# Axis - Two-dimensional
nums 


nums.mean()


nums.mean(axis=0)


nums  


nums.mean(axis=1)


nums.mean(axis=1, keepdims=True) 


# Three Dimensions
b = np.arange(70).reshape(7,5,2)
b  


b.mean(axis=0)


b.mean(axis=1)


b.mean(axis=2)


##  NumPy Indexing & Slicing
# Similar to Python, but not limited to one dimension:
nums 


nums[0]  # row 0


nums[[0, 5, 10]]  # rows 0,5,10


# Can slice along multiple dimensions:
nums[0:10]  # first 10 rows


nums[:, 0:3]  # all rows, 3 cols 














# #   Boolean Arrays

nums 


nums % 2 == 0


# Used as a filter
nums[nums % 2 == 0]


# Select rows where sum is less than 100
nums.sum(axis=1)


nums.sum(axis=1) < 100


nums[nums.sum(axis=1)< 100]


# Select columns where mean > 50:
nums.mean(axis=0)


nums.mean(axis=0) > 50


nums[:, nums.mean(axis=0) > 50] 




# ## NumPy Example

# Example - Standardize data. Each column has a mean value of 0 and a standard deviation of 1
import sklearn.datasets
iris = sklearn.datasets.load_iris().data
iris 


iris_z = (iris - np.mean(iris))/np.std(iris)
iris_z 


np.mean(iris_z)


np.std(iris_z)














# # Matplotlib

# ## Figure and Axis Creation

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 10, 0.2)
y = np.sin(x)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
plt.savefig('pyplot1.png', dpi=300)


from pylab import *
x = arange(0, 10, 0.2)
y = sin(x)
plot(x, y)
savefig('pylab1.png', dpi=300)


fig = plt.figure()
fig.set_size_inches((8.5, 4))


# single axes - position values are 0-1
left, bottom, width, height = .1, .2, .7, .5
ax = fig.add_axes((left, bottom, width, height))
ax.plot(x, y)
ax2 = fig.add_axes((.9, .9, .1, .1))
ax2.plot(x, y)
fig


# 3 axes - 1 row 3 cols (grid)
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
for ax in axes:
    ax.plot(x, y)




# 1 axes - 1 row 2 cols 2nd postition
ax = plt.subplot(122)  # or 1,2,2
ax.plot(x, y)


x = np.arange(0, 10, 0.2)
y = np.sin(x)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, color='r',
  linewidth=3, linestyle='--')
fig.savefig('img/pyplot2.png', dpi=300)















# ## Plot Types
#
# Matplotlib supports a variety of plots out of the box.

# Line Plot
fig, ax = plt.subplots()
ax.plot(x, y)

# Bar Plot
fig, ax = plt.subplots(figsize=(10,8))
ax.bar(x, y)

# Bar Plot
# width may need to be tweaked
fig, ax = plt.subplots(figsize=(10,8))
ax.bar(x, y, width=.02)

# Scatter Plot - Using .scatter can be slower than plot. Use .scatter when you want to 
# tweak attribute
fig, ax = plt.subplots(figsize=(10,8))
ax.scatter(x, y, marker='o', alpha=.5)

# Scatter Plot - test
fig, ax = plt.subplots(figsize=(10,8))
ax.plot(x, y, marker='o', alpha=.5, color='pink', markeredgecolor='red',
        markerfacecolor='black', markeredgewidth=3)


# Scatter Plot - Using .scatter can be slower than plot. Use .scatter when you want to 
# tweak attribute
fig, ax = plt.subplots(figsize=(10,8))
ax.scatter(x, y, marker='o', alpha=.5)

# Scatter Plot - Using .scatter can be slower than plot. Use .scatter when you want to 
# tweak attribute
fig, ax = plt.subplots(figsize=(10,8))
ax.scatter(x, y, marker='o', c=x, cmap='viridis', alpha=.5)

# boxplot
fig, ax = plt.subplots(figsize=(10,8))
_ = ax.boxplot(x, #vert=False
              )

# boxplot
fig, ax = plt.subplots(figsize=(10,8))
_ = ax.boxplot([x, x+2, x-3], labels=['Norm', '+2', '-3'])

# violin plot
fig, ax = plt.subplots(figsize=(10,8))
_ = ax.violinplot([x, x+2, x-3])

# Histogram 
fig, ax = plt.subplots(figsize=(10,8))
ax.hist(y)

# Histogram
fig, ax = plt.subplots(figsize=(10,8))
_ = ax.hist(y, bins=100)

# Pie
fig, ax = plt.subplots(figsize=(10,8))
_=ax.pie([10, 5], labels=['10', '5'])
ax.legend()



