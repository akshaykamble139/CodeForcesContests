from sys import stdout

l = 1
r = 1000000

while l != r:
    mid = (l + r + 1) // 2
    print(mid)
    stdout.flush()

    compare = input()
    if compare == "<":
        r = mid - 1
    else:
        l = mid

print(f"! {l}")
stdout.flush()