t = int(input())

alphabet = " abcdefghijklmnopqrstuvwxyz"
while t > 0:
    t -= 1
    n = int(input())
    ans = ""
    has_answer = False
    while n > 0 and not has_answer:
        if n >= 28:
            n -= 26
            ans += alphabet[26]
            if len(ans) == 3:
                has_answer = True
                print(ans)
                break
        else:
            if n == 26:
                l = len(ans)
                if l == 0:
                    has_answer = True
                    ans = "aa" + alphabet[n-2]
                    print(ans)
                elif l == 1:
                    has_answer = True
                    ans = "ayz"
                    print(ans)
                elif l == 2:
                    ans = alphabet[n] + "zz"
                    has_answer = True
                    print(ans)
                break
            else:
                l = len(ans)
                if l == 0:
                    has_answer = True
                    ans = "aa" + alphabet[n-2]
                    print(ans)
                elif l == 1:
                    has_answer = True
                    ans = "a" + alphabet[n-1] + "z"
                    print(ans)
                elif l == 2:
                    ans = alphabet[n] + ans
                    has_answer = True
                    print(ans)
                break
