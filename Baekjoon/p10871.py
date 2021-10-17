#10871 X보다 작은 수 브론즈3

n, x = map(int, input().split())
list1 = []
list1 += map(int, input().split())
for i in range(n):
    if list1[i] < x:
        print(list1[i], end=' ')
