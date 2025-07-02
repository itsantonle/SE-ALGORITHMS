from __future__ import annotations
import heapq
from board import Board
from typing import List, Optional

class Solver:
    class SearchNode:
        """Represents a node in the A* search tree."""
        def __init__(self, board: Board, moves: int, prev: Optional[Solver.SearchNode]):
            self.board = board
            self.moves = moves
            self.prev = prev
            self.priority = self.board.manhattan() + self.moves  # A* priority function

        def __lt__(self, other: Solver.SearchNode):
            return self.priority < other.priority  # Enables priority queue comparisons

    def __init__(self, initial: Board):
        """Finds the solution to the initial board using the A* algorithm."""
        if initial is None:
            raise ValueError("Initial board cannot be None.")

        self.initial = initial
        self.solution_path = []
        self.solution_moves = -1

        self._solve()

    def _solve(self):
        """Runs A* search to find the minimal solution path."""
        pq = []
        twin_pq = []
        heapq.heappush(pq, Solver.SearchNode(self.initial, 0, None))
        heapq.heappush(twin_pq, Solver.SearchNode(self.initial.twin(), 0, None))

        while pq and twin_pq:
            if self._step(pq):
                return
            if self._step(twin_pq):  # If twin finds goal first, the puzzle is unsolvable
                self.solution_path = None
                return

    def _step(self, pq: List[SearchNode]) -> bool:
        """Processes the next search node and expands neighbors."""
        node = heapq.heappop(pq)
        if node.board.is_goal():
            self._reconstruct_path(node)
            return True

        for neighbor in node.board.neighbors():
            if node.prev and neighbor.tiles == node.prev.board.tiles:
                continue  # Avoid redundant cycles
            heapq.heappush(pq, Solver.SearchNode(neighbor, node.moves + 1, node))
        return False

    def _reconstruct_path(self, node: SearchNode):
        """Traces the optimal sequence of moves back to the initial board."""
        path = []
        while node:
            path.append(node.board)
            node = node.prev
        self.solution_path = list(reversed(path))
        self.solution_moves = len(self.solution_path) - 1

    def is_solvable(self) -> bool:
        """Returns True if the puzzle is solvable using twin board approach."""
        return self.solution_path is not None

    def moves(self) -> int:
        """Returns the minimum number of moves required to solve the puzzle."""
        return self.solution_moves if self.is_solvable() else -1

    def solution(self) -> list[Board]:
        """Returns the sequence of boards from initial to goal state."""
        return self.solution_path if self.is_solvable() else None
    
def test_solver():
    """Runs basic tests to verify Solver class functionality."""

    # Solvable puzzle - puzzle 04
    solvable_puzzle = [
        [0,1,3],
        [4, 2,5],
        [7, 8,6]
    ]

    # Unsolvable puzzle -puzzle3x3 unsolvable
    unsolvable_puzzle = [
        [1, 2, 3],
        [4, 6,5],
        [7,8,0]
    ]

    print("Testing Solver with a solvable puzzle:")
    board = Board(solvable_puzzle)
    solver = Solver(board)

    assert solver.is_solvable() is True, "Puzzle should be solvable"
    print("Minimum moves:", solver.moves())
    print("Solution Path:")
    for step in solver.solution():
        print(step )
        print("")

    print("\nTesting Solver with an unsolvable puzzle:")
    unsolvable_board = Board(unsolvable_puzzle)
    unsolvable_solver = Solver(unsolvable_board)

    assert unsolvable_solver.is_solvable() is False, "Puzzle should be unsolvable"
    print("No solution possible.")

    print("\nSolver tests passed!")

if __name__ == '__main__':
    test_solver()
