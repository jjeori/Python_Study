1번 방법
a, b = map(int, input().split())
x, y = map(int, input().split())
i, j = map(int, input().split())

list = []
if a == x:
    list.append(i)
elif a == i:
    list.append(x)
elif x == i:
    list.append(a)


if b == y:
    list.append(j)
elif b == j:
    list.append(y)
elif y == j:
    list.append(b)

print(list[0], list[1])
================================
2번 방법
x_list = []
y_list = []

for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for j in range(3):
    if x_list.count(x_list[j]) == 1:
        x = x_list[j]
    if y_list.count(y_list[j]) == 1:
        y = y_list[j]

print(x, y)
