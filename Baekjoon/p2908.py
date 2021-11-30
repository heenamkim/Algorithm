#2908 상수 브론즈2

num1, num2 = map(int, input().split())
n_num1 = str(num1 % 10) + str(num1 % 100 // 10) + str(num1 // 100)
n_num2 = str(num2 % 10) + str(num2 % 100 // 10) + str(num2 // 100)


if int(n_num1) > int(n_num2):
    print(n_num1)
else:
    print(n_num2)
