from __future__ import print_function
import sys

def indent(n):
    for i in range(0, n):
        sys.stdout.write("    ")

def permute(mystr, chosen):
    #print str, chosen
    indent(len(chosen))
    print("permute(" + str(mystr) + "," + str(chosen) + ")")
    if len(mystr) == 0:
        #print chosen
        return
    for idx in range(0, len(mystr)):
        char=mystr[idx]
        # Choose
        chosen.append(char)
        # Explore
        permute(mystr[0:idx]+mystr[idx+1:], chosen)
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

permute(['A', 'B', 'C'],[])
    permute(['B', 'C'],['A'])
        permute(['C'],['A', 'B'])
            permute([],['A', 'B', 'C'])
        permute(['B'],['A', 'C'])
            permute([],['A', 'C', 'B'])
    permute(['A', 'C'],['B'])
        permute(['C'],['B', 'A'])
            permute([],['B', 'A', 'C'])
        permute(['A'],['B', 'C'])
            permute([],['B', 'C', 'A'])
    permute(['A', 'B'],['C'])
        permute(['B'],['C', 'A'])
            permute([],['C', 'A', 'B'])
        permute(['A'],['C', 'B'])
            permute([],['C', 'B', 'A'])


'''
