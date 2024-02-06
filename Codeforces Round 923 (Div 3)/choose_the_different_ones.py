t = int(input())

while t > 0:
    t -= 1
    word = [int(a) for a in input().split()]
    n = word[0]
    m = word[1]
    k = word[2]

    ans = [a for a in range(1,k+1)]
    A = [int(a) for a in input().split() if 1<=int(a)<=k]
    B = [int(a) for a in input().split() if 1<=int(a)<=k]

    if len(set(A + B))<k:
        print("NO")
    elif len(set(A))<k//2 or len(set(B))<k//2:
        print("NO")
    else:
        print("YES")
        # 1 2 3 4 5 6
        # 5 6 7 8 9 10
