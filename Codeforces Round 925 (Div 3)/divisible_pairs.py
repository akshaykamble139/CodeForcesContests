t = int(input())

while t > 0:
    t -= 1
    word = [int(a) for a in input().split()]
    arr = [int(a) for a in input().split()]
    n = word[0]
    x = word[1]
    y = word[2]

    y_dict = {}
    for i in range(n):
        r = arr[i] % y
        if r in y_dict:
            y_dict[r].append(i)
        else:
            y_dict[r] = [i]

    count = 0
    for k,v in y_dict.items():
        if len(v) > 1:
            l = len(v)
            for i in range(l-1):
                for j in range(i+1,l):
                    # print(f"count = {count} x = {x} y= {y} v[{i}]={v[i]} v[{j}]={v[j]} arr[v[{i}]]={arr[v[i]]} arr[v[{j}]]={arr[v[j]]} ")
                    if (arr[v[i]] + arr[v[j]]) % x == 0:
                        count += 1

    print(count)
