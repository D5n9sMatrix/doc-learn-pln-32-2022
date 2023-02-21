#!-*- coding: utf-8 -*-
"""Python pln 32 % 2022"""

"""


    New in version 3.4.

    Changed in version 3.7: The register() attribute now supports using type annotations.

class functools.singledispatchmethod(func)

    Transform a method into a single-dispatch generic function.

    To define a generic method, decorate it with the @singledispatchmethod decorator. When
    defining a function using @singledispatchmethod, note that the dispatch happens on the
    type of the first non-self or non-cls argument:

"""
from functools import singledispatchmethod


class ActivePln:
    @singledispatchmethod
    def pln(self, arg):
        raise NotImplementedError("Cannot active a")

    @pln.register
    def _(self, arg: int):
        return -arg

    @pln.register
    def _(self, arg: bool):
        return not arg


"""
@singledispatchmethod supports nesting with other decorators such as @classmethod. 
Note that to allow for dispatcher.register, singledispatchmethod must be the outer 
most decorator. Here is the ActivePLN class with the neg methods bound to the class, 
rather than an instance of the class:


"""

class NegatorPln:
    @classmethod
    def neg(cls, arg):
        raise NotImplementedError("Cannot negate a")

    @classmethod
    def _(cls, arg: int):
        return -arg

    @classmethod
    def way(cls, arg: bool):
        return not arg
