t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    word = input()
    ans = 0
    f = 0
    g = 1
    i = 1
    prev = 0
    while i<n:
        # print(f"ans = {ans} word[{i}] = {word[i]} {prev}")
        if i - prev > 2:
            break
        if word[i] == ".":
            prev = i
            i += 1
        else:
            if word[i] == "@":
                prev = i
                ans += 1
                i += 1
            else:
                i += 1
    print(ans)




