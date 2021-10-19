#1546 평균 브론즈1

num = int(input())
n_list = list(map(int, input().split()))
n_max = max(n_list)
total = 0

for i in range(num):
    n_list[i] = n_list[i]/(n_max)*100
    total += n_list[i]
    
print(total/num)
