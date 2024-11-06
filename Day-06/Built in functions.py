# A
print(abs(-5))  # abs
print(any([False, False, True]))  # any
print(all([True, True, False]))  # all
print(ascii("Café"))  # ascii

# B
print(bin(10))  # bin
print(bool(1))  # bool
breakpoint()  # breakpoint (Starts debugging here)
print(bytearray("abc", "utf-8"))  # bytearray
print(bytes("abc", "utf-8"))  # bytes

# C
print(callable(print))  # callable
print(chr(65))  # chr
class MyClass:
    @classmethod
    def greet(cls):
        return "Hello"
print(MyClass.greet())  # classmethod
print(complex(2, 3))  # complex

# D
obj = MyClass()
delattr(obj, 'greet')  # delattr
print(dict(a=1, b=2))  # dict
print(dir([]))  # dir
print(divmod(10, 3))  # divmod

# E
print(list(enumerate(['a', 'b', 'c'])))  # enumerate
print(eval('1 + 2'))  # eval
exec("print('Hello')")  # exec

# F
print(list(filter(lambda x: x > 0, [-1, 0, 1, 2])))  # filter
print(float("3.14"))  # float
print(format(3.14159, ".2f"))  # format
print(frozenset([1, 2, 3]))  # frozenset

# G
print(getattr(MyClass, 'greet', None))  # getattr
print(globals())  # globals

# H
print(hasattr("hello", "upper"))  # hasattr
print(hash("hello"))  # hash
help(str)  # help
print(hex(255))  # hex

# I
print(id(5))  # id
# Uncomment input line below if you want to prompt for user input:
# name = input("Enter name: ")  # input
print(int("10"))  # int
print(isinstance(5, int))  # isinstance
print(issubclass(bool, int))  # issubclass
iterator = iter([1, 2, 3])
print(next(iterator))  # next

# L
print(len("hello"))  # len
print(list((1, 2, 3)))  # list
print(locals())  # locals

# M
print(list(map(str.upper, ['a', 'b'])))  # map
print(max([1, 2, 3]))  # max
print(memoryview(b"abc"))  # memoryview
print(min([1, 2, 3]))  # min

# N
print(next(iterator, "End of iterator"))  # next

# O
print(object())  # object
print(oct(8))  # oct
# Uncomment open line below if you have a file to open:
# f = open("file.txt")  # open
print(ord('A'))  # ord

# P
print(pow(2, 3))  # pow
print("Hello")  # print
class MyClassWithProperty:
    @property
    def attr(self):
        return 10
obj = MyClassWithProperty()
print(obj.attr)  # property

# R
print(range(5))  # range
print(repr("Hello"))  # repr
print(list(reversed([1, 2, 3])))  # reversed
print(round(3.14159, 2))  # round

# S
print(set([1, 2, 3]))  # set
class MyStaticClass:
    @staticmethod
    def static_method():
        return "static method"
print(MyStaticClass.static_method())  # staticmethod
print(sorted([3, 2, 1]))  # sorted
print(str(123))  # str
print(sum([1, 2, 3]))  # sum
print(super())  # super

# T
print(tuple([1, 2, 3]))  # tuple
print(type(123))  # type

# V
print(vars())  # vars

# Z
print(list(zip([1, 2], ['a', 'b'])))  # zip

# _
import_module = __import__("math")  # __import__
print(import_module.sqrt(4))  # Using imported math module's sqrt function
