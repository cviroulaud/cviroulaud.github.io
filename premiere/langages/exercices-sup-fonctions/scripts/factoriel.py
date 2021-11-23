def facto(n):
    res = 1
    for i in range(1,n+1):
        res = res*i
    return res
a=facto(5)
print(a)