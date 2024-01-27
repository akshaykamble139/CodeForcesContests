t = int(input())

alphabet = "abcdefghijklmnopqrstuvwxyz"
while t>0:
    t -= 1
    word = [int(a) for a in input().split()]
    n = word[0]
    k = word[1]
    part = alphabet[:k]
    ans = ""
    for _ in range(n):
        ans += part

    print(ans)
