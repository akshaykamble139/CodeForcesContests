n = int(input())


def get_days():
    n = int(input())
    first = input()
    second = input()
    ones_1 = 0
    ones_2 = 0
    if first == second:
        print(0)
    else:
        for i in range(n):
            f = first[i]
            s = second[i]
            if f!=s:
                if f == '1':
                    ones_1 += 1
                else:
                    ones_2 += 1
        if ones_2 == ones_1:
            print(ones_1)
        else:
            print(max(ones_1,ones_2))


while n > 0:
    n -= 1
    get_days()
