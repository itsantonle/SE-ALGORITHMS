from lib.weighted_quick_union_uf import WeightedQuickUnionUF

class Percolation:
    def __init__(self, n: int):
        self.n = n
        # initialize with all False values
        self.grid = [[False for _ in range(n)] for _ in range(n)]
        
        # Create an instance of the WeightQuickUnion with a n x n nodes plus the 2 virtual nodes
        
        self.uf = WeightedQuickUnionUF(n * n + 2) 
        
        self.top_virtual = n * n 
        # this ensures that from the maximum nodes from 1 to n that it will always be max n + 1
        self.bottom_virtual = self.top_virtual + 1  # virtual bottom node

    def index(self, row: int, col: int) -> int:
        # flattedned nested list (accounting n-1 because index starts 0)
        # [0 , 1, 2,
        #  3, 4, 5,
        #  6, 7, 8 ] + [9. 10]
        
        # n-1 = 0
        # find(1,1)
        # == 1-1 * 3 + 1-1 == 1Darray[0] instead of nestedarr[1][1]
        return (row - 1) * self.n + (col - 1)

    def open(self, row: int, col: int) -> None:
        
        # check if already open or not
        if not self.is_open(row, col):
            self.grid[row - 1][col - 1] = True
            index = self.index(row, col)
            
            # connect all tops nodes to the vitual top node 
            if row == 1:
                self.uf.union(index, self.top_virtual)
            # the maximum last row in an nxn grid is n and so union this with the virtual bottom node 
            if row == self.n:
                self.uf.union(index, self.bottom_virtual)
            
            # check sides if open and perform a union operation (create connected components)
            if row > 1 and self.is_open(row - 1, col):
                self.uf.union(index, self.index(row - 1, col))
            if row < self.n and self.is_open(row + 1, col):
                self.uf.union(index, self.index(row + 1, col))
            if col > 1 and self.is_open(row, col - 1):
                self.uf.union(index, self.index(row, col - 1))
            if col < self.n and self.is_open(row, col + 1):
                self.uf.union(index, self.index(row, col + 1))

    def is_open(self, row: int, col: int) -> bool:
        # bool variable by accessing the nexted loop initialized  [false, true] only
        
        return self.grid[row - 1][col - 1]

    def is_full(self, row: int, col: int) -> bool:
        # bool variable returns true or false if the index is connected to the virtual top (means gaagi ang tubig halin sa babw?)
        
        return self.uf.connected(self.index(row, col), self.top_virtual)

    def number_of_open_sites(self) -> int:
        #coun the the number of trues in the initialized grid
        
        return sum(row.count(True) for row in self.grid)

    def percolates(self) -> bool:
        #if the top and the bottom virtual nodes are connected then it percolates? (they are part of the same component)
        return self.uf.connected(self.top_virtual, self.bottom_virtual)

# test client (optional)
    @staticmethod
    
    def main():
       pass

if __name__ == "__main__":
    Percolation.main()
