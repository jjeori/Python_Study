n = int(input())

b = 1
count = 1

while n > b:
    b += 6 * count
    count += 1

print(count)
