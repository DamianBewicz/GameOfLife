from typing import List, Optional
from utils import create_list_of_lists


class OutOfBoardException(Exception):
    pass


class InvalidBoardFormatException(Exception):
    pass


class Board:
    def __init__(self,  rows: int, columns: int) -> None:
        self.__board = create_list_of_lists(y=rows, x=columns)

    def __str__(self) -> str:
        str_ = ""
        for row in self.__board:
            for cell in row:
                cell = "●" if cell == 1 else "◌"
                str_ += str(cell) + " "
            str_ += "\n"
        return str_

    @property
    def rows(self) -> int:
        return len(self.__board)

    @property
    def columns(self) -> int:
        return len(self.__board[0])

    def is_out_of_board(self, y: int, x: int) -> bool:
        return (
            x < 0
            or y < 0
            or y > self.rows - 1
            or x > self.columns - 1
        )

    def get(self, x: int, y: int) -> int:
        if self.is_out_of_board(x=x, y=y):
            raise OutOfBoardException
        return self.__board[y][x]

    def set(self, x: int, y: int, value: int = None) -> None:
        if self.is_out_of_board(x=x, y=y):
            raise OutOfBoardException
        self.__board[y][x] = value

    @staticmethod
    def from_string(string: str) -> 'Board':
        string = string.strip()
        rows = string.split('\n')
        height = len(rows)
        width = len(rows[0])
        if width == 0 or height == 0:
            reason = 'width' if width == 0 else 'height'
            raise InvalidBoardFormatException(f'{reason} cannot be 0')
        board = Board(rows=height, columns=width)
        for y, row in enumerate(rows):
            if len(row) != width:
                raise InvalidBoardFormatException(f'Row {y} has different width')
            for x, cell in enumerate(row.replace(' ', '')):
                board.set(x=x, y=y, value=int(cell))
        return board



# print(Board.from_string("wtawfsasd"))
