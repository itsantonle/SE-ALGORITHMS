import sys
import os
from board import Board
from solver import Solver

def main():
    if len(sys.argv) != 2:
        print("Usage: python client.py [puzzle_file]")
        return
    
    # Construct the full path to the puzzle file inside `sample_puzzles`
    puzzle_path = os.path.join("sample_puzzles", sys.argv[1])  
    
    if not os.path.exists(puzzle_path):
        print(f"Error: Puzzle file '{puzzle_path}' not found.")
        return

    # Read the puzzle file
    with open(puzzle_path, 'r') as f:
        n = int(f.readline().strip())
        tiles = [list(map(int, f.readline().split())) for _ in range(n)]

    initial_board = Board(tiles)
    solver = Solver(initial_board)

    if not solver.is_solvable():
        print("No solution possible")
    else:
        print("Minimum number of moves =", solver.moves())
        for board in solver.solution():
            print(board)

if __name__ == '__main__':
    main()
