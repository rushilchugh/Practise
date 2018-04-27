"""
LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example,
“abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. So a string of length n has 2^n different
possible subsequences.

It is a classic computer science problem, the basis of diff (a file comparison program that outputs the differences
between two files), and has applications in bioinformatics.

LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
"""

def LCS(seqA, seqB):
    lenA = len(seqA)
    lenB = len(seqB)

    L = [0 for _ in range(max(lenA, lenB))]

    for i in range(max(lenA, lenB)):
        for j in range(0, i + 1):
            if seqA[i] == seqB[j] and L[j] + 1 > L[i]:
                L[i] = L[j] + 1

    return L

print(LCS("ABCDGH", "AEDFHR"))



