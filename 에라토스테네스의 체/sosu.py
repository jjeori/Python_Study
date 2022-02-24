m, n = map(int, input().split())

prime_list = [True]*(n+1)
a = int((n+1)**0.5)

for i in range(2, a+1):
    if prime_list[i] == True:
        for j in range(i + i, n + 1, i):
            prime_list[j] = False

# 1번째 출력 방법
# sieve = []
#
# for i in range(2, n+1):
#     if prime_list[i] == True:
#         sieve.append(i)
#
# 2번째 출력 방법
sieve = [i for i in range(2, n+1) if prime_list[i] == True]

print(sieve)
