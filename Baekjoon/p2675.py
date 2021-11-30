#2675 문자열 반복 브론즈2

ea = int(input())

for k in range(ea):
    num, alp = map(str, input().split())
    for i in alp:
        for j in range(int(num)):
            print(i, end="")
    print()
