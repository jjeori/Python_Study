x, y = map(int, input().split())

n_list = [i for i in range(x, y+1)]

import math

for i in n_list:
    if i != 1:
        a = int(math.sqrt(i))
        for j in range(2, a + 1):
            if i % j == 0:
                break
        else:
            print(i)