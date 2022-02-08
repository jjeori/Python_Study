x = list(map(int, input().split()))

A = x[0]
B = x[1]
V = x[2]

y = int((V-B)/(A-B))

if V == (A-B)*y+B:
    print(y)
else:
    print(y+1)
