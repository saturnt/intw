import sys
import math
import heapq

def reverse_vowels(s):
    left=0
    right=len(s)-1
    vowels = ['a', 'e', 'i', 'o', 'u']
    s=list(s)
    while(left <= right):
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            continue

        if s[left] not in vowels:
            left+=1
        if s[right] not in vowels:
            right-=1
    print ''.join(s)
reverse_vowels('leetcode')
