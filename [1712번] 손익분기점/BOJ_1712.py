n = list(map(int, input().split()))
A = n[0]
B = n[1]
C = n[2]

if A == 0:
    print(1)
elif B < C:
    print(A//(C-B) + 1)
else:
    print(-1)
