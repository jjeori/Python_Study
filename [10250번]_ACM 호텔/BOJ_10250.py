T = int(input())

for i in range(1,T+1):
    x = list(map(int, input().split()))

    H = x[0]
    W = x[1]
    N = x[2]

    y = []
    for j in range(1, W+1):
        for l in range(1, H+1):
            y.append(str(l)+str('{0:02d}'.format(j)))

    print(y[N-1])
