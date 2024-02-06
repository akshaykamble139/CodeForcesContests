t = int(input())

while t >0:
    t -= 1
    n = int(input())
    word = input()
    i = 0
    j = n-1
    while i<n:
        if word[i] == "W":
            i += 1
        else:
            break
    while j>=0:
        if word[j] == "W":
            j -= 1
        else:
            break
    print(j-i+1)