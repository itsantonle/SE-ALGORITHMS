import random
from typing import TypeVar, Generic

Item = TypeVar('Item')

class RandomizedQueue(Generic[Item]):
    # construct an empty randomized queue
    def __init__(self):
        self.items = []

    # is the randomized queue empty?
    def is_empty(self) -> bool:
        return len(self.items) == 0

    # return the number of items on the randomized queue
    def size(self) -> int:
        return len(self.items)

    # add the item
    def enqueue(self, item: Item) -> None:
        if item is None:
            raise ValueError("Cannot enqueue None")
        self.items.append(item)

    # remove and return a random item
    def dequeue(self) -> Item:
        if self.is_empty():
            raise IndexError("Cannot dequeue: the queue is empty")
        index = random.randint(0, len(self.items)-1)
        return self.items.pop(index)

    # return a random item (but do not remove it)
    def sample(self) -> Item:
        if self.is_empty():
            raise IndexError("Cannot sample: the queue is empty")
        index = random.randint(0, len(self.items)-1)
        return self.items[index]

    # for looping this object will loop over the items in a random order
    def __iter__(self):
        # shuffle for random iteration
        random.shuffle(self.items)
        self.current = 0
        return self

    # return the current item and tick the current item to the next
    # otherwise, raise StopIteration
    def __next__(self) -> Item:
        if self.current >= len(self.items):
            raise StopIteration
        item = self.items[self.current]
        self.current += 1
        return item
            
    # unit testing (required)
    @staticmethod
    def main():
    
        try:
            ran_que = RandomizedQueue()
            print("Empty:", ran_que.is_empty())  #True
            assert ran_que.is_empty() == True
            assert ran_que.size() == 0

            # Enqueue items
            ran_que.enqueue("S")
            ran_que.enqueue("O")
            ran_que.enqueue("R")
            ran_que.enqueue("E")

            # Test size and is_empty
            print("Size:", ran_que.size())  #4
            assert ran_que.size() == 4
            assert ran_que.is_empty() == False

            # Test sample
            sample_item = ran_que.sample()
            print("Sample:", sample_item) 
            assert sample_item in {"S", "O", "R", "E"}

            # Test dequeue
            dequeued_item = ran_que.dequeue()
            print("Dequeue:", dequeued_item)  
            assert dequeued_item in {"S", "O", "R", "E"}
            assert ran_que.size() == 3  # 4-1

            # Test iteration
            print("Random items in queue:")
            mock_array = []
            for item in ran_que:
                mock_array.append(item)
            print(mock_array)  # print remaining items in random order
            assert set(mock_array) == {"S", "O", "R", "E"} - {dequeued_item}

            # Test dequeue until empty
            ran_que.dequeue()
            ran_que.dequeue()
            ran_que.dequeue()
            assert ran_que.is_empty() == True
            assert ran_que.size() == 0

            try:
                ran_que.dequeue()
                raise AssertionError("Did not raise IndexError")
            except IndexError:
                print("IndexError")

            try:
                ran_que.sample()
                raise AssertionError("Did not raise IndexError")
            except IndexError:
                print("IndexError")

            try:
                ran_que.enqueue(None)
                raise AssertionError("Did not raise ValueError")
            except ValueError:
                print("ValueError")

            print("\nTests passed!")
        except Exception as e:
            raise AssertionError(f"Tests failed: {e}")
        
       
if __name__ == "__main__":
    RandomizedQueue.main()