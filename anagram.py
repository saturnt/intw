import sys

def isAnagram(s, t):
    charmap=[0]*26

    slen=len(s)
    tlen=len(t)
    if slen != tlen:
        return False
    idx=0
    for idx in range(0, len(s)):
        charmap[ord(s[idx]) - 97] += 1

    print charmap

    idx=0
    count=slen
    while(idx < len(t)):
        if charmap[ord(t[idx]) - 97] > 0:
            charmap[ord(t[idx]) - 97]-=1
        else:
            return False
        idx+=1

    return True

s = "rat"
t = "car"
print isAnagram(s, t)
sys.exit()
