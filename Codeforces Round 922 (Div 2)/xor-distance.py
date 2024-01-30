t = int(input())


def result(first, second, num):
    if num == 0:
        return abs(first - second)
    ans = 10 ** 19
    xor = first ^ second
    bit_and = first & second
    bit_or = first | second
    abs_diff = abs(a-b)
    # print(f"xor={xor} bit_and = {bit_and} bit_or = {bit_or}")
    # if bit_and == 0:
    #     print(first ^ 1)
    #     print(second ^ 1)
    #     return abs((first ^ 1) - (second ^ 1))
    for i in range(num + 1):
        p = first ^ i
        q = second ^ i

        diff = abs(p - q)
        ans = min(ans, diff)
        print(f"xor={xor} abs_diff={abs_diff} bit_and={bit_and} bit_or={bit_or} r={i} a^r = {p} b^r = {q} abs diff = {diff}")

    return ans


while t > 0:
    t -= 1
    word = [int(a) for a in input().split()]
    a = word[0]
    b = word[1]
    r = word[2]
    print(result(a, b, r))
