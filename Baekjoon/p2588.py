#2588 곱셈 브론즈4

a = int(input())
b = int(input())
print(a*(b%10))
print(a*((b%100)//10))
print(a*(b//100))
print(a*b)

