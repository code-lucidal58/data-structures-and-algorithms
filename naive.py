"""
Naive algorithm is used for finding the indices of the presence of a given substring pattern in a string.
Time Complexity O(m*(n-m+1)) or O(nm) where n and m are the lengths of string snd substrings respectively
"""


def naive(s: str, pat: str):
    n = len(s)
    m = len(pat)
    l = []
    i = 0
    while i < (n - m + 1):
        j = 0
        while j < m and s[i + j] == pat[j]:
            j += 1
        if j == m:
            l.append(i)
        i += 1
    return l


if __name__ == '__main__':
    print(naive("AABAACAADAABAABA", "AABA"))
    print(naive("AABCCAADDEE", "FAA"))
    print(naive("AAAAAAAAAAAAAAAAAA", "AAAAA"))  # worst case
    print(naive("AAAAAAAAAAAAAAAAAB", "AAAAB"))  # worst case
