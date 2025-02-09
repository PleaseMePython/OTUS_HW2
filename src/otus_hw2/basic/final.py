from typing import Final
"""
TODO:

Make sure `my_list` cannot be re-assigned to.
"""

my_list: Final = []

if __name__ == "__main__":
    my_list.append(1)
    my_list = [] # expect type error
    my_list = "new value" # expect type error