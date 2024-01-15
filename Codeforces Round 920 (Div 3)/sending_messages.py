t = int(input())


def is_possible():
    arr = [int(a) for a in input().split()]
    n = arr[0]
    f = arr[1]
    a = arr[2]
    b = arr[3]
    messages_time = [int(a) for a in input().split()]
    current_time = 0

    for t in messages_time:
        diff = t - current_time
        # print(f"f = {f} current before = {current_time} diff = {diff}" )
        if diff * a > b:
            current_time = t
            f -= b
        elif diff * a <= b:
            current_time = t
            f -= diff * a
        # print(f"f = {f} current after = {current_time} " )

    if f > 0:
        print("YES")
    else:
        print("NO")


while t > 0:
    t -= 1
    is_possible()

#7 21 1 3
# 4 6 10 13 17 20 26
# 18 16 13 10 7  4  1
