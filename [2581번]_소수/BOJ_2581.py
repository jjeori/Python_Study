x = int(input())
y = int(input())

a_list = []
for i in range(x, y+1):
    a_list.append(i)

b_list = []
for j in a_list:
    if j != 1:
        for i in range(2, j):
            if j % i == 0:
                break
        else:
            b_list.append(j)

if len(b_list) != 0:
    print(sum(b_list))
    print(min(b_list))

else:
    print(-1)
