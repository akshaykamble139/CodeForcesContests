n = int(input())


def find_area():

    x_values = []
    for _ in range(4):
        first = [int(a) for a in input().split()]
        if first[0] not in x_values:
            x_values.append(first[0])

    diff_x = abs(x_values[0] - x_values[1])
    print(diff_x ** 2)


while n > 0:
    n-=1
    find_area()
