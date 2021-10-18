#2577 숫자의 개수 브론즈2

a = int(input())
b = int(input())
c = int(input())
total = a * b * c
n_list = [0,0,0,0,0,0,0,0,0,0]

for i in str(total):
    for j in range(10):
        if int(i) == j:
            n_list[j] += 1

for k in n_list:
    print(k)
