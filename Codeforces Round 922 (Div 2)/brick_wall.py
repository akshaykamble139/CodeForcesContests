t = int(input())

while t>0:
    t-=1
    word = [int(a) for a in input().split()]
    n = word[0]
    m = word[1]
    print(n*(m//2))