x = int(input())

N = map(int, input().split())

cnt = 0
for i in N:
    if i != 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            cnt += 1

print(cnt)
