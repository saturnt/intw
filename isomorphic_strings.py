def IsomorphicStrings(s, t):
    #s = "egg", t = "add"
    idx=0
    hashmap=dict()
    n=len(s)

    while(idx<n):
        if s[idx] not in hashmap:
            if t[idx] in hashmap.values():
                return False
            hashmap[s[idx]]=t[idx]
        else:
            val = hashmap[s[idx]]
            if t[idx] != val:
                return False
        idx+=1
    return True

s = "egd"
t = "add"
print IsomorphicStrings(s, t)
