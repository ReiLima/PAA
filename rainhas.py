def rainhas(n, s, r):
    if n == r:
        print(s)##TODAS_RAINHAS
        return []##TODAS_RAINHAS
       #return s##N_RAINHAS
    else:
        for i in range(1,n+1):
            if compativel(s, r + 1, i):
                s_ = s[:]
                s_.append(i)
                s__ = rainhas(n, s_, r+1)
                if len(s__) != 0:
                    return s__
        return []

def compativel(s, r, i):
    for j in range(1,r):
        if i - r == s[j-1] - j:
            return 0
        if i + r == s[j-1] + j:
            return 0
        if i == s[j-1]:
            return 0
    return 1

rainhas(8,[],0)