# 4673 셀프넘버 실버5

num = set(range(1, 10001))
num_1 = set()


for j in range(1, 10001):
    for k in str(j):
        j += int(k)
        
    num_1.add(j)
    
num_2 = num - num_1

for i in sorted(num_2):
    print(i)
