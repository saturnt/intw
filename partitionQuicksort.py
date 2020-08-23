
'''
Quicksort partition:
'''

def find_partition(nums, left, right):
    pivot=nums[right]
    left_idx=left
    right_idx=right-1

    if left_idx > right_idx:
        return left_idx

    while(left_idx <= right_idx):
        if nums[left_idx] > pivot:
            nums[left_idx], nums[right_idx]=nums[right_idx], nums[left_idx]
            right_idx-=1
        else:
            left_idx+=1
    nums[left_idx], nums[right] = nums[right], nums[left_idx]
    print left_idx
    print nums
    return left_idx

def quicksort(nums, left, right):
    if(left < right):
        p = find_partition(nums, left, right)
        quicksort(nums, left, p-1)
        quicksort(nums, p+1, right)

nums=[6, 7, 8, 2, 1]
left=0
right=len(nums)-1
quicksort(nums, left, right)
sys.exit()
