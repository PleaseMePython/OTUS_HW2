"""
TODO:

foo should accept a argument that's either a string or integer.
"""


def foo(x: str | int):
    pass

if __name__ == "__main__":
    foo("foo")
    foo(1)
    foo([])  # expect-type-error