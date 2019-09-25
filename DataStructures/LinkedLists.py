# Linked List implementation in Python
# Coded 25/09/2019

'''
SOLUTION NOT WORKING, FIX...

1. Make it ordered linked list
2. Implement insertion algo correctly

'''


class Node:

    data = ""  # No data to begin with
    pointer = None  # None ptr will be taken as empty set

    def __init__(self, data_:str, pointer_:int):
        self.data = data_
        self.pointer = pointer_

class LinkedList:

    startPtr = None
    freeListPtr = 0
    thisNodePtr = -1
    previousNodePtr = -1
    listNode = []

    def __init__(self, length:int):

        for i in range(length-1):
            data = str(input(f"Enter data for node {i}: "))
            n = Node(data, i+1)  # Create first 6 nodes with pointers mapping consecutive values
            self.listNode.append(n)
            self.startPtr = 0  # If at least one value inserted, startPtr = first elt.

        self.listNode.append(Node("", None))  # Last position append node with NullPointer

    def output(self):
        
        print("{0:^10} | {1:^10}".format("DATA", "POINTER"))
        print("*"*25)

        for node in range(len(self.listNode)):
            data = self.listNode[node].data
            if len(data) > 6:
                data = data[:6]  # Crop data when outputting if larger than 6 (for aesthetic reasons)
            print(f"[{data:^8}] | [{self.listNode[node].pointer}]")

        print("*"*25)

    
    def findNode(self, dataItem:str):
        currentNodePtr = self.startPtr  # Start @ beginning of list
        
        while currentNodePtr != None \
                and self.listNode[currentNodePtr].data != dataItem:  
                
            # WHILE not end of the list AND Item not found in list
            # Follow the pointer to the next node

            currentNodePtr = self.listNode[currentNodePtr].pointer  

        return currentNodePtr

    def delete(self, dataItem:str):

        self.thisNodePtr = self.startPtr  # Start @ beginning of list

        while self.thisNodePtr != None and \
            self.listNode[self.thisNodePtr].data != dataItem:  # While not end of the list

            self.previousNodePtr = self.thisNodePtr  # Remember this node and follow the pointer to next node
            self.thisNodePtr = self.listNode[self.thisNodePtr].pointer

        if self.thisNodePtr != None:  # Node exists in list

            if self.thisNodePtr == self.startPtr:  # First node to be deleted
                self.startPtr = self.listNode[self.startPtr].pointer  # Update startPtr
            else:
                self.listNode[self.previousNodePtr].pointer = self.listNode[self.thisNodePtr].pointer

            self.listNode[self.thisNodePtr].pointer = self.freeListPtr
            self.freeListPtr = self.thisNodePtr 

    def insertNode(self, newItem:str):

        if self.freeListPtr != None:  # There is space in the array

            # Take node from free list and store data item
            newNodePtr = self.freeListPtr
            self.listNode[newNodePtr].data = newItem
            self.freeListPtr = self.listNode[self.freeListPtr].pointer
            # Find insertion point
            self.thisNodePtr = self.startPtr  # Start at beginning of list
            self.previousNodePtr = None
            while self.thisNodePtr != None and \
                ord(self.listNode[self.thisNodePtr].data[0]) < ord(newItem[0]):

                # While not end of list or empty list
                self.previousNodePtr = self.thisNodePtr  # Remember this node
                # Follow the pointer to the next node
                self.thisNodePtr = self.listNode[self.thisNodePtr].pointer

            if self.previousNodePtr == None:  # Insert new node at start of list
                self.listNode[newNodePtr].pointer = self.startPtr
                self.startPtr = newNodePtr
            else:  # Insert new node between previous node and this node
                self.listNode[newNodePtr].pointer = self.thisNodePtr
                self.listNode[self.previousNodePtr].pointer = newNodePtr

def main():

    l = LinkedList(10)
    l.output()

    l.insertNode("Miriam")

    l.output()


if __name__ == "__main__":
    main()

