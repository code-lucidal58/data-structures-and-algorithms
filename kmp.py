"""
KMP (Knuth Morris Pratt) Pattern Searching Algorithm is used for finding the indices of the presence of a given
substring pattern in a string. It is an improvement on Naive.
If you do not know the algorithm from beforehand, please watch this https://www.youtube.com/watch?v=V5-7GzOfADQ from 7:41
Time Complexity: O(n) or O(n+m)
"""


def kmp(s: str, pat: str):
    lps = [0] * len(pat)
    i, l = 1, 0
    while i < len(pat):  # create pi table
        if pat[i] == pat[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l != 0:
                l = lps[l - 1]
            else:
                i += 1
    i, j = 0, 0
    indices = []
    while i < len(s):
        if s[i] == pat[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j-1]
        if j == len(pat):
            indices.append(i - len(pat))
            j = lps[j-1]
    return indices


if __name__ == '__main__':
    print(kmp("AABAACAADAABAABA", "AABA"))
    print(kmp("AABCCAADDEE", "FAA"))
    print(kmp("AAAAAAAAAAAAAAAAAA", "AAAAA"))
    print(kmp("AAAAAAAAAAAAAAAAAB", "AAAAB"))
    print(kmp("ABCDCDDDCDE", "ADE"))
