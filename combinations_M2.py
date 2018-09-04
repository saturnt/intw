def permute(str, chosen):
    #print str, chosen
    if len(str) == 0:
        print chosen
        return
    for idx in range(0, len(str)):
        char=str[idx]
        # Choose
        chosen.append(char)
        # Explore
        permute(str[0:idx]+str[idx+1:], chosen)
        # unchoose
        chosen.remove(char)

chosen=[]
permute(['A', 'B', 'C'], chosen)

'''
Result:

['A', 'B', 'C']
['A', 'C', 'B']
['B', 'A', 'C']
['B', 'C', 'A']
['C', 'A', 'B']
['C', 'B', 'A']

'''
