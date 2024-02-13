t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    arr = [int(a) for a in input().split()]
    l = 0
    v = arr[0]
    for i in range(1,n):
        if arr[i] == v:
            l += 1
        else:
            break
    k = n-1
    w = arr[k]
    for j in range(n-1)[::-1]:
        if arr[j] == w:
            k -= 1
        else:
            break
    # print(f"n = {n} k = {k} l = {l}")
    if v == w:
        if k==0 and l==n-1:
            print(0)
        else:
            print(k-l-1)
    else:
        print(min(n-l-1,k))
