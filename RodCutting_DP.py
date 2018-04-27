__author__ = 'Rushil'

"""
The rod-cutting problem is the following. Given a rod of length n inches and a table of prices pi for i = 1, 2....N,
determine the maximum revenue rn obtainable by cutting up the rod and selling the pieces.
Note that if the price pn for a rod of length n is large enough, an optimal solution may require no cutting at all.
"""

length = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
price = [1, 5, 8, 9, 10, 17, 20, 24, 30]

#Recursive Relation

#Let the length of a given rod be N
#To Maximize profits,
#CutRod(N) = Max{CutRod(N - i) + Price[i]}
#CutRod(N - i) - Recurses to the subproblem solution in the recursion stack
#Note that, I'll have to consider all possible guesses, i.i all possible i's