#1065 한수 실버5

n = int(input())
result = 0

for i in range(1, n+1):
    if i <= 99:
        result += 1

    else:
        x = list(map(int, str(i)))
        if x[0] - x[1] == x[1] - x[2]:
            result += 1
print(result)
