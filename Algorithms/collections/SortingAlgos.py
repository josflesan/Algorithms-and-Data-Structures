# Collection of Sorting Algos in Python
# Coded 15/09/2019 - ?????

'''
CONTENTS...

Bubble Sort (O(n^2))... bubble(list)
Efficient Bubble Sort (O(n^2))... eff_bubble(list) 
Insertion Sort (O(n^2)/O(n))... insertion(list)
Selection Sort (O(n^2))... selection(list)

'''

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


def selection(l: list):
    for i in range(len(l)):
        minimum = i

        for j in range(i+1, len(l)):
            if l[j] < l[minimum]:
                minimum = j

        temp = l[i]
        l[i] = l[minimum]
        l[minimum] = temp

    return l


def insertion(l: list):

    for i in range(1, len(l)):

        item = l[i]
        j = i - 1

        while j > -1 and l[j] > item:
            l[j+1] = l[j]
            j -= 1

        l[j+1] = item

    return l
