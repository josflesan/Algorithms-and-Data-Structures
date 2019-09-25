# Insertion Sort in Python
# Algorithms pt.1
# Coded 15/09/2019

from time import time as t
from random import randint as r

def insertion(l: list):

    for i in range(1, len(l)):

        item = l[i]
        j = i - 1

        while j > -1 and l[j] > item:
            l[j+1] = l[j]
            j -= 1

        l[j+1] = item

    return l


def main():

    l = [r(0, 50) for x in range(100)]

    # Before sorting
    print("\nUnsorted list: ", l)

    # After sorting
    start = t()
    print("\nSorted list: ", insertion(l))
    elapsed = t() - start
    print(f"\nTime taken: {elapsed*1000} ms")


if __name__ == "__main__":
    main()
