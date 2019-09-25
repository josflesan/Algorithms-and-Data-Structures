# Binary Search in Python
# Algorithms pt. 2
# Coded 15/09/2019

from time import time as t
from random import randint as r

def binary(l: list, item: int):

    pos = None

    Found = False
    SearchFailed = False
    lowBound = 0
    upBound = len(l) - 1

    while not Found and not SearchFailed:

        mid = (lowBound + upBound) // 2

        if l[mid] == item:
            pos = mid
            Found = True

        elif lowBound >= upBound:
            SearchFailed = True

        elif l[mid] < item:
            lowBound = mid + 1

        else:
            upBound = mid - 1

    return pos


def main():

    l = [r(0, 50) for x in range(100)]

    # Output the list for the user
    print("\nList to be searched: ", l)

    # Ask for item to be searched
    search = int(input("\nPlease enter the number you would like to search for in the list: "))

    start = t()
    pos = binary(l, search)  # Position of item
    elapsed = float(t() - start)

    if pos != None:
        print(f"\nItem {search} found in position {pos+1}")
        print(f"Time taken: {elapsed}")
    else:
        print(f"\nItem {search} not found")


if __name__ == "__main__":
    main()
