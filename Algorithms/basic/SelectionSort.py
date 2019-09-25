# Selection Sort in Python
# Algorithms pt.5
# Coded 15/09/2019

from random import randint as r

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

def main():
    l = [r(0, 50) for x in range(10)]

    # Before Sorting
    print("\nUnsorted List: ", l)

    # After Sorting
    print(f"Sorted List: {selection(l)}\n")

if __name__ == "__main__":
    main()