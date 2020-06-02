import os
from board import Board, OutOfBoardException
from collections import namedtuple

coordinates = namedtuple('coordinated', ['x', 'y'])


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
        neighbors = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
        for neighbour_x, neighbour_y in neighbors:
            final_x = x + neighbour_x
            final_y = y + neighbour_y
            try:
                if self.board.get(y=final_y, x=final_x) == 1:
                    number_of_neighbours += 1
            except OutOfBoardException:
                continue
        return number_of_neighbours

    @staticmethod
    def choose_coordinates():
        while True:
            try:
                print("Jeśli chcesz wyjść naciśnij enter\n")
                x = int(input("Podaj kolumne\n"))
                if x is None:
                    break
                print()
                y = int(input("Podaj wiersz\n"))
                if y is None:
                    break
                return coordinates(x-1, y-1)
            except ValueError:
                print("Podana wartość jest nieprawidłowa! Spróbuj jeszcze raz\n")


def main():
    board = Board(20, 20)
    game = GameOfLife(board)
    print(game.board)
    while True:
        choice = input("\nNaciśnij enter aby kontynuować"
                       "\nJedynke aby zmienić wartość punktu,"
                       "\nl, aby wczytać z pliku"
                       "\nlub wpisz cokolwiek innego aby wyjść\n")
        if choice == "":
            os.system("clear")
            game.board_after_lifecycle()
            print(game.board)
        elif choice == "l":
            filename = input("Podaj nazwę pliku: ")
            try:
                with open(filename) as f:
                    board_string = ''.join(f.readlines())
                    board = Board.from_string(board_string)
                    game = GameOfLife(board)
            except FileNotFoundError:
                print(f'Plik o nazwie "{filename}" nie istnieje.')
        elif choice == "1":
            try:
                coordinates = game.choose_coordinates()
                value = game.board.get(coordinates.x, coordinates.y)
                game.board.set(coordinates.x, coordinates.y, 1 if value == 0 else 0)
                print(game.board)
            except OutOfBoardException:
                print("Podane koordynaty nie mieszczą się w skali planszy, spróbuj jeszcze raz!\n")
        else:
            break


if __name__ == "__main__":
    main()
