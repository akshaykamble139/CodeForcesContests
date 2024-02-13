t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    arr = [int(a) for a in input().split()]
    total = sum(arr)
    avg = total//n
    if n == 1:
        print("YES")
    elif n == 2:
        if arr[1] > arr[0]:
            print("NO")
        else:
            print("YES")
    else:
        curr = 0
        can_be_done = True
        for a in arr[::-1]:
            curr += (avg-a)
            # print(f"avg = {avg} a = {a} curr = {curr}")
            if curr < 0:
                can_be_done = False
                break
        if can_be_done:
            print("YES")
        else:
            print("NO")