#!/usr/bin/env python3
#coder
print("Hello. Welcome to CodeRunner!")
the_world = True
if the_world:
    print("Hello, World")

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    """Document parrot.
    
    It is a bird calling definition that parrots the arguments
    following anything that is long
    or short of it
    so this is line 3
    and this is line 4
    finally the end.

    not really...
    """
    
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
    print("-- This parrot wouldn't", action)
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    print()
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
parrot(type='type', action="action", state='state', voltage='voltage')
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
print(pairs)
pairs.sort(key=lambda pair: pair[1])
print(pairs)
print(parrot.__doc__)
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b
    
print()
c, d = 0, 1
print(0, end='')
while c < 1000:
    c, d = d, c+d
    print(',', c, end='')
    
    
print()
e = "hello, world."
for f in e:
    print(f)
    
g = ["a", "b", "cdef", "ghijkl", "mnopqrstuvwxyz"]
for h in g:
    print(h)
    
for i in range(92,20,-3):
    print(i, end=",")
    
print()
print(list(range(1,20,1)))
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

print("\n\nThat's all folks!")
import sys
print(dir(sys))
for name in dir(sys):
    print(name)
    
import builtins
print(dir(builtins))
for name in dir(builtins):
    print(name)

print(help(ascii))
def scope_test():
    def do_local():
        spam = "local spam"
        
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
        
    def do_global():
        global spam
        spam = "global spam"
        
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)
    
scope_test()
print("In global scope:", spam)
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print("x is (", x.r,",",x.i,")")
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1
    
    def g(self):
        return 'hello world'
    
    h = g
    
import os
print("directory is ", os.getcwd())
print("cwdb is ", os.getcwdb())
for name in dir(os):
    print(name)
    
print(os.environ)
# dates are easily constructed and formatted
from datetime import date
now = date.today()
print(now)
#datetime.date(2003, 12, 2)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
#'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'
# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days, end='\n')
#
#import pyplates
#
#123
#
