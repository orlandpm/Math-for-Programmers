class Wizard:
    def __init__(self, name, age):
        self.name = name
        self.age = age

square = lambda x : x * x

def is_even(n):
    return (n % 2 == 0)

def write_text(file_name, text):
    file = open(file_name, "w")
    file.write(text)
    file.close()


##################
from typing import Dict, List

xs : List[int] = ["a","b"]

def add_up(numbers:List[int]) -> int:
    sum(numbers)

add_up(xs)
