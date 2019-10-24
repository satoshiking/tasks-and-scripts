n, k = map(int, input().split())

def c(n, k):
    if k == 0:
        return 1

    if k > n:
        return 0
    else:
        return c(n-1, k) + c(n-1, k-1)

print(c(n, k))
