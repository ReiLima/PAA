def sat(f, n, k):
    s = [-1 for i in range(2*n)]
    return bt(f, n, k, s, 0)

def bt(f, n, k, s, r):
    if k == 0:
        return 1
    
    s_ = s[:]
    s_[r+1] = 1
    s_[n+r+1] = 0
    k_ = k
    i_ = 0
    f_ = f[:]

    for i in range(k):
        p = 0
        for x in f[i]:
            if x == r+1:
                k_ = k_-1
                p = 1
            if x == n+r+1:
                del(f_[i][f_[i].index(x)])
                i_+=1
                p = 1
                if(len(f[i]) == 1):
                    return 0
            if p == 0:
                f_[i_] = f[i][:]

    s__ = s[:]
    s__[r+1] = 1
    s__[n+r+1] = 0
    k__ = k
    i__ = 0
    f__ = f[:]

    for i in range(k):
        p = 0
        for x in f[i]:
            if x == r+1:
                k__ -= 1
                p = 1
            if x == n+r+1:
                del(f__[i][f__[i].index(x)])
                i__+=1
                p = 1
                if(len(f[i]) == 1):
                    return 0
            if p == 0:
                f__[i__] = f[i][:]
    
    return bt(f_, n, k_, s_, r+1) or bt(f__, n, k__, s__, r+1)



print(sat([[4,5,6],[4,5,3],[4,2,6],[4,2,3],[1,5,6],[1,5,3],[1,2,6],[1,2,3]], 3, 8))