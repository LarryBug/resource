"""
#1. SyntaxError : invalid syntax" caused by forget ":"

#2. SyntaxError: invalid syntax" caused by "="
"=" isassignment operation, "=" is for compare

error
if spam == 1
    print('Hello!')

    error
if spam = 1
    print('Hello!')

"""
if 1 == 1:
    print('Hello!')

"""#3.
IndentationError: unexpected indent
IndentationError: unindent does not match any outer indetation level
IndentationError: expected an indented block
###should be careful  retract

error:
if spam == 42:
print('Hello!')
"""

"""
#4.TypeError: 'list' object cannot be interpreted as an integer
TypeError: range() integer end argument expected, got list

for cycle forgot len()

Usually you want by index to iterate a list or a string of elements,
this requires the call range () function.
Remember to return len value rather than returning to the list you want,
usually through index to iterate a list or a string of elements,
this requires the call range () function.Remember to return len value rather than return to the list


error:
spam = ['cat', 'dog', 'mouse']
for i in range(spam):
    print(spam[i])

"""
spam = ['cat', 'dog', 'mouse']
for i in range(len(spam)):
    print(spam[i])

"""
#5.
TypeError: 'str' object does not support item assignment
The string is an immutable data types

error
spam = 'I have a pet cat.'
spam[13] = 'a'
print(spam)

"""
spam = 'I have a pet ct.'
spam=spam[:14] + 'a' + spam[14:]
print(spam)

"""#6
Try to connect the int value with string value
TypeError: Can't convert 'int' object to str implicitly

error:
numEggs = 12
print('I have ' + numEggs + ' eggs.')

numEggs = 12
print('I have ' + numEggs + ' eggs.')

"""
numEggs = 12
print('I have ' + str(numEggs) + ' eggs.')

print('I have %s eggs.' % (numEggs))

"""
#7
forgot ""
SyntaxError: EOL while scanning string literal

error:
print('Hello!)
"""
print('Hello!')

"""
#8
Spelling mistakes
NameError: name 'fooba' is not defined

error:
name = 'larry
print('My name is ' + nema)
"""
name = 'larry'
print('My name is ' + name)

"""
#9
function name spelling mistakes
AttributeError: 'str' object has no attribute 'lowerr

error:
spam = 'THIS IS IN LOWERCASE.'
spam = spam.lowerr()
"""
spam = 'THIS IS IN LOWERCASE.'
spam = spam.lower()
print spam

"""
#10.
overstep max vlaue
IndexError: list index out of range
error:
spam = ['cat', 'dog', 'mouse']
print(spam[6])
"""
spam = ['cat', 'dog', 'mouse']
print(len(spam))
print(spam[2])

"""
#11.
use there is no dictionary key values
KeyError:'spam's

error:
spam = {'cat': 'Zophie', 'dog': 'Basil', 'mouse': 'Whiskers'}
print('The name of my pet zebra is ' + spam['zebra'])
"""
spam = {'cat': 'Zophie', 'dog': 'Basil', 'mouse': 'Whiskers'}
print('The name of my pet zebra is ' + spam['cat'])


"""
#12.
use paython keyword
SyntaxError: invalid syntax

Python3 keyword: and, as, assert, break, class, continue, def,
del, elif, else, except, False, finally, for, from, global, if, import,
in, is, lambda, None, nonlocal, not, or, pass, raise, return, True, try, while, with, yield

error:
class = 'class'

"""
class1 = 'class'
print class1


"""
#13.
defined a new values with Value-added operators
NameError: name 'eggs' is not defined

error:
spam = 0
spam += 42
"""
spam = 0
spam += 42
print spam

"""
#14.
defining a local variable before use local variables in the function

UnboundLocalError: local variable 'someVar' referenced before assignment

error:
someVar = 42
def myFunction():
    print(someVar)
    someVar = 100
myFunction()
"""
someVar = 43
def myFunction():
    someVar = 100
    print(someVar)

myFunction()

"""
#15.
python2: rang() return  "list object"
python3: range() return "range object", not "list object", it will has error
typeError: 'range' object does not support item assignmen

error:
spam = range(10)
spam[4] = -1
"""
spam = list(range(10))
print spam[4]

"""
#16.
python no ++,-- it's only in C++, java, php
SyntaxError: invalid syntax

error:
spam = 1
spam++
"""
spam = 1
spam+=1
print spam

"""
#17.
Forgot adding self parameters for first function
TypeError: myMethod() takes no arguments (1 given)

error:
class Foo():
    def myMethod():
        print('Hello!')
a = Foo()
a.myMethod()

"""
class Foo():
    def myMethod(self):
        print('Hello!')

a = Foo()
a.myMethod()