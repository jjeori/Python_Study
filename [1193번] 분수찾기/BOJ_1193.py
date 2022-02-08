N = int(input())

a = 1
count = 1
while N > a:
    count += 1
    a += count

b = N-(a-count)

if count % 2 == 1:
    print(str(count-(b-1)) + '/' + str(b))
else:
    print(str(b) + '/' + str(count-(b-1)))
