def merge(nums1, nums2):
    print nums1, nums2
    if len(nums1) == 0:
        return nums2
    if len(nums2) == 0:
        return nums1
    if nums1[0] >= nums2[0]:
        return [nums2[0]] + merge(nums1, nums2[1:])
    else:
        return [nums1[0]] + merge(nums1[1:], nums2)

print merge([1, 2, 6], [0, 1, 2, 3])

# Divide and conquer
def merge_sort(nums, low, high):
    # Smallest problem is a problem with just 1 element
    if (high > low):

        # Lets divide the problem
        mid=(high+low)/2
        nums1=merge_sort(nums, low=low, high=mid) # Dont forget the low=low. Dont use low=0
        nums2=merge_sort(nums, low=mid+1, high=high)

        # Lets merge the problem to form a solution
        print "Merging " + str(nums1) + " and " + str(nums2)
        ans = merge(nums1, nums2)
        print ans
        return ans
    if low == high:
        print "low = " + str(low) + " Returning " + str([nums[low]])
        return [nums[low]]

nums=[45,12,85,32]
print merge_sort(nums, 0, len(nums) - 1)
