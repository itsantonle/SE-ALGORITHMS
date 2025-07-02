# Make sure you download python 3.12 +

this is to ensure python version supports type

# DEQUEUE (ANTON)

Dequeue. A double-ended queue or deque (pronounced “deck”) is a generalization of a stack and a queue that supports adding and removing items from either the front or the back of the data structure. Create a generic data type Deque that implements the following API using a doubly-linked list:

- to implement the genenric 'doubly' linked list queue

-Throw exception for the corners cases on DEQUEUE generic data type
-Raise a ValueError if the client calls either add_first() or add_last() with a None argument().

-Raise an IndexError if the client calls either remove_first() or remove_last() when the deque is empty.

-Unit testing: Your main() method must call directly every method to help verify that they work as prescribed (e.g., by printing results to standard output).

# RANDOMIZED QUEUE (SHEENA)

Randomized queue. A randomized queue is similar to a stack or queue, except that the item removed is chosen uniformly at random among items in the data structure. Create a generic data type RandomizedQueue that implements the following API using a list:

Corner cases. Throw the specified exception for the following corner cases:
-Raise a ValueError if the client calls enqueue() with a None argument.

-Raise an IndexError if the client calls either sample() or dequeue() when the randomized queue is empty.

-Unit testing. Your main() method must call directly every method to verify that they work as prescribed (e.g., by printing results to standard output).

# CLIENT

NOTE: USE THE DEQUEUE OR THE RANDOMIZED QUEUE TO IMPLEMENT THIS EASILY

Write a client program permutation.py that takes an integer k as a command-line argument; reads a sequence of strings from a .txt file and prints exactly k of them, uniformly at random. Print each item from the sequence at most once.

# SUBMISSIUON

Submit a .zip file containing only deque.py, randomized_queue.py and permutation.py . Deadline: February 24, 2025, 11:59pm
(https://www.dropbox.com/request/57rCIOiGOf1YrpSvPFBv.)

# Client code REFERENCE

```py
import sys
from typing import List

class RandomizedQueue(Generic[Item]):
    # construct an empty randomized queue
    def __init__(self):
        self.queue: List[Item] = []

    # is the randomized queue empty?
    def is_empty(self) -> bool:
        return len(self.queue) == 0

    # return the number of items on the randomized queue
    def size(self) -> int:
        return len(self.queue)

    # add the item
    def enqueue(self, item: Item) -> None:
        if item is None:
            raise ValueError("Cannot add None item to the queue")
        self.queue.append(item)

    # remove and return a random item
    def dequeue(self) -> Item:
        if self.is_empty():
            raise IndexError("Cannot remove from an empty queue")
        idx = random.randrange(len(self.queue))
        return self.queue.pop(idx)

    # return a random item (but do not remove it)
    def sample(self) -> Item:
        if self.is_empty():
            raise IndexError("Cannot sample from an empty queue")
        idx = random.randrange(len(self.queue))
        return self.queue[idx]

    # for looping this object will loop over the items in a random order
    def __iter__(self) -> Iterator[Item]:
        self._shuffled_indices = random.sample(range(len(self.queue)), len(self.queue))
        self._current_index = 0
        return self

    # return the current item and tick the current item to the next
    # otherwise, raise StopIteration
    def __next__(self) -> Item:
        if self._current_index >= len(self._shuffled_indices):
            raise StopIteration
        idx = self._shuffled_indices[self._current_index]
        self._current_index += 1
        return self.queue[idx]

def read_strings_from_file(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        strings = [line.strip() for line in file.readlines()]
    return strings

def main():
    if len(sys.argv) != 3:
        print("Usage: python permutation.py <k> <filename>")
        sys.exit(1)

    k = int(sys.argv[1])
    filename = sys.argv[2]

    strings = read_strings_from_file(filename)
    rq = RandomizedQueue[str]()

    for string in strings:
        rq.enqueue(string)

    for _ in range(k):
        print(rq.dequeue())

if __name__ == "__main__":
    main()

```
