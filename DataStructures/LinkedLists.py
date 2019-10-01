# Linked List Implementation
# Coded 27/09/2019

'''
TO FIX...

1. INSERTION ALGO (LESS THAN PROBLEM)
2. UI

'''

NULL_POINTER = -1  # Set null pointer to -1

import sys

class Node:

    def __init__(self):
        self.data = ""
        self.pointer = NULL_POINTER

    def __lt__(self, other):  # Code random behaviour for comparisons, so class behaves like record
        print(True)
        lowerThan = False  # Create flag to keep track of comparison status
        dataSelf = [ord(x) for x in self.data]  # ASCII data for string1
        dataNew = [ord(x) for x in other.data]  # ASCII data for string2

        i = 0  # Read strings in order from left to right
        while i < len(dataSelf) and i < len(dataNew):  # Both strings still have characters to compare 
            if dataSelf[i] < dataNew[i]:  # ASCII value @ index i lower in dataSelf
                lowerThan = True  # Set flag to True
                break

            i += 1

        return lowerThan  # Return comparison result


def createList():
    StartPointer = NULL_POINTER
    FreeListPointer = 0
    LinkedL = [Node() for i in range(7)]
    for i in range(6):
        LinkedL[i].pointer = i + 1

    LinkedL[6].pointer = NULL_POINTER

    return [LinkedL, StartPointer, FreeListPointer]
        

def insertNode(LinkedL: list, SP: int, FP: int, dataItem: str):

    if FP != NULL_POINTER:  # There is space in the array
        # Take node from free list and store the data item
        NewNodePtr = FP
        LinkedL[NewNodePtr].data = dataItem
        FP = LinkedL[FP].pointer
        # Find insertion sort
        thisNodePtr = SP
        previousNodePtr = NULL_POINTER

        while thisNodePtr != NULL_POINTER and \
                LinkedL[thisNodePtr] < LinkedL[NewNodePtr]:  # Pass node, otherwise have to override string function
            print(True)
            # While not at the end of the list and current item is less than new dataItem (not in alphabetical order)
            previousNodePtr = thisNodePtr  # Remember thisNodePtr
            # Follow the pointer to the next node
            thisNodePtr = LinkedL[thisNodePtr].pointer

            if previousNodePtr == NULL_POINTER:
                # Insert node @ start of the list
                LinkedL[NewNodePtr].pointer = SP
                print(SP)
                SP = NewNodePtr
                print(SP)
            else:  # Insert new node between previous node and this node
                LinkedL[NewNodePtr].pointer = thisNodePtr
                LinkedL[previousNodePtr].pointer = NewNodePtr

    return (LinkedL, SP, FP)


def findNode(LinkedL: list, SP: int, dataItem: str):
    currentNodePtr = SP
    while currentNodePtr != NULL_POINTER and \
        LinkedL[currentNodePtr].data != dataItem:

        currentNodePtr = LinkedL[currentNodePtr].pointer

    return currentNodePtr

def deleteNode(LinkedL: list, SP: int, FP: int, dataItem: str):
    thisNodePtr = SP

    while thisNodePtr != NULL_POINTER and \
        LinkedL[thisNodePtr].data != dataItem:

        previousNodePtr = thisNodePtr
        thisNodePtr = LinkedL[thisNodePtr].pointer

    if thisNodePtr != NULL_POINTER:
        if thisNodePtr == SP:
            SP = LinkedL[SP].pointer

        else:
            LinkedL[previousNodePtr].pointer = FP
            FP = thisNodePtr

    return (LinkedL, SP, FP)

def output(LinkedL: list):

    if len(LinkedL) != 0:
        
        print("\n{0:^10} | {1:^10} | {2:^10}".format("POSITION", "DATA", "POINTER"))
        
        for i in range(len(LinkedL)):
            print("{0:^10} | {1:^10} | {2:^10}".format(i, LinkedL[i].data, LinkedL[i].pointer))

    else:
        print("\nNo data in the list")

def end():
    sys.exit()

def main():

    listData = createList()

    while True:  # Loop until user exits program

        options = {0 : ("Insert a Node into List", insertNode),
                1 : ("Find a Node in the List", findNode),
                2 : ("Delete a Node from the List", deleteNode),
                3 : ("Output the Linked List", output),
                4 : ("End the program", end)}

        print("\nChoose an operation from the list... ")
        
        for key in options.keys():
            print("{}: {}".format(key, options[key][0]))

        decision = int(input("\nEnter your option: "))

        if decision == 0:
            item = input("Enter data for new node: ")
            [listData[0], listData[1], listData[2]] = options[0][1](listData[0], listData[1], listData[2], item)
        elif decision == 1:
            item = input("Enter item to be searched: ")
            options[1][1](listData[0], listData[1], item)
        elif decision == 2:
            item = input("Enter item to be deleted: ")
            options[2][1](listData[0], listData[1], listData[2], item)
        elif decision == 3:
            options[3][1](listData[0])
        elif decision == 4:
            options[4][1]()

if __name__ == "__main__":
    main()
