t = int(input())


def get_result():
    val = [int(a) for a in input().split()]
    n = val[0]
    q = val[1]
    arr = [int(a) for a in input().split()]
    sum_values = []
    while q > 0:
        q -= 1
        queries = [int(a) for a in input().split()]
        s = queries[0] - 1
        d = queries[1]
        k = queries[2]
        if (0<=s<n and 1<=d<=n and 1<=k<=n) and s + (k-1) * d < n:
            curr = k-1
            sum = 0
            while s < n and curr >= 0:
                sum += (k-curr) * arr[s]
                s += d
                curr -= 1
                # print(f"sum = {sum} curr = {curr}")
            sum_values.append(str(sum))

    print(" ".join(sum_values))


while t>0:
    t -=1
    get_result()