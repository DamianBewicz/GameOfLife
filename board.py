from typing import List
from utils import create_list_of_lists


class OutOfBoardException(Exception):
    pass


class Board:
    def __init__(self, rows: int = None, columns: int = None, ) -> None:
        self.__board = create_list_of_lists(rows, columns)

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
            or y > self.columns -1
            or x > self.rows - 1
        )

    def get(self, x: int, y: int) -> int:
        if self.is_out_of_board(x=x, y=y):
            raise OutOfBoardException
        return self.__board[y][x]

    def set(self, x: int, y: int, value: int) -> None:
        if self.is_out_of_board(x=x, y=y):
            raise OutOfBoardException
        self.__board[y][x] = value

    @staticmethod
    def from_string() -> List[List[int]]:
        try:
            file_name = input("\nPodaj nazwę pliku\n")
            if Board.is_format_correct(file_name):
                with open(file_name, "r") as f:
                    return [[
                        int(digit) for digit in line.strip('\n')]
                        for line in f
                    ]
            else:
                print("Niepoprawny format pliku!")
        except FileNotFoundError:
            print("\nTaki plik nie istnieje\n")

    @staticmethod
    def is_format_correct(file_path: str) -> bool:
        try:
            with open(file_path, "r") as f:
                board = [line.strip() for line in f.readlines()]
                row_len = len(board[0])
                if any(len(row) != row_len for row in board):
                    return False
                if any((int(cell) not in (0, 1)
                        for row in board
                        for cell in row.strip())):
                    return False
                return True
        except ValueError:
            return False
