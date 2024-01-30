from sys import stdout

t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    arr = [i for i in range(1, n + 1)]
    ans = []
    count = 0
    start = 0
    end = n - 1
    while len(ans) != n:
        mid = (start + end + 1) // 2
        print(f"? {arr[mid]}")
        stdout.flush()

        compare = input()
        if compare == "=":
            ans.append(arr[mid])
            arr.remove(arr[mid])
            start = 0
            end = len(arr) - 1
            if len(arr) == 1:
                ans.append(arr[0])
                break
        elif compare == ">":
            end = mid - 1
        elif compare == "<":
            start = mid

    answer = " ".join([str(a) for a in ans])
    print("! " + answer)
    stdout.flush()
