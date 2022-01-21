import heapq
from heapq import heappop, heappush

class Node:
    def __init__(self, dataval=None, next=None):
        self.dataval = dataval
        self.nextval = next
    
    # Override the `__lt__()` function to make `Node` class work with min-heap 
    def __lt__(self, other):
        return self.dataval < other.dataval

def printList(node):
    while node:
        print(node.dataval, end=' —> ')
        node = node.nextval
 
    print("None")


def mergeKs(lst):
 
    # create a min-heap using the first node of each list
    pq = [x for x in lst]
    heapq.heapify(lst) 


 
    # take two pointers, head and tail, where the head points to the first node
    # of the output list and tail points to its last node
    head = None
    last = None
 
    # run till min-heap is empty
    while pq:
 
        # extract the minimum node from the min-heap
        min = heappop(pq)
 
        # add the minimum node to the output list
        if head is None:
            head = min
            last = min
        else:
            last.nextval = min
            last = min
 
        # take the next node from the "same" list and insert it into the min-heap
        if min.nextval:
            heappush(pq, min.nextval)
 
    # return head node of the merged list
    return head
    


k=3
slst=Node()
lst=[None]*k

lst[0]=Node(1)
lst[0].nextval=Node(3)
lst[0].nextval.nextval=Node(5)
lst[0].nextval.nextval.nextval=Node(7)
# list1.listprint()


lst[1]=Node(2)
lst[1].nextval=Node(4)
lst[1].nextval.nextval=Node(6)
lst[1].nextval.nextval.nextval=Node(8)

lst[2]=Node(0)
lst[2].nextval=Node(9)
lst[2].nextval.nextval=Node(10)
lst[2].nextval.nextval.nextval=Node(11)

slst=mergeKs(lst)

printList(slst)







