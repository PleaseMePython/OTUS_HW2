from typing import Dict
"""
TODO:

foo should accept a dict argument, both keys and values are string.
"""

def foo(x: Dict[str,str]):
    pass


if __name__ == "__main__":
    foo({"foo" : "bar"})
    foo({"foo" : 1}) # expect type error