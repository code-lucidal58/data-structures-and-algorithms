"""
Rabin-Karp algorithm is for finding the indices of the presence of a given substring pattern in a string. It is an
improvement on Naive.
Time Complexity: O(n-m+1) (average case) O(mn) (worst case) when there are multiple spurious hits
Terminologies: Hashcode: (code calculated for pattern string and each substring of the main string of length m)
RollingHash Function: (calculating hash of substring in main string in O(1))
Spurious Hits: (Hascode match found but pattern match not found)
"""


def rabin_karp(s: str, pat: str):
    n = len(s)
    m = len(pat)
    q = 10 ** 7 + 1
    d = 256  # possible number of characters in the string
    hash_str = 0
    hash_pat = 0
    l = []
    for i in range(m):
        hash_str = ((hash_str * d) + ord(s[i])) % q
        hash_pat = ((hash_pat * d) + ord(pat[i])) % q
    for i in range(n - m + 1):
        if hash_str == hash_pat:
            j = 0
            while j < m:
                if s[i + j] != pat[j]:
                    break
                j += 1
            if j == m:
                l.append(i)
        if i < n - m:
            hash_str = ((hash_str - (ord(s[i]) * (d ** (m - 1)))) * d + ord(s[i + m])) % q
            if hash_str < 0:
                hash_str += q
    return l


if __name__ == '__main__':
    print(rabin_karp("AABAACAADAABAABA", "AABA"))
    print(rabin_karp("AABCCAADDEE", "FAA"))
    print(rabin_karp("AAAAAAAAAAAAAAAAAA", "AAAAA"))
    print(rabin_karp("AAAAAAAAAAAAAAAAAB", "AAAAB"))
    print(rabin_karp("ABCDCDDDCDE", "ADE"))
