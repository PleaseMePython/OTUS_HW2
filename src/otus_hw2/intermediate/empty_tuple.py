"""
TODO:

foo should accept a empty tuple argument.
"""
# from typing import Tuple

def foo(x:tuple[()]):
    pass

foo(())
foo((1,))  # expect-type-error
