n = int(input())

a = 1
b = 6
count = 1

while n > a:
    b += 6
    a += b
    count += 1
print(count)
