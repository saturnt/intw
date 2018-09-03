def permute(nums, invited, visiting):
    if len(invited) == 0:
        print visiting
        return
    else:
        curr=invited[0]
        rest=invited[1:]
        # Visit on an invitation
        permute(nums, rest, visiting+[curr])
        # Pass-on on the invitation
        permute(nums, rest, visiting)
        return
permute(['A', 'B', 'C'], ['A', 'B', 'C'], [])

'''
Result:

['A', 'B', 'C']
['A', 'B']
['A', 'C']
['A']
['B', 'C']
['B']
['C']
[]

'''
