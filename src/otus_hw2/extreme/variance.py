"""
TODO: Annotate function `f` and `g`, to make tests pass.
"""
from typing import List, Tuple


def f(a: List[int | str] | List[str]):
    pass


def g(a: List[int | str] | List[int] | Tuple | bytes | str):
    pass


l1: list[int] = [1, 2]
f(l1)  # expect-type-error
g(l1)

l2: list[int | str] = [1, 2]
f(l2)
g(l2)

f(1)  # expect-type-error
f("abc")  # expect-type-error
g("abc")
g(b"abc")
g([1, "2"])
g((1, "2", 3))
g(1)  # expect-type-error
g({1})  # expect-type-error