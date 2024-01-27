t = int(input())

alphabet = "abcdefghijklmnopqrstuvwxyz"
while t>0:
    t -= 1
    word = [int(a) for a in input().split()]
    n = word[0]
    k = word[1]
    m = word[2]
    s = input()
    part = alphabet[:k]
    did_loop_break = False
    for l in part:
        # print(f"letter = {l} count = {s.count(l)}")
        if s.count(l) < n:
            print("NO")
            print(l*n)
            did_loop_break = True
            break

    if not did_loop_break:
        print("YES")

