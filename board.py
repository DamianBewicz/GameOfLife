from typing import List, Optional
from utils import create_list_of_lists


class OutOfBoardException(Exception):
    pass


class Board:
    def __init__(self,  rows: Optional[int] = None, columns: Optional[int] = None, filename: Optional[str] = None) -> None:
        self.__board = Board.from_string(filename) if filename is not None else create_list_of_lists(y=rows, x=columns)

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

    def set(self, x: int, y: int, value: int) -> None:
        if self.is_out_of_board(x=x, y=y):
            raise OutOfBoardException
        self.__board[y][x] = value

    @staticmethod
    def from_string(path) -> List[List[int]]:
        with open(path, "r") as f:
            return [[
                int(digit) for digit in line.strip('\n')]
                for line in f
            ]

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
        except (ValueError, FileNotFoundError):
            print("\nNiepoprawny format pliku lub nazwa pliku!\n")
            return False

    @staticmethod
    def ask_for_columns() -> int:
        while True:
            try:
                choice = int(input("\nPodaj ilość kolumn\n"))
                return choice
            except ValueError:
                print("To nie jest liczba!\n"
                      "Podaj prawidłową liczbę")

    @staticmethod
    def ask_for_rows() -> int:
        while True:
            try:
                choice = int(input("\nPodaj ilość rzędów\n"))
                return choice
            except ValueError:
                print("To nie jest liczba!\n"
                      "Podaj prawidłową liczbę")

    @staticmethod
    def choose():
        options = {
            "1": "Wczytaj z pliku",
            "2": "Stwórz tablicę losową"
        }
        while True:
            board = None
            for number, choice in options.items():
                print(number, choice)
            choice = input("\nPodaj swój wybór\n")
            if choice == "1":
                file_name = input("\nPodaj nazwę pliku\n")
                if Board.is_format_correct(file_name):
                    return Board(filename=file_name)
            elif choice == "2":
                board = Board(rows=Board.ask_for_rows(), columns=Board.ask_for_columns())
            if board:
                break


# print(Board.from_string("wtawfsasd"))
