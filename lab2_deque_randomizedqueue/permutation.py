from randomized_queue import RandomizedQueue
import sys
def instructions(): 
    print('-----\nHow to use the system: \n First prompt: python permutation.py <int> \n\t use only VALID integer values \n\t the int value must be smaller or equal to the number of items in the text file \n Enter filename:<filname.txt> VALID FILES in the same directory. example ph.txt\n----- \n')
def main():
    
    k = None
    try: 
        integer = int(sys.argv[1]) 
    except ValueError: 
        instructions()
        print("INCORRECT ARGUMENT TYPE")
        sys.exit(1)
        
    if(len(sys.argv) != 2): 
        instructions()
        sys.exit(1)
    else: 
        
        k = int(sys.argv[1])
        if(k < 0): 
            instructions()
            print("the integer can't be negative")
            sys.exit(1)
            
        
    filename = input("Enter filename:")
    with open(filename, "r") as file: # with open() - open and write line, r - default of read
        items = file.readlines()

    ran_que = RandomizedQueue()

    for item in items:
        item = item.strip() # strip() - remove spaces, etc. from a string
        if item:
            ran_que.enqueue(item) 
    
    if k > ran_que.size():
        print("Error:\n n is larger than the number of items")
        return
    
    print(f"Random items:")
    for _ in range(k):
        print(ran_que.dequeue())
        


if __name__ == "__main__":
    main()




