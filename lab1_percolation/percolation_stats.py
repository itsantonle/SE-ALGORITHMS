import random
import math
from percolation import Percolation

class PercolationStats:
    # perform independent trials on an n-by-n grid
    def __init__(self, n: int, trials: int):
        if n <= 0 or trials <= 0:
            raise ValueError("n and trials must be greater than 0")
        self.n = n
        self.trials = trials
        self.threshold = []

        # Run the trials
        for _ in range(trials):
            perc = Percolation(n)
            # Keep opening random sites until system percolates
            while not perc.percolates():
                # Find a random closed site
                row = random.randint(1, n)
                col = random.randint(1, n)
                perc.open(row, col)
                if not perc.is_open(row, col): # only open if not already open
                    perc.open(row,col)
            # Calculate threshold for this trial
            self.threshold.append(perc.number_of_open_sites() / (n * n))
        

    # sample mean of percolation threshold
    def mean(self) -> float:
       return sum(self.threshold) / len(self.threshold)

    # sample standard deviation of percolation threshold
    def stddev(self) -> float:
        if len(self.threshold) <= 1:
            return 0.0
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.threshold) / (len(self.threshold) - 1)
        return math.sqrt(variance)

    # low endpoint of 95% confidence interval
    def confidence_lo(self) -> float:
        mean = self.mean()
        stddev = self.stddev()
        return mean - (1.96 * stddev / math.sqrt(len(self.threshold)))

    # high endpoint of 95% confidence interval
    def confidence_hi(self) -> float:
        mean = self.mean()
        stddev = self.stddev()
        return mean + (1.96 * stddev / math.sqrt(len(self.threshold)))

    # test client 
    @staticmethod
    def main():
        import sys 
        if len(sys.argv) != 3:
            print("Usage: python percolation_stats.py n trials")
            sys.exit(1)

        try: 
            n = int(sys.argv[1])
            trials = int(sys.argv[2])

            stats = PercolationStats(n, trials)

            print(f"mean                    = {stats.mean()}")
            print(f"stddev                  = {stats.stddev()}")
            print(f"95% confidence interval = [{stats.confidence_lo()}, {stats.confidence_hi()}]")
        except ValueError:
            print("Error: n and trials must be integers")
            

if __name__ == "__main__":
    PercolationStats.main()