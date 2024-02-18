t = int(input())
while t > 0:
    t -= 1
    sample = [int(a) for a in input().split()]

    n = sample[0]
    m = sample[1]
    arr = [int(a) for a in input().split()]
    i = 0
    j = n - 1

    mul = 1
    for a in arr:
        mul *= a

    word = input()
    ans = str(mul % m)
    if n > 1:
        for a in word[:-1]:
            # print(f"ans = {ans} mul = {mul} i = {i} j = {j}")
            if a == "L":
                mul //= arr[i]
                ans += " " + str(mul % m)
                i += 1
            else:
                mul //= arr[j]
                ans += " " + str(mul % m)
                j -= 1
        print(ans)
    else:
        print(mul % m)
