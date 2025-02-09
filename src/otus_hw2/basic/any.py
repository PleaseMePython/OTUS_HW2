from typing import Any
"""
TODO:

Modify `foo` so it takes an argument of arbitrary type.
"""

def foo(x: Any):
    pass


if __name__ == "__main__":
    foo(1)
    foo("10")
    foo(1,2) # Expect type-error