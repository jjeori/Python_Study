n = int(input())

x = n
while x != 1:
    for i in range(2, x+1):
        if x % i == 0:
            x = x//i
            print(i)

            break
