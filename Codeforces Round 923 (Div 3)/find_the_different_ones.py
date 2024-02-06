t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    arr = [int(a) for a in input().split()]
    q = int(input())
    dict = {}
    for i in range(n):
        if arr[i] in dict:
            dict[arr[i]].append(i)
        else:
            dict[arr[i]] = [i]
    print(dict)
    while q>0:
        q -= 1
        word = [int(a) for a in input().split()]
        l = word[0]-1
        r = word[1]-1








