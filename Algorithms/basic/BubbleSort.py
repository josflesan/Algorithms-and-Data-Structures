# Bubble Sort in Python
# Algorithms pt. 3
# Coded 15/09/2019

from time import sleep, time
from random import randint as r

def bubble(l: list):
    for i in range(len(l)):
        for j in range(len(l)-1-i):

            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp

    return l


def eff_bubble(l: list):
    Swapped = False
    i = 0
    while Swapped or i < len(l):

        Swapped = False

        for j in range(len(l)-1-i):

            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
                Swapped = True


        i += 1

    return l



def main():

    l = [r(0, 50) for x in range(100)]

    # Unsorted List
    print("\nUnsorted List: \n", l)

    # Sorted List with Normal Sort
    start1 = time()
    print("\nSorted List (Normal Bubble Sort): \n", bubble(l))
    elapsed1 = time() - start1
    print(f"\nTime taken: {elapsed1*1000} ms")

    sleep(2)

    # Sorted List with Improved Sort
    start2 = time()
    print("\nSorted List (Efficient Bubble Sort): ", eff_bubble(l))
    elapsed2 = time() - start2
    print(f"\nTime taken: {elapsed2*1000} ms")


if __name__ == "__main__":
    main()
