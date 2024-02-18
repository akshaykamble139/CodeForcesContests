t = int(input())
# 111 110 109 ... 100 99 .. 90 89 .. 80 79 .. 1

# 1-9 = n
# 10-99 = n + 1*(n/10)
# 100-999 = n + 2*(n/100) + 1*(n/10)
# 2*4+1*(42−4)=46
while t > 0:
    t -= 1
    n = int(input())
    num = input()
    ans = 0
    exclude = 0
    for i in range(1,n+1):
        ans += int(num[:i])

    print(ans)


