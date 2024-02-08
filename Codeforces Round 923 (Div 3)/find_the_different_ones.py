t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    arr = [int(a) for a in input().split()]
    p = [-1]*n
    for i in range(1,n):
        p[i] = p[i-1]
        if arr[i] != arr[i-1]:
            p[i] = i-1
    # print(f"p = {p}")
    q = int(input())

    while q>0:
        q -= 1
        word = [int(a) for a in input().split()]
        l = word[0]-1
        r = word[1]-1

        if p[r]<l:
            print("-1 -1")
        else:
            print(p[r]+1, r+1)








