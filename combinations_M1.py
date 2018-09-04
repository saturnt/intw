def swap(nums, start, end):
    temp=nums[start]
    nums[start]=nums[end]
    nums[end]=temp

def combinations(nums, start, end):
    if start >= end:
        print nums
        return
    else:
        for i in range(start, end):
            swap(nums, i, start)
            combinations(nums, start+1, end)
            swap(nums, i, start)

combinations(['A', 'B', 'C'], 0, 3)

'''
Result:
['A', 'B', 'C']
['A', 'C', 'B']
['B', 'A', 'C']
['B', 'C', 'A']
['C', 'B', 'A']
['C', 'A', 'B']
'''


