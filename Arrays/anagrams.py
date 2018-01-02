mylist=["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
mysortedlist=[]
mydict={}
i=0
for item in mylist:
    sitem=''.join(sorted(item))
    if sitem in mydict:
        mydict[sitem].append(item)
    else:
        mydict[sitem]=[item]


print mydict.values()
