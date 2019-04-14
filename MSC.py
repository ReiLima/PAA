def msc(l, i):
    if len(l) == 1:
        if l[0] > i:
            return 1
        else:
            return 0
    else:
        if l[0] > i:
            return max(msc(l[1:],i), msc(l[1:], l[0]) + 1)
        else:
            return msc(l[1:],i)

def scm(l, k):
    if len(l) == 0 or len(k) == 0:
        return 0
    else:
        if l[0] == k[0]:
            return scm(l[1:], k[1:]) + 1
        else:
            return max(scm(l[1:], k), scm(l, k[1:]))
    
        

def msc_d(l, x, j, M):
    

    if j == len(l):
        print(j)
        if l[j] > x:
            return 1
        else:
            return 0
    else:
        if x < 0:
            print(x, j+1)
            return max(msc_d(l, x, j+1, M), msc_d(l, l[j], j+1, M) + 1)
        else:
            print(x, j+1)
            if l[j] <= x:
                if M[x][j+1] == -1:
                   M[x][j+1] = msc_d(l, x, j+1, M)
    
                return M[x][j+1]
            else:
                if M[x][j+1] == -1:
                   M[x][j+1] = msc_d(l, x, j+1, M)
                if M[l[j]][j+1] == -1:
                   M[l[j]][j+1] = msc_d(l, l[j], j+1, M)
    
                return max(M[x][j+1], M[l[j]][j+1] + 1)


print (scm(['b', 'd', 'c', 'a', 'a', 'b', 'a'],['a', 'b', 'c', 'b', 'd', 'a', 'b']))
print(scm(['a', 'b', 'c'],['a', 'd', 'd']))
