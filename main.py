from Algorithms.collections.SearchingAlgos import *
from Algorithms.collections.SortingAlgos import *
# from DataStructures.collections.something import *

from random import randint as r

def main():

    l = [r(0, 50) for i in range(10)]

    command_dict = {
        "linear": [linear, "Linear Search"],
        "binary": [binary, "Binary Search"],
        "bubble": [bubble, "Bubble Sort"],
        "fbubble": [eff_bubble, "Efficient Bubble Sort"],
        "insertion": [insertion, "Insertion Sort"],
        "selection": [selection, "Selection Sort"]
    }

    print("***************************************")
    print("Welcome to Algorithms in Python v.0.1")
    print("Type the following commands to access desired algorithm\n")
    for key in command_dict.keys():
        print(f"'{key}'': Run {command_dict[key][1]}")
    print("***************************************")
    
    while True:
        try:
            command = input("Please enter the algorithm to run: ")
            cd = command_dict[command]  # Save command
            break
        except KeyError:
            print("Please, only choose commands that are on the list... ")

    # RUN APPROPRIATE PROGRAM
    print("\nList in use: ", l)

    if command == "linear" or command == "binary":
        while True:
            try:
                search = int(input("Please enter value to be searched: \n"))
                break

            except ValueError:
                print("Only integers here, please...") 

        print(f"Value {search} found in position {cd[0](l, search)+1}\n")
    else:
        print(f"Sorted list: {cd[0](l)}\n")

if __name__ == "__main__":
    main()
