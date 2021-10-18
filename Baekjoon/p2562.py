#2562 최댓값 브론즈2

n_list = []

for i in range(9):
    n_list.append(int(input()))

print(max(n_list))
print(n_list.index(max(n_list))+1)
