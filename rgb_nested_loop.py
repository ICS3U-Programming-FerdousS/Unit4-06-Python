#!/usr/bin/env python3
# Created by: Ferdous Sediqi
# Created on: April 28, 2022
# In this program we display all possible RGB color from 200 to 255 pixeles 
# using nested loops.


def main():
    # variables
    counter1 = 0
    counter2 = 0
    counter3 = 0

    # using nested loops to display colors code
    for counter1 in range(200, 256):
        for counter2 in range(200, 256):
            for counter3 in range(200, 256):
                print("\033[31m", "RGB '({0})' '({1})' '({2})' "
                    .format(counter1, counter2, counter3))
    

if __name__ == "__main__":
    main()
