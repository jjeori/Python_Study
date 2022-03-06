while True:
    n = list(map(int, input().split()))
    n.sort()
    if sum(n) == 0:
        break
    if n[2] ** 2 == n[0] ** 2 + n[1] ** 2:
        print('right')
    else:
        print('wrong')

