import pytest
from board import Board, InvalidBoardFormatException


def test_board_from_empty_string():
    # Arrange
    board_string = ''

    # Assert
    with pytest.raises(InvalidBoardFormatException):
        # Act
        Board.from_string(board_string)


def test_board_from_valid_string():
    # Arrange
    rows: int = 3
    cols: int = 5
    board_string = """10001
    10001
    10011"""

    # Act
    board = Board.from_string(board_string)

    # Assert
    for x in range(cols):
        for y in range(rows):
            assert str(board.get(x=x, y=y)) == [row.strip() for row in board_string.split('\n')][y][x]
