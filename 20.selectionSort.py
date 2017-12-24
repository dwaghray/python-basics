from tools import *

# takes an item, compares it to the smallest/largest value of the rest of the
# items, then makes a swap if it's smaller/larger than the first item, and it
# continues this process until all items are placed in order

def selection_sort(items):
    ordered = items.copy()

    for i in range(len(ordered)):
        next_smallest = -1
        
        for j in range(i, len(ordered)):
            
            if ordered[j] < ordered[next_smallest]:
                next_smallest = j
                
        swap(ordered, next_smallest, i)
        
    return ordered


#main
unsorted = [3, 1, 7, 2, 6, 5, 0, 4]
print("The unsorted list is: ", unsorted)
print("The sorted list is: ", selection_sort(unsorted))
