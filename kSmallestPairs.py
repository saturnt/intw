'''
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence: 
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

'''

import sys
import math
import heapq


def kSmallestPairs(nums1, nums2, k):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[List[int]]
    """
    import heapq
    h = []
    prev_i = None
    for i in range(0, len(nums1)):
        if prev_i != None and nums1[i] > nums1[prev_i] and len(h) == k:
            # No need to continue
            break
        for j in range(0, len(nums2)):
            num1 = nums1[i]
            num2 = nums2[j]

            if len(h) < k:
                heapq.heappush(h, (-(num1 + num2), [num1, num2]))
                continue

            if len(h) and h[0][0] < -(num1 + num2):
                heapq.heappop(h)
                heapq.heappush(h, (-(num1 + num2), [num1, num2]))

        prev_i = i
    result = []
    if len(h):
        while(len(h)):
            result.insert(0, heapq.heappop(h)[1])
    return result


nums1 = [1,7,11]
nums2 = [2,4,6]
#nums1 = [1,1,1]
#nums2 = [1,2,3]
nums1=[1, 2]
nums2=[3]
nums1=[1,1,2]
nums2=[1,2,3]
k=10
#k = 3
print kSmallestPairs(nums1, nums2, k)
sys.exit()
