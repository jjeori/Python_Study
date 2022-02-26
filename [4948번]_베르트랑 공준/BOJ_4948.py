f_list = [True] * 246913
x = int(246913 ** 0.5)

for i in range(2, x+1):
    if f_list[i] == True:
        for j in range(i + i, 246913, i):
            f_list[j] = False

while True:
    n = int(input())
    m = f_list[n+1:2*n]
    if n == 0:
        break
    elif n == 1:
        print(1)
    else:
        print(m.count(True))


