__author__ = 'Rushil'

import os
from CountingSheep.Solution import main

large_file_m, small_file_m = [i for i in os.listdir(".") if i.endswith("in")]


def small():
    global small_file_m

    small_file = open(small_file_m, "r")

    n_cases_small = int(small_file.readline())
    small_solution = open("small_ans.out", "w")

    for i in range(n_cases_small):
        print("Case #{0}: {1}".format(i + 1, main(int(small_file.readline()))), file = small_solution)

    small_solution.close()
    small_file.close()



def large():

    global large_file_m

    large_file = open(large_file_m, "r")

    n_cases_large = int(large_file.readline())
    large_solution = open("large_ans.out", "w")

    for i in range(n_cases_large):
        print("Case #{0}: {1}".format(i + 1, main(int(large_file.readline()))), file = large_solution)

    large_solution.close()
    large_file.close()

large()

