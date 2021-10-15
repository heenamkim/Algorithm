#10871 X보다 작은 수 브론즈3

n, x = map(int, input().split())
list1 = []
list1 += map(int, input().split())
list2 = []
for i in range(n):
    if list1[i] < x:
        list2[i] += list1[i]
print(list2)
