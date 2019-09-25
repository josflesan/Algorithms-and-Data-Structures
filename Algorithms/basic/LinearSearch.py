# Linear Search in Python
# Algorithms pt. 4
# Coded 15/09/2019

from time import time as t
from random import randint as r

def linear(l: list, search: int):

    pos = None  # By default, no position returned

    for i in range(len(l)):
        if l[i] == search:
            pos = i
            break
    
    return pos


def main():

    l = [r(0, 1000) for x in range(100)]

    # Output list for user to see
    print("\nList to be searched: ", l)

    # Ask user for value to be searched
    search = int(input("\nPlease enter the value you would like to search for in the list: "))

    # Run function and output result
    start = t()
    pos = linear(l, search)
    elapsed = float(t() - start)

    if pos is not None:
        print(f"\nValue {search} found in position {pos+1} in the list")
        print(f"Time taken: {elapsed*1000} ms")
    else:
        print(f"\nValue {search} not found in the list")

if __name__ == "__main__":
    main()

