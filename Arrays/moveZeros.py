nums = [0, 1, 0, 3, 12]
insert_idx=0
for i in xrange(0, len(nums)):
    if nums[i] != 0:
        nums[insert_idx]=nums[i]
        insert_idx+=1

for i in range(insert_idx, len(nums)):
    nums[i]=0

print nums
