import sys
import math
import heapq


def find_kth_largest(nums, k):
    h=[]
    capacity = k
    for num in nums:
        if len(h):
            element=h[0]
            if num >= element:
                heapq.heappush(h, num)
            elif len(h) < capacity:
                heapq.heappush(h, num)
            if len(h) > capacity:
                heapq.heappop(h)
        else:
            heapq.heappush(h, num)

    print h
    print heapq.heappop(h)

nums=[3,2,3,1,2,4,5,5,6]
k=4
find_kth_largest(nums, k)

sys.exit()
