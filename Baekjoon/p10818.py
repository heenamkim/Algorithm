#10818 최소, 최대 브론즈3

num = int(input())
n_list = []
n_list += map(int, input().split())
n_max = 0
n_min = n_list[0]

for i in n_list:
    if n_min > i:
        n_min = i
    elif n_max < i:
        n_max = i
    else:
        continue
print(n_min, n_max)
