#1110 더하기 사이클 브론즈1

n = int(input())
c_len = 0
total = (n // 10) + (n % 10)
new_n = (total % 10) + ((n % 10)*10)

while True:
    if n == new_n:
        c_len += 1
        break
    else:
        total = (new_n // 10) + (new_n % 10)
        new_n = (total % 10) + ((new_n % 10)*10)
        c_len += 1
print(c_len)     
        
    
        
