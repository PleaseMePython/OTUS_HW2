"""
TODO:

Create a new type called Vector, which is a list of float.
"""
from typing import List

Vector = List[float]

if __name__ == "__main__":
    def foo(v: Vector):
        pass

    foo([1.1, 2])
    foo(1)  # expect-type-error
    foo(["1"])  # expect-type-error