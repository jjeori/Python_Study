T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())

    a = []
    while k:
        for j in range(1, n+1):
            a.append(j)

        b = [1]
        for l in range(1, n):
            b.append(a[l]+b[l-1])

        a = b
        k -= 1

    print(a[-1])
