t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    arr = [int(a) for a in input().split()]
    year = 0
    year += arr[0]
    for a in arr[1:]:
        year += 1
        if year%a != 0:
            r = year%a
            year -= r
            year += a

    print(year)
