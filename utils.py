from random import randint
from typing import List


def create_list_of_lists(x: int, y: int) -> List[List[int]]:
    return [[
        randint(0, 1)
        for x_ in range(x)]
        for y_ in range(y)
    ]
