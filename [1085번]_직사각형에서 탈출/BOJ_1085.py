num_list = list(map(int, input().split()))

num_list.append(num_list[2]-num_list[0])
num_list.append(num_list[3]-num_list[1])

print(min(num_list))




