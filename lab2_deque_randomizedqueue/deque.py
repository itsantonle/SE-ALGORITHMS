

from typing import TypeVar, Generic

Item = TypeVar('Item')

class Node(Generic[Item]): 
  def __init__(self, item: Item):
        self.item: Item | None  = item
        self.next: Item | None =  None
        self.prev: Item | None = None 
        
class Deque(Generic[Item]):
    # construct an empty deque
    def __init__(self):
        self.n: int = 0
        self.first: Item | None  = None
        self.last : Item | None = None
   

    # is the deque empty?
    def is_empty(self) -> bool:
        return self.n == 0 

    # return the number of items on the deque
    def size(self) -> int:
        return self.n 

    # add the item to the front
    def add_first(self, item: Item) -> None:
        if item == None:
            raise ValueError("Cannot add None item to the deque")
        prev_first = self.first
        self.first = Node(item)
        self.first.next = prev_first
        if self.is_empty():
            self.last = self.first
        else:
            prev_first.prev = self.first
        self.n += 1
                
            

    # add the item to the back
    def add_last(self, item: Item) -> None:
        if item == None:
            raise ValueError("Cannot add None item to the deque")
        prev_last = self.last
        self.last = Node(item)
        self.last.prev = prev_last
        if self.is_empty():
            self.first = self.last
        else:
            prev_last.next = self.last
        self.n += 1
        


    # remove and return the item from the front
    def remove_first(self) -> Item:
        if(self.is_empty()): 
            raise IndexError('Cannot remove from empty Deque')
        
        # get the value 
        prev_first_item = self.first.item 
        
        # assign new first 
        self.first = self.first.next 
        
        # minus the number of elements 
        self.n -= 1 
        
        # ensures the pointer is always pointing to a valid value NONE or NODE
        if(self.is_empty()): 
            self.last = None
        else: 
            self.first.prev = None
        
        # return item 
        return prev_first_item
           
            
            
            

    # remove and return the item from the back
    def remove_last(self) -> Item:
        if(self.is_empty()): 
            raise IndexError('Cannot remove from empty Deque')
        
        # get the value 
        prev_last_item = self.last.item
        
        # assign new last
        self.last = self.last.prev
        
        # minus the number of elements 
        self.n -= 1 
        
        # ensures the pointer is always pointing to a valid value NONE or NODE
        if(self.is_empty()): 
            self.first = None 
        else: 
            self.last.next = None 
        
        # return item 
        return prev_last_item
           

    def __iter__(self):
        self.current = self.first
        return self

    # return the current item and tick the current item to the next
    # otherwise, raise StopIteration
    def __next__(self) -> Item:
        if self.current is None:
         raise StopIteration
        current_item = self.current.item
        self.current = self.current.next
        return  current_item

    # unit testing (required)
    @staticmethod
    def main():
   
        try: 
            deq = Deque[int]()
            deq.add_first(1)
            deq.add_last(2)
            deq.add_first(3)
            deq.add_last(4)
            
            assert deq.first.item == 3
            assert deq.last.item  == 4
            assert deq.n == 4
            
            print(f"Dequeue information \n size: {deq.n} \n first_node: {deq.first.item} \n last_node: {deq.last.item}\n ")
            print('items in deq')
            mock_array = []
            for item in deq: 
                mock_array.append(item)
            
            print(mock_array)
            print("\nRemoving first")
            deq.remove_first()
            assert deq.n == 3
            assert deq.first.item == 1
            assert deq.last.item == 4
            print(f"Dequeue information \n size: {deq.n} \n first_node: {deq.first.item} \n last_node: {deq.last.item}\n ")
            mock_array = []
            for item in deq: 
                mock_array.append(item)
            print('items in deq')
            print(mock_array)
            
            print("\nRemoving last")
            deq.remove_last()
            assert deq.n == 2
            assert deq.first.item == 1
            assert deq.last.item == 2
            print(f"Dequeue information \n size: {deq.n} \n first_node: {deq.first.item} \n last_node: {deq.last.item}\n ")
            mock_array = []
            for item in deq: 
                mock_array.append(item)
            print('items in deq')
            print(mock_array)
         
            
            print("\nTests passed!")
        except: 
            raise AssertionError("Tests failed")
            



if __name__ == "__main__":
    Deque.main()
