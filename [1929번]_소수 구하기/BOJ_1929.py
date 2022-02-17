# 기본적인 접근으로 풀이
# x, y = map(int, input().split())
#
# n_list = [i for i in range(x, y+1)]
#
# import math
#
# for i in n_list:
#     if i != 1:
#         a = int(math.sqrt(i))
#         for j in range(2, a + 1):
#             if i % j == 0:
#                 break
#         else:
#             print(i)

# 에라토스테니스의 체 풀이

x, y = map(int, input().split())

n_list = [i for i in range(x, y+1)]

import math

for j in n_list:
    if j != 1:
        b = []
        a = b
        for i in range(2, int(math.sqrt(y))+1):
            for l in range(2, y):
                a = b.append(i*l)

        for c in b:
            if j == c:
                break

        else:
            print(j)
