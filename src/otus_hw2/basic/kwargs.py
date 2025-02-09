from typing import Union
"""
TODO:

`foo` takes keyword arguments of type integer or string.
"""


def foo(**kwargs:Union[int,str]):
    pass

if __name__ == "__main__":
    foo(a=1,b="2")
    foo(a=[1]) # expect type error