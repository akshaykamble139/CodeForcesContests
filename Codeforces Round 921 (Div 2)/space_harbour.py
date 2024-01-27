word = [int(a) for a in input().split()]
n = word[0]
m = word[1]
q = word[2]

X = [int(a) for a in input().split()]
V = [int(a) for a in input().split()]

dict = {X[a]: V[a] for a in range(m)}
right = n
right_pos = {}
for i in range(1, n)[::-1]:
    if i in dict:
        right = i
    else:
        right_pos[i] = right


def result(low, high):
    global dict
    global right_pos
    total = 0
    prev = 1

    for i in range(2, high+1):
        if i in dict:
            prev = i
        elif low <= i <= high:
            total += dict[prev] * (right_pos[i] - i)

    return total


while q > 0:
    q -= 1
    temp = [int(a) for a in input().split()]
    q_type = temp[0]

    if q_type == 1:
        x = temp[1]
        v = temp[2]
        dict[x] = v
        right = right_pos[x]
        for i in range(x,right_pos[x])[::-1]:
            if i in dict:
                right = i
            elif i == x:
                right_pos[i] = right

    elif q_type == 2:
        l = temp[1]
        r = temp[2]
        print(result(l, r))
