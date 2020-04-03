import os
from board import Board, OutOfBoardException


class GameOfLife:
    def __init__(self, board: Board) -> None:
        self.board: Board = board

    def board_after_lifecycle(self) -> None:
        new_board = Board(rows=self.board.rows, columns=self.board.columns)
        for y in range(self.board.rows):
            for x in range(self.board.columns):
                neighbours_number = self.check_living_neighbours_number(x=x, y=y)
                if self.board.get(x=x, y=y) == 1 and neighbours_number in (2, 3):
                    new_board.set(x=x, y=y, value=1)
                elif self.board.get(x=x, y=y) == 0 and neighbours_number == 3:
                    new_board.set(x=x, y=y, value=1)
                else:
                    new_board.set(x=x, y=y, value=0)
        self.board = new_board

    def check_living_neighbours_number(self, y: int, x: int) -> int:
        number_of_neighbours = 0
        coordinates = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
        for neighbour_x, neighbour_y in coordinates:
            final_x = x + neighbour_x
            final_y = y + neighbour_y
            try:
                if self.board.get(y=final_y, x=final_x) == 1:
                    number_of_neighbours += 1
            except OutOfBoardException:
                continue
        return number_of_neighbours


def main():
    board = Board.choose()
    game = GameOfLife(board)
    print(game.board)
    while True:
        choice = input("\nNaciśnij enter aby kontynuować"
                       "\nJedynke aby zmienić wartość punktu,"
                       "\nlub wpisz cokolwiek innego aby wyjść\n")
        if choice == "":
            os.system("clear")
            game.board_after_lifecycle()
            print(game.board)
        if choice not in ("", 1):
            break


if __name__ == "__main__":
    main()
