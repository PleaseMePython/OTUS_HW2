from typing import List
"""
TODO:

foo should accept a list argument, whose elements are string.
"""


def foo(x: List[str]):
    pass


if __name__ == "__main__":
    foo(["foo", "bar"])
    foo(["foo", 1]) # expect type error