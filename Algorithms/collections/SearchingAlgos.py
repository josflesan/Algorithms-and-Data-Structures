# Searching Algorithms in Python
# Coded 15/09/2019 - ?????

'''
CONTENTS...

Linear Search... linear(list, integer)
Binary Search... binary(list, integer)

'''

def linear(l: list, search: int):

    pos = None  # By default, no position returned

    for i in range(len(l)):
        if l[i] == search:
            pos = i
            break

    return pos


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
            continue

        elif lowBound >= upBound:
            SearchFailed = True
            continue

        elif l[mid] < item:
            lowBound = mid + 1

        else:
            upBound = mid - 1

    return pos
