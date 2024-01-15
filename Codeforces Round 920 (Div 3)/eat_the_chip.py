n = int(input())


def get_result():
    arr = [int(a) for a in input().split()]
    h = arr[0]
    w = arr[1]
    a_h = arr[2]
    a_w = arr[3]
    b_h = arr[4]
    b_w = arr[5]

    if a_h == h or b_h == 1:
        print("Draw")
    else:
        h_diff = abs(a_h - b_h)
        w_diff = abs(a_w - b_w)
        alice_turn = True
        if h_diff < 2 and w_diff < 2 and a_h < b_h:
            if alice_turn:
                print("Alice")
            else:
                print("Bob")
            return
        elif w_diff > 2*h_diff:
            print("Draw")
            return
        else:
            if h_diff == 1:
                print("Draw")
                return
            elif h_diff == 2:
                if w_diff <= 1:
                    print("Bob")
                    return
            elif h_diff == 3:
                if w_diff < 2:
                    print("Alice")
                    return
                elif w_diff == 2 and (abs(b_w-1) <= 1 or abs(b_w-w) <= 1):
                    print("Alice")
                    return
            print("Draw")








while n>0:
    n -= 1
    get_result()

# 10 10 1 6 10 8
# A 2 5 B 9 7
# A 3 4 B 8 6
# A 4 3 B 7 5
# A 5 2 B 6 4
# A 2 5 B 9 7



