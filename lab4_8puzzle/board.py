from __future__ import annotations
from typing import Generator

class Board:
    def __init__(self, tiles: list[list[int]]):
        """Initializes the board from a given n-by-n list of lists."""
        self.tiles = tuple(tuple(row) for row in tiles)  # Immutable representation
        self.n = len(tiles)

    def dimension(self) -> int:
        """Returns the board dimension n."""
        return self.n

    def hamming(self) -> int:
        """Returns the number of tiles not in their goal position (excluding blank)."""
        count = 0
        for i in range(self.n):
            for j in range(self.n):
                tile = self.tiles[i][j]
                if tile != 0 and tile != (i * self.n + j + 1):
                    count += 1
        return count

    def manhattan(self) -> int:
        """Returns the sum of Manhattan distances for all tiles to their goal positions."""
        distance = 0
        for i in range(self.n):
            for j in range(self.n):
                tile = self.tiles[i][j]
                if tile == 0:
                    continue
                goal_i, goal_j = (tile - 1) // self.n, (tile - 1) % self.n
                distance += abs(i - goal_i) + abs(j - goal_j)
        return distance

    def is_goal(self) -> bool:
        """Returns True if the board matches the goal configuration."""
        return self.hamming() == 0

    def find_blank(self) -> tuple[int, int]:
        """Finds the blank tile position."""
        for i in range(self.n):
            for j in range(self.n):
                if self.tiles[i][j] == 0:
                    return i, j

    def neighbors(self) -> list[Board]:
        """Returns an iterable of all neighboring boards."""
        i, j = self.find_blank()
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for di, dj in directions:
            new_i, new_j = i + di, j + dj
            if 0 <= new_i < self.n and 0 <= new_j < self.n:
                new_tiles = [list(row) for row in self.tiles]
                new_tiles[i][j], new_tiles[new_i][new_j] = new_tiles[new_i][new_j], new_tiles[i][j]
                neighbors.append(Board(new_tiles))

        return neighbors

    def twin(self) -> Board:
        """Returns a twin board obtained by swapping any two adjacent non-blank tiles."""
        new_tiles = [list(row) for row in self.tiles]

        for i in range(self.n):
            for j in range(self.n - 1):
                if new_tiles[i][j] != 0 and new_tiles[i][j + 1] != 0:
                    new_tiles[i][j], new_tiles[i][j + 1] = new_tiles[i][j + 1], new_tiles[i][j]
                    return Board(new_tiles)

    def __str__(self) -> str:
        """Returns a formatted string representation of the board."""
        rows = [' '.join(map(str, row)) for row in self.tiles]
        return f"{self.n}\n" + "\n".join(rows)
    
def test_board():
    """Runs basic tests to verify Board class functionality."""
    sample_puzzle = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]  # Goal state
    ]

    board = Board(sample_puzzle)

    print("Testing Board Class:")
    print(board)
    
    assert board.dimension() == 3, "Dimension should be 3"
    assert board.hamming() == 0, "Hamming distance should be 0 (goal state)"
    assert board.manhattan() == 0, "Manhattan distance should be 0 (goal state)"
    assert board.is_goal() is True, "Board should be in goal state"

    print("\nTesting neighbors:")
    for neighbor in board.neighbors():
        print(neighbor)

    print("\nTesting twin board:")
    print(board.twin())

    print("\nBoard tests passed!")

if __name__ == '__main__':
    test_board()
