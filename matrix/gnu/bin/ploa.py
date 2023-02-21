#!-*- coding: utf-8 -*-
"""Python pln 32 % 2022"""

"""
Where there is no registered implementation for a specific type, its method resolution
order is used to find a more generic implementation. The original function decorated with
@singledispatch is registered for the base object type, which means it is used if no better
implementation is found.

If an implementation is registered to an abstract base class, virtual subclasses of the base
class will be dispatched to that implementation:

"""

from collections.abc import Mapping

import fun


@fun.register
def _(arg: Mapping, verbose=False):
    if verbose:
        print("Keys & Values")
    for key, value in arg.items():
        print(key, "=>", value)
