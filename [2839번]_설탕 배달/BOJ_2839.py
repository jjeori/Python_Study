N = int(input())

if N != 1 and N !=2 and N != 4 and N != 7:
    for i in range(0, N):
        y = (N - i * 3) / 5
        if y == int(y):
            print(int(i + y))
            break

else:
    print(-1)
