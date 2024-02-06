t = int(input())

alphabet = [a for a in "abcdefghijklmnopqrstuvwxyz"]
while t > 0:
    t -= 1
    n = int(input())
    arr = [int(a) for a in input().split()]
    high = max(arr)
    dict = {}
    for a in range(high+1):
        dict[a] = []
    index = 0
    ans = ""
    for a in arr:
        # print(f"ans = {ans} a = {a} dict = {dict}" )
        if a == 0:
            c = alphabet[index]
            if 1 in dict:
                dict[1].append(c)
            else:
                dict[1] = [c]
            ans += c
            index += 1
        else:
            for i in range(a+1)[::-1]:
                if i in dict:
                    r = dict[i][0]
                    dict[i] = dict[i][1:]
                    ans += r
                    if i+1 in dict:
                        dict[i + 1].append(r)
                    else:
                        dict[i+1] = [r]
                    break

    print(ans)
