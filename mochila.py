def mochila(v, p, c, i):
    if c <= 0 or i == 0:
        return 0
    else:
        if p[i] > c:
            return mochila(v, p, c, i-1)
        else:
            return max(mochila(v, p, c, i-1), mochila(v, p, c - p[i], i-1) + v[i])

v = [1, 3, 5, 7, 15, 2]
p = [5, 2, 10, 8, 10, 8]
c = 25
n = len(v)

print(mochila(v, p, c, n-1))