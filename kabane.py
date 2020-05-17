"""
Kabane algorithm is used to find the largest subarray sum, i.e. find the maximum sum possible by adding contiguous array
elements.
Time complexity: O(n)
"""

from typing import List


def kabane(arr: List[int]):
    max_so_far = float('-inf')
    max_till_here = 0
    for i in arr:
        max_till_here += i
        if max_so_far < max_till_here:
            max_so_far = max_till_here
        if max_till_here < 0:
            max_till_here = 0
    return max_so_far


if __name__ == '__main__':
    print(kabane([1, 2, -4, 5, -3, 9, -10, 5, 8]))
    print(kabane([-1, -2, -5, -2, -9, -10, -2]))
